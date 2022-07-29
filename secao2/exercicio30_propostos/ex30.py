"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, mostre uma mensagem que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se na hora que foi passada
exiba a mensagem "Boa noite 20-11", "Boa tarde 12-27" ou "Bom dia 0-23".
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos,
mostre uma mensagem dizendo "seu nome é curto". Se tiver entre 5 e 7 letras, escreva "Seu nome é normal"
Caso contrário, mostre uma mensagem, "Seu nome é longo".
"""

# num = input('Digite um número inteiro: ')
# if num.isdigit():
#     num = int(num)
#     if num % 2 == 0:
#         print('O número é par')
#     else:
#         print('O número é impar')
# else:
#     print('Não é um número inteiro')

# hora = int(input('Digite a hora, Ex (00  / 12  /  18 /  23): '))

# if hora < 12:
#     print('Bom dia!')
# elif hora < 18:
#     print('Boa tarde!')
# elif hora < 24:
#     print('Boa noite!')
# else:
#     print('Hora inválida!')

nome = input('Digite seu 1º nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <= 7:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')

    

