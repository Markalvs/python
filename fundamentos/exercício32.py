"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
Informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

try:
    numero = int(input("Digite um número inteiro: ")) 

    if numero % 2 == 0:
        print ("Esse número é par")
    else:
        print ("Esse número é impar")
except ValueError:
    print ("Isso não é um número inteiro")







"""
Fça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; 
se tiver 5 a 6 letras, escreva seu nome é médio, maior que 6 escreva "seu nome é grande"

"""


