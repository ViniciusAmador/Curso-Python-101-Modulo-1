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

# 📘 Aula 2: Estruturas de Decisão e Expressões Condicionais

Professor, Vinícius Costa Amador

---

## 🧭 6. Estruturas de Decisão em Python

Estruturas de decisão permitem ao programa **escolher caminhos diferentes** com base em condições.

### ✅ Decisão Simples (if)

```python
idade = 18
if idade >= 18:
    print("Você é maior de idade")
```

### ✅ Decisão Composta (if/else)

```python
idade = 16
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### ✅ Decisão Encadeada (if/elif/else)

```python
nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Reprovado")
```

### 🧠 Expressões Condicionais

São usadas dentro dos `if`, `elif` e `else`. Comparam variáveis e retornam True ou False.

```python
x = 10
y = 5
if x > y:
    print("x é maior que y")
```

---

### ✅ Decisão Aninhada (if dentro de if)

Decisões aninhadas ocorrem quando usamos um `if` dentro de outro `if`, permitindo verificar mais de uma condição de forma hierárquica.

```python
idade = 20
possui_carteira = True

if idade >= 18:
    if possui_carteira:
        print("Pode dirigir")
    else:
        print("É maior de idade, mas não tem carteira")
else:
    print("Menor de idade")
```

---

## ⚙️ Operador Ternário

Forma reduzida de escrever `if/else` em uma linha:

```python
idade = 20
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)
```

---

## 🔁 Uso de Operadores Lógicos nas Decisões

| Operador | Exemplo          | Resultado                      |
| -------- | ---------------- | ------------------------------ |
| and      | x > 5 and y < 10 | True se ambos forem True       |
| or       | x > 5 or y < 10  | True se pelo menos um for True |
| not      | not(x > 5)       | Inverte o resultado            |

```python
idade = 22
habilitacao = True

if idade >= 18 and habilitacao:
    print("Pode dirigir")
```

### ⚠️ Cuidados:

- Sempre use identação correta após o `if`, `elif` e `else`.
- Evite usar expressões muito longas numa única linha para manter a legibilidade.

---

**Parabéns, você concluiu a introdução às Algoritmos de Estruturas de Decisão para Expressões Condicionais! 🎉**

**Vá para o Exercício 2**
