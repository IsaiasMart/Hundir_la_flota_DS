import numpy as np
class Tablero:
    def __init__(self, dimensiones):
        self.dimensiones=dimensiones
    def crear_tablero(self, dimensiones):

        tablero=np.array(dimensiones,dimensiones)
        return tablero
