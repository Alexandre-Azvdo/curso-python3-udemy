# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

quant_acertos = 0
for pergunta in perguntas:   
    opcao = 0  
    print(f'Pergunta: {pergunta['Pergunta']}\n')
    print('Opções:')
    for _ in range(len(perguntas[opcao]['Opções'])):        
        print(f'{opcao}) {pergunta.get('Opções')[opcao]}') 
        resposta_certa = pergunta.get('Resposta')       
        opcao += 1
    
    resposta = int(input('Escolha uma opção: '))
   
    if resposta_certa == pergunta.get('Opções')[resposta]:
        print('Acertou!!!')
        quant_acertos += 1
    else :
        print('Errou!!!')
    print()
print(f'Você acertou {quant_acertos} de {len(perguntas)} perguntas.')