import tablero as t
class Barco:
    #tamanio puede ser cambiado de disposivcion usando su trasbersa
    def __init__(self, tamanio:int ,coordenada_generatriz:tuple, orientacion:tuple):
        self.tamanoi=tamanio
        self.coordenada_generatriz=coordenada_generatriz
        self.orientacion=orientacion
    def posicion_posible_barco(self, coordeada_generica, orientacion,tamanio):
        '''
        dada una posicion generica calcula si el barco cabe dentro de la matriz 
        usando una orientacion basada en los vectores v1=(1,0) y v2=(0,1)
        y el tamaño del barco
        '''
        es_posible=None
    

        
        return es_posible
    def coloca_barco_plus(tablero, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
        tablero_temp = tablero.copy()
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        for pieza in barco:
            fila = pieza[0]
            columna = pieza[1]
            if fila < 0  or fila >= num_max_filas:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if columna <0 or columna>= num_max_columnas:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if tablero[pieza] == "O" or tablero[pieza] == "X":
                print(f"No puedo poner la pieza {pieza} porque hay otro barco")
                return False
            tablero_temp[pieza] = "O"
        return tablero_temp
    #llamara a posicion posible barco para saber si puede pintarlo
    def generar_barco (self, coordenada_generica):

        return
    
    
    def bomazo(self, coordenadas_destino:tuple):
        resultado= bool

        return resultado

    
    def bombazo_recibido(self, coordenada):
        resultado=bool

        return resultado
tablero=t((10,10))
b1=Barco(3,(1,1),(1,0))