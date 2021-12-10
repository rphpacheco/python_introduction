''' DOCSTRINGS
    VARIÁVEIS SÃO VALORES DEFINIDOS E GUARDADOS EM ALGUM LUGAR DA MEMÓRIA DO COMPUTADOR, ONDE ESTE
    VALOR SERÁ UTILIZADO PARA ALGUM TIPO DE OPERAÇÃO
    SEUS NOMES NÃO PODEM INICIAR COM CACACTERES ESPECIAIS (EMBORA O _ POSSA) OU NÚMEROS
    ALÉM DISSO, ELAS NÃO PODEM RECEBER NOMES DE PALAVRAS RESERVADAS
    False, class, finally, is, return, None, continue, for, lambda, try, True, def, from, nonlocal
    while, and, del, global, not, with, as, elif, if, or, yield, assert, else, import, pass, break
    except, in, raise
'''
#_name = 'Raphael Pacheco'
#1name = 'Raphael Pacheco'
#print(_name)

#var atrubuição valor
name = "John Doe"  # string
age = 22  # int
height = 1.81  # float
isHuman = True  # boolean

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(isHuman, type(isHuman))
##################################################################################################

#print('My name is ' + name + ", i'm " + age + ' years old, ' + height + ' tall')  # TYPING ERROR 
print('My name is ' + name + ", i'm " + str(age) + ' years old and ' + str(height) + ' tall')
print('My name is', name, ", i'm", str(age), 'years old and', str(height), 'tall')
#F-Strings
print(f"My name is {name}, i'm {age} years old and {height:.1f} tall")
print("My name is {}, i'm {} years old and {:.1f} tall".format(name, age, height))
print("My name is {0}, i'm {0} {1} years old and {2} tall".format(name, age, height))
print("My name is {n}, i'm {a} years old and {h} tall".format(n=name, a=age, h=height))
##################################################################################################

# CONSTANTS
PROJECT_HOST = 'http://localhost'
PROJECT_PORT = '8080'
URI = PROJECT_HOST + ':' + PROJECT_PORT

print(URI, type(URI))
##################################################################################################

# MUTABLE
PROJECT_HOST = 'http://10.204.43.2'
PROJECT_PORT = '80'
URI = PROJECT_HOST + ':' + PROJECT_PORT

print(URI, type(URI))
##################################################################################################

# INCREMENT VARIABLES

count = 0
print(count)

count += 1
print(count)

count -= 1
print(count)
