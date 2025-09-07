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
          ├── 0.0. -Nivelamento de Conceitos (📍Você está aqui)/
          |           ├── 0.1. Pensamento Computacional
          |           ├── 0.2. Máquina de Von Neumann
          |           ├── 0.3. Linguagens de Programação
          |           └── 0.4. Linguagem Compilada x Interpretada
          ├── 1.0.0. -Sintaxe Básica/
          ├── 1.1.0.-Variáveis/
          ├── 1.2.0.-Operadores/
          ├── 1.3.0.-Expressões/
          ├── 1.4.0.-Entrada e Saída/
          └── 1.5.0.-Exercícios/
```
## 0.0. - **Nivelamento de Conceitos**
---

Este módulo apresenta os fundamentos teóricos que servem de base para o estudo da programação.
## 📌 0.1. Pensamento Computacional
O pensamento computacional é a habilidade de resolver problemas de forma sistemática, estruturada e eficiente, semelhante à forma como os computadores processam informações. 
#### Ele é composto por quatro pilares principais:
- **Decomposição** – dividir um problema complexo em partes menores e mais fáceis de resolver.
- **Reconhecimento de Padrões** – identificar semelhanças ou repetições que ajudam a simplificar o problema.
- **Abstração** – focar apenas nos aspectos essenciais, ignorando detalhes desnecessários.
- **Algoritmos** – criar uma sequência de passos para resolver o problema.

> 🔎 Exemplos do Cotidiano
> #### Organizar um lanche
> - Decomposição: separar ingredientes (pão, queijo, presunto).
> - Algoritmo: 1. Cortar o pão → 2. Colocar queijo → 3. Adicionar presunto → 4. Fechar o pão.
> #### Calcular troco em uma compra
> - Decomposição: identificar valor pago e valor da compra.
> - Algoritmo: Subtrair → decidir quantidade de cédulas/moedas.
Essas ideias são a base da lógica que usaremos em programação.
>   

## 📌 0.2. Máquina de Von Neumann
A arquitetura de Von Neumann é a estrutura clássica dos computadores modernos. 
#### Ela é formada por três etapas fundamentais:
- **Entrada** – dados que entram no sistema (teclado, mouse, sensores, arquivos).
- **Processamento** – a CPU interpreta e processa as instruções.
- **Saída** – o resultado exibido para o usuário (tela, impressora, som, etc.).

## 📌 Esquema Simplificado:
Entrada  →  Processamento  →  Saída
```python
💻 Exemplo em Python
# Entrada
nome = input("Digite seu nome: ")
# Processamento
mensagem = f"Olá, {nome}! Bem-vindo ao curso."
# Saída
print(mensagem)
```

>➡️ O usuário digita (entrada), o computador organiza a informação (processamento) e mostra o resultado (saída).


## 📌 0.3. Linguagens de Programação

Uma linguagem de programação é um conjunto de regras que permite que seres humanos escrevam instruções compreensíveis pelo computador.

#### 🔎 Por que existem?
Para traduzir o raciocínio humano em instruções que o computador consiga executar.
Para resolver problemas de forma automatizada.
#### 📖 Breve Histórico
- Assembly (baixo nível) – linguagem próxima do código de máquina.
- C (1972) – trouxe portabilidade e ainda é a base de muitos sistemas.
- Python (1991) – linguagem de alto nível, simples e legível.
- Java (1995) – orientada a objetos, amplamente usada em sistemas corporativos.

## ⚙️ 0.4  Linguagem Compilada x Interpretada
##### Compiladas (C, C++): precisam ser traduzidas para código de máquina antes de executar.
- ✅ Mais rápidas
- ❌ Processo de compilação mais demorado
##### Interpretadas (Python, JavaScript): são lidas e executadas linha a linha por um interpretador.
- ✅ Mais fáceis de testar e depurar
- ❌ Geralmente mais lentas
- ✅ Resumo do Módulo 0

> - Pensamento Computacional: decomposição, padrões, abstração e algoritmos.
> - Máquina de Von Neumann: entrada → processamento → saída.
> - Linguagens de Programação: histórico, por que existem e diferença entre compiladas e interpretadas.
---