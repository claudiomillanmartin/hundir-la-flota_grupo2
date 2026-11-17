import numpy as np
import variables as var


class Tablero:
    # declaración de los tipos de casillas en números para facilidad de control
    agua = 0
    barco = 1
    impacto = 2
    fallo = 3
    
    #como se muestran las casillas al jugador
    simbolos_tablero = {
        "Agua": "~",
        "Barco": "■",
        "Impacto": "X",
        "Fallo": "O"
    }

# declaración de los tipos de barco (diccionario indicando la eslora y cuantos hay ¿funcionará?)
    barcos = {
    "Portaviones": {"eslora": 4, "cantidad" :1},
    "Acorazado": {"eslora": 3, "cantidad" :2},
    "Fragata": {"eslora": 2, "cantidad" :3},
    "Destructor": {"eslora": 1, "cantidad" :4},
    }

# definición de atributos
    def __init__(self, lado = var.TAMANO_TABLERO):
        self.lado = lado
        self.grid = np.zeros((lado, lado), dtype = int) # creamos cuadrícula de 10x10 con un array de NumPy con puros valores "0", correspondientes a "Agua" para comenzar la partida. 

    """Actualmente el método funciona. Sin embargo, hay que comprobar cómo guardar la posición de los barcos rivales y mostrar solo agua e impactos (en barco o agua)"""

    def colocar_barcos(self):
        for barco, numero in self.barcos.items():
            eslora = numero["eslora"]
            cantidad = numero["cantidad"]
            """Extraemos las esloras y cantidad de unidades del diccionario con dichos datos para poder ser utilizados"""
            
            for unidades in range(cantidad): #declaramos un bucle for para colocar todos los barcos
                colocado = False
                
                while not colocado: #declaramos un bucle while para garantizar que todas las piezas se coloquen
                    orientacion = np.random.choice(["H", "V"]) #elegimos aleatoriamente la orientación: H para Horizontal, V para Vertical
                    
                    fila = np.random.randint(0, self.lado) #elegimos de manera aleatoria la fila de inicio entre "0" y el lado del tablero.
                    columna = np.random.randint(0, self.lado) ##elegimos de manera aleatoria la fila de inicio entre "0" y el lado del tablero.

                    if orientacion == "H": #comprobamos que el barco no sale del tablero en la orientación Horizontal.
                        if columna + eslora <= self.lado:
                            if np.all(self.grid[fila, columna: columna + eslora] == 0): #se verifica que los valores asignados corresponden a casillas libres (agua = 0)
                                self.grid[fila, columna : columna + eslora] = 1 #se reasigna el valor de esas casillas a barco = 1
                                colocado = True #se cambia el estado de colocado de False a True para romper el bucle
                                
                                
                    else: #comprobamos que el barco no sale del tablero en la orientación Vertical. También se podría haber hecho con un "if orientacion == "V":"
                        if fila + eslora <= self.lado:
                            if np.all(self.grid[fila: fila + eslora, columna] == 0): #se verifica que los valores asignados corresponden a casillas libres (agua = 0)
                                self.grid[fila: fila + eslora, columna] = 1 #se reasigna el valor de esas casillas a barco = 1
                                colocado = True #se cambia el estado de colocado de False a True para romper el bucle


    """Actualmente el método funciona a medias. Falta determinar cómo romper el bucle infinito (cambiar el while de true a false) y como configurar el input del usuario y de la máquina."""

    def recibir_disparo(self, fila: int, columna: int): # se crea el metodo recibir disparo con atributos obligatorios de fila y columna de tipo int.
        self.fila = fila
        self.columna = columna
        #fila = fila - 1 # se resta uno para que el calor corresponda con el índice de la posición.
        #columna = columna - 1
        
        while True: #entramos en un bucle while para validar todas las posibles opciones de disparos y posibles repeticiones de turno, ya sea por valores inválidos o por impactos en barco.
        
            #if self.grid[fila, columna] == 2 or self.grid[fila, columna] == 3: # se verifica el valor de las celdas seleccionadas para comprobar si ya han sido seleccionadas previamente. Si lo han sido, se idica con un print
                #print("Esta casilla ya ha sido disparada. Seleccione otra casilla.")
                #break # debe haber un continue pero ahora mismo el bucle se ejecuta en infinito ya que no se cumple la condición. Pendiente de revisión


            if self.grid[fila,  columna] == 0: # se valida si el disparo ha caido en agua y se cambia el valor a disparo en agua.
                self.grid[fila, columna] = 3
                #print("¡Splash! Tu disparo ha caido en agua")
                return self.grid[fila, columna]
        
            elif self.grid[fila,  columna] == 1: # se valida si el disparo ha caido en un barco y se cambia el valor a impacto.
                self.grid[fila, columna] = 2
                #print("¡KABOOM! ¡Impacto en barco enemigo! Vuelve a disparar.")                
                return self.grid[fila, columna] # debe haber un continue pero ahora mismo el bucle se ejecuta en infinito ya que no se cumple la condición. Pendiente de revisión




    def mostrar_tablero(self):
        for fila in self.grid:
            for casilla in fila:
                if casilla == self.agua: #seleccionamos las casillas de acuerdo a su valor (agua, barco, impacto, fallo)
                    print(self.simbolos_tablero["Agua"], end=" ") # la mostramos como el caracter seleccionado para dicho valor de casilla separado por espacios para que no haya salto de carro.
                elif casilla == self.barco:
                    print(self.simbolos_tablero["Barco"], end=" ")
                elif casilla == self.impacto:
                    print(self.simbolos_tablero["Impacto"], end=" ")
                elif casilla == self.fallo:
                    print(self.simbolos_tablero["Fallo"], end=" ")
            print()
