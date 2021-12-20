"""
    :s = string
    :d = decimal
    :f = float
    :b = binary
    :o = octal
    :x = hexadecimal
"""
cnpj = 237000110

# > - esquerda
# < - direita
# ^ - centralizado
print("{:0>14}".format(cnpj))
print("{:0<14}".format(cnpj))
print("{:0^14}".format(cnpj))
# built-in functions
print(str(cnpj).ljust(14, '.'))
print(str(cnpj).rjust(14, '.'))
print(str(cnpj).center(14, '.'))
# combinando com o formato
print("{:0>14.2f}".format(cnpj))
# formatando números percentuais
print("{:.2%}".format(0.8))
# formatando números inteiros, hexadeciamais, octais e binários
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

# built-in functions
print(int(42))
print(hex(42))
print(oct(42))
print(bin(42))
# python3 -m compileall 09\ -\ format_values.py