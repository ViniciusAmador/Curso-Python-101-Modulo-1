# Exercício Completo: Cadastro e Print de Usuaário
# Conteúdo: Variáveis, Expressões e Subrotina Leia e Escreva
# Vinícius Costa Amador

# Etapa A — Entrada de Dados. Objetivo: Receber os dados do usuário via input(). Teste: execute e veja se tudo é solicitado corretamente.

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
ano_atual = int(input("Digite o ano atual: "))
altura = float(input("Digite sua altura em metros: "))

# Etapa B — Processamento. Objetivo: Criar as variáveis processadas que usaremos depois. Teste: imprima cada variável separadamente para conferir se estão corretas.

# Requisitos:
# - Nome completo com iniciais maiúsculas
# - Ano de nascimento = ano atual - idade
# - Email sugerido no formato nome.sobrenome@exemplo.com (minúsculo)
# - Quantidade de letras no primeiro nome


print(
    "\n--- ETAPA B: PROCESSAMENTO ---",
    "\nNome completo:", nome.capitalize() + " " + sobrenome.capitalize(),
    "\nAno de nascimento:", ano_atual - idade,
    "\nEmail sugerido:", nome.lower() + "." + sobrenome.lower() + "@exemplo.com",
    "\nLetras no primeiro nome:", len(nome)
)

# Etapa C — Apresentação dos Dados. Objetivo: Apresentar o resumo com nome, nascimento, altura e email. 
# Requisitos:
# - Exibir os dados brutos digitados, com formatação


print(
    "\n--- ETAPA C: APRESENTAÇÃO DOS DADOS ---",
    "\nNome:", nome.capitalize(),
    "\nSobrenome:", sobrenome.capitalize(),
    "\nIdade:", idade,
    "\nAltura:", altura, "m"
)

# Etapa D — Tipos das Variáveis. Mostrar o tipo de cada variável em um único print().
# Requisitos:
# - Mostrar o tipo de cada variável em um único print()

print(
    "\n--- ETAPA D: TIPOS DAS VARIÁVEIS ---",
    "\nNome:", type(nome),
    "\nSobrenome:", type(sobrenome),
    "\nIdade:", type(idade),
    "\nAno atual:", type(ano_atual),
    "\nAltura:", type(altura),
    "\nNome completo:", type(nome.capitalize() + " " + sobrenome.capitalize())
)