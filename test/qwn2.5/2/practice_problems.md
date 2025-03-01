# Sistemas bioinspirados: el juego de la vida

## Optimización con métodos bioinspirados

### Problema 1 (Nivel Básico): Algoritmos Evolutivos
**Descripción del problema:** Implemente un algoritmo genético básico para encontrar el mínimo global de una función.

**Función a optimizar:**
\[ f(x) = x^2 - 3x + 4 \]

**Resolución:**

1. **Inicialización de la población**: Cada individuo en la población es representado por un valor \(x\). Podemos generar una población aleatoria inicial entre los límites de búsqueda, por ejemplo, entre \([-5, 5]\).

2. **Función fitness**: Definir la función fitness como el valor absoluto de la función objetivo.
\[ Fitness(x) = |f(x)| \]

3. **Selección**: Seleccione individuos con mayor probabilidad para ser padres basándose en su fitness.

4. **Cruce (Reproducción)**: Crea nuevos individuos combinando los genes de dos padres. Puedes usar la cruza unión o punto simple.

5. **Mutación**: Con cierta probabilidad, cambia el valor \(x\) de algunos individuos en la población.

6. **Iterar hasta convergencia**: Repite los pasos 3-5 hasta que se cumpla una condición de parada (por ejemplo, un número de iteraciones máxima o un mínimo fitness).

**Solución:**
\[ x = \frac{3}{2} \]

### Problema 2 (Nivel Intermedio): Colonias de hormigas
**Descripción del problema:** Implemente el algoritmo de colonia de hormigas para resolver un problema de optimización combinatorial.

**Problema**: Encontrar la ruta más corta entre dos ciudades en una red de ciudades.

**Resolución:**
1. **Inicialización de las feromonas**: Colocar una cantidad de feromonas inicial en cada arista de la red.
2. **Depósito de hormigas**: Cada hormiga se posiciona aleatoriamente en una ciudad y comienza a buscar la ruta más corta hacia otra ciudad.
3. **Actualización de las feromonas**: Después de que todas las hormigas hayan explorado, se actualiza el nivel de feromonas en cada arista basándose en la calidad del camino recorrido por cada hormiga.

**Solución:**
Ruta óptima entre las ciudades (depende de los datos).

### Problema 3 (Nivel Avanzado): Inteligencia de enjambres
**Descripción del problema:** Implemente un algoritmo de inteligencia de enjambres para optimizar una función multivariable.

**Función a optimizar:**
\[ f(x, y) = x^2 + 2y^2 - xy \]

**Resolución:**
1. **Inicialización de los partículas**: Cada partícula se posiciona en un punto aleatorio en el espacio de búsqueda.
2. **Actualización del movimiento**: Las partículas actualizan su posición basándose en su mejor posiciones pasada y global.
3. **Convergencia**: Repita hasta que la solución converja a un mínimo global.

**Solución:**
El valor óptimo para \(x\) y \(y\).

# Introducción a las redes neuronales: el modelo de la neurona de los mamíferos

## Perceptrones y backpropagation

### Problema 4 (Nivel Básico): Perceptrón
**Descripción del problema:** Implemente un perceptrón para resolver una clasificación binaria.

**Datos de entrenamiento:**
- Entrada1: [0, 0] -> Salida: 0
- Entrada2: [0, 1] -> Salida: 1
- Entrada3: [1, 0] -> Salida: 1
- Entrada4: [1, 1] -> Salida: 0

**Resolución:**
\[ w_1 = 1, w_2 = -1, b = -0.5 \]

### Problema 5 (Nivel Intermedio): Backpropagation
**Descripción del problema:** Implemente el backpropagation para entrenar una red neuronal simple.

**Red Neuronal:**
- Entrada a capa oculta
- Capa oculta a salida

**Datos de entrenamiento:**
- Entrada1: [0, 0] -> Salida: 0.5
- Entrada2: [0, 1] -> Salida: 0.7
- Entrada3: [1, 0] -> Salida: 0.8
- Entrada4: [1, 1] -> Salida: 0.9

**Resolución:** 
\[ w_{11} = 0.5, w_{21} = -0.3, b_1 = 0.1 \]

# Aplicación de redes neuronales a datos tabulares

### Problema 6 (Nivel Básico): Regresión
**Descripción del problema:** Implemente una red neuronal para predecir el precio de una casa en función de sus características.

**Datos:**
- Tamaño: [100, 200, 300]
- Precio: [50k, 80k, 100k]

**Resolución:** 
\[ w = 0.2 \]

### Problema 7 (Nivel Intermedio): Clasificación de series de tiempo
**Descripción del problema:** Implemente una red neuronal recurrente para predecir el próximo valor en una serie de tiempo.

**Serie temporal:**
- [1, 3, 5, 7, 9]

**Resolución:** 
\[ w_{input} = 0.2, w_{hidden} = 0.4 \]

# Aprendizaje profundo y frameworks de trabajo

### Problema 8 (Nivel Básico): Aumentación de datos
**Descripción del problema:** Utilice un framework para aumentar la cantidad de datos de entrenamiento.

**Resolución:**
- Aplicación de rotaciones, escalas y distorsiones en las imágenes existentes.

### Problema 9 (Nivel Intermedio): Redes neuronales convolucionales
**Descripción del problema:** Implemente una red neuronal convolucional para clasificar imágenes.

**Datos de entrenamiento:**
- Categorías: Perro, Gato

**Resolución:** 
\[ w_{input} = 0.2, w_{conv1} = 0.3, w_{pooling} = 0.4 \]

### Problema 10 (Nivel Avanzado): Aprendizaje por refuerzo
**Descripción del problema:** Implemente un algoritmo de aprendizaje por refuerzo para una tarea sencilla.

**Resolución:**
- Uso del método Q-Learning

---

Este conjunto de problemas cubre una amplia gama de aplicaciones y nivel de complejidad, desde implementar componentes básicos de redes neuronales hasta resolver problemas más avanzados con redes profundas. Cada problema incluye la descripción del enfoque a seguir para llegar a una solución óptima. 

¡Espero que te sea útil! Si necesitas más ayuda o detalles sobre algún aspecto, no dudes en preguntar. ¡Saludos! 🚀🤖💻🔍📊🚀💡📈🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗🔗