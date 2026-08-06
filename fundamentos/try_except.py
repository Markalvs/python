#O try/except costuma ser um dos primeiros recursos que faz o programa parecer "profissional". 
#Antes dele, qualquer entrada inválida derruba a aplicação. 
# Depois dele, você consegue prever erros comuns e responder ao usuário de forma elegante, sem interromper a execução.


numero_str = input("Vou dobrar o número que vc digitar: ")

try:
    numero_float = float(numero_str)
    print(f"O dobro de {numero_str} é {numero_float * 2}")

except:
    print("Isso não é um número")