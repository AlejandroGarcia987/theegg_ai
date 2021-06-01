##Tarea 24. Programar un conversor "Analógico digital"
numero = input("introduce un número decimal: ")
numero = numero.replace(",",".")

#comprobamos que no se haya introducido un String y lo pasamos a número tipo int para poder convertirlo a binario,
#de lo contrario, mandamos un mensaje
try:
    numero = int(numero)
except:
    print("No has introducido un número válido");
    exit()

numero_binario = bin(numero)

print("El numero binario es: ")
print(numero_binario)