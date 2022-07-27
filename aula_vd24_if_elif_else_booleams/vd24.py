"""
CONDIÇÕES if, elif, else
"""

if True:
    print("Verdadeiro")

if False:
    print("Verdadeiro")
print("Talvez essa não seja tão verdadeira")

if False == False:
    print("Uma Verdadeira falsidade")

if True == False:
    print("Verdadeiro")
else:
    print("Falsário")

print()
print('OUTROS EXEMPLOS')
print()

if False:
    print("Verdadeiro")
elif False:
    print("Verdadeiro")
elif True:
    print("Verdadeiro")
else:
    print("Falsário")

print()
print('OUTROS EXEMPLOS')
print()

if False:
    print("Verdadeiro")
elif True:
    print("Verdadeiro")
elif False:
    print("Nem vem que não têm")
else:
    print("Aqui nem se fala")

print()
print('OUTRO GATO')
print()

if False:
    print("Verdadeiro")
elif False:
    print("Verdadeiro")
elif False:
    print("Verdadeiro")
else:
    print("Falsário é a mãe")

print()
print('O GATO DO OUTRO')
print()

if False:
    print("Verdadeiro")
elif True:
    print("Verdadeiro")
    print(1+1)
    nome = input("Que nome você quer dar ao gato? ")
    print("O gato chama-se " + nome)
    if nome == "Felix":
        print("Felix é o nome do gato")
elif False:
    print("Verdadeiro")
else:
    print("Falsário é a mãe")


