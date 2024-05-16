"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '927.761.160-04'
numero_sem_caractere = ''
multiplicador = 10
somados = 0

# Tratando os dados: excluindo '.' e '-' da string_CPF passada
for digito in cpf:
    if digito.isdigit():
        numero_sem_caractere += digito

try:
    for numero_separado in numero_sem_caractere: 
        if multiplicador >= 2:
            # Regra 1: multiplicando cada um dos valores por uma contagem regressiva 
            # Regra 2: Somar todos os resultados
            somados += (int(numero_separado) * multiplicador)
            multiplicador -= 1     
except TypeError:
    print('Erro de tipagem: operador não suportar operação entre "inteiro" e "string"')

# Regra 3: Multiplicar o resultado anterior por 10
multiplicado_10 = somados * 10
# Regra 4: Obter o resto da divisão da conta anterior por 11
resto_divisao = multiplicado_10 % 11
# Regra 5: Condições para validar o primeiro dígito 
digito_1 = resto_divisao if resto_divisao <= 9 else 0
print(f'O primeiro dígito do CPF é {digito_1}')
