# tarea 44
import time


def suma_lineal(cantidad):  # sumar uno por uno cada número

    array = list(range(1,cantidad))
    suma = 0
    for i in range(cantidad): #Utilizamos un bucle for en vez de usar el comando "sum()"
        suma = suma + i
    print(suma)

def suma_constante(cantidad): #sumar utilizando el método optimizado.

    array = list(range(1, cantidad))
    dimension = len(array)
    suma = int((dimension / 2)) * (dimension + 1)
    print(suma)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cantidad = 100000 #cuidado, si se excede el número en demasia, se puede bloquear el ordenador

    for i in range(4): #Mediomos el tiempo necesario para realizar cada oepración
        t0 = time.time()
        suma_lineal(cantidad + 1)
        t1 = time.time()
        suma_constante(cantidad + 1)
        t2 = time.time()

        print("lineal:",t1 - t0)
        print("constante:",t2 - t1)

        cantidad *= 10
