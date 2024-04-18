nome = 'Alexandre'
altura = 1.71
peso = 76
imc = ... # Ellipsis
# IMC = peso / (altura x altura)

imc = peso / (altura ** 2)
print (nome, 'tem', str(altura), 'de altura, pesa', str(peso), 'quilos e seu IMC é', str(imc))