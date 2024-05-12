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
    + - Concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_A = [1, 2, 3]
lista_B = [4, 5, 6]
lista_C = lista_A + lista_B # Concatena listas
print(lista_C)
lista_A.extend(lista_C) # Estendeu a lista_A com a lista_C
print(lista_A)