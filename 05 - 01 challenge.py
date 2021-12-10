"""
    Criar variável para nome (string), idade (int), altura (float) e peso (float)
    Criar variável para o ano atual (int)
    Obter o ano de nascimento da pessoa (a partir da idade e ano atual)
    Obter o IMC (peso / altura²) com 2 casas decimais
    Exibir um texto com todos os valores na tela usando F-Strings
"""
from datetime import date

name = "Raphael"
age = 38
height = 1.8
weight = 97.5
current_year = date.today().year
birth = current_year - age
imc = weight / height ** 2

print(f'{name} tem {age} anos e {height} altura.')
print(f'{name} pesa {weight} e seu imc é {imc:.2f}.')
print(f'{name} nasceu em {birth}')