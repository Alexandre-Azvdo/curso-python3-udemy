# @property - um getter no modo Pythônico 
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# em Python.

# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo. 
# 🤯🤯🤯🤯🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - para evitar quebra de código cliente
# - para habilitar setter
# - para executar ações ao obter um atributo

# Código Cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 1234546

####################################

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)

########################################################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# ####################################

# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
