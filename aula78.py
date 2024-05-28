"""
Exercícios

Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmentro
"""

def criar_multiplicador(multiplicador):    
    def multiplicar(numero):
        return numero * multiplicador     
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

numero = 2

print(duplicar(numero))
print(triplicar(numero))
print(quadruplicar(numero))