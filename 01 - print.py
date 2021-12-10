print("Hello World!")

# COMENTÁRIO DE APENAS 1 LINHA

''' DOCSTRINGS
    VARIÁVEIS SÃO VALORES DEFINIDOS E GUARDADOS EM ALGUM LUGAR DA MEMÓRIA DO COMPUTADOR, ONDE ESTE
    VALOR SERÁ UTILIZADO PARA ALGUM TIPO DE OPERAÇÃO
'''

print(123456)
#print(alguma coisa)
##################################################################################################

#print('Este valor é uma 'cadeia' de (caracteres)')
print('Este valor é uma \'cadeia\' de (caracteres)')
print("Este valor é uma 'cadeia' de (caracteres)")
##################################################################################################

print('Este valor é uma cadeia de \n (caracteres)')
print(r'Este valor é uma cadeia de \n (caracteres)')
##################################################################################################

print("Raphael", ", Analista de BI na", "Neoway Business Solutions")
print("Raphael", ", Analista de BI na", "Neoway Business Solutions", sep='-')
print("Raphael", ", Analista de BI na", "Neoway Business Solutions", sep='|', end='')
print('')

# EXERCICIOS PRINTAR UM CPF SEM COLOCAR EXPLICITAMENTE A MASCARA NOS ARGUMENTOS
# 824.176.070-18

##################################################################################################
print('824','176','070', sep='.', end='-')
print('18')