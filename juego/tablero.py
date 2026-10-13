import numpy as np
import string

class Tablero:
    def __init__(self, dimensiones:tuple):
        self.dimensiones=dimensiones
      
    def crear_tablero(self):
        '''
        crea el tablero y lo retorna
        '''

        tablero=np.full((self.dimensiones[0]+1,self.dimensiones[1]+1), "🌊")
        return tablero
    
    def formato_tablero(self):
        '''
        funcion para dar formato de juego con columnas de la A a la letra que se ajuste al tamaño designado por usuario
        y filas con el numero tb asignado por usuario

        retorna el tablero
        '''
        tablero=self.crear_tablero()
        lista_letras=['A','B','C','D','E','F','G','H','Y','J','K','L','M','O']
        filas= tablero.shape[0]
        columnas=tablero.shape[1]
        
        for i in range(columnas):
            nuevo_tablero=np.where(tablero[:,1]=="🌊", i, tablero)
        return nuevo_tablero

    def formato_tablero1(self):
        tablero = self.crear_tablero()
        filas, columnas = tablero.shape

        letras = string.ascii_uppercase
        if columnas > len(letras):
            raise ValueError(f"Máximo {len(letras)} columnas, pediste {columnas}")

        cabecera = np.array([" "] + list(letras[:columnas]), dtype=object)
        numeros = np.array([str(i) for i in range(1, filas + 1)], dtype=object).reshape(-1, 1)

        cuerpo = np.hstack([numeros, tablero.astype(object)])
        return np.vstack([cabecera, cuerpo])
    '''
    def pintar_barco(self,barco):
        if barco.posicion_posible_barco():
            pass
        return None
    '''

    
t=(5,5)
t1=Tablero(t)

#print(t1.formato_tablero())
print(t1.formato_tablero1())

