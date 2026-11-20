# Variables globales del juego HUNDIR LA FLOTA
# Usadas por clases.py (var.TAMANO_TABLERO) y funciones.py (mensajes de entrada).

# --- Tablero
TAMANO_TABLERO = 10

# --- Barcos (mismo formato que Tablero.barcos en clases.py)
BARCOS = {
    "Portaviones": {"eslora": 4, "cantidad": 1},
    "Acorazado": {"eslora": 3, "cantidad": 2},
    "Fragata": {"eslora": 2, "cantidad": 3},
    "Destructor": {"eslora": 1, "cantidad": 4},
}

# Casillas con barco por tablero (20).
CASILLAS_CON_BARCO = sum(b["eslora"] * b["cantidad"] for b in BARCOS.values())

# --- Símbolos del tablero (mismas claves y símbolos que Tablero.simbolos_tablero)
SIMBOLOS_TABLERO = {
    "Agua": "~",
    "Barco": "■",
    "Impacto": "X",
    "Fallo": "O",
}

# --- Mensajes para el jugador
MSG_BIENVENIDA = (
    "Bienvenido a HUNDIR LA FLOTA\n"
    "Este proyecto ha sido realizado por el grupo 2"
)
MSG_ENTRADA = (
    f"Introduce fila y columna separadas por coma, entre 0 y {TAMANO_TABLERO - 1}: "
)
# Nombre usado en funciones.py (antes MSG_ENTRADA_INVALIDA)
MSG_WRONG_INPUT = (
    "Entrada no válida. Debes escribir dos números enteros entre 0 y "
    f"{TAMANO_TABLERO - 1} separados por una coma (ejemplo: 1,5)."
)
MSG_REPETIDO = "Ya habías disparado a esa casilla. Elige otra."

# Mensajes: turnos
MSG_TURNO_JUGADOR = "Es tu turno."
MSG_TURNO_MAQUINA = "Turno de la máquina."  # Aquí podríamos cambiar máquina por oponente o rival
MSG_DISPARO_MAQUINA = "La máquina dispara a la casilla ({fila}, {columna})."

# Mensajes: resultado de un disparo
# Jugador
MSG_TOCADO_JUGADOR = "¡Tocado! Vuelves a disparar."
MSG_AGUA_JUGADOR = "Agua. Pasa el turno a la máquina."

# Máquina
MSG_TOCADO_MAQUINA = "La máquina ha tocado uno de tus barcos y vuelve a disparar."
MSG_AGUA_MAQUINA = "La máquina ha fallado. Es tu turno."

# Mensajes: fin de partida
MSG_VICTORIA = "¡Has hundido toda la flota enemiga! ¡Has ganado!"
MSG_DERROTA = "La máquina ha hundido toda tu flota. Has perdido."  # Aquí también podríamos cambiar máquina por oponente o rival
