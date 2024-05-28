"""
Exercícios com funções
"""
"""
1 - Crie uma função que multiplica todos os argumentos
não nomeados recebidos.
Retorne o total para uma variável e mostre o valor
da variável.
"""

def multiplicar(*args):
    multiplicados = 1
    for numero in args:
        multiplicados *= numero

    return multiplicados

resultado = multiplicar(1, 2, 3, 4, 5)
print(resultado)

"""
2 - Crie uma função que fale se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    return f'{numero} é ímpar'


print(par_impar(0))
print(par_impar(3))
print(par_impar(6))
print(par_impar(9))
print(par_impar(15))
print(par_impar(22))