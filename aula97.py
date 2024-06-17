# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
# print(produto)

dc = { # Dictionary Comprehension
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
# print(dc)

lista = [
    ('a', 'valor A'),
    ('b', 'valor B'),
    ('c', 'valor C'),
]

dc = {
    chave: valor
    for chave, valor in lista
}
# print(lista)
# print(dict(lista))

s1 = {i ** 2 for i in range(10)}
print(s1)