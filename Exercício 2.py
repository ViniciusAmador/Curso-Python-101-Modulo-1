#Exercício 2:
#Vinícius Costa Amador
# Uso do Loop While
#Créditos ao colega professor Aldo Moura pela ideia didático-criativa de aplicação criada inicialmete em C

# Etapa 1 – O programa deve continuar rodando até que o usuário digite “sim”. Pergunta: Como manter o programa em execução até que o usuário queira sair?

sair = ""

while sair.lower() != "sim":
    sair = input("\nDeseja sair? Digite 'sim' para encerrar: ")

# Etapa 2 – O programa deve pedir o valor da conta. Pergunta: Como solicitar o valor da conta do usuário?

sair = ""

while sair.lower() != "sim":
    valor_conta = float(input("Digite o valor da conta: "))
    sair = input("Deseja sair? Digite 'sim' para encerrar: ")

# Etapa 3 – O valor da conta não pode ser negativo. Pergunta: Como evitar que o valor da conta seja menor que zero?

sair = ""

while sair.lower() != "sim":
    valor_conta = float(input("Digite o valor da conta: "))
    
    while valor_conta < 0:
        print("Valor não pode ser negativo.")
        valor_conta = float(input("Digite o valor da conta novamente: "))
    
    sair = input("Deseja sair? Digite 'sim' para encerrar: ")

# Etapa 4 – Devemos pedir quantos adultos e quantas crianças participaram. Pergunta: Como coletar a quantidade de adultos e crianças?

sair = ""

while sair.lower() != "sim":
    valor_conta = float(input("Digite o valor da conta: "))
    
    while valor_conta < 0:
        print("Valor não pode ser negativo.")
        valor_conta = float(input("Digite o valor da conta novamente: "))
    
    adultos = int(input("Quantidade de adultos: "))
    criancas = int(input("Quantidade de crianças: "))
    
    sair = input("Deseja sair? Digite 'sim' para encerrar: ")

# Etapa 5 – O valor da conta deve ser dividido entre os participantes, considerando que cada adulto paga por 2 partes e cada criança por 1. Pergunta: Como calcular o valor proporcional para cada um?

sair = ""

while sair.lower() != "sim":
    valor_conta = float(input("Digite o valor da conta: "))
    
    while valor_conta < 0:
        print("Valor não pode ser negativo.")
        valor_conta = float(input("Digite o valor da conta novamente: "))
    
    adultos = int(input("Quantidade de adultos: "))
    criancas = int(input("Quantidade de crianças: "))
    
    partes = adultos * 2 + criancas
    valor_parte = valor_conta / partes
    valor_adulto = valor_parte * 2
    valor_crianca = valor_parte
    
    sair = input("Deseja sair? Digite 'sim' para encerrar: ")

# Etapa 6 – Mostrar o valor por adulto e por criança. Pergunta: Como apresentar os valores finais? 

sair = ""

while sair.lower() != "sim":
    valor_conta = float(input("Digite o valor da conta: "))
    
    while valor_conta < 0:
        print("Valor não pode ser negativo.")
        valor_conta = float(input("Digite o valor da conta novamente: "))
    
    adultos = int(input("Quantidade de adultos: "))
    criancas = int(input("Quantidade de crianças: "))
    
    partes = adultos * 2 + criancas
    valor_parte = valor_conta / partes
    valor_adulto = valor_parte * 2
    valor_crianca = valor_parte

    print("\nValor por adulto:", valor_adulto)
    print("Valor por criança:", valor_crianca)

    sair = input("\nDeseja sair? Digite 'sim' para encerrar: ")

# ----------------------------------------------------------------------------------
#Vinícius Costa Amador
# Uso do Loop For

# Etapa 1 – O programa deve exibir uma sequência de números de 1 a 20.
# Pergunta: Como gerar uma sequência numérica de 1 até 20 em Python?

for numero in range(1, 21):
    print(numero)

# Etapa 2 – Agora queremos indicar quais desses números são múltiplos de 5.
# Pergunta: Como testar se um número é múltiplo de 5?

for numero in range(1, 21):
    if numero % 5 == 0:
        print(numero, "é múltiplo de 5")
    else:
        print(numero)

# Etapa 3 – Vamos melhorar a apresentação exibindo todos os resultados em uma única linha por número.
# Pergunta: Como mostrar se o número é ou não múltiplo de 5, lado a lado com o número?

for numero in range(1, 21):
    if numero % 5 == 0:
        print(numero, "- múltiplo de 5")
    else:
        print(numero, "- não é múltiplo de 5")

# Etapa 4 – Agora queremos mostrar uma contagem final de quantos múltiplos de 5 foram encontrados.
# Pergunta: Como contar apenas os múltiplos de 5 ao longo do loop?

contador_multiplos = 0

for numero in range(1, 21):
    if numero % 5 == 0:
        print(numero, "- múltiplo de 5")
        contador_multiplos += 1
    else:
        print(numero, "- não é múltiplo de 5")

print("\nTotal de múltiplos de 5 encontrados:", contador_multiplos)

