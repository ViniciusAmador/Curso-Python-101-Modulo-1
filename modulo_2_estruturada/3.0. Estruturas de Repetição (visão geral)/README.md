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
    ├── 2.0. Conceitos elementares e a Programação Estruturada
    |           ├── 2.1. O que é Programação Estruturada?/
    |           ├── 2.2. Fluxo de Processos/
    |           └── 2.3. Estruturas de Decisão/
    |                    ├── 2.3.1. Decisão Simples (`if`)/
    |                    ├── 2.3.2. Decisão Composta (`if ... else`)/
    |                    ├── 2.3.3. Decisão Encadeada (`if ... elif ... else`)/
    |                    ├── 2.3.4. Decisão Aninhada (`if` dentro de `if`)/ 
    |                    └── 2.3.5. Operador Ternário/
    ├── 3.0. Estruturas de Repetição (visão geral)(📍Você está aqui)/
    └── 4.0. Funções/
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
## 🔎 Como funciona o `for` em Python?
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
## 🔁 Diferença entre `for` e `while`
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

## 4.0. Funções  

As funções são blocos de código que realizam uma tarefa específica. Elas evitam repetição e tornam o programa mais organizado.  

### Estrutura de uma função  
```python
def nome_da_função(parâmetros):
    instruções
    return valor_opcional
```

### Exemplos  

- Função sem parâmetros:  
```python
def saudacao():
    print("Olá, bem-vindo(a)!")
```

- Função com parâmetros e retorno:  
```python
def soma(a, b):
    return a + b

print(soma(5, 3))  # saída: 8
```

- Função com valor padrão:  
```python
def boas_vindas(nome="Visitante"):
    print(f"Olá, {nome}!")
```

- Escopo de variáveis:  
```python
x = 10  # variável global

def exemplo():
    y = 5  # variável local
    print("Dentro da função:", x, y)

exemplo()
print("Fora da função:", x)
```
---
