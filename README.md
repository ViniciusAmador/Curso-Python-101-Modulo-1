# 📘 Estudo Dirigido Python 101 – Variáveis, Operadores e Expressões

## Módulo 1
### Professor, Dr. Vinícius Costa Amador 


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

## 📦 2. Variáveis em Python

Variáveis são nomes que usamos para guardar informações na memória do computador. Em Python, você não precisa declarar o tipo da variável: ele é definido automaticamente.

### 🎯 Boas práticas para nomear variáveis:

- Use nomes **sem espaços**. Exemplo correto: `nome_completo`
- Evite **caracteres especiais** como `!`, `@`, `%`, etc.
- Não comece o nome da variável com **números**.
- Não use **palavras reservadas** do Python (ex: `if`, `print`, `for`).
- Python diferencia letras maiúsculas e minúsculas: `idade` ≠ `Idade`.

Essas práticas ajudam a evitar erros e tornam seu código mais legível e organizado.

### 📘 Manipulando strings (alfanuméricos)

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

### ℹ️ Casos especiais:

- Nomes de variáveis não podem começar com números.
- Não pode haver espaços ou símbolos especiais (como `!`, `@`, `%`).
- Palavras reservadas do Python (ex: `if`, `print`, `for`) não podem ser usadas como nomes de variáveis.
- Python é sensível a maiúsculas/minúsculas: `nome` ≠ `Nome`.

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

## ➕ 3. Operadores em Python

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

### 🔢 Aritméticos

| Operador | Exemplo  | Significado      |
| -------- | -------- | ---------------- |
| `+`      | 3 + 2    | Soma             |
| `-`      | 5 - 1    | Subtração        |
| `*`      | 4 * 2    | Multiplicação    |
| `/`      | 8 / 4    | Divisão real     |
| `//`     | 9 // 2   | Divisão inteira  |
| `%`      | 9 % 2    | Resto da divisão |
| `**`     | 2 ** 3   | Potência         |

### 🔍 Relacionais (Comparativos)

| Operador | Exemplo | Resultado |
| -------- | ------- | --------- |
| `==`     | 5 == 5  | True      |
| `!=`     | 5 != 3  | True      |
| `>`      | 7 > 4   | True      |
| `<`      | 3 < 5   | True      |
| `>=`     | 6 >= 6  | True      |
| `<=`     | 2 <= 4  | True      |

### 🧠 Lógicos

| Operador | Exemplo        | Significado |
| -------- | -------------- | ----------- |
| `and`    | True and False | E lógico    |
| `or`     | True or False  | OU lógico   |
| `not`    | not True       | Negação     |

---

## 🧮 4. Expressões

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

## ⌨️ 5. Entrada (input) e Saída (print)

### 🎯 Boas práticas com entrada e saída:

- Sempre identifique claramente o que o usuário deve digitar no `input()`.
- Use `print()` de forma clara, explicando o que está sendo mostrado.
- Converta os valores de entrada para o tipo correto (`int`, `float`, etc.) antes de usar em contas.

### ℹ️ Casos especiais:

- A função `input()` sempre retorna uma `string`, mesmo que o usuário digite um número.
- Para realizar operações matemáticas, converta o valor com `int()` ou `float()`.
- `print()` pode aceitar múltiplos argumentos separados por vírgulas ou concatenar com `+`, desde que tudo seja string.

### 📥 Receber dados do usuário

```python
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
```

Lembre-se: tudo que vem do `input()` é string.

### 📤 Exibir dados com `print()`

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

---

**Parabéns, você chegou ao fim do Estudo Dirigido Python 101 - Parte 1 🎉**

**Vá para o Exercício 1**
