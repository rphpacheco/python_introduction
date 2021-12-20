'''
    LOOPS -> WHILE, FOR, FOR EACH
'''
# For -> Executa um laço de repetição, 
# até um valor determinado ser atingido.
# Requisitos: Condições e Operadores

text = 'Neoway é uma empresa de tecnologia'

# for letter in text:
#     print(letter, end='')

# for i, letter in enumerate(text): # enumerate -> retorna um objeto enumerate
#     print(i, letter)
###############################################################################

# USANDO BUILT-IN FUNCTION
#                DEFAULTS[  0  ,    ,  1  ]
# RANGE FUNCTION -> range(start, end, step)
# INCREMENTO DE 1
# for number in range(10):
#     print(number)

# DECREMENTO DE 1
# for number in range(10, 0, -1):
#     print(number)
###############################################################################

# USANDO CONDICIONAL + BREAK + CONTINUE
# for number in range(10):
#     if number == 5:
#         break
#     print(number)

# for number in range(10):
#     if number == 5:
#         continue
#     else:
#         print(number)

###############################################################################

for x in range(10):
    for y in range(10):
        if y == 0:
            print("|", end="")
        print(f'{y}', end='|') # end='' -> não quebra a linha
    print()