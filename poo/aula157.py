# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso,
# Mas podemos seguir as seguintes convenções:
#   (    sem underline) = public
#        pode ser usado em qualquer lugar
#   ( _  um underline) = protected
#        não DEVE ser usado fora da classe
#        ou suas subclasses
#   ( __ dois underlines) = private
#        "name mangling" (desfuguração de nomes) = em Python só DEVE ser
#        usado na classe em que foi declarado.
class Foo:
    def __init__(self):
        self.public = 'Variável pública'
        self._protected = 'Variável protegida'
        self.__private = 'Variável privada'
    
    def metodo_public(self):
        return 'Método público'
    
    def _metodo_protected(self):
        return 'Método protegido'
    
    def __metodo_private(self):
        return 'Método privado'

f = Foo()
# print(f.public)
# print(f.metodo_public())

# Contra indicado, pois não DEVERIA ser utilizada, de acordo com a convenção, acessar essa variável fora da classe
# print(f._protected) 
# print(f._metodo_protected())


# Contra indicado, pois não PODE ser utilizada sem ajustes visíveis na chamada nda variável e método
print(f._Foo__private) 
print(f._Foo__metodo_private())
