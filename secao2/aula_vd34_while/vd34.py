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

x = 0
while x < 10:
    # chegou no 3 ele pula para o 4 e não imprime o 3
    if x == 3:
        x+=1
        continue  # pula para o próximo laço (quando passou a valer 3, ele acrescentou 1 e passou a valer 4) e não printou a linha debaixo print(x) ele voltou lá para cima no while x < 10
    print(x)
    x += 1
print('Fim')