#Tarea 52 The egg

from collections import Counter

#Pedimos un numero

Lista_numeros = []
numero_usuario = 1; #defino un estado inicial para que entre en el bucle al menos una vez

while numero_usuario != 0:
    numero = input("Inserta un número entero: ")

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
        print("introduce un numero entero")


#pedimos al usuario un número a borrar

numero_eliminar = int(input("Inserta un número a eliminar: "))


if numero_eliminar in Lista_numeros:
    numero_usuario = int(numero_eliminar)
    Lista_numeros.remove(numero_usuario)
    print("La nueva lista es: ")
    print(*Lista_numeros)
    sumatorio = sum(Lista_numeros)
    print("El sumatorio es: ")
    print(sumatorio)
else:
    print("No has introducido un numero valido")



Numero_limite = int(input("introduce el numero limite: "))
Lista_numeros_menores = [] #Defino una nueva lista

#voy comprobando el valor de cada uno de los numeros y, si es menor que el limite, lo meto en la nueva lista

for i in Lista_numeros:
    if i<Numero_limite:
        Lista_numeros_menores.append(i)


print("EL numero de repeticiones de cada numero es: ")
print(Counter(Lista_numeros).most_common())


















