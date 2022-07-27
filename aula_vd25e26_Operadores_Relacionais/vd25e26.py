"""
OPERADORES RELACIONAIS
== igualdade, >= maior ou igual, <= menor ou igual, != diferente, < menor, > maior (==, >=, <=, !=, <, >) 
"""

# Um sinal de =, estou afirmando que o valor da esquerda é igual ao da direita
# Dois sinais de (=) ou seja ==, estou "perguntando" se o valor da esquerda é igual ao da direita
# Um sinal de !=, estou afirmando que o valor da esquerda é diferente do da direita ou vice versa
# Um sinal de <, estou "perguntando" se o valor da esquerda é menor que o da direita
# Um sinal de >, estou "perguntando" se o valor da esquerda é maior que o da direita
# Um sinal de <=, estou "perguntando" se o valor da esquerda é menor ou igual que o da direita
# Um sinal de >=, estou "perguntando" se o valor da esquerda é maior ou igual que o da direita

idade = 25 # << estou afirmando que a idade é 25
mais_idade = 30
igualdade = idade == mais_idade # << estou perguntando se a idade é igual a mais_idade
print(igualdade)
menor = idade < mais_idade # << estou perguntando se a idade é menor que mais_idade
print(menor)
maior = idade > mais_idade # << estou perguntando se a idade é maior que mais_idade
print(maior)
menor_igual = idade <= mais_idade # << estou perguntando se a idade é menor ou igual que mais_idade
print(menor_igual)
maior_igual = idade >= mais_idade # << estou perguntando se a idade é maior ou igual que mais_idade
print(maior_igual)
diferente = idade != mais_idade # << estou perguntando se a idade é diferente de mais_idade
print(diferente)

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

idade_limite = 18

if idade >= idade_limite:
    print("Bem-vindo(a) {}, você pode pegar empréstimo".format(nome))
else:
    print("Bem-vindo(a) {}, mas infelizmente você não pode pegar empréstimo".format(nome))

# # OPERADORES LOGICOS
# # and, or, not
# # in (está dentro de), not in (não está dentro de)

exmp1 = 5 > 3 and 5 < 10 # << estou perguntando se 5 é maior que 3 e se 5 é menor que 10 (and)
print(exmp1)
exmp2 = 5 > 3 or 5 < 10 # << estou perguntando se 5 é maior que 3 ou se 5 é menor que 10 (or)
print(exmp2)
exmp3 = not 5 > 3 # << estou perguntando se 5 é maior que 3, e ao adicionar (not) caso seja verdadeiro, retorna falso
print(exmp3)

a = ''

if not a:
    print("A variável a está vazia")
    print('Preencha a variável a')

nome = 'João'

if 'o' in nome:
    print("O nome contém o")

if 'jofe' not in nome:
    print("O nome não contém jofe")


# Exemplo de log em sistema

nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

nome_db = 'joao'
senha_db = '123'

if nome == nome_db and senha == senha_db:
    print("Bem-vindo(a) {}, você está logado!".format(nome))
else:
    print("Nome ou senha incorretos")