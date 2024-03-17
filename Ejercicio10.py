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