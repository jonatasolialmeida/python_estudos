"""
* Criar variáveis para nome (str), idade (int),
* altura (float), peso (float), de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
* Obter o IMC da pessoa  com 2 casas decimais (baseado no peso e altura)
* Exibir um texto com todos os valores (nome, idade, altura, peso, ano de nascimento, IMC), usando f-strings
"""

nome = "João"
idade = 30
altura = 1.75
peso = 80.5
ano_atual = 2022


print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg.')
print(f'{nome} nasceu em {ano_atual - idade}.')
print(f'{nome} tem o IMC de {peso / (altura ** 2):.2f}.')

