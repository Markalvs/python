"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; 
se tiver 5 a 6 letras, escreva seu nome é médio, maior que 6 escreva "seu nome é grande"
"""
try:
    nome = input("Qual o seu nome? ")

    quantidade_de_letras = len(nome)

    if quantidade_de_letras <= 4:
        print("Seu nome é pequeno.")
    elif quantidade_de_letras <=6:
        print ("Seu nome é médio. ")
    else:
        print("Seu nome é grande. ")
except ValueError:
    print ("Isso não é um nome")