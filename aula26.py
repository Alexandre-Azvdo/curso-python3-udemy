# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígito>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o número a aparecer antes do zeros
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

var = 'ABC'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: <10}.')
print(f'{var: ^10}.')
print(f'{1000.4875362145:0=+10,.1f}')
print(f'O hexadecimal de %d é {1500:08X}' % 1500)
print(f'{var!r}')