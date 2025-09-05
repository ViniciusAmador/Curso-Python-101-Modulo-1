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
### ✨ Welcome! This document was lovingly prepared to welcome you to the Python course for the basic programming cycle. I hope you enjoy it and that it helps we grow! 
---
# *📘Módulo 1: Conceitos elementares e a Programação Sequencial - 0.0 Nivelamento de Conceitos*
Navegue pelos diretórios do curso!! 📍
```
python101/
    └──Módulo 1/
          ├── 0.0-Nivelamento de Conceitos/
          ├── 1.0-Sintaxe Básica/
          ├── 1.1-Variáveis/
          ├── 1.2-Operadores (📍Você está aqui)/
          ├── 1.3-Expressões/
          ├── 1.4-Entrada e Saída/
          └── 1.5-Exercícios/
```

# Módulo 1
## 🐍 Unit 3 – Operators in Python
Operators perform actions on variables and literal values. Mastering them lets you build expressions, make decisions, and transform data.
---
### 🎯 Style & Best Practices
* Put **one space** on each side of an operator for readability: `a = b + c` —not `a=b+c`.
* Use **parentheses** to clarify complex expressions: `total = (a + b) * c`.
* Avoid cramming many operations on one line if it hurts clarity—split across lines instead.
---
### 🔢 Arithmetic Operators
| Operator | Example | Meaning              |
| -------- | ------- | -------------------- |
| `+`      | `3 + 2` | Addition             |
| `-`      | `5 - 1` | Subtraction          |
| `*`      | `4 * 2` | Multiplication       |
| `/`      | `8 / 4` | True division        |
| `//`     | `9 // 2`| Floor (integer) div. |
| `%`      | `9 % 2` | Modulus (remainder)  |
| `**`     | `2 ** 3`| Exponentiation       |
**String tricks**  
`+` concatenates: `'Py' + 'thon' → 'Python'`  
`*` repeats: `'Ha' * 3 → 'HaHaHa'`
```python
name = "Ana" + " Silva"    # Ana Silva
print("Wow! " * 2)         # Wow! Wow!
```
---
### 🔍 Comparison (Relational) Operators
| Operator | Example | Evaluates to |
| -------- | ------- | ------------ |
| `==`     | `5 == 5`| `True`       |
| `!=`     | `5 != 3`| `True`       |
| `>`      | `7 > 4` | `True`       |
| `<`      | `3 < 5` | `True`       |
| `>=`     | `6 >= 6`| `True`       |
| `<=`     | `2 <= 4`| `True`       |
String comparisons use **lexicographic order** (alphabetical for ASCII).
---
### 🧠 Logical Operators
| Operator | Expression       | Result        |
| -------- | ---------------- | ------------- |
| `and`    | `True and False` | `False`       |
| `or`     | `True or False`  | `True`        |
| `not`    | `not True`       | `False`       |
Logical operators work on any object that can be **truth‑tested**. Non‑zero numbers, non‑empty strings/lists are `True`; `0`, `None`, and empty containers are `False`.
```python
logged_in = True
has_token = False
if logged_in and has_token:
    print("Welcome!")
else:
    print("Access denied")
```
---
### ⚙️ Assignment Variants (augmented)
| Syntax | Equivalent to | Purpose              |
| ------ | ------------- | -------------------- |
| `x += 1` | `x = x + 1` | Increment            |
| `x -= 1` | `x = x - 1` | Decrement            |
| `x *= 2` | `x = x * 2` | Scale / repeat       |
| `x //= 2`| `x = x // 2`| Floor divide & store |
---
### 🗜️ Bitwise (Preview)
| Operator | Example  | Meaning    |
| -------- | -------- | ---------- |
| `&`      | `a & b`  | AND        |
| `|`      | `a | b`  | OR         |
| `^`      | `a ^ b`  | XOR        |
| `~`      | `~a`     | NOT        |
| `<<`     | `a << n` | Shift left |
| `>>`     | `a >> n` | Shift right|
These operate on the binary representation of integers. They’re essential for low‑level tasks but optional for beginners.
---
### 🚩 Common Pitfalls & Tips
* **String + number** raises `TypeError` → cast with `str(number)`.
* Remember **operator precedence**: `**` > unary `+ -` > `* / // %` > `+ -` > comparisons > `not` > `and` > `or`.
* Use underscores for large numeric literals: `budget = 1_000_000` (still an `int`).
---
🎉 **Great!** You now wield Python’s arithmetic, comparison, logical, and assignment operators. Next unit: control flow with `if`/`elif`/`else` and loops.
