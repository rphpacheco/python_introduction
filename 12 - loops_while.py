'''
    LOOPS -> WHILE, FOR, FOR EACH
'''
# While -> Executa um laço de repetição, 
# onde uma determinada condição seja verdadeira
# Requisitos: Condições e Operadores

# while True:
#     # Executa o bloco de código
#     # Loop infinito
#     nome=input('Qual o seu nome?: ')
#     print('Olá, {}!'.format(nome))

# print('Fim do programa!') # Nunca será executado
###############################################################################

# x=0

# while x < 10:
#     print(x)
#     x+=1 # x = x + 1
# else:
#     print('Fim do loop!')
# print('Fim do programa!')
###############################################################################

# while x < 10:
#     if x == 5 or x == 7:
#         print("#")
#         x+=1
#         continue # Pula para o próximo laço

#     print(x)
#     x+=1 # x = x + 1

#  print('Fim do programa!')
###############################################################################
# x=0

# while x < 10:
#     if x == 5:
#         print("#")
#         x+=1
#         break # Finaliza o laço

#     print(x)
#     x+=1 # x = x + 1

# print('Fim do programa!')
###############################################################################

# x=0

# while x < 10:
#     print(x)
#     x+=1 # x = x + 1
# else:
#     print('Fim do loop!')
# print('Fim do programa!')
###############################################################################

# x=0  # coluna
# y=0  # linha

# while x < 10:
#     while y < 10:
#         if y == 0:
#             print("|", end="")
#         print(f'{y}', end='|') # end='' -> não quebra a linha
#         y+=1
#     print()  # pula para a próxima linha
#     x+=1
#     y=0
###############################################################################

# ITERAR SOBRE UMA STRING
nome = 'Geek University'
lenght = len(nome)
count = 0
new_string = ''

# while count < lenght:
#     print(nome[count])
#     count += 1

while count < lenght:
    new_string += nome[count]
    print(new_string)
    count += 1


# OBS: Esta não é a melhor forma de fazer isso