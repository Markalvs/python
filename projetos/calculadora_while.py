#Calculadora com while
#my fist projet

while True:
    try:
        numero_1 = float(input("Digite o primeiro número: "))
        numero_2 = float(input("Digite o segundo número:"))

        print("Selecione a opção desejada: ")
        print("1 - soma")
        print("2 - subtração")
        print("3 - multiplicação")
        print("4 - divisão")

        opção = int(input("Digite a opção desejada: "))


        soma = numero_1 + numero_2
        subtração = numero_1 - numero_2
        multiplicação = numero_1 * numero_2
        divisão = numero_1 / numero_2

        if opção == 1:
            print (f"O resultado é {soma}.")

        elif opção == 2:
            print (f"O resultado é {subtração}.")

        elif opção == 3:
            print (f"O resultado é {multiplicação}.")

        elif opção == 4:
            print (f"O resultado é {divisão}.")

        else:
            print("Selecione uma opção válida")

        sair = input("Quer sair? [s]im: ").lower().startswith("s")

        if sair is True:
            break

    except ValueError:
            print("Digite valores válidos.")