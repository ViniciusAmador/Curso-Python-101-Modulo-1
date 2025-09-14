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
    ├── 2.0. Conceitos elementares e a Programação Estruturada (📍Você está aqui)/
    |           ├── 2.1. O que é Programação Estruturada?/
    |           ├── 2.2. Fluxo de Processos/
    |           └── 2.3. Estruturas de Decisão/
    |                    ├── 2.3.1. Decisão Simples (`if`)/
    |                    ├── 2.3.2. Decisão Composta (`if ... else`)/
    |                    ├── 2.3.3. Decisão Encadeada (`if ... elif ... else`)/
    |                    ├── 2.3.4. Decisão Aninhada (`if` dentro de `if`)/ 
    |                    └── 2.3.5. Operador Ternário/
    ├── 3.0. Estruturas de Repetição (visão geral)/
    └── 4.0. Funções/
```
# 📘 Módulo 2: Conceitos elementares e a Programação Estruturada  

## 2.1. O que é Programação Estruturada?  
A **programação estruturada** é um paradigma que organiza o código em blocos lógicos e bem definidos, permitindo que o programa seja mais claro, confiável e fácil de manter. Diferente da programação desorganizada (chamada de “espaguete”), ela estabelece uma sequência ordenada de instruções e o uso de estruturas de controle que direcionam o fluxo do programa.  

Todo algoritmo estruturado se baseia em três pilares principais:  
1. **Sequência** → execução das instruções na ordem em que aparecem.  
2. **Decisão (Seleção)** → escolha de caminhos diferentes de acordo com uma condição lógica.  
3. **Repetição (Iteração)** → execução de um bloco de código várias vezes, enquanto uma condição for verdadeira.  
---
## 2.2. Fluxo de Processos  
O fluxo de execução em programação estruturada segue estas etapas:  

1. **Início** – o programa começa a execução.  
2. **Sequência** – as instruções são executadas linha a linha.  
3. **Decisão** – ao encontrar uma condição (`if`), o fluxo segue para um caminho (verdadeiro) ou outro (falso).  
4. **Repetição** – quando há laços (`while`, `for`), o programa retorna e repete o bloco até a condição ser falsa.  
5. **Fim** – ocorre quando não há mais instruções a executar.  

Esse fluxo pode ser representado em **fluxogramas**, onde:  
- Retângulos representam **processos**.  
- Losangos representam **decisões**.  
- Setas indicam o **caminho lógico** que o programa segue.  

---
## 2.3. Estruturas de Decisão  

### 2.3.1. Decisão Simples (`if`)  
Executa um bloco apenas se a condição for verdadeira.  
```python
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
```

### 2.3.2. Decisão Composta (`if ... else`)  
Oferece duas alternativas: uma se a condição for verdadeira e outra se for falsa.  
```python
nota = 5
if nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")
```

### 2.3.3. Decisão Encadeada (`if ... elif ... else`)  
Permite verificar várias condições em sequência.  
```python
media = 8
if media >= 9:
    print("Excelente")
elif media >= 7:
    print("Bom")
elif media >= 5:
    print("Regular")
else:
    print("Reprovado")
```

### 2.3.4. Decisão Aninhada (`if` dentro de `if`)  
Usada quando uma condição só faz sentido dentro de outra.  
```python
idade = 20
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Pode dirigir")
    else:
        print("Não pode dirigir")
else:
    print("Menor de idade")
```

### 2.3.5. Operador Ternário  
Forma compacta do `if ... else`.  
```python
idade = 17
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
```
---