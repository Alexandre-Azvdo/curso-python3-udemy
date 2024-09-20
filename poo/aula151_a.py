# Exercício - Salve sua classe em JSON
# Salve os dados da sua clase em JSON
# e depois crie novamente as instâncias
# Faça em arquivos separados.
import json 

CAMINHO_ARQUIVO = 'C:\\Users\\PC\\Documents\\Cursos-TI\\Udemy\\curso-python3\\projetos\\venv\\aulas\\poo\\aula151.json'

class Automovel:
    
    def __init__(self, marca, modelo, placa, ano_fabricacao, ano_modelo):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo

def salvar(instancia, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'w', encoding='utf8') as auto:
            dados = json.dump(instancia, auto, ensure_ascii=False, indent=2)
        print('Automóvel salvo com sucesso!')
    except:
        print('Automóvel NÃO foi salvo!')
    return dados

a1 = Automovel('Fiat', 'Punto','RZZ1F56', '2020', '2021')
a2 = Automovel('Chevolet', 'Onix','KKF4R56', '2022', '2023')
a3 = Automovel('Hyday', 'HB20','RZH6T56', '2024', '2024')
instancias = [vars(a1), vars(a2), vars(a3)]

if __name__ == '__main__':
    salvar(instancias, CAMINHO_ARQUIVO)
