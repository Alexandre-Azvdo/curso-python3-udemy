# Fatiamento de strings
#  012345678
#  Olá mundo
# -987654321
# Fatiamento [i:f:p] [::]
# Obs.: a função (len) retorna a quantidade
# de caracteres da string

variavel = 'Olá mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[4:])
print(variavel[0:5])
print(variavel[-9:-4])

print(len(variavel))
print(variavel[0:9:2])
print(variavel[::-1])