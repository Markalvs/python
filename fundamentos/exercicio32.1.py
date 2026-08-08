"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
Informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

try:
    numero = int(input("Digite um número inteiro: ")) 

    if numero % 2 == 0:
        print (f"O número {numero} é par")
    else:
        print (f"O número {numero} é impar")
except ValueError:
    print ("Isso não é um número inteiro")

"""
# ==============================
# NOTAS DE DÚVIDAS
# ==============================

# TRY / EXCEPT
# try tenta executar um código que pode gerar um erro.
# except trata o erro para o programa não quebrar.
#
# ValueError acontece, por exemplo, quando tentamos converter
# um texto que não representa um número:
#
# int("abc") -> ValueError
#
# Importante:
# try/except não detecta qualquer entrada inválida.
# float("30") funciona, mesmo que 30 não seja um horário válido.
# Por isso precisamos de condições para validar o intervalo.

# % (MÓDULO)
# % retorna o RESTO da divisão.
#
# 10 % 2 = 0 -> número par
# 7 % 2 = 1 -> número ímpar
#
# Para verificar se um número é par:
# numero % 2 == 0

# INT x FLOAT
# int() tenta transformar a entrada em número inteiro.
# float() tenta transformar a entrada em número decimal.
#
# int("abc") -> ValueError
# float("abc") -> ValueError
#
# input() sempre recebe inicialmente uma string.
"""