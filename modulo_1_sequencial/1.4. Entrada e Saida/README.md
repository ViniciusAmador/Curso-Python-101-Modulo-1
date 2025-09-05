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
          ├── 1.2-Operadores/
          ├── 1.3-Expressões/
          ├── 1.4-Entrada e Saída (📍Você está aqui)/
          └── 1.5-Exercício/
```

## 🐍 Unit 5 – Input & Output in Python
User interaction in a terminal program boils down to two things:
* **Input** – data flowing *into* your script (typically via `input()` or `sys.stdin`).
* **Output** – data flowing *out* (via `print()` or `sys.stdout`).
---
### 🎯 Best Practices
| ✅ Do | ❌ Avoid |
|-------|---------|
| Prompt clearly: `age = input("Enter your age: ")` | Cryptic prompts like `input("?")` |
| Convert to the right type *immediately* (`int()`, `float()`) | Doing math on raw strings |
| Use f‑strings or commas in `print()` for readability | String concatenation with `+` if it forces many `str()` casts |
| Handle invalid input with `try/except` | Letting the script crash on bad user data |
---
### ℹ️ Quick Facts
* `input()` **always** returns a **`str`**, even if the user types `42`.
* `print()` can take **multiple arguments** separated by commas; it automatically inserts spaces.
* Use `sys.stdin` / `sys.stdout` for advanced piping or redirection (covered later).
---
### 📥 Reading Data with `input()`
```python
name  = input("Enter your name: ")
age   = input("Enter your age: ")  # still a string!
```
---
### 📤 Writing Data with `print()`
```python
print("Hello", name, "you are", age, "years old")
# Same result with an f‑string
print(f"Hello {name}, you are {age} years old")
```
---
### ✅ Complete Example
```python
name   = input("Name: ")
age    = int(input("Age: "))            # cast to int
height = float(input("Height (m): "))    # cast to float
print(f"Hi, I'm {name}.")
print(f"I'm {age} years old and {height} m tall.")
```
---
### ❌ Common Error
```python
height = float(input("Height: "))
print("Recorded height: " + height)   # TypeError → height is float, needs str
```
**Fix**
```python
print("Recorded height: " + str(height))
# or, better
print(f"Recorded height: {height}")
```
---
### 🔄 Type Conversion Summary
| Function    | Converts to | Example              | Output |
|-------------|-------------|----------------------|--------|
| `int(x)`    | integer     | `int("10")`          | `10`   |
| `float(x)`  | float       | `float("3.14")`      | `3.14` |
| `str(x)`    | string      | `str(42)`            | `'42'` |
| `bool(x)`   | boolean     | `bool(0)`            | `False`|
---
### 🏋️‍♂️ Exercise 1 – Simple BMI Calculator *(Terminal Only)*
1. Ask the user for **weight** in kilograms and **height** in meters.  
2. Convert the inputs to `float`.
3. Calculate **BMI**: `weight / height ** 2`.
4. Print the BMI rounded to **one decimal place** using an f‑string.
```python
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / height ** 2
print(f"Your BMI is {bmi:.1f}")
```
Try running the script and redirecting input from a file:
```bash
echo -e "70\n1.75" | python bmi.py
```
---
### 🚀 Advanced Note: `sys.stdin`, `sys.stdout`, `sys.stderr`
```python
import sys
data = sys.stdin.read()       # read piped data
sys.stdout.write(data.upper()) # write result
sys.stderr.write("Done!\n")    # separate error/diagnostic stream
```
These streams power Unix‐style piping (`cat file | python script.py`) and are invaluable for building CLI tools.
---
🎉 **Nice work!** You can now gather user input, display clear output, and convert data types safely. Next unit: branching with `if/elif/else`.
