#EJERCICIO 1

'''Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5, 
en el rango de 1500 y 2700 (ambos incluidos)'''

numeros_divisibles = []

for nro in range(1500, 2701):

    if nro % 5 == 0 and nro % 7 == 0:
   
        numeros_divisibles.append(nro)

print(numeros_divisibles)

#EJERCICIO 2
#Escriba un programa en Python para construir el siguiente patrón.

x = 5
for i in range(1, x + 1):
        print('* ' * i)

for i in range(x - 1, 0, -1):
        print('* ' * i)

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

# EJERCICIO 4
#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de susmaterias.

lista_alumnos = []
nro_alumnos = int(input("Ingrese el número de alumnos: "))

for i in range(nro_alumnos):
    x = str(input("Ingrese el nombre del alumno: "))
    n1 = float(input("Ingrese la primera nota de: "))
    n2 = float(input("Ingrese la segunda nota de: "))
    n3 = float(input("Ingrese la tercera nota de: "))
   
    diccionario_alumnos = {
        "Alumno": x,        
        "Notas": [n1, n2, n3]
    }
    lista_alumnos.append(diccionario_alumnos)

print("Listado total de alumnos:")
for alumno in lista_alumnos:
    print("Alumno:", alumno["Alumno"])
    print("Notas:", alumno["Notas"])

# EJERCICIO 5

#Genere una función que tenga como parámetros el ingreso de un número entero y un dígito. Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.

def contar_dig(nro, digito):
    numero_text = str(nro)
  
    cantidad = numero_text.count(str(digito))

    return cantidad
digito = 0
nro = 15789000
print(f"Cantidad de veces {digito} en el número: {contar_dig(nro, digito)}")

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

# EJERCICIO 7
#Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no.

def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Escriba un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


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


# EJERCICIO 9
#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio, por ejemplo, omitiendo las vocales.

def omitir_vocales(cadena):

    vocales = ['A', 'E', 'I', 'O', 'U','a', 'e', 'i', 'o', 'u']
    reemplazar = ''

    for caracter in cadena:
        if caracter not in vocales:
            reemplazar += caracter
    return reemplazar

texto = input("Ingrese una cadena de texto: ")
print("Texto con vocales omitidas:", omitir_vocales(texto))

#EJERCICIO 10

#Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como8/9/1636 o Septiembre 8, 1636

def obtener_nro_mes():
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
    
    fecha_entrada = input("Escriba la fecha en el formato número mes/día/año o Mes día, año: ")
    partes = fecha_entrada.split()
    
    if len(partes) == 1: 
        mes, dia, anio = map(int, partes[0].split('/'))
    elif len(partes) == 3:  
        mes = meses.index(partes[0]) + 1
        dia = int(partes[1][:-1])
        anio = int(partes[2])
    else:
        print("Formato de fecha no válido. Después de la coma coloque un espacio y escriba el nombre del mes con la primera letra en mayúscula")
        return
    mes_str = f"{mes:02}"
    dia_str = f"{dia:02}"
    anio_str = str(anio)
    
    return f"{anio_str}-{mes_str}-{dia_str}"

fecha_formateada = obtener_nro_mes()
print("Fecha en formato AAAA-MM-DD:", fecha_formateada)


