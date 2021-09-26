#Tarea 45: Algoritmos de búsqueda

La tarea 45 consiste en analizar la eficiencia de dos algoritmos de búsqueda, llamados búsqueda lineal y búsqueda binaria.

El primer algoritmo recorre el array dado,  buscando un número en concreto, de manera incremental hasta dar con él.
Por su parte, el segundo algoritmo ordena el array de menor a mayor y basa su búsqueda en determinar si el elemento central
del array es el número buscado y, de serlo, el algoritmo acaba. En caso que el número central no sea el elemento buscado,
el algoritmo determina si el número en el que se encuentra es menor o mayor que el número a buscar, descartando todos los números que queden fuera de
rango.

A la hora de ejecutar ambos algoritmos, si el número a buscar se encuentra en las primeras posiciones del array, la busqueda lineal
puede necesitar menos iteraciones que la búsqueda binaria, pero en caso que esto no ocurra, el número de iteraciones necesarias 
por la búsqueda lineal crece con el número de datos de entrada.