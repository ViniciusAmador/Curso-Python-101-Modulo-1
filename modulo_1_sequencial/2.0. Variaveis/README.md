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

# *📘Módulo 1: Conceitos elementares e a Programação Sequencial - 2.0 Variáveis*
Navegue pelos diretórios do curso!! 📍
```
python101/
    └──Módulo 1/
          ├── 0.0-Nivelamento de Conceitos/
          ├── 1.0-Sintaxe Básica/
          ├── 2.0-Variáveis (📍Você está aqui)/
          │     ├── 2.1-O que é uma variável?/
          │     ├── 2.2-Tipos de Dados em Python — Definições Claras/
          │     │     ├── 2.2.1-Strings (detalhes que importam)/
          │     │     ├── 2.2.2-Inteiros (int)/
          │     │     ├── 2.2.3-Floats (float)/
          │     │     └── 2.2.4-Booleanos (bool)/
          │     ├── 2.3-Conversão-de-tipos/
          │     └── 2.5-Tipos-estruturados/
          ├── 3.0-Operadores/
          ├── 4.0-Expressões/
          ├── 5.0-Entrada e Saída/
          └── 6.0-Exercícioss/
```


## 2.1 🐍 O que é uma variável?

Uma variável é um espaço nomeado na memória do computador que armazena um valor.
Ela é formada por três elementos essenciais:

- **Nome (identificador)** – como você irá se referir a ela no código.
Ex.: idade, altura, nome_usuario.
- **Tipo** – define que tipo de informação pode ser armazenada.
Ex.: número inteiro, número decimal, texto, etc.
- **Valor** – a informação efetivamente guardada.
Ex.: 25, 1.75, "Maria".
- **Espaço na memória** - 
```python
idade = 21         # nome: idade | tipo: int | valor: 21 | na memória: objeto int(21)
```
>📌 Em Python, o tipo é atribuído dinamicamente no momento em que você dá um valor à variável:
---

- **Declaração (declaration):**
Usado em linguagens estaticamente tipadas (C, Java). Ex.: int idade; estou declarando a variável idade como do tipo inteiro, mas ainda não dei um valor.
- **Inicialização (initialization):**
Quando você declara e dá o primeiro valor. Ex.: int idade = 25; em Java ou C.
- **Atribuição (assignment):**
Quando você dá um valor a uma variável (seja o primeiro ou outro depois). Em Python, como não existe declaração prévia de tipo, usamos direto a atribuição:

```python
idade = 25          # int
altura = 1.75       # float
nome = "Maria"      # str
```
## 2.2 🔑 Tipos de Dados em Python — Definições Claras
| Tipo        | O que é                                                  | Imutável? | Exemplos                          | Para que serve                         | Pegadinhas importantes                                                                      |
| ----------- | -------------------------------------------------------- | --------- | --------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------- |
| `int`       | Inteiro de precisão arbitrária (sem limite fixo de bits) | ✔️        | `0`, `42`, `-7`, `0b1010`, `0xFF` | Contagem, índices, aritmética exata    | Divisão `/` retorna `float`; use `//` para divisão inteira                                  |
| `float`     | Número em ponto flutuante (IEEE-754, dupla precisão)     | ✔️        | `3.14`, `-2.0`, `1e-3`            | Medidas, cálculos científicos          | **Imprecisão**: `0.1 + 0.2 != 0.3` (use `Decimal` se precisar de exatidão monetária)        |
| `complex`   | Número complexo (parte real + imaginária)                | ✔️        | `2+3j`, `-1j`                     | Sinais, engenharia, FFT                | Impressão pode usar `j`; operações são fechadas no conjunto                                 |
| `bool`      | Verdadeiro/Falso (subclasse de `int`)                    | ✔️        | `True`, `False`                   | Condições, lógica                      | `True == 1` e `False == 0`; `True + True == 2`                                              |
| `NoneType`  | “Sem valor” / ausência de resultado                      | ✔️        | `None`                            | Sentinelas, parâmetros opcionais       | **Não** é `0`, `""` ou `False`; é um tipo próprio                                           |
| `str`       | Texto Unicode (sequência **imutável** de caracteres)     | ✔️        | `"Olá"`, `'A'`                    | Mensagens, I/O, parsing                | **Imutável**; indexa com `[]`; `len()` conta **code points** (cuidado com emojis compostos) |
| `bytes`     | Sequência **imutável** de bytes (0–255)                  | ✔️        | `b'ABC'`, `b'\x48'`               | Arquivos binários, redes, criptografia | É **binário**, não texto; converta com `.decode()`/`.encode()`                              |
| `bytearray` | Sequência **mutável** de bytes                           | ❌         | `bytearray(b'ABC')`               | Edição de buffers binários             | Mesmas conversões de `bytes`                                                                |

> ⚠️ Em Python, tudo é objeto. “Primitivo” não é uma categoria oficial da linguagem; usamos, na prática, as ideias de “embutido” (built-in) e “imutável vs mutável”.

## 2.2.1. 🧵 Strings (detalhes que importam)

Strings são sequências imutáveis de caracteres Unicode.
Isso significa que cada caractere tem um índice (posição) e pode ser acessado usando colchetes []. Você acessa posições com colchetes [] e pode fatiar com [início:fim:passo].
### 📌 Exemplo prático:
```python
texto = "Bom dia"
print(texto[0])    # B (primeiro caractere)
print(texto[1:3])  # om (fatiamento de índice 1 até 2)
print(texto[-1])   # a (último caractere)
print(s[::-1])     # string invertida (cuidado com emojis compostos)
s = "X" + s[1:]  # correto: cria uma nova string
```
### ❗ Imutabilidade: você não pode alterar um caractere “no lugar”:
```python
# s[0] = "X"   # ERRO: TypeError (string é imutável)
```
Texto x Binário
Texto (str) precisa de codificação ao virar bytes:
```python
b = "café".encode("utf-8")   # b'caf\xc3\xa9'
print(b.decode("utf-8"))     # 'café'
```
Use str para mensagens humanas e bytes/bytearray para dados binários.
### 🔧 Métodos úteis em strings
```python
texto = "Bom Dia"
print(texto.upper())         # BOM DIA
print(texto.lower())         # bom dia
print(texto.count('o'))      # 1
print(texto.replace("Bom", "Ótimo"))  # Ótimo Dia
print(len(texto))            # 7
```
**🧠 Python x Java: “String é primitiva?”**
- **Java:** tem tipos primitivos (ex.: int, double, boolean, char) e tipos de referência (objetos). String não é primitivo; é um objeto imutável da classe String. Existe string pool/interning.
- **Python:** não usa a distinção “primitivo vs referência”. Tudo é objeto. str é um tipo embutido, imutável e onipresente, mas não é “primitivo” no sentido de Java.

> Em Python falamos em tipos embutidos e imutáveis/mutáveis; em Java, falamos em primitivos x objetos.

## 2.2.2.🔢 Inteiros (int)

O que são?
Números inteiros, positivos ou negativos, sem parte decimal.
São valores discretos, ideais para contagem, índices, classificação e enumeração.

```python
n = 42
print(n.bit_length())       # 6 → número de bits necessários
print(n.to_bytes(2, 'big')) # b'*' → representação em bytes
print((-7).bit_count())     # 3 → bits em complemento de dois
```
>**Aplicações comuns:**
Contar itens (ex.: número de alunos em uma sala).
Índices de listas (lista[0], lista[1], …).
Operações aritméticas exatas (somar, subtrair).
Representação de categorias (1 = sim, 0 = não).

```python
# Exemplo prático: contagem de alunos
alunos_presentes = 25
alunos_faltaram = 5
total = alunos_presentes + alunos_faltaram
print("Total de alunos:", total)  # 30
# Métodos úteis
n = 42
print(n.bit_length())       # 6 → bits necessários para representar 42
print(n.to_bytes(2, 'big')) # b'\x00*' → representação em bytes
print((-7).bit_count())     # 3 → número de bits '1' em |7|
```

## 2.2.3.🔣 Floats (float)
O que são?
Números em ponto flutuante, com parte decimal.
Representam valores contínuos — usados em medidas, cálculos científicos e aproximações.

```python
x = 3.5
print(x.is_integer())        # False
print(x.as_integer_ratio())  # (7, 2)
print(x.hex())               # '0x1.cp+1' → forma hexadecimal
```
> **Aplicações comuns:**
Medidas (altura, peso, temperatura).
Taxas e proporções (velocidade, juros, média).
Cálculos científicos e estatísticos.
```python
# Exemplo prático: calcular média
notas = [7.5, 8.0, 6.8]
media = sum(notas) / len(notas)
print("Média:", media)  # 7.433...

# Métodos úteis
x = 3.5
print(x.is_integer())        # False (não é inteiro)
print(x.as_integer_ratio())  # (7, 2) → fração equivalente
print(x.hex())               # '0x1.cp+1' → forma hexadecimal
```
> **⚠️ Atenção:** Floats têm imprecisão binária:
```python
print(0.1 + 0.2)  # 0.30000000000000004
```

## 2.2.4.⚙️ Booleanos (bool)
O que são?
Um tipo especial que representa apenas dois valores: True e False.
Internamente, são tratados como 0 e 1 (subclasse de int).

```python
flag = True
print(int(flag))   # 1 – True se comporta como 1
print(not flag)    # False – negação lógica
a = None
print(bool(a))     # False – teste de valor lógico
```
> **Aplicações comuns:**
 Controle de fluxo (if, while).
 Condições lógicas (comparações).
 Representar estados binários (ligado/desligado, sim/não, 0/1).
```python
# Exemplo prático: verificar maioridade
idade = 20
maior_de_idade = idade >= 18
print(maior_de_idade)   # True
print(int(maior_de_idade))  # 1

# Operações lógicas
flag = True
print(not flag)        # False
print(True and False)  # False
print(True or False)   # True
```
## 2.3.🔄 Conversão de Tipos (Casting)
| Função         | Converte para   | Exemplo         | Resultado |
| -------------- | --------------- | --------------- | --------- |
| `int(x)`       | inteiro         | `int("7")`      | `7`       |
| `float(x)`     | ponto flutuante | `float("3.14")` | `3.14`    |
| `str(x)`       | string          | `str(42)`       | `'42'`    |
| `bool(x)`      | booleano        | `bool(0)`       | `False`   |
| `complex(a,b)` | complexo        | `complex(2,3)`  | `(2+3j)`  |

## 🏷️ Nomeação e Atribuição de Variáveis

Identificadores podem conter letras, dígitos e underscores (_), mas não podem começar com dígito.
```python
Variáveis em Python armazenam referências:
x = 5      # x → 5
y = x      # y também aponta para 5
x = 7      # agora x → 7, mas y continua → 5
```
> Não use palavras reservadas (for, while, class, etc.) nem nomes de tipos (list, int, etc.).

## 2.4.📦 Tipos Estruturados (Contêineres – visão rápida)

| Categoria         | Tipo        | Exemplo literal     | Propriedade principal       |
| ----------------- | ----------- | ------------------- | --------------------------- |
| Sequência         | `list`      | `[1, 2, 3]`         | Mutável, ordenada           |
| Sequência         | `tuple`     | `(1, 2, 3)`         | Imutável, ordenada          |
| Mapeamento        | `dict`      | `{"a": 1}`          | Pares chave–valor           |
| Conjunto          | `set`       | `{1, 2, 3}`         | Elementos únicos, sem ordem |
| Conjunto imutável | `frozenset` | `frozenset({1, 2})` | Pode ser usado como chave   |
| Bytes mutáveis    | `bytearray` | `bytearray(b'ABC')` | Sequência mutável de bytes  |
- ✅ Exemplos Corretos
```python
idade       = 30                 # int
altura      = 1.75               # float
nome        = "Maria"            # str
ativo       = True               # bool
temperatura = None               # NoneType
valores     = [1, 2, 3]          # list
dimensoes   = (1920, 1080)       # tuple
config      = {"tema": "escuro"} # dict
ids_unicos  = {101, 102, 103}    # set
pacote      = b"\x48\x49"        # bytes
z           = 2 + 3j             # número complexo
```
- ❌ Exemplos Incorretos
```python
30 = idade          # Não pode atribuir a um literal
nome! = "João"      # Identificador inválido – contém "!"
float = 3.14        # Sobrescrevendo tipo interno – evite!
```
