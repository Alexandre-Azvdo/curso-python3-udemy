# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Alexandre',
    'sobrenome': 'Azevedo',
}

# a, b = pessoa.values()
# print(a, b)

# a , b = pessoa.items()
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)


dados_pessoa = {
    'idade': 39,
    'altura': 1.70,
}

pessoa_completa = {
    'chave': 1,
    **pessoa,
    'nome': 'Gustavo',
    **dados_pessoa,
}

# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumento nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome='Jessica', qlq=123)
# mostro_argumentos_nomeados(**pessoa_completa)
        
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)