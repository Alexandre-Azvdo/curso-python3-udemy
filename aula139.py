# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os 

def cabecario():
    print('Comandos: listar, desfazer, refazer, limpar')
    opcao = input('Digite uma tarefa ou comando: ')
    print()   
    print('TAREFAS:')
    return opcao

def mostrar_tarefas(lista):
    for item in lista:
        print(item)
    print()

lista_tarefas = [] 
aux = ''

while True:
    opcao = cabecario()
    
    match opcao: 
        case 'listar':
            if not lista_tarefas:
                print('Você não possui tarefas!')

        case 'desfazer':
            if not lista_tarefas:
                print('Nada a desfazer!')
            else:
                aux = lista_tarefas[-1]
                lista_tarefas.pop(-1)

        case 'refazer':
            if not aux:
                print('Nada a refazer!')
            else:
                lista_tarefas.append(aux)
                aux = None
        case 'limpar':
            os.system('cls')

        case _:
            lista_tarefas.append(opcao)
    mostrar_tarefas(lista_tarefas)
    