# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

caminho_arquivo = 'C:\\Users\\PC\\Documents\\Cursos-TI\\Udemy\\curso-python3\\projetos\\venv\\aulas\\poo\\aula175.txt'

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo...')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu o erro', e)        
    finally:
        print('Fechando arquivo...')
        arquivo.close()


with my_open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
