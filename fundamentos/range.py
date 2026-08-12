"""
For + Range
range -> range(start, stop, step)
"""

#range não depende do for e for não depende de range

#Quando eu passo só um valor, que é o de start, quando passa um vlaor só vira stop, start vira 0 stop vira 1
"""
numeros1 = range(10)
numeros2 = range(5, 10) #5 a 9 o último valor não é inserido
numeros3 = range(5, 10, 2) #strp é de quanto em quanto
print (numeros1, numeros2, numeros3)
"""

numeros = range(5, 10)
for numero in numeros:
    print(numero)