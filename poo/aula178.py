# Método especial __cal__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 'Chamada finalizada'


call1 = CallMe('83996547901')
retorno = call1('Alexandre Azevedo')
print(retorno)
