"""
Enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz', 'João']

# lista_enumerada = enumerate(lista)

# for item in lista_enumerada :
#     print(item)

# for item in lista_enumerada :
#     print(item)

# print(next(lista_enumerada))
# print(type(next(lista_enumerada)))
# OBS: Ao usar o enumerate dentro de uma variável como os exemplos 
#      comentados acima só poderá usar uma única vez, diferente da 
#      forma abaixo nesses 'for'

# for item in enumerate(lista):
#     print(item)

# for item in enumerate(lista):
#     print(item)

# for item in enumerate(lista):
#     print(item)
#####################################
# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)
###################################
# for tupla_enumerada in enumerate(lista):
#     indice, nome = tupla_enumerada
#     print(indice, nome)
# print()

# for tupla_enumerada in enumerate(lista):
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
# print()

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

