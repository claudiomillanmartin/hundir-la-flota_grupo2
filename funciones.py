#Necesitamos las variables globales
import variables


"""
Fichejo con el diccionario completo de las funciones del juego 
"""
#Funcion para verificar si la coordenada es un entero
def es_entero(valor):
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
            entrada = input(MSG_ENTRADA).strip()
            partes = entrada.split(",")

            
            #Verificamos que la entrada esta en el formato requerido que las dos entradas son enteros
            if len(partes) != 2 or not (es_entero(partes[0].strip()) and es_entero(partes[1].strip())):
                            print(MSG_WRONG_INPUT)
                            continue
            
            fila = int(partes[0].strip())
            col = int(partes[1].strip())

            # Verificamos que estamos dentro de los límites del tablero
            if not (0 <= fila < tablero.tamano and 0 <= col < tablero.tamano):
                print(MSG_WRONG_INPUT)
                continue

            # Verificamos que el usuario no realizo este disparo previamente
            casilla = tablero.matriz[fila][col]
            if casilla in (tablero.tocado, tablero.fallo):
                print(MSG_REPETIDO)
                continue


            return fila, col

        except ValueError:
            print(MSG_WRONG_INPUT)


def procesar_disparo(tablero_objetivo, fila, col):
    """
    Ejecuta el disparo en el tablero indicado y actualiza su estado.
    Devuelve True si hubo impacto (Tocado) y False si cayó en agua (Fallo).
    """
    return True


def disparo_maquina(tablero_jugador, historial_maquina):
    """
    Crear un disparo para computer si repetir uno existente
    Ver como gestionar este historial
    """
    fila = 0
    col = 0
    acierto = "(Agua o Tacado) o (True / False)"
    return fila, col, acierto