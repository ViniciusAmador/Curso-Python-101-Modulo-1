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
# *📘Módulo 2: Conceitos elementares e a Programação Estruturada*
Navegue pelos diretórios do curso!! 📍
```
python101/
    ├──modulo_1_sequencial/
    ├──modulo_2_estruturado/
    |           ├── 2.0. Conceitos elementares e a Programação Estruturada
    |           ├── 2.1. O que é Programação Estruturada?/
    |           ├── 2.2. Fluxo de Processos/
    |           └── 2.3. Estruturas de Decisão/
    |                    ├── 2.3.1. Decisão Simples (`if`)/
    |                    ├── 2.3.2. Decisão Composta (`if ... else`)/
    |                    ├── 2.3.3. Decisão Encadeada (`if ... elif ... else`)/
    |                    ├── 2.3.4. Decisão Aninhada (`if` dentro de `if`)/ 
    |                    ├── 2.3.5. Operador Ternário/
    |                    ├── 2.3.6. Revisitando Tabela Verdade/  
    |                    └── 2.3.7. Dedução e Lógica Proposicional/ 
    ├── 3.0. Estruturas de Repetição (visão geral)/
    |           ├── 3.1. Laço de Repetição For/ 
    |           ├── 3.2. Laço de Repetiçao While/
    |           └── 3.3. Complexidade Algoritmica em Programação Estruturada
    ├── 4.0. Funções/
    └── 5.0. Exercicios
```
# 📘 Módulo 2: Conceitos elementares e a Programação Estruturada  

## 3.0. 🔄 Estruturas de Repetição (Laços)
## 📌 O que é um laço?
Um **laço de repetição** (ou loop) é uma estrutura que permite executar um mesmo bloco de código várias vezes, de forma automática, até que uma condição seja satisfeita.  
Isso evita repetição desnecessária de instruções no programa.  

Exemplo sem laço:
```python
print(1)
print(2)
print(3)
print(4)
print(5)
```
Exemplo com laço `for`:
```python
for i in range(1, 6):
    print(i)
```
---
## 3.1. Laço de Repetição For
O `for` em Python é um laço de **iteração**: ele percorre uma sequência de valores (como uma lista, string ou intervalo de números) e executa o bloco de código para cada valor.
### Estrutura da sintaxe:
```python
for variável in sequência:
    instruções
```
- **`variável`** → recebe, a cada volta, um valor da sequência.  
- **`sequência`** → pode ser uma lista, uma string, ou um intervalo gerado pela função `range()`.  
- **`instruções`** → bloco de código que será repetido em cada volta (iteração).  
---
## 📍 Exemplo 1 – Usando `range()`
```python
for i in range(1, 6):   # começa em 1, vai até 5
    print("Valor de i:", i)
```
Saída:
```
Valor de i: 1
Valor de i: 2
Valor de i: 3
Valor de i: 4
Valor de i: 5
```
---
## 📍 Exemplo 2 – Percorrendo uma lista
```python
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print("Eu gosto de", fruta)
```
Saída:
```
Eu gosto de maçã
Eu gosto de banana
Eu gosto de uva
```
---
## 📍 Exemplo 3 – Percorrendo uma string
```python
palavra = "Python"

for letra in palavra:
    print(letra)
```
Saída:
```
P
y
t
h
o
n
```
---
## 🔁 3.2. Laço de Repetiçao While
- O **`for`** → usado quando já sabemos **quantas vezes** queremos repetir ou temos uma sequência para percorrer.  
- O **`while`** → usado quando a repetição depende de uma **condição lógica** que pode variar.  

Exemplo com `while`:  
```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```
---

## 3.3. Complexidade Algoritmica em Programação Estruturada 

A análise assintótica é o estudo do crescimento da complexidade de um algoritmo quando o tamanho da entrada aumenta.
Ela não se preocupa com valores exatos de tempo, mas com a tendência de crescimento.
Exemplos de ordens de complexidade:

- **O(1)** – constante.

- **O(log n)** – logarítmica.

- **O(n)** – linear.

- **O(n²)** – quadrática.

- **O(2ⁿ)** – exponencial.

##  Exercícios de Algoritmos Estruturados
### 3.3.1. Estrutura Sequencial (O(1))
```python
import time
def soma_constante(a, b):
    return a + b

inicio = time.time()
print(soma_constante(5, 10))
fim = time.time()
print("Tempo de execução:", fim - inicio, "segundos")
```

> 🔎 Sempre executa no mesmo tempo → complexidade O(1).

### 3.3.2. Estrutura de Repetição Simples (O(n))

```python
import time
def soma_lista(n):
    total = 0
    for i in range(n):   # loop simples → O(n)
        total += i
    return total

inicio = time.time()
print(soma_lista(1000000))
fim = time.time()
print("Tempo de execução:", fim - inicio, "segundos")
```
### 3.3.3. Estrutura Aninhada – Loop no Loop (O(n²))
```python
import time

def pares(n):
    pares = []
    for i in range(n):          # primeiro loop
        for j in range(n):      # loop dentro do loop
            pares.append((i, j))
    return pares

inicio = time.time()
print("Total de pares:", len(pares(1000)))
fim = time.time()
print("Tempo de execução:", fim - inicio, "segundos")

```
>🔎 Cresce quadraticamente → O(n²).