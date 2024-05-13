"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o porgrama quebre com 
erros de índices inexistentes na lista
"""
import os 

lista = []
while True:
    opcao = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar: ')
    
    
    # Verifica o inserir
    if opcao == 'i':
        print('Inserindo...')
        item = input('Valor: ')
        lista.append(item)
        os.system('cls')
        
    # Verifica o apagar
    if opcao == 'a':
        print('Apagando...')
        indice_str = input('Escolha o índice para apagar: ')
        os.system('cls')
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('A opção não é válida como índice.')

    # Verifica o listar
    if opcao == 'l':
        # Verifica se a lista está vazia
        if len(lista) == 0:
            print('Lista de compras vazia')

        else:
            print('Listando...')
            for indice, nome in enumerate(lista):
                print(indice, nome)
    else:
        print('Opção inválida. Por favor, escolha [i] [a] [l]')
