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
# *📘Módulo 1: Conceitos elementares e a Programação Sequencial - 4.0 Expressões*
Navegue pelos diretórios do curso!! 📍
```
python101/
    └──Módulo 1/
          ├── 0.0-Nivelamento de Conceitos/
          ├── 1.0-Sintaxe Básica/
          ├── 2.0-Variáveis/
          ├── 3.0-Operadores/
          ├── 4.0-Expressões (📍Você está aqui)/
          │     ├── 4.1-Ordem, Operadores e Expressões/
          │     ├── 4.2-Exemplo de Expressão Aritmética/
          │     └── 4.3-Exemplo de Expressão Booleana/
          ├── 5.0-Entrada e Saída/
          └── 6.0-Exercícioss/
```

## 🐍 Unidade 4 – Expressões em Python
Uma expressão combina valores, variáveis e operadores para produzir um único resultado.
Na prática, quase toda linha não trivial de Python que você escreve é uma expressão — ou contém uma.
---
### 4.1- 🎯 Ordem, operadores e expressões
* **Parênteses primeiro** – use-os generosamente para indicar a precedência, mesmo quando o Python resolveria corretamente sem eles.
* **Uma ideia por linha** – se uma expressão ficar muito longa, divida-a e atribua resultados intermediários a variáveis com nomes descritivos.
* **Nomes descritivos** – um bom nome de variável torna a expressão autoexplicativa.
```python
# 👍 Claro
preco_liquido = (preco_bruto - desconto) * (1 + taxa_imposto)
# 👎 Claro
preco_liquido = (preco_bruto - desconto) * (1 + taxa_imposto)
```
---
### Precedência dos Operadores (recapitulando)

`()` > `**` > `*` `/` `//` `%` > `+` `-` > comparações `>` `not` `>` `and` `>` `or`

> O Python segue a hierarquia matemática padrão; tudo que estiver dentro de parênteses é executado primeiro.
---
### 4.2- ✅ Exemplo de Expressão Aritmética
```python
resultado = 2 + 3 * 4  
print(resultado)  
```
`14, porque * tem precedência maior que +`

### 4.3- ✅ Exemplo de Expressão Booleana
```python
valido = 10 > 5 and 3 < 2
print(valido)        # False
```
>Operadores lógicos (and, or, not) podem encadear comparações para formar condições complexas.
---
### ❌ Erro Comum
```python
valor = 5 +           # SyntaxError → expressão incompleta
```
> Sempre garanta que ambos os operandos e o operador estejam presentes.
---
### 🚩 Dicas

- A divisão `/` sempre gera `float`; use `//` se precisar de `int`.
- Comparações entre strings são lexicográficas (`'abacaxi' < 'banana'` → `True`).
- Ao misturar tipos numéricos, o Python promove para o tipo mais “complexo”: `int → float → complex`.
- Uma expressão pode ser passada diretamente para funções: `print((2 + 3) * 4)`.
---
