# @property + setter - getter e setter no modo Python
# - como getter
# - para evitar quebra de código cliente
# - para habilitar setter
# - para executar ações ao obter um atributo
# 🤯🤯🤯🤯🤯
# Atributor que começar com um ou dois underlines
# não devem ser usados fora da classe.
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self._cor_tampa = None
    
    @property
    def cor(self):
        print('Estou no GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Estou no SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
    

caneta = Caneta('Azul')
caneta.cor = 'Preta'
# getter -> obter um valor
print(caneta.cor)
print(caneta.cor_tampa) # -> None

caneta.cor_tampa = 'Verde'
print(caneta.cor_tampa)
