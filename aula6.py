# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de coverter um tipo em outro
# Tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1)
print('a' + 'b')
# print('1' + 1) # Apresentaria um erro (Não se pode concatenar um str com um int)
print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 1)

print(bool(0))
print(bool(1))

print(bool(''))
print(bool(' '))

print(str(1) + 'b') 