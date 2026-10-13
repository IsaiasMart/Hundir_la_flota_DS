import jugador as ju

class Juego:
    def __init__(self, jugador1, jugador2):
        self.jugador1=jugador1
        self.jugador2=jugador2

    def inciciar_juego(self,ju:ju,otro_ju:ju):
        while True:
            ju.turno()
            otro_ju.turno()

        return None