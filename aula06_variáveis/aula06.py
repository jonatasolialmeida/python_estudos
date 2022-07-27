"""
VARIAVEIS
Iniciar com letra, pode conter números, separar_, letras minúsculas,
"""

nome = 'João'
print(nome, type(nome))
idade = 20
print(idade, type(idade))
salario = 987.65
print(salario, type(salario))
e_maior = idade > 18
print(e_maior, type(e_maior))
peso = 80.5
altura = 1.80
imc = peso / (altura ** 2)


# variáveis guardam valores que podem ser utilizados
# em qualquer parte do código
# variáveis são declaradas com o símbolo de igual (=)

# EXEMPLO
super_salario = salario * idade
print(idade * salario)
print(super_salario)
print(nome, 'tem', idade, 'anos', 'e seu imc é', imc)	# concatenação