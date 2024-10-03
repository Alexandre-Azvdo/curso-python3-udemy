# super() é a supper classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Clientes)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno
    
# string = MinhaString('Gustavo')
# print(string.upper())

class A:
    atributo_a = 'valor A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor B'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Burlei o sistema')

    def metodo(self):
#       super().metodo() # B
#       super(B, self).metodo() # A
#       super(A, self).metodo() # Object
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo PAI', 'Outra coisa')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()