''' Calculadora com while '''

while True:
    print('Solicita números')
    sair = input('Quer sair: [s]im: ').lower().startswith('s')

    if sair is True:
        break