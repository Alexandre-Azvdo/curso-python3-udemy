# dir, hasattr e getattr em Python

string = 'Alexandre'
metodo = 'upper'

# if hasattr(string, 'upper'):
#     print('Existe upper')
#     print(string.upper())

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('Não existe o método', metodo)