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
# 1st Unity
-You are here:
```
Curso-Python-101-Modulo-1/
├── README.md                   ← Root
├── assets/
└── Unidade-1/
    ├── README.md               ← Sumário do módulo (YOU ARE HERE)
    └── EXERCICIO-1/            ← Sumário do módulo
```
## 🐍 1. First Code
```python
print("Hello, World!")
```
This is the classic first program in any programming language. It prints a message to the screen.
---
### ✍️ About Syntax and Indentation
- In Python, **indentation is mandatory**. It defines code blocks.
- A code block starts automatically after a colon `:` followed by **Enter**.
- The convention is **4 spaces** (or a single *Tab*), but **never mix the two** in the same file!
```python
if 5 > 2:
    print("Five is greater than two!")  # Correct
```
❌ The example below will raise an **IndentationError**:
```python
if 5 > 2:
print("Indentation error")  # Error
```
---
### 💬 Comments with `#`
- In Python, any text after the symbol `#` is ignored by the interpreter.
- Comments help explain code, structure your thinking, or temporarily disable a line.
```python
# This line is a comment and will not be executed
print("This line will run")
```
---
### 🎯 Best Practices: Camel Case
| ✅ Do        | ❌ Avoid                        |
|--------------|--------------------------------|
| totalPrice   | total_price in CamelCase context|
| userAge      | User Age (spaces)              |
| isLoggedIn   | if (reserved word)             |
- Stick to letters, numbers and underscores—no special symbols like `! @ %`.
- **Do not** use reserved words such as `if`, `print`, `for`, `class`, etc.
- Python is **case-sensitive**: `age` ≠ `Age`.
These conventions prevent errors and keep your code readable.
---
