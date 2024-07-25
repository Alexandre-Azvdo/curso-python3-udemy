# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main_ está e as pastas
# abaico dele.
# Ele não reconhece pastas e mósulos acima do __main__ por
# padrão
# O Python conhece todos os módulos e pacotes presentes 
# nos caminhos de sys.path

import aula110_m
from aula110_m import soma, variavel_modulo

# print('Este módulo se chma', __name__)
print(aula110_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula110_m.soma(2, 3))