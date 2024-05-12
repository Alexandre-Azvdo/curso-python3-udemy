"""
Tipo túpla - uma lista imutável
"""
nomes = ['Maria', 'Helena', 'Luiz']
print(nomes)
print(type(nomes))
print()

nomes = tuple(nomes)
print(nomes)
print(type(nomes))
print()

nomes = list(nomes)
print(nomes)
print(type(nomes))
print()

nomes = 'Maria', 'Helena', 'Luiz'
print(type(nomes))