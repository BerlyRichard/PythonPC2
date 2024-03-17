# EJERCICIO 5

#Genere una función que tenga como parámetros el ingreso de un número entero y un dígito. Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.

def contar_dig(nro, digito):
    numero_text = str(nro)
  
    cantidad = numero_text.count(str(digito))

    return cantidad
digito = 0
nro = 15789000
print(f"Cantidad de veces {digito} en el número: {contar_dig(nro, digito)}")