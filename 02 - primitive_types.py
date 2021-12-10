"""
    TIPOS DE DADOS
    STR - STRING -> 'ISSO AQUI É UM TEXTO'
    INT - INTEIRO -> 123456 0 -10 -50 -1500 500
    FLOAT - REAL/PONTO FLUTUANTE -> 10.50 1.75 -60.93 -7.89
    BOOL - BOOLEANO/LÓGICO -> TRUE/FALSE (10 == 10 -> TRUE)
"""

# STRING
print('Raphael', type('Raphael'))
print('1' + '1', type('1' + '1'))
#print('Raphael', type('Raphael'), type(int('Raphael')))  # ERROR

# INT
print(155, type(155))
print('155', type('155'), type(int('155')))  # TYPE CASTING

# FLOAT
print(122.78, type(122.78))
print(122.78, type(122.78), float('122.78'), type(float('122.78')))

# BOOL
print(10 == 10, type(10 == 10))
print('M' == 'M'), type('M' == 'M')
print(bool(''))
print(bool(0))
print(bool('Raphael'))
##################################################################################################

print(int('155'), type(int('155')))
print(eval('155'), type(eval('155')))
print(eval('10 + 10'), type(eval('10 + 10')))