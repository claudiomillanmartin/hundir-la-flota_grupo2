#Lista de Variables
import numpy as np

#Lista de Variables
TAMANO_TABLERO = 10

# Esloras de los barcos
BARCOS = np.array([4, 3, 3, 2, 2, 2, 1, 1, 1, 1])  
# Símbolos del tablero
BARCO = "■"
AGUA = " "
TOCADO = "X"
FALLO = "O"

# Mensajes para el usuario
MSG_ENTRADA = f"Introduce fila y columna separadas por coma entre [0-{TAMANO_TABLERO - 1}]:"
MSG_WRONG_INPUT = ( "Entrada no válida. Debe entrar dos numeros enteros entre 0 y "
                f"{TAMANO_TABLERO-1} separados por una coma (ejemplo: 1,5).")

MSG_BIENVENIDO = ("Bienvenido a nuestro version de HUNDIR LA FOLTA"
              "\n"
              "Este proyecto ha sido realizado por el grupo 2")

MSG_TOCADO = "¡¡¡Ha tocado un barco!!! ¡Juega otra vez!"
MSG_AGUA = "Disparo al agua. ¡Pierde su turno!"
MSG_REPETIDO = "Coordenada ya utilizada. Elige otra."


