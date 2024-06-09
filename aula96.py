lista1 = []

for x in range(3):
    for y in range(3):
        lista1.append((x, y))
# print(lista1)

lista2 = [
    (x, y)
    for x in range(3) #  List comprehension
    for y in range(3)
]
# print(lista2)

lista = [
    [(x, letra) for letra in 'Alexandre'] #  List comprehension (complexidade alta)
    for x in range(3)
]
print(lista)