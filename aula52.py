"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Alexandre', 'Gustavo', 1, True, 38.9]
lista_b =  lista_a.copy()
lista_a[0] = 'Pai'
print(lista_a)
print(lista_b)