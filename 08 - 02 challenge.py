"""
    Sistema de empréstimos
    Objetivo é criar um programa simples que a partir de uma idade (> 18) é verificado se a pessoa
    pode ou não pegar empréstimo.
    O sistema deverá perguntar qual o valor de empréstimo
    Além disso, se a pessoa tiver idades entre 18 a 30 anos, o sistema deverá printar o juro de 2.09
    Se a pessoa tiver entre 31 a 60, os juros serão de 3.87
    Mas se a pessoa for maior de 60, os juros serão de 4.22
    E no final, o sistema deverá exibir o valor total que a pessoa irá pagar com juros
"""

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você não pode pegar empréstimo.")
    exit()

valor = float(input("Digite o valor do empréstimo: "))

if idade < 31:
    juros = 2.09
elif idade < 61:
    juros = 3.87
else:
    juros = 4.22

print("O valor dos juros é de: {:.2f}%".format(juros))
print("O valor total a pagar é: R$ %.2f" % (valor + (valor * juros / 100)))