"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores por parâmetros (argumentos)
e retirnar um valor específico.
Por padrão, funções Python retoirnam None (nada)
"""
# def Print():
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

def imprimir(a, b, c):
    print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)
    
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Alexandre Azevedo')
saudacao('Gustavo Rafael')
saudacao()