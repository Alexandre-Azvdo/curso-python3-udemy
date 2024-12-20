# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, só 
# precisa herdar de akguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Laçando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MyError(Exception):
    ...


class My2Error(Exception):
    ...


def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    # 1/0
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()    
    exception_ = My2Error('Vou lançar de novo')    
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error
