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