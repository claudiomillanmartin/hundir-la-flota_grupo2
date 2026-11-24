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
        self.grid = np.zeros((lado, lado), dtype = int) # creamos cuadrícula de 10x10 con un array de NumPy con puros valores "0", correspondientes a "Agua" para comenzar la partida. 

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
                    if orientacion == "H" and columna + eslora <= self.lado and np.all(self.grid[fila, columna: columna + eslora] == self.agua): #comprobamos que el barco no sale del tablero en la orientación Horizontal y se verifica que los valores asignados corresponden a casillas libres
                        self.grid[fila, columna : columna + eslora] = self.barco #se reasigna el valor de esas casillas a barco
                        colocado = True #se cambia el estado de colocado de False a True para romper el bucle
                    else:
                        if fila + eslora <= self.lado and np.all(self.grid[fila: fila + eslora, columna] == self.agua): # se verifica que el barco entra en el tablero en orientación Vertical y que las casillas asignadas corresponden a agua.
                            self.grid[fila: fila + eslora, columna] = self.barco #se reasigna el valor de esas casillas a barco
                            colocado = True #se cambia el estado de colocado de False a True para romper el bucle

    def recibir_disparo(self, fila: int, columna: int): # se crea el metodo recibir disparo con atributos obligatorios de fila y columna de tipo int.
        self.fila = fila
        self.columna = columna

        while True: #entramos en un bucle while para validar todas las posibles opciones de disparos y posibles repeticiones de turno, ya sea por valores inválidos o por impactos en barco.
            if self.grid[fila, columna] == self.impacto or self.grid[fila, columna] == self.fallo: # se verifica el valor de las celdas seleccionadas para comprobar si ya han sido seleccionadas previamente. Si lo han sido, se idica con un print
                print("Esta casilla ya ha sido disparada. Seleccione otra casilla.")
                return # debe haber un continue pero ahora mismo el bucle se ejecuta en infinito ya que no se cumple la condición. Pendiente de revisión
            if self.grid[fila, columna] == self.agua: # se valida si el disparo ha caido en agua y se cambia el valor a disparo en agua.
                self.grid[fila, columna] = self.fallo
                return self.grid[fila, columna]
            elif self.grid[fila, columna] == self.barco: # se valida si el disparo ha caido en un barco y se cambia el valor a impacto.
                self.grid[fila, columna] = self.impacto
                return self.grid[fila, columna]

    def mostrar_tablero(self, mostrar_barcos = False):
        self.mostrar_barcos = mostrar_barcos
        
        if mostrar_barcos == True:
            for fila in self.grid:
                for casilla in fila:
                    if casilla == self.agua: #seleccionamos las casillas de acuerdo a su valor (agua, barco, impacto, fallo)
                        print(var.SIMBOLOS_TABLERO["Agua"], end=" ") # la mostramos como el caracter seleccionado para dicho valor de casilla separado por espacios para que no haya salto de carro.
                    elif casilla == self.barco:
                        print(var.SIMBOLOS_TABLERO["Barco"], end=" ")
                    elif casilla == self.impacto:
                        print(var.SIMBOLOS_TABLERO["Impacto"], end=" ")
                    elif casilla == self.fallo:
                        print(var.SIMBOLOS_TABLERO["Fallo"], end=" ")
                print()

        if mostrar_barcos == False:
            for fila in self.grid:
                for casilla in fila:
                    if casilla == self.agua: #seleccionamos las casillas de acuerdo a su valor (agua, barco, impacto, fallo)
                        print(var.SIMBOLOS_TABLERO["Agua"], end=" ") # la mostramos como el caracter seleccionado para dicho valor de casilla separado por espacios para que no haya salto de carro.
                    elif casilla == self.barco:
                        print(var.SIMBOLOS_TABLERO["Agua"], end=" ")
                    elif casilla == self.impacto:
                        print(var.SIMBOLOS_TABLERO["Impacto"], end=" ")
                    elif casilla == self.fallo:
                        print(var.SIMBOLOS_TABLERO["Fallo"], end=" ")
                print()