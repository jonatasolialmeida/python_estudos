"""
TIPOS DE DADOS
str - string - textos 'assim' ou "assim"
int - inteiro - 123456 - 0 - 10 - 20 - 1500
float - real/ponto flutuante - 1.2345 - 0.1 - 0.2 - 0.3
bool - booleano - True - False 10 == 10
"""

print(   type(10)  )
print(   type(10.5)  )
print(   type('john')  )
print(   type(True)  )

print(bool(10))
print(bool(0))
print(bool(''))
print(bool('arthur'))
print(bool(None))
print(bool([]))
print(bool({}))

# CONVERSÕES

# converteu str para int
print(type('10'), type(int('10')))

# converteu str para float
print(type('10.5'), type(float('10.5')))

# converteu str para bool
print(type('True'), type(bool('True')))

# converteu int para str
print(type(10), type(str(10)))

# converteu float para str
print(type(10.5), type(str(10.5)))

# converteu bool para str
print(type(True), type(str(True)))

# Problemas de conversão

# error de conversão
print( int('luiz'))
print( int('10.5'))

# conversão certa
print( int('10'))
print( float('10.5'))