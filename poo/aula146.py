# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados) 
# Instância da class (objeto) - Tem dados
# Uma calasse pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'O {self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)

fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
