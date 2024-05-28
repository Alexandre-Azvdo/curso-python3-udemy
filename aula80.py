# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'
# Criando chaves e valores dentro de um dicionário
pessoa[chave] = 'Alexandre Azevedo'
pessoa['sobrenome'] = 'Rodrigues dos Santos'

print(pessoa[chave])

pessoa[chave] = 'Maria'
print(pessoa)

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])
