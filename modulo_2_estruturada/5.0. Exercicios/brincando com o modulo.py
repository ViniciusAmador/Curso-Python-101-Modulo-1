# Fixando e nomeando valores de entrada em variáveis
discreta = 33 # int
continua = 1.76 # float # ponto e não vírgula, porque esta notação é EUA
string = "Vinicius" # str alfanuméricos entre áspas
aula = True # armazena bits escritos como True e False
# quatro variáveis primitivas que armazenam valores de tipo: discretos, contínuo, lógicos, e alfanuméricos
# Variáveis tem nome, valor, e ocupam um espaço na memória (RAM)
faculdade = str(input("Digite o nome da sua faculdade:"))
# Regras  para print "" exibe integralmente o que está entre áspas, fora eu posso chamar a variável
print(aula) # exibe o valor armazenado na variável lógica
print(type(aula)) # mostrará o tipo de variável que foi armazenada
print("Olá,", string, "você está", "ativo como professor" if aula else "inativo como professor", "seu email sugerido é:", string.lower() + "@gmail.com") # operdor ternário
print("Você tá dando aula na:", faculdade)

Construindo uma expressão:

a = 24 #pode ser um número
b = 33**24 #numeros + operadores
c = a*b #expressão aritmética
print(c)
