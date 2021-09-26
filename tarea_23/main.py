#Tarea 23. Criptografía.


def algoritmo_encriptador(Texto):

    #Eliminamos los espacios
    Texto = Texto.replace(" ","")

    #Agrupo por lotes de 5 letras
    n = 5;
    bloques = [Texto[i:i+n] for i in range(0, len(Texto), n)]











if __name__ == "__main__":
    #1. Pedimos al usuario que introduzca una frase

    Texto = input("introduce una frase a encriptar: ")
    algoritmo_encriptador(Texto)