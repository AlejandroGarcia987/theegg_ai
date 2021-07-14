#Palindromos


def obtener_numero_primo_palindromo(numero_usuario):

    while True:
        if numero_primo(numero_usuario) and numero_palindromo(numero_usuario):
            return numero_usuario
            break
        numero_usuario = numero_usuario + 1



def numero_palindromo(numero_usuario):
    numero_final = 0
    var_temp = numero_usuario
    while numero_usuario > 0:
        elementos_individuales = numero_usuario % 10  # estudio el número desde la última cifra
        numero_final = numero_final * 10 + elementos_individuales  # construyo de nuevo el número introducido, usando el orden inverso
        numero_usuario = numero_usuario // 10  # Elimino la cifra ya utilizada
    if (var_temp == numero_final):  # compruebo que mi variable temporal, que es igual al numero original, sea idéntico a la transformación inversa
        return True


def numero_primo(numero_usuario):
    if numero_usuario > 1:
            for i in range(2, numero_usuario):
                if(numero_usuario % i) == 0:
                    break
                else:
                    return True
                break





if __name__ == "__main__":

    print("introduce un número")
    numero_usuario = int(input())
    var_temp = numero_usuario
    siguiente_numero = obtener_numero_primo_palindromo(numero_usuario)
    print("el siguiente número primo y palíndromo es: ")
    print(siguiente_numero)