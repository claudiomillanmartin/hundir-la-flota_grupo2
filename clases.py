import numpy as np
import variables as var

class Tablero:
    # declaración de los tipos de casillas en números para facilidad de control
    agua = 0
    barco = 1
    impacto = 2
    fallo = 3

    # definición de atributos
    def __init__(self, lado = var.TAMANO_TABLERO):
        self.lado = lado
        self.grid_barcos = np.zeros((lado, lado), dtype = int) # creamos cuadrícula de 10x10 con un array de NumPy con puros valores "0", correspondientes a "Agua" para comenzar la partida. 
        self.grid_disparos = np.zeros((lado, lado), dtype = int) # creamos cuadrícula de 10x10 con un array de NumPy puros valores "0" donde registraremos los disparos. 

    def colocar_barcos(self):
        for barco, numero in var.BARCOS.items():
            eslora = numero["eslora"]
            cantidad = numero["cantidad"]
            """Extraemos las esloras y cantidad de unidades del diccionario con dichos datos para poder ser utilizados"""

            for unidades in range(cantidad): #declaramos un bucle for para colocar todos los barcos
                colocado = False

                while not colocado: #declaramos un bucle while para garantizar que todas las piezas se coloquen
                    orientacion = np.random.choice(["H", "V"]) #elegimos aleatoriamente la orientación: H para Horizontal, V para Vertical
                    fila = np.random.randint(0, self.lado) # elegimos aleatoriamente la fila de inicio entre "0" y el lado del tablero.
                    columna = np.random.randint(0, self.lado) # elegimos aleatoriamente la fila de inicio entre "0" y el lado del tablero.
                    if orientacion == "H" and columna + eslora <= self.lado and np.all(self.grid_barcos[fila, columna: columna + eslora] == self.agua): #comprobamos que el barco no sale del tablero en la orientación Horizontal y se verifica que los valores asignados corresponden a casillas libres
                        self.grid_barcos[fila, columna : columna + eslora] = self.barco #se reasigna el valor de esas casillas a barco
                        colocado = True #se cambia el estado de colocado de False a True para romper el bucle
                    else:
                        if fila + eslora <= self.lado and np.all(self.grid_barcos[fila: fila + eslora, columna] == self.agua): # se verifica que el barco entra en el tablero en orientación Vertical y que las casillas asignadas corresponden a agua.
                            self.grid_barcos[fila: fila + eslora, columna] = self.barco #se reasigna el valor de esas casillas a barco
                            colocado = True #se cambia el estado de colocado de False a True para romper el bucle

    def recibir_disparo(self, fila: int, columna: int): # se crea el metodo recibir disparo con atributos obligatorios de fila y columna de tipo int.
        self.fila = fila
        self.columna = columna

        if self.grid_disparos[fila, columna] != self.agua: #comprobamos si esta casilla ya ha sido disparada.
            print("Esta casilla ya ha sido disparada. Seleccione otra casilla")
            return None
        if self.grid_barcos[fila, columna] == self.barco: #comprobamos si esta casilla contiene un barco y de ser así se cambia su valor a impacto.
            self.grid_disparos[fila, columna] = self.impacto
            return self.impacto
        else:
            self.grid_disparos[fila, columna] = self.fallo # de lo contrario se registra como fallo.
            return self.fallo

    def mostrar_tablero(self, mostrar_barcos = False):
        self.mostrar_barcos = mostrar_barcos
        
        if mostrar_barcos == True:
            for fila_barcos, fila_disparos in zip(self.grid_barcos, self.grid_disparos): # iniciamos un bucle for en ambos grids para llegar a las casillas individuales
                for casilla_barco, casilla_disparo in zip(fila_barcos, fila_disparos): 
                    if casilla_disparo == self.impacto:
                        print(var.SIMBOLOS_TABLERO["Impacto"], end=" ") # se verifica cada casilla con el grid correspondiente para mostrar los simbolos asignados a cada valor.
                    elif casilla_disparo == self.fallo:
                        print(var.SIMBOLOS_TABLERO["Fallo"], end=" ")
                    elif casilla_barco == self.barco:
                        print(var.SIMBOLOS_TABLERO["Barco"], end=" ")
                    else:
                        print(var.SIMBOLOS_TABLERO["Agua"], end=" ")
                print()
        
        if mostrar_barcos == False:
            for fila_barcos, fila_disparos in zip(self.grid_barcos, self.grid_disparos):
                for casilla_barco, casilla_disparo in zip(fila_barcos, fila_disparos):
                    if casilla_disparo == self.impacto:
                        print(var.SIMBOLOS_TABLERO["Impacto"], end=" ")
                    elif casilla_disparo == self.fallo:
                        print(var.SIMBOLOS_TABLERO["Fallo"], end=" ")
                    else:
                        print(var.SIMBOLOS_TABLERO["Agua"], end=" ") # se verifica cada casilla con el grid correspondiente para mostrar los simbolos asignados a cada valor. En este caso el valor de barco y agua se muestra como agua.
                print()