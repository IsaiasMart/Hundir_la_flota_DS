import numpy as np
import string
from barco import Barco 

class Tablero:
    def __init__(self, dimensiones:tuple):
        self.dimensiones=dimensiones
      
    def crear_tablero(self):
        '''
        crea el tablero y lo retorna
        '''

        tablero=np.full((self.dimensiones[0],self.dimensiones[1]), "🌊")
        return tablero
    
    
          
    def posicion_posible(self, barco:Barco):
        tablero=self.crear_tablero()
        
        if barco.coordenada_generatriz>tablero.shape:
            raise IndexError("")
        for i in range(barco.tamanio):
            pass
            
        return

    def pintar_barco(self,barco:Barco):
        tablero=0
        if  self.posicion_posible(barco):
             pass
        return tablero
    
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