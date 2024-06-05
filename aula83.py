# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Alexandre',
    'sobrenome': 'Azevedo',
}

# print(p1['nome'])
# print(p1.get('nome'))

# nome = p1.get('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'Alex',
#     'sobrenome': 'Azevedo',
#     'idade': 39,
# })
# p1.update(nome='Novo nome', idade=40)
tupla = (('nome', 'nome em tupla'), ('idade', 45))
lista = [['nome', 'nome em tupla'], ['idade', 45]]
p1.update(tupla)
print(type(tupla))
print(p1)

p1.update(lista)
print(type(lista))
print(p1)