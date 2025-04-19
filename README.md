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
## Módulo 1
### Seja bem vindo. Este material foi preparado carinhosamente por mim, para acolhê-los no curso de Python do ciclo básico de programação. Espero que o material seja proveitoso!
### Professor, Dr. Vinícius Costa Amador 

## 📍 Sobre o Curso | About the Course | 关于课程

Aqui eu documento um curso de Python do **básico ao avançado**, cujo nome será **“python101”**.  
O material tem **forte inspiração** no curso [Python for Everybody (PY4E)](https://www.py4e.com/) desenvolvido pela Universidade de Michigan e ministrado pelo professor **Charles Severance**.  
Material extra utilizado como suporte adicional pode ser consultado em: [w3schools.com/python](https://www.w3schools.com/python/default.asp).  
Para os alunos brasileiros, recomenda-se também conhecer a comunidade [Python Brasil](https://python.org.br/), que incentiva o aprendizado e a colaboração em todo o país.

Here I document a Python course from basic to advanced, named **“python101”**.  
**Strongly inspired** by the [Python for Everybody (PY4E)](https://www.py4e.com/) course, developed by the University of Michigan and taught by Professor **Charles Severance**.  
Additional learning references can be found at: [w3schools.com/python](https://www.w3schools.com/python/default.asp).  
For Portuguese-speaking students, we recommend engaging with the vibrant [Python Brasil community](https://python.org.br/), which promotes learning and collaboration.

这里我记录了一个从基础到高级的 Python 课程，名为 **“python101”**。  
该课程受密歇根大学 **Charles 教授** 主讲的 [Python for Everybody (PY4E)](https://www.py4e.com/) 课程的 **启发很大**。  
所使用的额外学习资料可参考：[w3schools.com/python](https://www.w3schools.com/python/default.asp)。  
对于讲葡萄牙语的学生，推荐加入 [Python Brasil 社区](https://python.org.br/)，该社区鼓励学习和协作。

---

## 🐍 Instalação do Python | Python Installation | Python 安装指南

Para começar a programar em Python, é necessário instalar o interpretador da linguagem.  
A versão mais recente disponível é a **Python 3.13.3** ([python.org](https://www.python.org/downloads/?utm_source=chatgpt.com)).

### 💻 Windows

1. Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads/)
2. Clique em "Download Python 3.13.3" para Windows.
3. Execute o instalador baixado.
4. **Importante:** Marque a opção “Add Python to PATH” antes de clicar em “Install Now”.

### 🍎 macOS

1. Visite: [python.org/downloads](https://www.python.org/downloads/)
2. Clique em "Download Python 3.13.3" para macOS.
3. Abra o arquivo `.pkg` baixado e siga as instruções do instalador.

### 🐧 Linux

A maioria das distribuições Linux já vem com o Python instalado. Para verificar, abra o terminal e digite:

```bash
python3 --version
```

Se não estiver instalado ou desejar uma versão mais recente, utilize o gerenciador de pacotes da sua distribuição.  
Exemplo no Ubuntu:

```bash
sudo apt update
sudo apt install python3
```

Para outras distribuições, consulte a documentação específica ou compile a partir do código-fonte disponível em [python.org/downloads](https://www.python.org/downloads/).


# 📘 Aula 1: Introdução à Programação com Python: Variáveis, Operadores, Expressões e Entrada de Dados | Introduction to Programming with Python: Variables, Operators, Expressions and Input/Output | 使用 Python 编程入门：变量、运算符、表达式与输入输出

---

## 🐍 1. Primeiro Programa em Python

```python
print("Hello, World!")
```

Esse é o clássico primeiro programa em qualquer linguagem de programação. Ele imprime uma mensagem na tela.

### ✍️ Sobre Sintaxe e Identação

- Em Python, **a identação é obrigatória**. Ela define blocos de código.
- Um bloco de código é criado automaticamente quando usamos dois pontos `:` e pressionamos Enter.
- O padrão é usar 4 espaços (ou Tab), mas nunca misture os dois!

```python
if 5 > 2:
    print("Cinco é maior que dois!")  # Correto
```

❌ Este exemplo abaixo geraria erro de identação:

```python
if 5 > 2:
print("Erro de indentação")  # Erro
```

### 💬 Comentários com `#`

- Em Python, qualquer texto após o símbolo `#` é ignorado pelo interpretador.
- Comentários servem para explicar o código, organizar o raciocínio ou anotar algo que não deve ser executado.

---

## 📦 2. Variáveis em Python | Variables in Python | Python 中的变量

Variáveis armazenam dados em memória com nomes escolhidos pelo programador. Em Python, o tipo é atribuído automaticamente. | Variables store data in memory using names. In Python, the type is assigned automatically. | 变量使用名称在内存中存储数据，在 Python 中类型由系统自动推断。

### 📌 Tipos mais comuns:

- `int`: números inteiros (ex.: 10, -3)
- `float`: números com vírgula (ex.: 3.14, -2.0)
- `str`: textos (ex.: "Olá")
- `bool`: lógicos (ex.: True, False)

### ✅ Exemplos corretos:

```python
idade = 30           # int
altura = 1.75        # float
nome = "Maria"       # str
ativo = True         # bool
```

### ❌ Exemplos com erro:

```python
30 = idade           # Erro: não se pode começar com número
nome! = "João"       # Erro: nome de variável inválido
```

---

### 🎯  Boas Práticas | Best Practices | 最佳实践

- Sem espaços ou símbolos especiais. | No spaces or special symbols. | 不允许空格或特殊字符。`!`, `@`, `%`, etc.
- Não usar palavras reservadas. | Don't use reserved words. | 不要使用保留字。 (ex: `if`, `print`, `for`).
- Python diferencia maiúsculas de minúsculas. | Python is case-sensitive. | Python 区分大小写。 `idade` ≠ `Idade`.

Essas práticas ajudam a evitar erros e tornam seu código mais legível e organizado.


### 📘  Strings (Textos) | Strings (Text) | 字符串（文本）


Strings em Python têm várias funcionalidades:

- Transformar tudo em maiúsculo:

```python
texto = "bom dia"
print(texto.upper())  # BOM DIA
```

- Transformar tudo em minúsculo:

```python
texto = "OLÁ"
print(texto.lower())  # olá
```

- Contar caracteres específicos:

```python
frase = "banana"
print(frase.count("a"))  # 3
```

- Acessar parte da string (fatiamento):

```python
palavra = "Python"
print(palavra[0:3])  # Pyt
```

- Saber o tamanho de uma string:

```python
mensagem = "Olá mundo"
print(len(mensagem))  # 9
```

- Substituir partes do texto:

```python
msg = "bom dia"
print(msg.replace("bom", "boa"))  # boa dia
```

---

## ➕ 3. Operadores em Python | Operators in Python | Python 中的运算符

Operadores são usados para realizar operações com variáveis e valores. | Operators are used to perform operations on variables and values. | 运算符用于对变量和值进行操作。

### 🎯 Boas práticas ao usar operadores:

- Deixe espaços ao redor de operadores para melhorar a legibilidade. Exemplo: `a = b + c` e **não** `a=b+c`.
- Use parênteses para organizar expressões complexas e evitar confusões.
- Evite fazer muitas operações em uma mesma linha se o código ficar difícil de entender.

### ℹ️ Casos especiais:

- Usar `+` para números e para concatenar strings.
- `*` pode ser usado para repetir strings.
- Operadores relacionais com strings comparam a ordem alfabética.
- Operadores lógicos funcionam com qualquer tipo que possa ser avaliado como verdadeiro ou falso.

### 📍 Também é possível operar com strings

- Usar `+` para **concatenar** (juntar) strings:

```python
nome = "Ana"
sobrenome = "Silva"
print(nome + " " + sobrenome)  # Ana Silva
```

- Usar `*` para **repetir** uma string:

```python
print("Olá! " * 3)  # Olá! Olá! Olá!
```

⚠️ Não é possível somar string com número diretamente:

```python
idade = 20
print("Idade: " + idade)  # ERRO
```

✅ Correto:

```python
print("Idade: " + str(idade))
```

### 🔢 Aritméticos | Arithmetic Operators | 算术运算符

| Operador | Exemplo  | Significado      |
| -------- | -------- | ---------------- |
| `+`      | 3 + 2    | Soma             |
| `-`      | 5 - 1    | Subtração        |
| `*`      | 4 * 2    | Multiplicação    |
| `/`      | 8 / 4    | Divisão real     |
| `//`     | 9 // 2   | Divisão inteira  |
| `%`      | 9 % 2    | Resto da divisão |
| `**`     | 2 ** 3   | Potência         |

### 🔍 Relacionais | Relational Operators | 关系运算符

| Operador | Exemplo | Resultado |
| -------- | ------- | --------- |
| `==`     | 5 == 5  | True      |
| `!=`     | 5 != 3  | True      |
| `>`      | 7 > 4   | True      |
| `<`      | 3 < 5   | True      |
| `>=`     | 6 >= 6  | True      |
| `<=`     | 2 <= 4  | True      |

### 🧠 Lógicos | Logical Operators | 逻辑运算符

| Operador | Exemplo        | Significado |
| -------- | -------------- | ----------- |
| `and`    | True and False | E lógico    |
| `or`     | True or False  | OU lógico   |
| `not`    | not True       | Negação     |

### 🧵 Strings e Operadores | Strings and Operators | 字符串与运算符

```python
nome = "Ana"
sobrenome = "Silva"
print(nome + " " + sobrenome)  # Concatenação | Concatenation | 连接字符串
print("Olá! " * 3)               # Repetição | Repetition | 重复

```
⚠️ Não é possível concatenar string com número diretamente:

```python
idade = 20
# print("Idade: " + idade)  # Erro | Error | 错误
print("Idade: " + str(idade))  # Correto | Correct | 正确
```
---

## 🧮 4. Expressões em Python | Expressions in Python | Python 中的表达式

Expressões são combinações de valores, variáveis e operadores que geram um resultado. | Expressions combine values, variables, and operators to produce a result. | 表达式是由值、变量和运算符组成的语句，用于计算结果。

### 🎯 Boas práticas ao escrever expressões:

- Utilize parênteses para indicar claramente a ordem das operações.
- Evite expressões muito longas em uma única linha. Separe em partes se necessário.
- Nomes de variáveis devem ser descritivos para facilitar a leitura.

### ℹ️ Casos especiais:

- Expressões podem ser usadas diretamente em funções como `print()`.
- O Python respeita a ordem das operações (precedência): parênteses > potência > multiplicação/divisão > adição/subtração.
- Expressões booleanas misturam operadores lógicos e relacionais.

### ✅ Aritmética

```python
soma = 2 + 3 * 4   # 14
```

### ✅ Comparativa

```python
resultado = 10 > 5 and 3 < 2
print(resultado)  # False
```

### ❌ Erro comum:

```python
valor = 5 +       # Incompleto → ERRO
```

---

## ⌨️ 5. Entrada e Saída | Input and Output | 输入与输出

### 🎯 Boas práticas com entrada e saída:

- Sempre identifique claramente o que o usuário deve digitar no `input()`.
- Use `print()` de forma clara, explicando o que está sendo mostrado.
- Converta os valores de entrada para o tipo correto (`int`, `float`, etc.) antes de usar em contas.

### ℹ️ Casos especiais:

- A função `input()` sempre retorna uma `string`, mesmo que o usuário digite um número.
- Para realizar operações matemáticas, converta o valor com `int()` ou `float()`.
- `print()` pode aceitar múltiplos argumentos separados por vírgulas ou concatenar com `+`, desde que tudo seja string.

### 📥 Entrada com input() | Input with input() | 使用 input() 输入

```python
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
```

Lembre-se: tudo que vem do `input()` é string.

### 📤 Saída com print() | Output with print() | 使用 print() 输出

```python
print("Olá", nome, "você tem", idade, "anos")
```

### ✅ Exemplo completo:

```python
nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura (em metros): "))

print("Olá, meu nome é", nome)
print("Tenho", idade, "anos e", altura, "m de altura")
```

### ❌ Exemplo com erro:

```python
altura = float(input("Altura: "))
print("Altura registrada: " + altura)   # ERRO → precisa converter altura para string
```

✅ Correção:

```python
print("Altura registrada: " + str(altura))
```
⚠️ Conversão de tipos | Type Conversion | 类型转换

```python
altura = float(input("Altura: "))
print("Altura registrada: " + str(altura))
```
---

🎉 Parabéns! Você concluiu a Aula 1 sobre estruturas básicas de programação com Python. Agora você entende variáveis, operadores, expressões, entrada e saída de dados. [✅ Vá para o Exercício 1 e pratique o que aprendeu!](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exercicio%201.py) | Congratulations! You've completed Lesson 1 on Python basics. Now you understand variables, operators, expressions, input and output. [✅  Go to Exercise 1 to practice what you've learned!](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exercicio%201.py) | 恭喜你完成了第 1 课！你已经掌握了变量、运算符、表达式、输入与输出的基本知识。[✅ 前往练习 1 来巩固所学内容！](https://github.com/ViniciusAmador/Curso-Python-101/blob/main/Exercicio%201.py)

---

# 📘 Aula 2: Estruturas de Decisão e Expressões Condicionais | Decision Structures and Conditional Expressions | 决策结构与条件表达式

Professor, Vinícius Costa Amador

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
