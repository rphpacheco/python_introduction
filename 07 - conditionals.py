"""
    CONDIÇÕES -> IF, ELIF, ELSE
"""

if True:
    print("Hello")

    number1 = 2 + 2

    print(number1)

if False:
    print("Bye")

##################################################################################################

if False:
    print("primeira condicional")
elif True:
    print("Segunda condicional")
elif True:
    print("Mais uma verdadeira")
else:
    print("Terceira condicional")

##################################################################################################

"""
    OPERADORES RELACIONAIS -> ==, >, >=, <, <=, !=
    OBS: = -> atribuição
"""

number1 = 2
number2 = "2"

print(number1 == number2)

##################################################################################################

if number1 == number2:
    print("Os valores são iguais")
elif number1 > int(number2):
    print("number1 é maior que number2")
else:
    print("Nenhuma condição foi atendida :(")

##################################################################################################

"""
    OPERADORES LÓGICOS -> and, or, not, in, not in
"""

a = 2
b = 2
c = 3
d = 0
name = "Raphael"

print(a == b and b < c)
print(a != b or b > c)

# (Verdadeiro E Verdadeiro) = TRUE
# (Verdadeiro E Falso) = FALSE
# (Verdadeiro OU Falso) = TRUE
# (Verdadeiro OU Verdadeiro) = TRUE
# (Falso OU Falso) = FALSE
# (not) INVERTE
# (in) ESTÁ EM
print(not d)

print("R" in name)
print("T" not in name)