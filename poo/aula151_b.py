import json

from aula151_a import CAMINHO_ARQUIVO

def ler(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as auto:
            dados = json.load(auto)
        
    except FileNotFoundError:
        print('Não foi possível ler nenhum arquivo')
              
    return dados

print(ler(CAMINHO_ARQUIVO))
