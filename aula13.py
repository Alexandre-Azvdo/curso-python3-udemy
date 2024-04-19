nome = 'Alexandre Azevedo'
altura = 1.71
peso = 76
imc = ... # Ellipsis
# IMC = peso / (altura x altura)

imc = peso / (altura ** 2)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'{peso} quilos e seu IMC é {imc:.2f}'
print(linha_1)
print(linha_2)