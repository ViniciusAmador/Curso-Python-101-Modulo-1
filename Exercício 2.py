# Exercício sobre Estrtuturas de Decisão e Expressões Condicionais
# Vinícius Costa Amador

# Exercício: Cálculo e Classificação do IMC com Estruturas de Decisão

# Etapa 1 – O programa deve pedir o peso e a altura do usuário.
# Pergunta: Como coletar peso e altura em Python?

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Etapa 2 – O programa deve calcular o IMC.
# Pergunta: Como calcular o IMC com base no peso e na altura?

imc = peso / (altura ** 2)

# Etapa 3 – O programa deve exibir o valor do IMC calculado.
# Pergunta: Como apresentar esse valor ao usuário?

print("Seu IMC é:", imc)

# Etapa 4 – O programa deve interpretar o IMC com base em faixas classificadas.
# Pergunta: Como classificar o IMC com estruturas de decisão aninhadas?

if imc < 16:
    print("Classificação: Magreza grave")
elif imc >= 16 and imc < 17:
    print("Classificação: Magreza moderada")
elif imc >= 17 and imc < 18.5:
    print("Classificação: Magreza leve")
elif imc >= 18.5 and imc < 25:
    print("Classificação: Saudável")
elif imc >= 25 and imc < 30:
    print("Classificação: Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Classificação: Obesidade Grau I")
elif imc >= 35 and imc < 40:
    print("Classificação: Obesidade Grau II (severa)")
else:
    print("Classificação: Obesidade Grau III (mórbida)")

# -------------------------------------------------------------------
# Exercício: Encontre a ordem entre 3 números usando estruturas de decisão:

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a <= b:
    if b <= c:
        print(a, b, c)
    elif a <= c:
        print(a, c, b)
    else:
        print(c, a, b)
else:
    if a <= c:
        print(b, a, c)
    elif b <= c:
        print(b, c, a)
    else:
        print(c, b, a)

# -------------------------------------------------------------------
# Exercício: Verificação de Alistamento com Uso de Variável Lógica

# Etapa 1 – O programa deve pedir o nome, sexo, ano de nascimento e ano atual.
# Pergunta: Como coletar os dados básicos do usuário?

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (masculino/feminino): ").strip().lower()
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# Etapa 2 – O programa deve calcular a idade do usuário.
# Pergunta: Como calcular a idade com base no ano atual e de nascimento?

idade = ano_atual - ano_nascimento

# Etapa 3 – O programa deve usar uma variável lógica para indicar se é homem.
# Pergunta: Como armazenar a verificação de sexo como um valor booleano?

eh_homem = sexo == "masculino"

# Etapa 4 – O programa deve exibir os dados informados e a idade.
# Pergunta: Como mostrar ao usuário um resumo antes da decisão?

print("\nNome:", nome)
print("Idade:", idade)
print("Sexo informado:", sexo)

# Etapa 5 – O programa deve usar estruturas de decisão para verificar a situação de alistamento.
# Pergunta: Como aplicar a lógica de alistamento com base no sexo e na idade?

if eh_homem and idade == 18:
    print("Situação: Você deve se alistar no exército este ano.")
elif eh_homem and idade < 18:
    print("Situação: Você ainda não tem idade para o alistamento.")
elif eh_homem and idade > 18:
    print("Situação: Você passou da idade de alistamento obrigatório.")
else:
    print("Situação: O alistamento não é obrigatório para o seu sexo.")
