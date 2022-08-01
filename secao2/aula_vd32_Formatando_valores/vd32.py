"""
Formatando valores com modificadores 

:s - texto (string)
:d - inteiro (int)
:f - float (float)  ou real (float)
:. (NÚMERO DE CASAS DECIMAIS) - float
: (CARACTERE) (> ou < ou ^) QUANTIDADE

> - esquerda
< - direita
^ - centralizado

:b - binário (int)
:o - octal (int)
:x - hexadecimal (int)
:% - porcentagem (float)
:e - exponencial (float)

"""

# Exemplo 1

# num1 = 10
# num2 = 3
# divisao = num1 / num2
# print(f'{num1} / {num2} = {divisao}')
# print(f'{num1} / {num2} = {divisao:.2f}')

# exemplo = 1

# print(f'{exemplo:0>10}')
# print(f'{exemplo:0<10}')
# print(f'{exemplo:0^10}')

# exemplo2 = 2050

# print(f'{exemplo2:0<15}')
# print(f'{exemplo2:0>15}')
# print(f'{exemplo2:0^15}')

# exemploo1 = 'joao'
# exemploo2 = 'joao'
# exemploo3 = 'joao'

# # mesmas funções direto na variável
# exemploo1 = exemploo1.ljust(15, '-')
# print(exemploo1)
# exemploo2 = exemploo2.rjust(15, '-')
# print(exemploo2)
# exemploo3 = exemploo3.center(15, '-')
# print(exemploo3)

# exemplo3 = 154
# print(f'{exemplo3:0<15.2f}')
# print(f'{exemplo3:0>15.2f}')
# print(f'{exemplo3:0^15.2f}')

# nome_exemplo = 'João'

# print(f'{nome_exemplo:#^10}')
# print(f'{nome_exemplo:#<10}')
# print(f'{nome_exemplo:#>10}')

# nam1 = 'Joãoz'
# nam2 = 'Joãoy'
# nam3 = 'Joãow'

# print('VARIAVEIS NOMEADAS DENTRO DO FORMAT')
# print('{n1}\n{n3}\n{n2}\n{n3}\n{n2:*<10}'.format(n1=nam1, n2=nam2, n3=nam3))
# print('VARIAVEIS POR INDICE DENTRO DO FORMAT')
# print('{0}\n{2}\n{1}\n{2}\n{1:*<10}'.format(nam1, nam2, nam3))

meu_nome = '  o  João TeXeIRa do nascimento      n  '
nome1 = meu_nome.upper()
print(nome1)
nome2 = meu_nome.lower()
print(nome2)
nome3 = meu_nome.capitalize()
print(nome3)
nome4 = meu_nome.title()
print(nome4)
nome5 = meu_nome.swapcase()
print(nome5)
nome6 = meu_nome.strip()
print(nome6)
nome7 = meu_nome.lstrip()
print(nome7)
nome8 = meu_nome.rstrip()
print(nome8)
nome9 = meu_nome.strip('n')
print(nome9)
