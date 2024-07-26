from sys import path

import aula113_package.modulo
from aula113_package import modulo
from aula113_package.modulo import soma_do_modulo
from aula113_package.modulo import *


# print(__name__)
# print(*path, sep='\n')
print(aula113_package.modulo.soma_do_modulo(2, 3))
print(modulo.soma_do_modulo(2, 3))
print(soma_do_modulo(2, 3))
print(variavel)