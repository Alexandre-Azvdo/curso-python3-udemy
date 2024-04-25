# Operadores lógicos
# and (e) or (ou) not (not)
# and - Todas as condições precoisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0, 0.0, '', False
# Também existe o tipo None que é 
# usado para representar um não valor


""" entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitada = '123456'
# if True:
#    ...
if entrada == 'E' and senha_digitada == senha_permitada:
    print('Entrar')
else:
    print('Sair') """

print(True and bool(0) and True)