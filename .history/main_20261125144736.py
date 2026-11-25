import variables as var
from clases import Tablero
from funciones import (
    pedir_coordenadas,
    disparo_maquina,
    quedan_barcos
)



def jugar():
    print("----------------------------------------")
    print("-   BIENVENIDO A HUNDIR LA FLOTA       -")
    print("========================================")

    # 1. Inicializamos nuestros dos tableros jugador vs maquina
    tablero_jugador = Tablero()
    tablero_maquina = Tablero()
    historial_maquina = set()

    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    #Gestion para activar el modo Demo que enseña los barcos de la maquina
    mostrar_barcos_maquina = False

    while True:
        reponse = input("Demo (si/no) : ").strip().lower()
        es_valide = reponse in ["oui", "o", "true", "1"]

    def activar_debug(): 
        nonlocal mostrar_barcos_maquina    
        mostrar_barcos_maquina = True
        print("\n[DEBUG ACTIVADO] Los barcos se mostrarán en el siguiente turno.")
           
    turno_jugador = True  # Empieza el jugador siempre
    # 2. Bucle principal de la partida
    while True:
        if turno_jugador:
            print("\n" + "-" * 30)
            print(var.MSG_TURNO_JUGADOR)
            
            # Habria que ocultar los barcos en mostrar_tablero
            tablero_maquina.mostrar_tablero(mostrar_barcos_maquina)

            fila, col = pedir_coordenadas(tablero_maquina)
            acierto = tablero_maquina.recibir_disparo(fila, col)
        
            if acierto!= 3:
                print(var.MSG_TOCADO_JUGADOR)
                # Comprobar victoria inmediata del jugador
                if not quedan_barcos(tablero_maquina):
                    print(var.MSG_VICTORIA)
                    tablero_maquina.mostrar_tablero(mostrar_barcos_maquina)
                    break
            else:
                print(var.MSG_AGUA_JUGADOR)
                turno_jugador = False

        else:
            print("\n" + "-" * 30)
            print(var.MSG_TURNO_MAQUINA)

            fila, col = disparo_maquina(tablero_jugador)
            acierto = tablero_jugador.recibir_disparo(fila, col)

            if acierto!=3:
                print(var.MSG_TOCADO_MAQUINA)
                tablero_jugador.mostrar_tablero(True)
                # Comprobar derrota del jugador
                if not quedan_barcos(tablero_jugador):
                    print(var.MSG_DERROTA)
                    print("\n Tablero de la máquina:")
                    tablero_maquina.mostrar_tablero()
                    break
            else:
                print(var.MSG_AGUA_MAQUINA)
                tablero_jugador.mostrar_tablero(True)
                turno_jugador = True


if __name__ == "__main__":
    jugar()