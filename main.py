import os
import random
import readchar
from mapas import mapas

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f"Mapa:\n{self.mapa}\nInicio: {self.inicio}\nFin: {self.fin}"

    def mover(self, direccion):
        x, y = self.inicio
        if direccion == "w":
            x -= 1
        elif direccion == "s":
            x += 1
        elif direccion == "a":
            y -= 1
        elif direccion == "d":
            y += 1

        if self.mapa[x][y] != "#":
            self.inicio = (x, y)

        if self.inicio == self.fin:
            return True

        return False

    def jugar(self):
        while True:
            print(self)
            print("Presione 'w' para arriba, 's' para abajo, 'a' para izquierda, 'd' para derecha")
            direccion = readchar.readkey().lower()
            if self.mover(direccion):
                print("¡Has llegado al final!")
                break

class JuegoArchivo(Juego):
    def __init__(self, mapa):
        super().__init__(mapa["mapa"], mapa["inicio"], mapa["fin"])

if __name__ == "__main__":
    mapa_ejemplo = [
        "#######",
        "#     #",
        "#o# ###",
        "#  #  #",
        "## # ##",
        "#     #",
        "# ### #",
        "#     #",
        "# ### #",
        "#x    #",
        "#######",
    ]

    # Creando una instancia del juego con el mapa de ejemplo
    juego = Juego(mapa_ejemplo, (2, 1), (9, 1))
    juego.jugar()

    # Creando una instancia del juego leyendo un mapa desde un archivo
    mapa_desde_archivo = random.choice(mapas)
    juego_archivo = JuegoArchivo(mapa_desde_archivo)
    juego_archivo.jugar()
