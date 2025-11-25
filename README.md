# Polymorphic and Metamorphic Python Code Generator

This project demonstrates **polymorphic** and **metamorphic code generation** techniques in Python. It generates multiple variants of a simple "Hello, World"-style script while preserving functionality. These variants use obfuscation, junk code insertion, and structural changes to appear different while producing the same output.

---

## 📌 Overview

### What is Polymorphic/Metamorphic Code?
- **Polymorphic code** changes its appearance (e.g., variable names, structure) without altering behavior.
- **Metamorphic code** rewrites itself entirely while maintaining the same functionality (e.g., shuffling logic, adding junk functions).

This project generates both types of variants for educational purposes, showcasing how code can be transformed to evade static analysis or signature-based detection.

---

## 🛠️ Features

- **Polymorphic Variants**:
  - XOR-encrypted payloads with random keys.
  - Junk functions with arithmetic operations.
  - Randomized variable/function names.
- **Metamorphic Variants**:
  - AST-based renaming of identifiers.
  - Insertion of unused junk functions.
  - Structural shuffling (e.g., reordering function definitions).
  - Arithmetic expression transformations (e.g., `a * 2` → `a + a`).

---

## 🚀 Usage

### Prerequisites
- Python 3.x

### Generate Variants
Run the following commands from the project root:

```bash
# Generate polymorphic variants
python test.py -n 5 -o variants_polymorphic

# Generate metamorphic variants
python test2.py
```

- `-n`: Number of variants to generate.
- `-o`: Output directory for polymorphic variants.

Generated files will be saved in:
- `variants_polymorphic/` (polymorphic)
- `variants_metamorphic/` (metamorphic)

---

## 📁 Output Example

### Polymorphic Variant (`variant_1.py`)
```python
def UIEaTZWAk():
    TJJzCx = bytes([129, 162, 0, 103, ...])
    key = [243, 215, 110, 9, ...]
    def dec(data, k):
        out = bytearray()
        for i, b in enumerate(data):
            out.append(b ^ k[i % len(k)])
        return bytes(out)
    print(dec(TJJzCx, key).decode())

UIEaTZWAk()
```

### Metamorphic Variant (`meta_variant_2.py`)
```python
def gre_hmwupf(nam_rzntgy):
    if False:
        __jgqepl = 12345
    return 'Hello, ' + nam_rzntgy + '!'

def mai_dquadw():
    for n in ['Alice', 'Bob', 'Eve']:
        print(gre_hmwupf(n))
```

All variants will output:
```
Hello, Alice!
Hello, Bob!
Hello, Eve!
```

---

## 🧪 How It Works

### Polymorphic Generator (`test.py`)
- Encrypts a payload (e.g., `running!!!!`) using XOR.
- Embeds encrypted data and a random key in the script.
- Adds junk functions with arithmetic operations.
- Uses random variable names and structure.

### Metamorphic Generator (`test2.py`)
- Parses the original script into an AST.
- Renames variables/functions with random identifiers.
- Inserts junk functions and shuffles code order.
- Applies arithmetic expression transformations.

---

## 📌 Notes
- **Educational Use Only**: This project is for studying obfuscation techniques, not for malicious purposes.
- **Ethical Use**: Do not use these techniques for harmful or illegal activities.
- **Dependencies**: No external libraries required (uses Python's `ast`, `random`, etc.).

