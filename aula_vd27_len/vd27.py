"""
len >> retorna o tamanho de uma string
len() << só pode ser utilizado com strings
"""
# usuario = input('digite seu usuario: ')
# # Ao usar len(), a tipagem que retorna é um inteiro (int)
# qtd_caracteres = len(usuario)

# # print('usuario:',usuario,'\nquantidade de caracteres:', qtd_caracteres,'\ntipagem:', type(qtd_caracteres))

# if qtd_caracteres < 6:
#     print('Você precisa digitar pelo menos 6 caracteres')
# else:
#     print('Usuário validado com sucesso"')


# Outro exemplo

string1 = input('Digite algo: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade de caracteres digitados foi: {len(string1) + len(string2)}')