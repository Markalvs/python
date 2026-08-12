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
#sequencia de 5 até 9
#Para cada número dentro de numeros, coloque esse numero na varivavel numero
numeros = range(5, 10)
for numero in numeros:
    print(numero)

    #a variável numero pode receber vários valores diferentes ao longo da execução, mas um por vez.