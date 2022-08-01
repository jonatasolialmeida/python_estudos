"""
Manipulamdo Strings
* String indices
* Fatiamento de string [inicio:fim:passo]
* funções built-in len, abs, type, print, etc...
- essas funções podem ser usadas diretamente em cada tipo.
"""

# positivos
texto = 'Python s2'
print(texto[:6])
print(texto[-9:-3])
print(texto[0:6:2])
print(texto[::3])
print(texto[7:])
print(texto[0],texto[2],texto[4])
print(texto[-1],texto[-3],texto[-5])
print(texto[0:3],texto[0:6:2])
print(texto[:3],texto[3:],texto[:])
print(texto[::2],texto[::-1])
print(texto[::-2],texto[::-3])
url = 'https://www.google.com.br/'
print(url[:-1])
nova_string = url[12:18]
print(nova_string)

# funções built-in
print(len(texto))

