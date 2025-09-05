<p align="center">
  <img src="https://img.shields.io/badge/versão-1.0-blue" alt="Versão">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" alt="Status do Curso">
  <img src="https://img.shields.io/badge/feito%20com-Python%203.x-blue?logo=python&logoColor=white" alt="Feito com Python">
  <img src="https://img.shields.io/badge/licença-MIT-green" alt="Licença">
</p>

<p align="center">
  <img src="assets/banner_python101.png" width="400" alt="Python101 Logo">
</p>

# 🐍 python101
## Professor, Dr. Vinícius Costa Amador 
### ✨ Welcome! This material was lovingly prepared to welcome you to the Python course for the basic programming cycle. I hope you enjoy it and that it helps you grow! 

# *📘Módulo 1: Conceitos elementares e a Programação Sequencial - 1.1 Variáveis*
Navegue pelos diretórios do curso!! 📍
```
python101/
    └──Módulo 1/
          ├── 0.0-Nivelamento de Conceitos/
          ├── 1.0-Sintaxe Básica/
          ├── 1.1-Variáveis (📍Você está aqui)/
          ├── 1.2-Operadores/
          ├── 1.3-Expressões/
          ├── 1.4-Entrada e Saída/
          └── 1.5-Exercícioss/
```
# 0.0
## 🐍 Unit 1 – Primitive Data Types in Python
Python assigns a type **dynamically** the moment you bind a value to a variable name.\
Understanding these core (built‑in) types is the foundation for every script you will write.
---
### 🔑 Core Scalar Types
| Type       | Literal examples             | What it represents                             |
| ---------- | ---------------------------- | ---------------------------------------------- |
| `int`      | `42`, `-7`, `0b1010`, `0xFF` | Whole numbers of arbitrary size                |
| `float`    | `3.14`, `-2.0`, `1e‑3`       | Double‑precision floating‑point                |
| `complex`  | `2+3j`                       | Real **+** imaginary part                      |
| `bool`     | `True`, `False`              | Logical truth values *(subclass of **`int`**)* |
| `NoneType` | `None`                       | Absence of value                               |
| `str`      | `'hello'`, "Hi"              | Immutable Unicode text                         |
| `bytes`    | `b'ABC'`                     | Immutable sequence of raw bytes                |
> **Tip**  Keep the names of these types intact—never overwrite them with your own variables (e.g. `int = 5`).
---
### 📦 Core Container Types (briefly)
| Category        | Type        | Example literal     | Key property               |
| --------------- | ----------- | ------------------- | -------------------------- |
| Sequence        | `list`      | `[1, 2, 3]`         | Mutable, ordered           |
| Sequence        | `tuple`     | `(1, 2, 3)`         | Immutable, ordered         |
| Mapping         | `dict`      | `{"a": 1}`          | Key‑value pairs            |
| Set             | `set`       | `{1, 2, 3}`         | Unordered, unique elements |
| Set (immutable) | `frozenset` | `frozenset({1, 2})` | Hashable                   |
| Mutable bytes   | `bytearray` | `bytearray(b'ABC')` | Mutable bytes              |
Container types will be explored in depth later; for now, recognise their literals and mutability.
---
### ✅ Correct Usage Examples
```python
age         = 30                 # int
height      = 1.75               # float
name        = "Maria"            # str
is_active   = True               # bool
temperature = None               # NoneType – placeholder
vector      = [1, 2, 3]          # list
dimensions  = (1920, 1080)       # tuple
config      = {"theme": "dark"}  # dict
unique_ids  = {101, 102, 103}    # set
payload     = b"\x48\x49"        # bytes
z           = 2 + 3j             # complex number
```
### ❌ Incorrect Usage Examples
```python
30 = age           # Cannot assign to a literal
name! = "John"     # Invalid identifier – contains '!'
float = 3.14       # Shadowing built‑in type name – avoid!
```
---
### 📝 Useful `str` Methods (Aqui é preciso mencionar que as strings tem um índice (index) e nesse caso é possível operar usando colchetes [] dentro de uma string)
```python
text = "Good Morning"
print(text.upper())          # GOOD MORNING
print(text.lower())          # good morning
print(text.count('o'))       # 3
print(text[0:4])             # Good
print(len(text))             # 12
print(text.replace("Good", "Great"))  # Great Morning
```
---
### 🔢 Useful `int` Methods
```python
n = 42
print(n.bit_length())   # 6  → number of bits needed
print(n.to_bytes(2, 'big'))  # b' *' → 16‑bit big‑endian bytes
print((‑7).bit_count())  # 3 – number of set bits in two’s‑complement representation
```
> *Remember*: `bool` is a subclass of `int`, so most integer methods work on `True` (`1`) and `False` (`0`).
---
### 🔣 Useful `float` Methods
```python
x = 3.5
print(x.is_integer())        # False
print(x.as_integer_ratio())  # (7, 2)
print(x.hex())               # '0x1.cp+1' → hexadecimal representation
```
---
### ⚙️ Boolean Shortcuts
```python
flag = True
print(int(flag))      # 1  – coercion to int
print(not flag)       # False – logical negation
a = None
print(bool(a))        # False – truth‑value testing
```
---
### 🔄 Type Conversion Cheat‑Sheet
| Function       | Converts to | Example         | Result   |
| -------------- | ----------- | --------------- | -------- |
| `int(x)`       | integer     | `int("7")`      | `7`      |
| `float(x)`     | float       | `float("3.14")` | `3.14`   |
| `str(x)`       | string      | `str(42)`       | `'42'`   |
| `bool(x)`      | boolean     | `bool(0)`       | `False`  |
| `complex(a,b)` | complex     | `complex(2,3)`  | `(2+3j)` |

> Use these functions to **cast** values explicitly when automatic inference is not enough.
---
### 🏷️ Variable Naming & Assignment Essentials
- **Identifiers** may contain letters, digits, and underscores, but **never** start with a digit.
- Avoid reserved words (`for`, `while`, `class`, …) and built‑in type names (`list`, `int`, …).
- Python variables are **references**: assigning `b = a` does **not** copy the object; it creates a new reference to the same value. Use `copy` / slicing for independent copies when needed.
- Reassignment simply points the name to a new object; the original value is released when no names reference it.
```python
x = 5      # x → 5
y = x      # y → 5 (same object)
x = 7      # now x → 7, y still → 5
```
---
🎉 **Well done!** You now recognise Python’s fundamental data types and can verify or convert them at runtime.
> Next up: arithmetic & logical operators.

