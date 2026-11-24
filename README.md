# Hundir la Flota

Versión por consola del clásico juego **Hundir la Flota**, desarrollada en Python, como Team Challenge para el Bootcamp en Data Science de The Bridge.

El jugador se enfrenta a la máquina en tableros de 10x10 con los barcos colocados de forma aleatoria.

## Estructura del proyecto

```
.
├── main.py          # Punto de entrada: bucle principal de la partida
├── clases.py        # Clase Tablero (colocación de barcos, disparos, visualización)
├── funciones.py     # Funciones auxiliares (entrada del jugador, disparo de la máquina, fin de partida)
└── variables.py     # Variables globales: tamaño, flota, símbolos y mensajes
```

## Requisitos

- **Python 3.8 o superior**
- **NumPy**
- **Biblioteca Keyboard**


## Ejecución

Desde la carpeta del proyecto, ejecuta:

```bash
python main.py
```

(En algunos sistemas puede ser `python3 main.py`.)

## Cómo se juega

1. Al iniciar, se crean dos tableros de 10x10 (jugador y máquina) y los barcos se colocan automáticamente de forma aleatoria, en horizontal o vertical.
2. **Empieza siempre el jugador.** En tu turno, introduce las coordenadas del disparo con el formato `fila,columna`, con valores entre `1` y `10`:

   ```
   Introduce fila y columna separadas por coma, entre 1 y 10: 3,5
   ```

3. Reglas de turno:
   - **Tocado:** si aciertas en un barco, **vuelves a disparar**.
   - **Agua:** si fallas, el turno pasa a la máquina.
   - La máquina sigue las mismas reglas: si toca, repite; si falla, te devuelve el turno.
4. No se puede disparar dos veces a la misma casilla; el juego te pedirá otra.
5. **Gana** quien hunda primero todos los barcos del rival.

Las coordenadas empiezan en 1: la casilla superior izquierda es `1,1` y la inferior derecha es `10,10`. La fila es el número de línea (de arriba abajo) y la columna es la posición dentro de la línea (de izquierda a derecha).

## Flota

Cada jugador dispone de la siguiente flota (20 casillas ocupadas en total):

| Barco        | Eslora (casillas) | Cantidad |
|--------------|:-----------------:|:--------:|
| Portaviones  | 4                 | 1        |
| Acorazado    | 3                 | 2        |
| Fragata      | 2                 | 3        |
| Destructor   | 1                 | 4        |

## Símbolos del tablero

| Símbolo | Significado                                   |
|:-------:|-----------------------------------------------|
| `~`     | **Agua** (casilla sin disparar)               |
| `■`     | **Barco** (solo visible en tu propio tablero) |
| `X`     | **Impacto** (disparo que ha tocado un barco)  |
| `O`     | **Fallo** (disparo que ha caído en el agua)   |

En el tablero de la máquina los barcos permanecen ocultos: las casillas con barco sin tocar se muestran como agua (`~`). En tu propio tablero sí se ven tus barcos (`■`).

### Ejemplo de tablero

```
~ ~ ~ ■ ■ ■ ■ ~ ~ ~
~ O ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ■ ~ ~ ~
~ ~ X ~ ~ ~ ■ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~
```

## Personalización

Todos los parámetros del juego están en `variables.py`:

- `TAMANO_TABLERO`: tamaño del tablero (por defecto 10).
- `BARCOS`: tipos de barco, eslora y cantidad.
- `SIMBOLOS_TABLERO`: caracteres usados para representar cada tipo de casilla.
- Mensajes (`MSG_*`): textos que se muestran al jugador.

## Créditos

Proyecto realizado por el grupor 2 del Bootcamp de Data Scinece.
**Jean-Marc, Gabriel y Claudio**
