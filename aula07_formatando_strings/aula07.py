"""
Formatação de strings
f-strings
colocamos f'antes da string' para formatá-la
EXEMPLO
print(f'{nome} tem {idade} anos e seu imc é {imc}')
"""

nome = 'João'
idade = 20
imc = 20.5

print(f'{nome} tem {idade} anos e seu imc é {imc}')

imc2 = 20.554164841
print(f'{nome} tem {idade} anos e seu imc é {imc2:.2f}') # 2 casas decimais após a vírgula (:.2f)

# também temos format()
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc2))

"""
nesse formato também podemos usar parametros nomeáveis
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc2))
"""

# Exemplo com parametros nomeáveis
print('{nm} tem {id} anos e seu imc é {im:.2f}'.format(nm=nome, id=idade, im=imc2))