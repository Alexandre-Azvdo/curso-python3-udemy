"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import sys

# cpf = '11111111111'
cpf = '746.824.890-70'
cpf_sem_caractere = cpf.replace('.', '').replace('-', '')
multiplicador_1 = 10
multiplicador_2 = 11
somados_1 = 0
somados_2 = 0

entrada_e_sequencial = cpf == cpf[0] * len(cpf)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

try:
    for numero_separado in cpf_sem_caractere: 
        # Regra 1: Multiplicando cada um dos valores por uma contagem regressiva 
        # Regra 2: Somar todos os resultados
        if multiplicador_1 >= 2:            
            somados_1 += (int(numero_separado) * multiplicador_1)
            multiplicador_1 -= 1
        if multiplicador_2 >= 2:
            somados_2 += (int(numero_separado) * multiplicador_2)
            multiplicador_2 -= 1     
except TypeError:
    print('Erro de tipagem: operador não suportar operação entre "inteiro" e "string"')

# Regra 3: Multiplicar o resultado anterior por 10
multiplicado_1_10 = somados_1 * 10
multiplicado_2_10 = somados_2 * 10
# Regra 4: Obter o resto da divisão da conta anterior por 11
resto_divisao_1 = multiplicado_1_10 % 11
resto_divisao_2 = multiplicado_2_10 % 11
# Regra 5: Condições para validar o primeiro dígito 
digito_1 = resto_divisao_1 if resto_divisao_1 <= 9 else 0
digito_2 = resto_divisao_2 if resto_divisao_2 <= 9 else 0

cpf_gerado_pelo_calculo = cpf_sem_caractere[:9] + str(digito_1) + str(digito_2)

if cpf_sem_caractere == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido')
else:
    print(f'{cpf} é inválido')