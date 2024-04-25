# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precoisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que você já viu)
# 0, 0.0, '', False
# Também existe o tipo None que é 
# usado para representar um não valor

""" entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitada = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitada:
    print('Entrar')
else:
    print('Sair') """

# Avaliação de curto circuito
senha = 0 or 0.0 or False or '' or bool('abc') 
print(senha)