"""
Escopo de funções Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos
externos.
A palavra global faz um variável do escopo externo
ser a mesma no escopo interno.
"""
x = 1

def funcao1():
    # global x 
    #         Não é uma boa prática de programação usar 'global'
    #         dentro a função para acessar uma variável externa, 
    #         melhor seria passar por parâmetro.
    x = 10
    def funcao2():
        # global x
        x = 11
        print(f'Id de x dentro do escopo funcao2()     {id(x)}')   
    print(f'Id de x dentro do escopo funcao1()     {id(x)}')
    funcao2()

print(f'Id de x fora do escopo global (externo){id(x)}')
funcao1()
print(f'Id de x fora do escopo global (externo){id(x)}')