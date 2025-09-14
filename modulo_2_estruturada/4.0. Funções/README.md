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
    ├── 3.0. Estruturas de Repetição (visão geral)/
    └── 4.0. Funções(📍Você está aqui)/
```
# 📘 Módulo 2: Conceitos elementares e a Programação Estruturada  

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
