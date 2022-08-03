"""
while:
    utilizado para repetir um bloco de código enquanto uma condição for verdadeira.
"""

# Exemplo 1

# while True:  # loop infinito
#     nome = input("Digite seu nome, ou sair para finalizar: ")
#     print("Olá, {}".format(nome))
#     print('-' * 20)
#     if nome == 'sair':
#         break

# Exemplo 2

# x = 0
# while x < 10:
#     print(x)
#     x += 1
#     if x == 5:
#         break  # para o loop e sai do while

# Exemplo 3

# x = 0
# while x < 10:
#     # chegou no 3 ele pula para o 4 e não imprime o 3
#     if x == 3:
#         x+=1
#         continue  # pula para o próximo laço (quando passou a valer 3, ele acrescentou 1 e passou a valer 4) e não printou a linha debaixo print(x) ele voltou lá para cima no while x < 10
#     print(x)
#     x += 1
# print('Fim')

# x = 0 # col

# while x <= 10:
#     y = 0 # linha
#     x += 1
#     if x == 11:
#         break
#     while y < 5:
#         y += 1
#         print(x,y)

# Exemplo Calculadora

x = 0
while True:
    contador = 0
    print()
    if x == 0:
        num1  = input('Digite um número: ')
        x+=1
    else:
        contador += total
        print(contador)
    operador = input('Digite um operador ( + - / *): ')
    if operador not in '+-/*':
        print('Operador inválido!\n Os Operadores são:\n (+) = soma\n (-) = subtração\n (/) = divisão\n (*) = multiplicação')
        continue
    num2 = input('Digite outro número: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Não é um número')
        continue

    num1 = int(num1)
    num2 = int(num2)

        # na primeira vez que o usuário digita um número ele é armazenado na variável num1 e os calculos são feitos com num1
        # na segunda vez os cálculos precisam ser feitos com o último total
    if operador == '+':
        total = num1 + num2
        print(f'{num1} + {num2} =',total)
    elif operador == '-':
        total = num1 - num2
        print(f'{num1} - {num2} =',total)
    elif operador == '*':
        total = num1 * num2
        print(f'{num1} * {num2} =',total)
    elif operador == '/':
        total = num1 / num2
        print(f'{num1} / {num2} =',total)