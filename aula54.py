"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
3 João
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
indices = range(len(lista))
         
for indice in indices:
    print(indice, lista[indice])