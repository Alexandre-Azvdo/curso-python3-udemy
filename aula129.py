# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 2', 'preco': 2},
    {'nome': 'Produto 3', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

################

# print(sum([p['preco']for p in produtos]))

################
def funcao_do_reduce(acumulador, produto):
    return acumulador + produto['preco']


total = reduce(
    funcao_do_reduce,
    # lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('Total é', total)