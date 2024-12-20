# Funções decoradoras e decoradores com classes


def adcionar_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls


# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

@adcionar_repr
class Time: #(MyReprMixin) extensão
    def __init__(self, nome):
        self.nome = nome


@adcionar_repr
class Planeta: #(MyReprMixin) extensão
    def __init__(self, nome):
        self.nome = nome


# Time = adcionar_repr(Time)
brasil = Time('Brasil')
portugal = Time('Portugal')

#Planeta = adcionar_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)
