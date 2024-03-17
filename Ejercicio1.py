#EJERCICIO 1

'''Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5, 
en el rango de 1500 y 2700 (ambos incluidos)'''

numeros_divisibles = []

for nro in range(1500, 2701):

    if nro % 5 == 0 and nro % 7 == 0:
   
        numeros_divisibles.append(nro)

print(numeros_divisibles)
