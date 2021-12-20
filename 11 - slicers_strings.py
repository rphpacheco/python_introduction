'''
    INDICES E FATIAMENTO DE STRINGS
'''
#      [123456] -> INDICES
text = 'Python'

# built-in functions
# print(len(text))
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])
#print(text[6]) -> index out of range

#SLICES
#[start:stop:step]
#                       -[543210]
#                        [Python]
print(text[-4:6:2]) # -> [012345]+
print(text[-6] == text[0])

print(text[2:6])
print(text[2:])
print(text[:2])
print(text[:-2])
print(text[2:-2])
print(text[::3])
# Por built-in functions
print(text[slice(2,6,3)])

# Exemplo
url = 'https://www.google.com.br/'
print(url[:-1])
print(url[:len(url)-1])
print(url[::2])