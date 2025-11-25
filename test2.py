
import ast, random, copy, os, sys

def rnd_ident(base="id", n=6):
    return base + "_" + ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))

def make_junk_function_ast():
    name = rnd_ident("junkf", 8)
    fn_src = f"""
def {name}():
    a = {random.randint(1,100)} * {random.randint(1,100)}
    b = a // {random.randint(2,20)}
    if False:
        print("this is never executed", a, b)
"""
    return ast.parse(fn_src).body[0]

def is_main_if(node: ast.AST) -> bool:
    if not isinstance(node, ast.If): return False
    comp = node.test
    if isinstance(comp, ast.Compare) and isinstance(comp.left, ast.Name) and comp.left.id == "__name__":
        if comp.comparators and isinstance(comp.comparators[0], ast.Constant) and comp.comparators[0].value == "__main__":
            return True
    return False

class MetaTransformer(ast.NodeTransformer):
    def __init__(self): #карта изменений
        super().__init__()
        self.name_map = {}

    def _eligible(self, name: str) -> bool:
        if not name: return False
        if name.startswith("__") and name.endswith("__"): return False
        if name in ("__name__", "__file__", "__main__", "print", "range", "len", "True", "False", "None", "int", "str", "list", "dict", "set", "bool"):
            return False
        return True

    def ensure_map(self, orig: str):
        if orig not in self.name_map and self._eligible(orig):
            self.name_map[orig] = rnd_ident(orig[:3], 6)
        return self.name_map.get(orig, orig)

    def visit_FunctionDef(self, node: ast.FunctionDef): #Переименовывает функций и аргументы
        if self._eligible(node.name):
            node.name = self.ensure_map(node.name)
        def rename_arg(a: ast.arg): #
            if not a: return
            if self._eligible(a.arg):
                a.arg = self.ensure_map(a.arg)
        posonly = getattr(node.args, "posonlyargs", None)
        if posonly:
            for a in posonly: rename_arg(a)
        for a in node.args.args: rename_arg(a)
        if node.args.vararg: rename_arg(node.args.vararg)
        for a in node.args.kwonlyargs: rename_arg(a)
        if node.args.kwarg: rename_arg(node.args.kwarg)
        if random.random() < 0.6:
            junk_if = ast.If(test=ast.Constant(False),
                             body=[ast.Assign(targets=[ast.Name(id='_', ctx=ast.Store())], value=ast.Constant(12345))],
                             orelse=[])
            node.body.insert(0, junk_if)
        self.generic_visit(node)
        return node

    def visit_Assign(self, node: ast.Assign):
        def process_target(t):
            if isinstance(t, ast.Name):
                if self._eligible(t.id):
                    t.id = self.ensure_map(t.id)
            elif isinstance(t, (ast.Tuple, ast.List)):
                for elt in t.elts:
                    process_target(elt)
        for targ in node.targets:
            process_target(targ)
        self.generic_visit(node)
        return node

    def visit_For(self, node: ast.For):
        def ensure_target(t):
            if isinstance(t, ast.Name):
                if self._eligible(t.id):
                    t.id = self.ensure_map(t.id)
            elif isinstance(t, (ast.Tuple, ast.List)):
                for elt in t.elts:
                    ensure_target(elt)
        ensure_target(node.target)
        self.generic_visit(node)
        return node

    def visit_Name(self, node: ast.Name):
        if isinstance(node.ctx, ast.Load):
            if node.id in self.name_map:
                node.id = self.name_map[node.id]
        return node

    def visit_BinOp(self, node: ast.BinOp):
        self.generic_visit(node)
        if isinstance(node.op, ast.Add) and isinstance(node.right, ast.Constant) and isinstance(node.right.value, int) and node.right.value == 1 and random.random() < 0.5:
            return ast.copy_location(ast.BinOp(left=node.left, op=ast.Sub(), right=ast.UnaryOp(op=ast.USub(), operand=ast.Constant(value=-1))), node)
        if isinstance(node.op, ast.Mult) and isinstance(node.right, ast.Constant) and isinstance(node.right.value, int) and node.right.value == 2 and random.random() < 0.4:
            return ast.copy_location(ast.BinOp(left=node.left, op=ast.Add(), right=copy.deepcopy(node.left)), node)
        return node

def generate_metamorph(template_path: str, outdir="variants_metamorphic", n=5):
    if not os.path.isfile(template_path):
        print(f"Template not found: {template_path}")
        return
    with open(template_path, "r", encoding="utf-8") as f:
        src = f.read()
    tree_orig = ast.parse(src)
    os.makedirs(outdir, exist_ok=True)
    print(f"Generating {n} variants into {os.path.abspath(outdir)}")
    for i in range(1, n+1):
        tree = copy.deepcopy(tree_orig)
        if random.random() < 0.9:
            for _ in range(random.randint(1,3)):
                tree.body.insert(random.randint(0, len(tree.body)), make_junk_function_ast())
        main_nodes = [n for n in tree.body if is_main_if(n)]
        other_nodes = [n for n in tree.body if not is_main_if(n)]
        random.shuffle(other_nodes)
        tree.body = other_nodes + main_nodes
        transformer = MetaTransformer()
        # pre-collect function names so calls are updated correctly
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and transformer._eligible(node.name):
                transformer.ensure_map(node.name)
            # also collect assign targets to avoid load-before-store issues (optional)
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name) and transformer._eligible(t.id):
                        transformer.ensure_map(t.id)
        new_tree = transformer.visit(tree)
        ast.fix_missing_locations(new_tree)
        code = f"# Metamorphic variant {i} - rnd={random.random()}\n" + ast.unparse(new_tree)
        out_path = os.path.join(outdir, f"meta_variant_{i}.py")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(code)
        print("  wrote", out_path)
    print("Done.")

if __name__ == "__main__":
    tpl = "template.py"
    out = "variants_metamorphic"
    num = 3
    generate_metamorph(tpl, out, num)
    first = os.path.join(out, "meta_variant_1.py")
    if os.path.isfile(first):
        print("\nRunning", first)
        os.system(f'"{sys.executable}" "{first}"')
