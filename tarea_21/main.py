
#Pedimos un numero al usuario y, en caso que lo haya introducido con coma, lo cambiamos a punto.
numero_1 = input("introduce un numero entre 0.0001 y 0.9999: ")
numero_1 = numero_1.replace(",",".")

#Comprobamos que el número introducido esté en rango. De lo contratio, el programa se acaba y avisa al usuario
try:
    numero_1 = float(numero_1)
except:
    print("No has introducido un número válido");
    exit()

if numero_1 < 0.0001 or numero_1 > 0.9999:
    print("Introduce un numero dentro del rango pedido!")
    exit()

#Comprobamos el número de decimales existentes
numero_decimales = str(numero_1)[::-1].find('.')
print("Numero de decimales: ",numero_decimales)

potencia = 10**numero_decimales
numero_entero = numero_1 * potencia

numerador = numero_entero
denominador = potencia

contador = numerador


while contador >= 1: #Se busca, de manera descendente, la mínima fracción posible
    if numerador % contador == 0 and denominador % contador == 0:
        numerador = numerador / contador
        denominador = denominador / contador
    contador = contador - 1

print("Numerador: ")
print(numerador)

print("Denominador: ")
print(denominador)












