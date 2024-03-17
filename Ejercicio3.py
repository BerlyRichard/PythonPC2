#PROBLEMA 3
'''Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.'''

nros_pares = 0
nros_impares = 0
nros = []
print("Bienvenido al menú interactivo")
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        nros.append(numero)
    elif respuesta == "NO":
        break
    else:
        print("Solo se admite de respuesta: SI o NO.")

for x in nros:
    if x % 2 == 0:
        nros_pares += 1
    else:
        nros_impares += 1

print("Números ingresados:", nros)
print("Cantidad de números pares:", nros_pares)
print("Cantidad de números impares:", nros_impares)