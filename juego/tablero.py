import numpy as np
import string
from barco import Barco 
qwe="💥"
ewq='💦'
class Tablero:
    def __init__(self, dimensiones:tuple):
        self.dimensiones=dimensiones
      
    def crear_tablero(self):
        '''
        crea el tablero y lo retorna
        '''

        tablero=np.full(self.dimensiones, "🌊",dtype=object)
        return tablero

    
    def cambio_orientacion (self, barco):
        barco.orientacion=(barco.orientacion[1],barco.orientacion[0])
        return barco.orientacion
    
    def listado_pos_validas(self, barco: Barco):
        ls = []
        fila, columna = barco.coordenada_generatriz
        x,y= barco.orientacionY
        for i in range(barco.tamanio):
            n_coordenada = (fila + i * y, columna + i * x)
            if not (0 <= n_coordenada[0] < self.tablero.shape[0]
                    and 0 <= n_coordenada[1] < self.tablero.shape[1]):
                raise IndexError("El barco se sale del tablero")
            if self.tablero[n_coordenada] != "🌊":
                raise ValueError("El barco se solapa con otro barco")
            ls.append(n_coordenada)
        return ls
        
    
    def pintar_barco(self, barco: Barco):
        posiciones = self.listado_pos_validas(barco)

        for fila, columna in posiciones:
            self.tablero[fila, columna] = "🚢"

        return self.tablero

    
    def danio_barco(self):

        return
        
    def conversion_coordenadas(self, coordenada_input):
            letras = string.ascii_uppercase
            coordenada_nuevo_input=()

            for i in letras:
                if coordenada_input[0]==i: 
                    coordenada_nuevo_input[0]=i.index()
                    coordenada_nuevo_input[1]-=1
                    break
            return coordenada_nuevo_input
    
    
      #ultima funciuon para dar fomrato al tablero post-jugadas
    def formato_tablero(self):
        #ultima transformacion del tablero/ultime func q retorne tablerowzwz
        tablero = self.crear_tablero()
        #-----------------------------
        filas, columnas = tablero.shape
        letras = string.ascii_uppercase

        if columnas > len(letras):
            raise ValueError(f"Máximo {len(letras)} columnas, pediste {columnas}")

        cabecera = np.array([" "] + list(letras[:columnas]), dtype=object)
        numeros = np.array([str(i) for i in range(1, filas + 1)], dtype=object).reshape(-1, 1)

        cuerpo = np.hstack([numeros, tablero.astype(object)])
        final=np.vstack([cabecera, cuerpo])
        return final  
#PARCIALMENTE TERMINADO


