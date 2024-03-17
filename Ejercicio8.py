# EJERCICIO 8
#Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.

def calcular_factorial(x):
    if x < 0:
         return "El factorial no está definido para números negativos."
    fact=1
    for i in range(1, x+1):
        fact *=i
    return fact

numero = int(input("Ingrese un número entero no negativo: "))
print("El factorial de", numero, "es:", calcular_factorial(numero))