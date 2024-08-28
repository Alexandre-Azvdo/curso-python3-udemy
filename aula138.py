# Problema dos parâmetros mutáveis em funções Python
def adiciona_cientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_cientes('Gustavo')
adiciona_cientes('João', cliente1)
adiciona_cientes('Fernando', cliente1)
cliente1.append('Eduardo')

cliente2 = adiciona_cientes('Jéssica')
adiciona_cientes('Maria', cliente2)

cliente3 = adiciona_cientes('Antony')
adiciona_cientes('Amélio', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)