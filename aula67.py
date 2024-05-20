import random

for _ in range(100):

    cpf = '' 
    for i in range(9):
        cpf += str(random.randint(0, 9))

    # cpf_sem_caractere = cpf.replace('.', '').replace('-', '')
    cpf_sem_caractere = cpf

    try:
        multiplicador_1 = 10
        somados_1 = 0
        for numero_separado in cpf_sem_caractere: 
            # Regra 1: Multiplicando cada um dos valores por uma contagem regressiva 
            # Regra 2: Somar todos os resultados
            if multiplicador_1 >= 2:            
                somados_1 += (int(numero_separado) * multiplicador_1)
                multiplicador_1 -= 1      

        # Regra 3: Multiplicar o resultado anterior por 10
        multiplicado_1_10 = somados_1 * 10
        # Regra 4: Obter o resto da divisão da conta anterior por 11
        resto_divisao_1 = multiplicado_1_10 % 11
        # Regra 5: Condições para validar o primeiro dígito 
        digito_1 = resto_divisao_1 if resto_divisao_1 <= 9 else 0
        
        cpf_sem_caractere_2 = cpf_sem_caractere + str(digito_1)

        multiplicador_2 = 11
        somados_2 = 0
        for numero_separado in  cpf_sem_caractere_2: 
            # Regra 1: Multiplicando cada um dos valores por uma contagem regressiva 
            # Regra 2: Somar todos os resultados
            if multiplicador_2 >= 2:            
                somados_2 += (int(numero_separado) * multiplicador_2)
                multiplicador_2 -= 1            
        
    except TypeError:
        print('Erro de tipagem: operador não suportar operação entre "inteiro" e "string"')

    # Regra 3: Multiplicar o resultado anterior por 10
    multiplicado_2_10 = somados_2 * 10
    # Regra 4: Obter o resto da divisão da conta anterior por 11
    resto_divisao_2 = multiplicado_2_10 % 11
    # Regra 5: Condições para validar o primeiro dígito 
    digito_2 = resto_divisao_2 if resto_divisao_2 <= 9 else 0

    cpf_gerado_pelo_calculo = cpf + str(digito_1) + str(digito_2)
    print(cpf_gerado_pelo_calculo)