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
# *📘Módulo 3: Algoritmos de Busca
Navegue pelos diretórios do curso!! 📍
```
python101/
    ├──modulo_1_sequencial/
    ├──modulo_2_estruturado/
    ├── modulo_3_estruturas_de_dados/
    ├── modulo_4_algoritmos/ (📍Você está aqui)/
    |           ├── 4.1. Conceito de Algoritmo de Busca/
    |           ├── 4.2. Abstração Clássica – “Estou pensando em um número...”/
    |           ├── 4.3. Complexidade Assintótica/
    |           ├── 4.4. Busca Linear/
    |           ├── 4.5. Busca Binária/
    |           ├── 4.6. Comparação Prática/
    |           └── 4.7. Conclusão/

```

## 4.1. Conceito de Algoritmo de Busca

Um algoritmo de busca é uma sequência de passos que tem como objetivo encontrar um elemento específico em uma coleção de dados.
Esses algoritmos são fundamentais, pois localizar rapidamente um valor é uma operação que aparece em praticamente todos os sistemas computacionais.

A eficiência do algoritmo depende do tamanho da estrutura de dados, de como os dados estão organizados (ordenados ou não) e da estratégia usada para percorrê-los.

## 4.2. Abstração Clássica — “Estou pensando em um número...”

## **Imagine o seguinte diálogo:**

— Estou pensando em um número de 1 a 10. Qual é?  
— 2  
— Não, é maior.  
— 6  
— Acertou! É 6.

Esse exemplo representa duas formas diferentes de busca:

## **🧩 Caso 1 — Sem dicas (Busca Linear)**
Se nenhuma informação for dada, a única forma é testar número por número:

1? não  
2? não  
3? não  
...  
6? sim!


Nesse caso, o algoritmo precisa percorrer todos os elementos até encontrar o valor procurado.
Chamamos isso de busca linear.

## **🧮 Caso 2 — Com dicas (Busca Binária)**
Agora, se a pessoa disser “é maior” ou “é menor”, conseguimos eliminar metade das possibilidades a cada tentativa.
Esse processo é chamado de busca binária.

Exemplo:

Chuto 5 → “é maior” → elimino 1 a 5.
Chuto 8 → “é menor” → elimino 9 e 10.
Só pode ser 6 ou 7 → chuto 6 → acertei! 🎯
Cada dica reduz o espaço de busca pela metade, tornando o processo muito mais rápido.

## 4.3. Complexidade Assintótica

A notação assintótica descreve o crescimento do tempo de execução de um algoritmo conforme o tamanho da entrada (n) aumenta.

Algoritmo	Complexidade	Interpretação
Busca Linear	O(n)	O tempo cresce proporcionalmente ao tamanho da lista
Busca Binária	O(log n)	O tempo cresce de forma logarítmica — muito mais lenta

## 4.4. Busca Linear

A busca linear (ou sequencial) percorre todos os elementos de uma lista um por um até encontrar o valor desejado.

**💡 Exemplo em Python:**
```python
def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1  # Retorna -1 se o valor não for encontrado

dados = [15, 8, 32, 47, 22, 5]
resultado = busca_linear(dados, 47)
print(f"Resultado: {resultado}")
# Saída: Resultado: 3
```

🧠 Comentário:

Funciona mesmo se a lista não estiver ordenada.
No pior caso, precisa testar todos os elementos.
Complexidade: O(n).

## 4.5. Busca Binária

A busca binária é mais eficiente, mas exige que a lista esteja ordenada.
Ela compara o valor procurado com o elemento central e decide se deve continuar à esquerda ou à direita, reduzindo a área de busca pela metade.

**💡 Exemplo em Python:**
```python
def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

dados = [5, 8, 15, 22, 32, 47]
resultado = busca_binaria(dados, 47)
print(f"Resultado: {resultado}")
# Saída: Resultado: 5
```

**🧠 Comentário:**

Funciona apenas com listas ordenadas.
Reduz o espaço de busca pela metade a cada iteração.
Complexidade: O(log n).

## 4.6. Comparação Prática
Critério	Busca Linear	Busca Binária
Estrutura necessária	Qualquer lista	Lista ordenada
Estratégia	Percorre tudo	Divide pela metade
Complexidade	O(n)	O(log n)
Melhor caso	1 comparação	1 comparação
Pior caso	n comparações	log₂(n) comparações