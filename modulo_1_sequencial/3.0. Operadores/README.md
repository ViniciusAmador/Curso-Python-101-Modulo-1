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
# *📘Módulo 1: Conceitos elementares e a Programação Sequencial - 3.0 Operadores*
Navegue pelos diretórios do curso!! 📍
```
python101/
    └──Módulo 1/
          ├── 0.0-Nivelamento de Conceitos/
          ├── 1.0-Sintaxe Básica/
          ├── 2.0-Variáveis/
          ├── 3.0-Operadores (📍Você está aqui)/
          │     ├── 3.1-Operadores-Aritméticos/
          │     ├── 3.2-Operadores-Relacionais/
          │     ├── 3.3-Operadores-Lógicos/
          │     ├── 3.4-Operadores-de-Atribuição/
          │     └── 3.5-Operadores-Binários/
          ├── 4.0-Expressões/
          ├── 5.0-Entrada e Saída/
          └── 6.0-Exercícioss/
```
## 🐍 Unidade 3 – Operadores em Python

Operadores executam ações sobre variáveis e valores literais. Dominar seu uso permite construir expressões, tomar decisões e transformar dados.

### 🎯 Estilo & Boas Práticas

Coloque um espaço de cada lado do operador para melhor legibilidade:

a = b + c — e não a=b+c.

> Use parênteses para esclarecer expressões complexas:
total = (a + b) * c.

> Evite colocar muitas operações em uma mesma linha se isso prejudicar a clareza — quebre em várias linhas quando necessário.
---
### 3.1 🔢 Operadores Aritméticos
Usados para cálculos matemáticos.

| Operador | Exemplo  | Significado               |
| -------- | -------- | ------------------------- |
| `+`      | `3 + 2`  | Adição                    |
| `-`      | `5 - 1`  | Subtração                 |
| `*`      | `4 * 2`  | Multiplicação             |
| `/`      | `8 / 4`  | Divisão real (float)      |
| `//`     | `9 // 2` | Divisão inteira (floor)   |
| `%`      | `9 % 2`  | Resto da divisão (módulo) |
| `**`     | `2 ** 3` | Exponenciação             |

#### 📌 Aplicação prática:calcular o preço total de compras ou verificar se um número é par (x % 2 == 0).
```python
# Cálculo de compras
preco_unitario = 5
quantidade = 3
total = preco_unitario * quantidade  # 15

# Verificar se o total é par
print(total % 2 == 0)  # False
```
#### 👉 Strings também usam operadores:
```python
nome = "Ana" + " Silva"
print(nome)         # Ana Silva
print("Ha" * 3)     # HaHaHa
```
---
### 3.2 🔍 Operadores Relacionais (Comparação)

Usados para comparar valores.

| Operator | Example | Evaluates to |
| -------- | ------- | ------------ |
| `==`     | `5 == 5`| `True`       |
| `!=`     | `5 != 3`| `True`       |
| `>`      | `7 > 4` | `True`       |
| `<`      | `3 < 5` | `True`       |
| `>=`     | `6 >= 6`| `True`       |
| `<=`     | `2 <= 4`| `True`       |

#### 📌 Aplicação prática:
```python
idade = 18
print(idade >= 18)   # True (pode dirigir)
print("Ana" < "João") # True (ordem alfabética)
```
---
### 3.3 🧠 Operadores Lógicos
Combinam expressões booleanas.

| Operador | Expressão        | Resultado |
| -------- | ---------------- | --------- |
| `and`    | `True and False` | `False`   |
| `or`     | `True or False`  | `True`    |
| `not`    | `not True`       | `False`   |

#### 📌 Aplicação prática:
```python
logado = True
tem_token = False

if logado and tem_token:
    print("Acesso liberado")
else:
    print("Acesso negado")
```
### 3.4 ⚙️ Operadores de Atribuição (compostos)
Permitem atualizar valores de forma mais concisa.
| Sintaxe  | Equivalente a | Uso comum         |
| -------- | ------------- | ----------------- |
| `x += 1` | `x = x + 1`   | Incrementar       |
| `x -= 1` | `x = x - 1`   | Decrementar       |
| `x *= 2` | `x = x * 2`   | Escalar / repetir |
| `x //=2` | `x = x // 2`  | Divisão inteira   |

#### 📌 Aplicação prática:
```python
contador = 0
contador += 1   # contador = 1
contador *= 5   # contador = 5
```
### 3.5 🗜️ Operadores Binários (bit a bit)
Atuam sobre a representação binária de inteiros.

| Operador | Exemplo  | Significado             |     |              |
| -------- | -------- | ----------------------- | --- | ------------ |
| `&`      | `a & b`  | AND bit a bit           |     |              |
| \`       | \`       | \`a                     | b\` | OR bit a bit |
| `^`      | `a ^ b`  | XOR                     |     |              |
| `~`      | `~a`     | NOT (inversão)          |     |              |
| `<<`     | `a << n` | Desloca bits à esquerda |     |              |
| `>>`     | `a >> n` | Desloca bits à direita  |     |              |

#### 📌 Aplicação prática:
```python
a = 6   # 110 em binário
b = 3   # 011 em binário
print(a & b)   # 2 (010)
print(a | b)   # 7 (111)
print(a ^ b)   # 5 (101)
print(a << 1)  # 12 (1100)
```
#### 🚩 Cuidados Importantes
String + número gera erro:

```python
print("Idade: " + 25)  # ❌ TypeError
print("Idade: " + str(25))  # ✅
```
- Respeite precedência dos operadores: ** > * / // % > + - > comparações > not > and > or.
- Use parênteses para clareza.
```python
total = (2 + 3) * 4
```