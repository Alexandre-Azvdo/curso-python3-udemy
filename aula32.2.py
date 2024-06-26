"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um número inteiro: ')

# try:    
#     if int(numero) % 2 == 0:
#         print(f'O número {numero} é par!')
#     else: 
#         print(f'O número {numero} é ímpar!')
# except:
#     print(f'Valor {numero} repassado não é inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Qual o horário atual em número inteiro (0 - 23): ')
try:    
    hora = int(entrada)   
    if hora >= 0 and hora <=11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Você digitou um número que não compreende as horas (0 - 23)')
except:
    print('Você forneceu dados que não atendem as horas convencionais de um relógio')
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""