# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Respostas:
# 1ª forma
def ziper(cidades, siglas):
    intervalo_maximo = min(len(cidades), len(siglas))
    return [
        (cidades[i], siglas[i] ) for i in range(intervalo_maximo)
    ]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(ziper(l1, l2))

# 2ª forma
print(list(zip(l1, l2)))

# 3ª forma
from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue='Sem cidade')))