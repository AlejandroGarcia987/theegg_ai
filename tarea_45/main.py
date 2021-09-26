
#tarea 45

def algoritmo_ordenacion(Array_ordenado):
    #Algoritmo de ordenación de mayor a menor. En el segunfo "for" comprobamos cada numero con el inmediatamente contiguo
    #si se cumple la condición, cambiamos el orden de los mismos.
    #el primer bucle "for" se encarga de realizar esta operación tantas veces como largo sea el array de entrada
    for j in range(len(Array_ordenado)):
        for i in range(len(Array_ordenado)-1):
            if Array_ordenado[i] > Array_ordenado[i+1]:
                num_temp = Array_ordenado[i]
                Array_ordenado[i] = Array_ordenado[i+1]
                Array_ordenado[i + 1] = num_temp
    busqueda_binaria(Array_ordenado)

def busqueda_lineal(Array_ordenado):

    for i in range(len(Array_ordenado)):
        if Array_ordenado[i] == 874:
            print("Encontrado, iteraciones búsqueda lineal: ")
            print(i)


def busqueda_binaria(Array_ordenado):
    encontrado = False
    iteraciones = 0
    while(encontrado == False):
        posición_inicial = (int(((len(Array_ordenado))/ 2))) - 1 #restamos 1 ya que empezamos en 0

        if(Array_ordenado[posición_inicial] == 874):
            print("Encontrado, iteraciones búsqueda binaria: ")
            print(iteraciones)
            encontrado = True
        else: #Si el número en la posción dada no es el correcto, decidimos con qué parte del array quedarnos en base al valor del dato
            iteraciones = iteraciones + 1
            array_1 = Array_ordenado[:len(Array_ordenado) // 2]
            array_2 = Array_ordenado[len(Array_ordenado) // 2:]

            if Array_ordenado[posición_inicial] > 847:
                Array_ordenado = array_1
            else:
                Array_ordenado = array_2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Array de entrada
    #Array = [3,56,21,33,874,123,66,1000,23,45,65,56] #Array dado por el enunciado

    Array = [3, 56, 21,33, 123, 66, 1000, 23, 45, 65, 56, 456, 78, 1215, 65, 23, 511, 5, 7, 4, 1, 2, 336, 3, 5598,
             21545, 1, 15, 465,874, 3, 543, 45, 6] #Array de prueba, con este array queda mucho más clara la diferencia entre un algoritmo y otro.
                                               #Variar la posición del número para ver la diferencia en el número de iteraciones

    #Utilizamos una llamada al algorimto de búsqueda lineal, que no necesita ordenación, y después llamamos al de ordenación
    busqueda_lineal(Array)
    algoritmo_ordenacion(Array)
