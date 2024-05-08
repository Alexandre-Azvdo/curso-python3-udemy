'''
Iterando strings com while
'''
nome = 'Alexandre Azevedo' # Iteráveis

novo_nome = '*'
index = 0
while index < len(nome):    
    novo_nome += nome[index] + '*' 
    index += 1

print(
novo_nome
)