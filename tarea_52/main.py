#Tarea 52 The egg

#Pedimos un numero

Lista_numeros = []
numero_usuario = 1; #defino un estado inicial para que entre en el bucle al menos una vez

while numero_usuario != 0:
    numero = input("Inserta un número: ")

    #A continuación compruebo qué tipo de número es, int o float y, dependiendo de ello,
    #lo trato y lo añado a la lista
    try:

        numero_usuario = int(numero) #

        if numero_usuario != 0:
            Lista_numeros.append(numero_usuario)

        else:
            print("La lista introducida es: ")
            print(*Lista_numeros)

    except:
        numero_usuario = float(numero)

        if numero_usuario != 0:
            Lista_numeros.append(numero_usuario)

        else:
            print("La lista introducida es: ")
            print(*Lista_numeros)


#pedimos al usuario un número a borrar

numero_eliminar = input("Inserta un número a eliminar: ")

try:

    numero_usuario = int(numero)
    Lista_numeros.remove(numero_usuario)

except:
    numero_usuario = float(numero)
    Lista_numeros.remove(numero_usuario)

print("La lista introducida es: ")
print(*Lista_numeros)









