#Invertir palabras

print("Introduce una frase a tu elección: ")

frase = input()
frase_separada = frase.split()
print(frase_separada)

x=0
lista_invertida=[]

while x <= -len(frase_separada):
    lista_invertida.append(frase_separada[x-1])
    x = x-1

print(' '.join(frase.split()[::-1]))