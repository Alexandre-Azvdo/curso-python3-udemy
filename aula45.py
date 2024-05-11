'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me etregue seu iterador
'''
# for letra in texto
texto = 'Alexandre' # Iterável

# iterador = iter(texto)   # .__iter__()   # iterador

# while True:
#     try:
#         letra = next(iterador) # .__next(__)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)