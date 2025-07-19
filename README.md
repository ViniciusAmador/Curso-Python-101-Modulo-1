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

# Módulo 1

## 📍 About the Course

Here I document a Python course from basic to advanced, named **“python101”**.  
**Strongly inspired** by the [Python for Everybody (PY4E)](https://www.py4e.com/) course, developed by the University of Michigan and taught by Professor **Charles Severance**, also I am inspired by Profa. Dra. Raquel C. de Melo-Minardi from Departamento de Ciência da Computação-UFMG.  
Additional learning references can be found at: [w3schools.com/python](https://www.w3schools.com/python/default.asp).  
For Portuguese-speaking students, we recommend engaging with the vibrant [Python Brasil community](https://python.org.br/), which promotes learning and collaboration.

# [Módulo 1](./Curso-Python-101-Modulo-1)


### **Class 2: Non Sequential Programming**

5. **Conditional Statements**
- Simple Conditional Structure (if)
- Compound Conditional Structure (if-else)
- Chained Conditional Structure (if-elif-else)
- Ternary Conditional Expression (x if cond else y)
- Nested Conditional Structures
- Exception

6. **Repetition Structures (Loops)**
- while Loop
- for Loop
- break and continue
- nested Loop
- Exception
---



## 🧭 6. Estruturas de Decisão em Python | Decision Structures in Python | Python 中的决策结构

Estruturas de decisão permitem ao programa **escolher caminhos diferentes** com base em condições.Decision structures allow a program to **choose different paths** based on conditions.决策结构允许程序根据条件**选择不同的路径**。

### ✅ Decisão Simples (if) | Simple Decision (if) | 简单决策（if）

Uma decisão simples executa um bloco de código **apenas se** a condição for verdadeira. Caso contrário, nada acontece.  
A simple decision executes a block of code **only if** the condition is true. Otherwise, nothing happens.  
当条件为真时，简单决策会执行一段代码，否则不执行。

```python
idade = 18
if idade >= 18:
    print("Você é maior de idade")  # You are an adult | 你已成年
```

### ✅ Decisão Composta (if/else) | Composite Decision (if/else) | 复合决策（if/else）

A decisão composta avalia uma condição e executa um bloco de código para o caso verdadeiro e outro para o caso falso.  
A composite decision evaluates a condition and executes one block of code if it's true and another if it's false.  
复合决策根据条件判断，在条件为真时执行一段代码，为假时执行另一段代码。

```python
idade = 16
if idade >= 18:
    print("Maior de idade")  # Adult | 成年
else:
    print("Menor de idade")  # Minor | 未成年
```

### ✅ Decisão Encadeada (if/elif/else) | Chained Decision (if/elif/else) | 链式决策（if/elif/else）

A decisão encadeada permite avaliar múltiplas condições sequencialmente. O programa testa cada `if`/`elif` até encontrar uma condição verdadeira e executa o bloco correspondente.  
Chained decision allows evaluating multiple conditions in sequence. The program checks each `if`/`elif` until it finds a true condition and executes the corresponding block.  
链式决策允许按顺序评估多个条件。程序会依次检查每个 `if`/`elif`，直到找到为真的条件并执行相应代码块。

```python
nota = 7
if nota >= 9:
    print("Excelente")  # Excellent | 优秀
elif nota >= 7:
    print("Bom")        # Good | 良好
elif nota >= 5:
    print("Regular")    # Average | 一般
else:
    print("Reprovado")  # Failed | 不及格
```

### 🧠 Expressões Condicionais | Conditional Expressions | 条件表达式

São usadas dentro dos `if`, `elif` e `else`. Comparam variáveis e retornam True ou False.Used inside `if`, `elif`, and `else`. They compare variables and return True or False.用于 `if`、`elif` 和 `else` 中，比较变量并返回 True 或 False。

```python
x = 10
y = 5
if x > y:
    print("x é maior que y")  # x is greater than y | x 大于 y
```

---

### ✅ Decisão Aninhada | Nested Decision | 嵌套决策

A decisão aninhada ocorre quando um `if` está **dentro de outro `if`**, permitindo testar uma nova condição apenas se a anterior for verdadeira. Isso é útil quando há múltiplas etapas ou regras para considerar.  
Nested decision happens when one `if` is **inside another `if`**, allowing a second condition to be tested only if the first is true. This is useful when multiple rules or stages need to be checked.  
嵌套决策是指一个 `if` **嵌套在另一个 `if` 中**，只有当前面的条件为真时，才会检查下一个条件。这在需要多重判断时非常有用。

Um `if` dentro de outro `if`.An `if` inside another `if`.一个 `if` 嵌套在另一个 `if` 中。

```python
idade = 20
possui_carteira = True

if idade >= 18:
    if possui_carteira:
        print("Pode dirigir")  # Can drive | 可以开车
    else:
        print("É maior de idade, mas não tem carteira")  # No license | 成年但无驾照
else:
    print("Menor de idade")  # Minor | 未成年
```

---

## ⚙️ Operador Ternário | Ternary Operator | 三元运算符

Forma reduzida do `if/else` em uma linha.Short version of `if/else` in one line.一行中写 `if/else` 的简洁形式。

```python
idade = 20
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)
```

---

## 🔁 Uso de Operadores Lógicos nas Decisões | Logical Operators in Decisions | 决策中的逻辑运算符

| Operador | Exemplo          | Resultado (PT/EN/ZH)                           |
| -------- | ---------------- | ---------------------------------------------- |
| and      | x > 5 and y < 10 | True se ambos forem True / Both True / 两者为真时为真 |
| or       | x > 5 or y < 10  | True se um for True / One is True / 只要一个为真即为真  |
| not      | not(x > 5)       | Inverte o resultado / Negates / 结果取反           |

```python
idade = 22
habilitacao = True

if idade >= 18 and habilitacao:
    print("Pode dirigir")  # Can drive | 可以开车
```

### ⚠️ Cuidados | Tips | 注意事项

- Sempre use identação correta após `if`, `elif`, `else`.  Always indent correctly.  一定要正确缩进。
- Evite expressões longas em uma linha.  Avoid long one-line expressions.  避免一行中写过长的表达式。

---

🎉 Parabéns! Você concluiu a Aula 2 sobre estruturas de decisão e expressões condicionais em Python. Agora você entende como aplicar decisões simples, compostas e encadeadas, além de operadores lógicos. [✅ Vá para o Exercício 2 e pratique o que aprendeu!](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exerc%C3%ADcio%202.py) | 🎉 Congratulations! You've completed Lesson 2 on decision structures and conditional expressions in Python. Now you understand how to apply simple, compound, and chained decisions, as well as logical operators. [✅ Go to Exercise 2 to practice what you've learned!](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exerc%C3%ADcio%202.py) | 🎉 恭喜你完成了第 2 课！你已经掌握了条件语句的使用，包括简单、复合和链式结构，以及逻辑运算符。[✅ 前往练习 2 来巩固所学内容！](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exerc%C3%ADcio%202.py)

---

# 📘 Aula 3: Estruturas de Repetição com while e for | Repetition Structures with while and for | 循环结构：while和for

Professor, Vinícius Costa Amador

---

## 🔁 O que são Estruturas de Repetição? | What Are Loop Structures? | 什么是循环结构？

Permitem que um bloco de código seja executado várias vezes, enquanto uma condição for verdadeira. Isso evita repetições manuais e automatiza tarefas.

They allow a block of code to run multiple times while a condition is true. This avoids manual repetition and automates tasks.

循环结构允许在条件为真时重复执行一段代码，用于自动化操作。

---

## 🌀 Estrutura `while` | `while` Loop | `while`循环

Repete o bloco de código enquanto a condição for verdadeira.

Repeats a block of code **while** the condition is `True`.

当条件为 True 时，重复执行代码块。

```python
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

### ❌ Exemplo de espera por uma resposta | Waiting for input | 等待用户输入

A estrutura `while` é comumente usada em menus ou para aguardar uma ação do usuário.
The `while` structure is commonly used in menus or to wait for user input.
`while`循环经常用于菜单或等待用户操作。

```python
resposta = ""
while resposta != "sim":
    resposta = input("Deseja continuar? Digite 'sim' para sair: ")
```

### ⚠️ Cuidado com loops infinitos | Beware of infinite loops | 谨慎无限循环

Sempre verifique se a condição do `while` será eventualmente falsa.
Always ensure the condition will eventually become `False`.
确保循环条件最终会失效，以免循环不终止。

---

## 🔁 Estrutura `for` | `for` Loop | `for`循环

Utilizada para percorrer sequências como listas, strings ou intervalos.
Used to iterate over sequences like lists, strings, or ranges.
用于遍历列表、字符串或范围。

```python
for numero in range(5):
    print("Número:", numero)
```

O `range(5)` gera os números de 0 a 4.
`range(5)` generates numbers from 0 to 4.
`range(5)` 生成从 0 到 4 的数字。

### 🎯 Exemplo com `for` e `if`: pares de 0 a 10 | Even numbers from 0 to 10 | 0 到 10 的偶数

```python
for i in range(11):
    if i % 2 == 0:
        print(i)
```

### ❌ Exemplo de `for` com `input()` | User-driven iteration | 用户输入驱动的迭代

```python
nomes = []
for i in range(3):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    nomes.append(nome)

print("Nomes cadastrados:", nomes)
```

---

## 🔁 `break` e `continue`

- `break`: Interrompe o loop imediatamente.
- `continue`: Pula para a próxima iteração.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

---

🎉 Parabéns! Você concluiu a Aula 3 sobre estruturas de repetição com `while` e `for`. Agora você entende como repetir instruções de forma eficiente em Python. [✅ Vá para o Exercício 3 e pratique o que aprendeu!](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exerc%C3%ADcio%203.py) | 🎉 Congratulations! You've completed Lesson 3 on repetition structures using `while` and `for`. Now you know how to efficiently repeat instructions in Python. [✅ Go to Exercise 3 to practice what you've learned!](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exerc%C3%ADcio%203.py) | ✨ 恭喜你完成了第 3 课！你已经掌握了 Python 中的 while 和 for 循环。[✅ 前往练习 3 来巩固所学内容！](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exerc%C3%ADcio%203.py)

# 📚 Agora que você terminou, por que não tenta o Módulo 2? | Now that you’ve finished, why not try Module 2? | 既然你完成了，不妨试试模块 2？
##👉 [Clique aqui](https://github.com/ViniciusAmador/Curso-Python-101-Modulo-2/tree/main)) | [Click here](https://github.com/ViniciusAmador/Curso-Python-101-Modulo-2/tree/main) | [点此进入](https://github.com/ViniciusAmador/Curso-Python-101-Modulo-2/tree/main)

---

<p align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=ViniciusAmador.Curso-Python-101-Modulo-1" alt="repo views"/>
</p>


