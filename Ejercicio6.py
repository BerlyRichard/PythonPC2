# EJERCICIO 6
#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.

def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

i = 0
while fibonacci(i) <= 50:
    print(fibonacci(i))
    i = i+ 1