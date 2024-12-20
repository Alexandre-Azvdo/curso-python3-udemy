# @staticmethod (métodos estáticos) são inúteis em Python =(
# Métodos estáticos são métodos que estão dentro da 
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua classe.
class Classe:
    @staticmethod
    def funcao_que_existe_na_classe(*args, **kwargs):
        print('oi', args, kwargs)



def funcao(*args, **kwargs):
    print('oi', args, kwargs)

c1 = Classe()
c1 = Classe.funcao_que_existe_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_existe_na_classe(nomeado=1)
funcao(nomeado=1)
