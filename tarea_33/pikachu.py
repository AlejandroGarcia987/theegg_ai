# El juego de Pikachu. tarea The Egg 33.

#definicion de la clase "POKEMON" Con los atributos "nombre, ataque y vida"
class Pokemon:
    def __init__(self,nombre,vida,ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

#declaración de los Pokemon con sus nombres, vida y ataque
Pikachu = Pokemon("Pikachu",100,55)
Jiglypuff = Pokemon("Jiglypuff", 100, 45)

#inicializamos el turno a "1", Pikachu empieza el ataque
turno = 1

while Pikachu.vida > 0 and Jiglypuff.vida > 0:
    if turno == 1:
        Jiglypuff.vida = Jiglypuff.vida - Pikachu.ataque
        turno = 0
        print(Jiglypuff.vida)

    if turno == 0:
        Pikachu.vida = Pikachu.vida - Jiglypuff.ataque
        turno = 1

if Pikachu.vida > 0:
    print("gana Pikachu!")
else:
    print("gana Jiglypuff")



