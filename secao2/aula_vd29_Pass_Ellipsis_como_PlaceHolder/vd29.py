"""
Pass Ellipsis como PlaceHolder
Pass é um placeholder para um valor que não é utilizado.
Ellipsis é um placeholder para um número indefinido de valores.
"""

# Exemplo 1:
valor = True

if valor:
    pass
else:
    print('Não vai mostrar nada porquê o valor é True, mas como Pass é um placeholder, não vai mostrar nada')

valor = False

if valor:
    print('Não vai mostrar nada porquê o valor é False, mas como Pass é um placeholder, não vai mostrar nada')
else:
    pass

# Exemplo 2: Ellipsis
valor = True

if valor:
    ...
else:
    print('Não vai mostrar nada porquê o valor é True, mas como ellipsis é um placeholder, não vai mostrar nada')