"""
#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    horario = float(input("Quais horas são em número inteiro? "))

    if horario >= 0 and horario <=11:
        print ("Bom dia!")
    elif horario >= 12 and horario <=17:
        print ("Boa tarde!")
    elif horario >= 18 and horario <=23:
        print ("Boa noite!")
    else:
        print("Isso não é uma hora")
except ValueError:
    print ("Isso não é um horário válido")

"""
# ==============================
# NOTAS DE DÚVIDAS
# ==============================

# IF x ELIF
# if verifica a primeira condição.
# elif só é verificado se a condição anterior for falsa.
# Usar elif quando as possibilidades são alternativas entre si.
#
# Exemplo:
# if horario <= 11:
#     print("Bom dia")
# elif horario <= 17:
#     print("Boa tarde")
# elif horario <= 23:
#     print("Boa noite")

# AND
# and exige que as duas condições sejam verdadeiras.
#
# Exemplo:
# horario >= 0 and horario <= 11
#
# Significa:
# "horario é maior ou igual a 0 E menor ou igual a 11?"

# INDENTAÇÃO
# No Python, a indentação define a qual bloco o código pertence.
#
# Código dentro do try precisa estar indentado:
#
# try:
#     numero = int(input(...))
#
# O except volta para o mesmo nível do try:
#
# try:
#     ...
# except ValueError:
#     ...

"""