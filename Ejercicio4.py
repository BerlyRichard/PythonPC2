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
