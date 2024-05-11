"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) # Acrescenta um item no final da lista
print(lista)
lista.pop()      # Remove o último item da lista
print(lista)
lista.append(60)
lista.append(70)
print(lista)
lista.pop(0)     # Remove o item da lista indicando o index
print(lista)
lista.clear()    # Apagar todos os item da lista
print(lista)