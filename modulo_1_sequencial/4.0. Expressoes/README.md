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
### ✨ Bem-vindo! Este material foi preparado com carinho para receber você no curso de Python para o ciclo básico de programação. Espero que aproveite e que ele ajude no seu crescimento! 
---
### 📍 Sobre o Curso
Aqui está documentado um curso de Python do **básico ao avançado**, chamado **“python101”**.  
**Fortemente inspirado** no curso [Python for Everybody (PY4E)](https://www.py4e.com/), desenvolvido pela Universidade de Michigan e ministrado pelo Professor **Charles Severance**, e também inspirado pela Profa. Dra. **Raquel C. de Melo-Minardi**, do Departamento de Ciência da Computação da UFMG.  

> Referências adicionais podem ser encontradas em: [w3schools.com/python](https://www.w3schools.com/python/default.asp).  
Para estudantes de língua portuguesa, recomendamos a [Comunidade Python Brasil](https://python.org.br/), que promove aprendizado e colaboração.
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
          ├── 1.3-Expressões (📍Você está aqui)/
          ├── 1.4-Entrada e Saída/
          └── 1.5-Exercícios/
```

## 🐍 Unit 4 – Expressions in Python
An **expression** combines values, variables, and operators to produce a single result. In practice, nearly every non-trivial line of Python you write is an expression—or contains one.
---
### 🎯 Style & Best Practices
* **Parentheses first** – use them liberally to show precedence, even when Python would get it right without them.
* **One idea per line** – if an expression grows too long, split it and assign intermediate results to descriptively named variables.
* **Descriptive names** – a well-chosen variable name makes an expression self-explanatory.
```python
# 👍 Clear
net_price = (gross_price - discount) * (1 + tax_rate)
# 👎 Hard to read
np = gp - d * (1 + t)
```
---
### ⏫ Operator Precedence (recap)
`()` **>** `**` **>** `* / // %` **>** `+  -` **>** comparisons **>** `not` **>** `and` **>** `or`
Python follows the standard mathematical hierarchy; anything inside parentheses runs first.
---
### ✅ Arithmetic Expression Example
```python
result = 2 + 3 * 4    # 14, because * binds tighter than +
print(result)
```
---
### ✅ Boolean Expression Example
```python
is_valid = 10 > 5 and 3 < 2
print(is_valid)        # False
```
Logical operators (`and`, `or`, `not`) can chain comparisons to build complex conditions.
---
### ❌ Common Error
```python
value = 5 +           # SyntaxError → expression is incomplete
```
Always ensure both operands and the operator are present.
---
### 🚩 Tips & Edge Cases
* Division always produces `float`; use `//` if you need an `int`.
* String comparisons are lexicographic (`'apple' < 'banana'` → `True`).
* Mixing numeric types promotes to the most “complex” type: `int → float → complex`.
* An expression can be passed directly to functions: `print((2 + 3) * 4)`.
---
🎉 **Good job!** You now understand how to build and evaluate arithmetic and boolean expressions, and how operator precedence affects the final result. Next up: flow control with `if` statements.
