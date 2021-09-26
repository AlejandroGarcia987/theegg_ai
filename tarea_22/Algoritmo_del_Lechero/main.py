#El algoritmo del lechero

import numpy as np


def algoritmo(num_vacas, peso_max, pesos_vacas, prod_vacas):

        N = len(prod_vacas)
        m = {}
        for c in range(peso_max + 1):
            m[(0,c)] = 0

        for i in range(1 ,N+1):
            for c in range(peso_max + 1):
                if pesos_vacas[i - 1] <= c:
                    m[(i,c)] = max(m[(i-1,c)], prod_vacas[i - 1] + m[(i - 1, c-pesos_vacas[i-1])])
                else:
                    m[(i,c)] = m[(i-1,c)]

        return m[(N,peso_max)]



if __name__ == "__main__":

    print("Introduce el numero de vacas a la venta:")
    num_vacas = int(input())
    print("Introduce el peso total que el camión puede transportar:")
    peso_max = int(input())

    print("inserta el peso de cada una de las vacas")
    pesos_vacas = list()
    prod_vacas = list()

    for i in range(num_vacas):
        print(f"inserta el peso de la vaca número {i+1}")
        peso = int(input())
        pesos_vacas.append(peso)

    for i in range(num_vacas):
        print(f"inserta la producción en litros de cada vaca {i+1}")
        litros = int(input())
        prod_vacas.append(litros)


    print("La cantidad máxima de leche a producir es: ")
    print (algoritmo(num_vacas, peso_max, pesos_vacas, prod_vacas))
