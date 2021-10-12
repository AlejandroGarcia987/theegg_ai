import sys


def AlgoritmoCompresion(cadena):
    diccionario_palabras_sinRepetir = {}
    diccionario_num = {}
    cnt = 0

    cadena_separada = list(cadena.split(" "))
    diccionario_palabras_sinRepetir = list(dict.fromkeys(cadena_separada))

    # definimos un diccionario para eliminar las palabras duplicadas del mismo, ya que un diccionario no puede tener
    # palabras repetidas, para posteriormente asignar un valor numérico a las palabras de manera individual
    for i in diccionario_palabras_sinRepetir:
        diccionario_num[i] = cnt
        cnt = cnt + 1

    # una vez cada palabra tiene un valor numérico asignado, construimos la cadena original pero utilizando los números asignados
    # para ello, declaramos una variable nueva. Esta cadena NO es un diccionario ya que nos interesa tener todas las palabras
    # codificadas en ella.

    #con la funcion append vamos añadiendo los valores sacados del diccionario que hemos creado, donde "i" es cada
    #una de las palabras guardadas en el diccionario.

    cadena_numeros = []

    for i in cadena_separada:
        cadena_numeros.append(str(diccionario_num[i]))

    tamaño_bytes_comprimida = sys.getsizeof(cadena_numeros)
    tamaño_caracteres_comprimida = len(cadena_numeros)

    #utilizamos la función join para crear el mensaje codificado
    mensaje_codificado = " ".join(cadena_numeros)

    print("El tamaño de la cadena comprimida es de", tamaño_caracteres_comprimida, "caracteres")
    AlgoritmoCompresionDescompresion(cadena_numeros, diccionario_num,mensaje_codificado)

def AlgoritmoCompresionDescompresion(cadena_numeros,diccionario_num,mensaje_codificado):

#para descomprimir el mensaje, recorremos la cadena creada de numeros y, utilizando cada uno de los valores introducidos,
#se van obteniendo las palabras almacenadas en el diccionario previamente. Finalmente, se crea una variablellamada
# "cadena comprimida" donde se guardan cada una de las palabras de la cadena original.

    cadena_descomprimida = []

    for i in cadena_numeros:
        cadena_descomprimida.append(list(diccionario_num.keys())[int(i)])

    mensaje_Decodificado = " ".join(cadena_descomprimida)

    print("mensaje descomprimido:",mensaje_Decodificado)
    tamaño_descomprimido = len(mensaje_Decodificado);
    print("el tamaño de la cadena descomprimida es de: ",tamaño_descomprimido,"caracteres")






if __name__ == '__main__':
    print("Introduce una cadena de máximo 30 caracteres")

    #pedimos una cadena de máximo 30 caracteres, si la cadena excede dicho tamaño, se solicita una nueva
    while (True):
        cadena = input()
        if len(cadena) > 30:
            print("La cadena es demasiado larga, prueba de nuevo")
        else:
            break

    tamaño_bytes = sys.getsizeof(cadena)
    tamaño_caracteres = len(cadena)

    print("El tamaño de la cadena es de",tamaño_caracteres, "caracteres")

    AlgoritmoCompresion(cadena)