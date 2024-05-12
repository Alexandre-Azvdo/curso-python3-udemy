"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove item do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista 
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
lista.append('Amor') # Adiciona um item ao final
print(lista)         
nome = lista.pop()   # Remove item do final
print(lista)
del lista[-1]        # Apaga um índice
print(lista)
lista.clear()        # Limpa a lista
print(lista)
lista = [10, 20, 30, 40]
lista.insert(0, 5)   # Adiciona um item no índice escolhido (índice, valor)
print(lista)