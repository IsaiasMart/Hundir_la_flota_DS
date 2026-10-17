import jugador as ju
import numpy as np
def pc_pos_posible_ataque():
    #idea principal: coordenada aleatoria si acierta 1/4 de probabilidad
    #  de volver a acertary despues 1/2 hasta fallar o terminar de atacar

    pos=(0,0) #pos sin sintanciar
    return pos


class Juego:
    def __init__(self, jugador1, jugador2):
        self.jugador1=jugador1
        self.jugador2=jugador2
    def modos_juego():
        # modo facil= aleatorio total/// modo dificil= pc con probabilidad modificada
        return
    def inciciar_juego(self,ju:ju,otro_ju:ju):
        i=input(">>")
        while True:
            ju.turno()
            otro_ju.turno()
            i+=1
            if i ==4:
                break

        return None
    def iniciar_juego_mod():
        return





    #NO TERMINADO, FALTA MAS LOGICA