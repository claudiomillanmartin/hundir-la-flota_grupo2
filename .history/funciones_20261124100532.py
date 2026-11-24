#Necesitamos las variables globales
import variables  as var
import numpy as np

"""
Fichejo con el diccionario completo de las funciones del juego 
"""
#Funcion para verificar si la coordenada es un entero
def es_entero(valor):
    """Verifica si un valor dado es entero solo sirve dentro de funciones
        Args:
            valor cualquiera
        Returns:
            Bool: True or False
    """
    try:
        int(valor)
        return True
    except ValueError:
        return False
    

#tablero_rival matriz TAMANO_TABLERO x TAMANO_TABLERO
def pedir_coordenadas(tablero):
    """
    Lo que esta funcion requiere :
    - Una entrada (fila,columna) ambos enteros positivos e inferiores a TAMANO_TABLERO
    - Que las coordenadas no fueron utilizadas previamente
    """
    while True:
        try:
            #Pedimos coordenadas al jugador
            entrada = input(var.MSG_ENTRADA).strip()
            partes = entrada.split(",")

            
            #Verificamos que la entrada esta en el formato requerido que las dos entradas son enteros
            if len(partes) != 2 or not (es_entero(partes[0].strip()) and es_entero(partes[1].strip())):
                            print(var.MSG_WRONG_INPUT)
                            continue
            
            fila = int(partes[0].strip())-1
            col = int(partes[1].strip())-1

            # Verificamos que estamos dentro de los límites del tablero
            if not (0 <= fila < tablero.lado and 0 <= col < tablero.lado):
                print(var.MSG_WRONG_INPUT)
                continue

            # Verificamos que el usuario no realizo este disparo previamente
            casilla = tablero.grid[fila,col]
            if casilla > 1 : # Si la casilla esta a 2 o 3 (Impacto o fallo) es un disparo repetido
                print(var.MSG_REPETIDO)
                continue


            return fila, col

        except ValueError:
            print(var.MSG_WRONG_INPUT)


def disparo_maquina(tablero):
    """Crea un nuevo disparo en un zona libre.
        Args:
            tablero con todos sus elementos
        Returns:
            int: fila y columna
    """
    max_coord = tablero.lado - 1
    while True:
        fila = np.random.randint(0, max_coord)
        columna = np.random.randint(0, max_coord)
        estado_casilla = tablero.grid[fila, columna]

        # Solo disparamos si la casilla es agua o barco (1 o 2) segun la clase
        if estado_casilla < 3: 
            return fila, columna

def quedan_barcos(tablero):
    """Devuelve True si queda al menos una casilla de barco sin hundir.
        Args:
            tablero con todos sus elementos
        Returns:
            Bool: True or False
    """
    for fila in tablero.grid:
        if tablero.barco in fila:
            return True
    return False