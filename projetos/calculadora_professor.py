"""Calculadora com while"""

# Mantém a calculadora funcionando até o usuário escolher sair#
while True:

    # Recebe os dois números como texto (input sempre retorna uma string)
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')

    # Recebe o operador que o usuário deseja utilizar
    operador = input('Digite o operador (+-/*): ')

    # Começamos assumindo que os números ainda não foram validados
    # None = ainda não temos um valor definido para essa variável
    numeros_validos = None

    # Criamos as variáveis que posteriormente receberão os números convertidos
    num_1_float = 0
    num_2_float = 0

    # Vamos tentar transformar os textos recebidos em números decimais
    try:

        # Tenta converter o primeiro número de string para float
        num_1_float = float(numero_1)

        # Tenta converter o segundo número de string para float
        num_2_float = float(numero_2)

        # Se as duas conversões funcionaram, os números são válidos
        numeros_validos = True

    # Se alguma conversão acima gerar um erro, entra aqui
    except:

        # Marca os números como inválidos
        numeros_validos = None

    # Verifica se os números não foram convertidos corretamente
    if numeros_validos is None:

        # Informa ao usuário que existe um problema com os números
        print('Um ou ambos os números são inválidos.')

        # Interrompe essa rodada do while
        # e volta para o começo para pedir os números novamente
        continue

    # Define quais operadores a calculadora aceita
    operadores_validos = '+-/*'

    # Verifica se o operador digitado não está entre os operadores permitidos
    if operador not in operadores_validos:

        # Informa que o operador não é válido
        print('Operador inválido.')

        # Abandona essa rodada e volta para o começo do while
        continue

    # Se o operador escolhido for +
    if operador == '+':

        # Realiza a soma
        resultado = num_1_float + num_2_float

        # Mostra o resultado
        print(f'{num_1_float} + {num_2_float} = {resultado}')

    # Se o operador escolhido for -
    elif operador == '-':

        # Realiza a subtração
        resultado = num_1_float - num_2_float

        # Mostra o resultado
        print(f'{num_1_float} - {num_2_float} = {resultado}')

    # Se o operador escolhido for *
    elif operador == '*':

        # Realiza a multiplicação
        resultado = num_1_float * num_2_float

        # Mostra o resultado
        print(f'{num_1_float} * {num_2_float} = {resultado}')

    # Se o operador escolhido for /
    elif operador == '/':

        # Verifica se o segundo número é zero
        if num_2_float == 0:

            # Não podemos dividir um número por zero
            print('Não é possível dividir por zero.')

            # Volta para o começo do while
            continue

        # Realiza a divisão
        resultado = num_1_float / num_2_float

        # Mostra o resultado
        print(f'{num_1_float} / {num_2_float} = {resultado}')

    # Pergunta se o usuário deseja encerrar a calculadora
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    # Se a resposta começar com "s", encerra o while
    if sair:
        break