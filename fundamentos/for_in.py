"""
texto = 'Python s2'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)

    i += 1
"""

#while comumente utilizado quando não se sabe ao certo o número de repetições que serão realizadas, confrome o exemplo abaixo:

"""
senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva!= senha_digitada:
    senha_digitada = input (f'Sua senha({repeticoes}x): ')

    repeticoes += 1

print ('Aquele laço acima pode ter repetições infinitas')

"""

# iteravel te entrega um elemento por vez.
texto = 'Python'

for letra in texto:
    print(letra)

#Quando você escreve:

texto = 'Python'

for letra in texto:
    print(letra)

"""

leia como:

"Para cada elemento dentro de texto, coloque esse elemento na variável letra."

O Python percorre:

'Python'
   ↓
P → letra
y → letra
t → letra
h → letra
o → letra
n → letra
"""
