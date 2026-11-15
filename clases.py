import numpy as np


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
    def __init__(self, lado = 10):
        self.lado = lado
        self.grid = np.zeros((lado, lado), dtype = int) # creamos cuadrícula de 10x10 con un array de NumPy con puros valores "0", correspondientes a "Agua" para comenzar la partida. 

    def colocar_barcos(self):
        for barco, numero in self.barcos.items():
            eslora = numero["eslora"]
            cantidad = numero["cantidad"]
            """Extraemos las esloras y cantidad de unidades del diccionario con dichos datos para poder ser utilizados"""

            for unidades in range(cantidad): #declaramos un bucle for para colocar todos los barcos
                colocado = False
                while not colocado:
                    orientacion = np.random.choice(["H", "V"]) #elegimos aleatoriamente la orientación: H para Horizontal, V para Vertical

                    fila = np.random.randint(0, self.lado) #elegimos de manera aleatoria la fila de inicio entre "0" y el lado del tablero.
                    columna = np.random.randint(0, self.lado) ##elegimos de manera aleatoria la fila de inicio entre "0" y el lado del tablero.

                    if orientacion == "H": #comprobamos que el barco no sale del tablero en la orientación Horizontal.
                        if columna + eslora <= self.lado:
                            
                            # Comprobamos que las casillas están libres ¿cómo?


                    else: #comprobamos que el barco no sale del tablero en la orientación Vertical. También se podría haber hecho con un "if orientacion == "V":"
                        if fila + eslora <= self.lado:
                            
                            # Comprobamos que las casillas están libres ¿cómo?


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



    # def recibir_disparo(self):
        