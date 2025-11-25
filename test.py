
import os, random, string, textwrap

# типо вредонос
PAYLOAD = "running!!!!)!)!)!)!)!)!)!)!!)"

# XOR-функция
def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# Генерация случайных имен
def rnd_ident(n=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

# мусора накидать
def make_junk_function():
    name = rnd_ident(10)
    body_lines = []
    # вычисляем
    for i in range(random.randint(2,5)):
        a = random.randint(1,100)
        b = random.randint(1,100)
        body_lines.append(f"    _ = {a} * {b}  # junk")
    if random.random() < 0.4:
        body_lines.append("    if False:\n        print('never')\n")
    body = "\n".join(body_lines)
    return f"def {name}():\n{body}\n"

# Создаёт вариант скрипта с уникальным ключом/имёнами/мусором
def create_variant(output_path, payload_text):
    # ключ случайной длины 4..12
    key = os.urandom(random.randint(4,12))
    enc = xor_bytes(payload_text.encode('utf-8'), key)
    # кодируем зашифр. байты как список чисел для встраивания
    enc_list = ", ".join(str(b) for b in enc)

    func_name = rnd_ident(9)
    dec_var = rnd_ident(6)
    junk_funcs = [make_junk_function() for _ in range(random.randint(1,3))]
    # Иногда меняем порядок функций — демонстрация «shuffle»
    random.shuffle(junk_funcs)

    template = f'''


{''.join(junk_funcs)}

def {func_name}():
    {dec_var} = bytes([{enc_list}])
    key = {list(key)}
    # простой XOR-декриптор
    def dec(data, k):
        out = bytearray()
        for i, b in enumerate(data):
            out.append(b ^ k[i % len(k)])
        return bytes(out)
    try:
        msg = dec({dec_var}, key).decode('utf-8')
    except Exception:
        msg = "<decode error>"
    print(msg)

# иногда вызываем мусорные функции to vary traces
if {random.choice([True, False])}:
    pass
{func_name}()
'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(textwrap.dedent(template))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate polymorphic benign variantfs")
    parser.add_argument("-n", "--num", type=int, default=5, help="how many variants to generate")
    parser.add_argument("-o", "--outdir", default="variants_polymorphic", help="output folder")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    for i in range(args.num):
        path = os.path.join(args.outdir, f"variant_{i+1}.py")
        create_variant(path, PAYLOAD)
    print(f"Generated {args.num} variants in {args.outdir}")
