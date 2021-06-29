import collections


Estudiantes_primero = []
Estudiantes_segundo = []

#Obtener los nombres de los alumnos de primero

print("Introduce, individualmente, los nombres de los alumnos de primero. introduce X para finalizar")

nombre = ''

while nombre != "X":

    nombre = input()


    if nombre != 'X':
        Estudiantes_primero.append(nombre)

print("Introduce, individualmente, los nombres de los alumnos de segundo. introduce X para finalizar")

nombre = ''

while nombre != "X":

    nombre = input()


    if nombre != 'X':
        Estudiantes_segundo.append(nombre)

Estudiantes_primero_sin_rep = list(dict.fromkeys(Estudiantes_primero))
Estudiantes_segundo_sin_rep = list(dict.fromkeys(Estudiantes_segundo))

print("Nombres de los alumnos de primero")
print(Estudiantes_primero_sin_rep)

print("Nombres de los alumnos de segundo")
print(Estudiantes_segundo_sin_rep)

# Nom_Rep_primero = Counter(Estudiantes_primero)
# Nom_Rep_segundo = Counter(Estudiantes_segundo)

print("Nombres repetidos de los alumnos de primero")
print([item for item, count in collections.Counter(Estudiantes_primero).items() if count > 1])
print("Nombres repetidos de los alumnos de segundo")
print([item for item, count in collections.Counter(Estudiantes_segundo).items() if count > 1])


print("Nombres de alumnos de primero que no se repiten en los de segundo: :")
for Estudiantes_primero in set(Estudiantes_primero):
    if Estudiantes_primero not in Estudiantes_segundo:
                print(Estudiantes_primero)