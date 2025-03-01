**Practicando Sistemas Bioinspirados**

### Problema 1: Optimización con Algoritmos Evolutivos (Facil)

Un grupo de hormigas está buscando la mejor ruta para recoger alimentos. La función de fititud es la siguiente:

F(x) = 10 - x^2

Donde x es la distancia entre el punto de partida y el punto de recogida.

La hormiga comienza en la posición inicial (0, 0). Cada turno, la hormiga elige una dirección aleatoria entre las tres direcciones cardinal (Norte, Sur, Este, Oeste).

En cada turno, la hormiga calcula su nuevo estado utilizando la función de fititud. Si la función es mayor que 5, la hormiga se detiene. De lo contrario, la hormiga sigue la ruta más adecuada.

Escribe un algoritmo en pseudocódigo para simular este proceso durante 10 turnos.

```pseudocódigo
INPUT: inicialización de posición (x, y)
OUTPUT: ruta recorrida

INICIALIZA:
x = 0
y = 0

REPITE TURNOS DE 10:

   CALCULA F ITUD:
     si F(x, y) > 5 THEN
        detén la hormiga
      FI
   SI NO:
     SELECCIONA DIRECCIÓN ALEATORIA
     CALCULA NUEVO ESTADO:
       IF dirección es Norte THEN
         x = x + 1
       SI dirección es Sur THEN
         x = x - 1
       SI dirección es Este THEN
         y = y + 1
       SI dirección es Oeste THEN
         y = y - 1

REPITE:
   IMPRIMA (x, y)

FIN REPETICIÓN
```

### Solución:

```pseudocódigo
INPUT: inicialización de posición (x, y)
OUTPUT: ruta recorrida

INICIALIZA:
x = 0
y = 0

REPITE TURNOS DE 10:

   CALCULA F ITUD:
     si F(x, y) > 5 THEN
        detén la hormiga
      FI
   SI NO:
     SELECCIONA DIRECCIÓN ALEATORIA
     CALCULA NUEVO ESTADO:
       IF dirección es Norte THEN
         x = x + 1
       SI dirección es Sur THEN
         x = x - 1
       SI dirección es Este THEN
         y = y + 1
       SI dirección es Oeste THEN
         y = y - 1

REPITE:
   IMPRIMA (x, y)

FIN REPETICIÓN
```

### Output:

La salida del algoritmo será la ruta recorrida por la hormiga durante los 10 turnos. La ruta estará representada por una coordenada x e y.

**Practicando Sistemas Bioinspirados**

### Problema 2: Optimización con Colonias de Hormigas (Medio)

Una colonia de hormigas está organizada en una red de nodos interconectados. Cada nodo tiene un valor de "fama" asociado a él, que representa la popularidad del nodo.

La función de fititud es la siguiente:

F(x) = 10 - x^2

Donde x es el valor de "fama" de un nodo.

El objetivo de la hormiga es encontrar el camino más eficiente para recorrer la red de nodos, maximizando la suma de los valores de "fama".

Escribe un algoritmo en pseudocódigo para simular este proceso durante 10 iteraciones.

```pseudocódigo
INPUT: red de nodos con valores de "fama"
OUTPUT: camino más eficiente

INICIALIZA:
camino = []
actual = nodo inicial

REPITE ITERACIONES DE 10:

   CALCULA F ITUD:
     si F(actual) > 5 THEN
        detén la hormiga
      FI
   SI NO:
     SELECCIONA NODO ALEATORIO CON VALOR DE "FAMA" MAYOR
     CALCULA NUEVO CAMINO:
       camino = agregar nodo al camino actual
       actual = nodo seleccionado

REPITE:
   IMPRIMA (camino)

FIN ITERACIONES
```

### Solución:

```pseudocódigo
INPUT: red de nodos con valores de "fama"
OUTPUT: camino más eficiente

INICIALIZA:
camino = []
actual = nodo inicial

REPITE ITERACIONES DE 10:

   CALCULA F ITUD:
     si F(actual) > 5 THEN
        detén la hormiga
      FI
   SI NO:
     SELECCIONA NODO ALEATORIO CON VALOR DE "FAMA" MAYOR
     CALCULA NUEVO CAMINO:
       camino = agregar nodo al camino actual
       actual = nodo seleccionado

REPITE:
   IMPRIMA (camino)

FIN ITERACIONES
```

### Output:

La salida del algoritmo será el camino más eficiente recorrido por la hormiga durante las 10 iteraciones. El camino estará representado como una lista de nodos.

**Practicando Sistemas Bioinspirados**

### Problema 3: Optimización con Inteligencia de Enjambres (Difícil)

Un grupo de animales está viajando por un territorio desconocido. Cada animal tiene un conjunto de habilidades y restricciones personales que afectan su movimiento.

La función de fititud es la siguiente:

F(x) = 10 - x^2

Donde x es el número total de pasos recorridos.

El objetivo del grupo es encontrar el camino más eficiente para cubrir el territorio, minimizando el número de pasos necesarios.

Escribe un algoritmo en pseudocódigo para simular este proceso durante 10 iteraciones.

```pseudocódigo
INPUT: conjunto de habilidades y restricciones personales para cada animal
OUTPUT: camino más eficiente

INICIALIZA:
camino = []
actual = anima inicial

REPITE ITERACIONES DE 10:

   CALCULA F ITUD:
     si F(total pasos) > 5 THEN
        detén el grupo
      FI
   SI NO:
     SELECCIONA ANIMA ALEATORIA QUE NO SE HA MUESTRADO EN EL ÚLTIMO PASO
     CALCULA NUEVO CAMINO:
       camino = agregar animal al camino actual
       total pasos = sumar pasos del animal al total de pasos

REPITE:
   IMPRIMA (camino)

FIN ITERACIONES
```

### Solución:

```pseudocódigo
INPUT: conjunto de habilidades y restricciones personales para cada animal
OUTPUT: camino más eficiente

INICIALIZA:
camino = []
actual = anima inicial

REPITE ITERACIONES DE 10:

   CALCULA F ITUD:
     si F(total pasos) > 5 THEN
        detén el grupo
      FI
   SI NO:
     SELECCIONA ANIMA ALEATORIA QUE NO SE HA MUESTRADO EN EL ÚLTIMO PASO
     CALCULA NUEVO CAMINO:
       camino = agregar animal al camino actual
       total pasos = sumar pasos del animal al total de pasos

REPITE:
   IMPRIMA (camino)

FIN ITERACIONES
```

### Output:

La salida del algoritmo será el camino más eficiente recorrido por el grupo durante las 10 iteraciones. El camino estará representado como una lista de animales.

**Practicando Sistemas Bioinspirados**

### Problema 4: Optimización con Inteligencia Artificial (Difícil)

Un sistema de recompensas está diseñado para optimizar la solución de un problema complejo. La función de fititud es la siguiente:

F(x) = 10 - x^2

Donde x es el valor de "fama" asociado a una solución.

El objetivo del sistema es encontrar la solución más eficiente posible, maximizando la suma de los valores de "fama".

Escribe un algoritmo en pseudocódigo para simular este proceso durante 10 iteraciones.

```pseudocódigo
INPUT: conjunto de recompensas asociadas a cada variable
OUTPUT: solución más eficiente

INICIALIZA:
solución = []
actual = variable inicial

REPITE ITERACIONES DE 10:

   CALCULA F ITUD:
     si F(actual) > 5 THEN
        detén el sistema
      FI
   SI NO:
     SELECCIONA VARIABLE ALEATORIA QUE NO SE HA MUESTRADO EN EL ÚLTIMO PASO
     CALCULA NUEVO SOLUCIÓN:
       solución = agregar variable a la solución actual
       actual = variable seleccionada

REPITE:
   IMPRIMA (solución)

FIN ITERACIONES
```

### Solución:

```pseudocódigo
INPUT: conjunto de recompensas asociadas a cada variable
OUTPUT: solución más eficiente

INICIALIZA:
solución = []
actual = variable inicial

REPITE ITERACIONES DE 10:

   CALCULA F ITUD:
     si F(actual) > 5 THEN
        detén el sistema
      FI
   SI NO:
     SELECCIONA VARIABLE ALEATORIA QUE NO SE HA MUESTRADO EN EL ÚLTIMO PASO
     CALCULA NUEVO SOLUCIÓN:
       solución = agregar variable a la solución actual
       actual = variable seleccionada

REPITE:
   IMPRIMA (solución)

FIN ITERACIONES
```

### Output:

La salida del algoritmo será la solución más eficiente posible, representada como una lista de variables.