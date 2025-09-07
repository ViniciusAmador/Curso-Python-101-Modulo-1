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

>Referências adicionais podem ser encontradas em: [w3schools.com/python](https://www.w3schools.com/python/default.asp).  
Para estudantes de língua portuguesa, recomendamos a [Comunidade Python Brasil](https://python.org.br/), que promove aprendizado e colaboração.
---
# *📘Módulo 1: Conceitos elementares e a Programação Sequencial - 1.0. Sintaxe Básica*
Navegue pelos diretórios do curso!! 📍
```
python101/
    └──Módulo 1/
          ├── 0.0.-Nivelamento de Conceitos/
          ├── 1.0.-Sintaxe Básica (📍Você está aqui)/
          |          ├── 1.1. Primeiro Código
          |          ├── 1.2. Regras de Linguagens de Programação
          |          ├── 1.3. Comentários com `#` ou `'`
          |          ├── 1.4. Exemplos de paradigmas
          |          ├── 1.5. Regras lógicas e sintáticas
          |          └── 1.6. Boas Práticas: Camel Case e Nomes de Variáveis
          ├── 1.1-Variáveis/
          ├── 1.2-Operadores/
          ├── 1.3-Expressões/
          ├── 1.4-Entrada e Saída/
          └── 1.5-Exercício/
```
## 1.0. Sintaxe Básica do Python
---
## 🐍 1.1. Primeiro Código
🔹 Em um simulador como GDB ou Python online digite:
```python
print("Hello, World!")
```
Esse é o clássico primeiro programa em qualquer linguagem de programação.
> Ele imprime `(print)` uma mensagem `("mensagem")` na tela.
---
## ✍️ 1.2. Regras de Linguagens de Programação
- No Python, a identação é obrigatória. Ela define os blocos de código.
- Um bloco começa automaticamente após dois pontos : seguidos de Enter.
> A convenção é usar 4 espaços (ou um único Tab), mas nunca misture os dois no mesmo arquivo!

**Exemplo correto:**
```python
if 5 > 2:
    print("Five is greater than two!")  # Correct
```
❌ Exemplo incorreto:
```python
if 5 > 2:
print("Indentation error")  # Error
```
---
## ✍️ 1.3. Comentários com `#` ou `'`
#### 🔹 Em Python, qualquer texto após o símbolo `#` é ignorado pelo interpretador.
- Usado para explicações curtas ou desativar uma linha.
```python
# Este é um comentário de uma linha
print("Esta linha será executada")  # Também pode ser no fim da linha
```
 Comentários ajudam a explicar o código, estruturar o raciocínio ou desativar temporariamente uma linha.
#### 🔹 Comentários de múltiplas linhas (`'''` ou `"""`)
- São criados usando aspas simples ou duplas triplas.
- Não são tecnicamente comentários, mas strings não atribuídas (sem variável associada).
- Muito usados para documentação (docstrings) ou anotações longas.
```python
'''
Este é um comentário
de múltiplas linhas
usando aspas simples
'''
print("Exemplo 1")
"""
Também podemos usar
aspas duplas triplas
para escrever várias linhas
"""
print("Exemplo 2")
```
> ⚠️ Importante: quando usados no início de funções, classes ou módulos, essas strings são interpretadas como docstrings (documentação interna).
---
> 🌎 Paradigmas, Regras Lógicas e Sintáticas
Cada linguagem de programação possui seu próprio paradigma, além de regras lógicas e sintáticas que devem ser respeitadas.
## ✍️ 1.4. Exemplos de paradigmas
- **Imperativo:** foca em como resolver o problema. Ex.: `C`, `Pascal`.
- **Orientado a Objetos (OO):** organiza o código em classes e objetos. Ex.: `Java`, `C++`, `C#`.
- **Funcional:** prioriza funções puras e imutabilidade. Ex.: `Haskell`, `Lisp`, `Scala`.
- **Lógico:** baseado em regras e fatos. Ex.: `Prolog`.
- **Multiparadigma:** permite mais de um estilo. Ex.: `Python` (suporta imperativo, OO e funcional).
### ✍️ 1.5. Regras lógicas e sintáticas
#### Cada linguagem define sua própria sintaxe (regras de escrita).
- **Em Python:** blocos definidos por identação.
- **Em C/Java:** blocos definidos por chaves `{ }`.
#### As regras lógicas determinam como o código é interpretado.
- **Em Python:** `and`, `or`, `not`.
- **Em C/Java:** `&&`, `||`, `!`.
Exemplo comparativo
🔹 Python:
```python
if idade >= 18:
    print("Maior de idade")
```
🔹 C:
```python
if (idade >= 18) {
    printf("Maior de idade");
}
```
> Apesar de ambos realizarem a mesma tarefa, a sintaxe e parte da lógica diferem entre as linguagens.
## 🎯 1.6. Boas Práticas: Camel Case e Nomes de Variáveis
| ✅ Faça     | ❌ Evite                            |
| ---------- | ---------------------------------- |
| totalPrice | total\_price em contexto CamelCase |
| userAge    | User Age (com espaço)              |
| isLoggedIn | if (palavra reservada)             |
> - Use apenas letras, números e underscores — nunca símbolos especiais como `! @ %`.
> - Não utilize palavras reservadas como `if`, `print`, `for`, `class`, etc.
> - Python é case-sensitive: `idade` ≠ `Idade`.
Essas convenções evitam erros e mantêm seu código mais legível.
---
#### ⚠️ Erros Lexicais e de Sintaxe
🔹 Erro Lexical
Ocorre quando você usa um símbolo ou palavra que não existe na linguagem.
```python
prin("Olá")   # Erro lexical: 'prin' não é reconhecido
```
🔹 Erro de Sintaxe
Acontece quando você quebra as regras de escrita do Python.
```python
if 5 > 2       # Erro de sintaxe: faltou dois pontos (:)
    print("Ok")
```
---
> ✅ Resumo:
> Neste módulo aprendemos:
> - Como escrever o primeiro programa;
> - A importância da identação obrigatória;
> - Diferença entre comentários com `#` e comentários com `'''` ou `"""`;
> - Paradigmas de programação e diferenças entre regras > lógicas e sintáticas;
> - Convenções como Camel Case e nomes válidos;
> - Diferença entre erros lexicais e erros de sintaxe.