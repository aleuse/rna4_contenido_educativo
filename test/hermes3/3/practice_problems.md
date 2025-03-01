## Ejercicios de práctica

### Optimización con métodos bioinspirados

#### Problema 1: Algoritmos Evolutivos (Fácil)

**Enunciado:** Utilizando el algoritmo evolutivo de selección natural, se desea optimizar la solución de un problema de viaje del tipo TSP (Travelling Salesman Problem) con n ciudades y distancias conocidas entre ellas. Diseñar un algoritmo que encuentre la ruta óptima.

**Solución:**
1. Inicializar una población aleatoria de soluciones (rutas).
2. Calcular el fitness de cada individuo.
3. Realizar la selección de padres utilizando un criterio como tournament selection.
4. Aplicar los operadores genéticos de crossover y mutación para generar una nueva generación de soluciones.
5. Reemplazar la población anterior con la nueva generación.
6. Repetir los pasos 2-5 durante un número suficiente de generaciones o hasta que se alcance un fitness objetivo.

**Problema 2: Colonias de Hormigas (Intermedio)**

**Enunciado:** Se tiene una gráfica con n nodos representando ciudades y distancias conocidas entre ellos. Utilizando el algoritmo de colonias de hormigas, encontrar la ruta óptima para visitar todas las ciudades.

**Solución:**
1. Inicializar una población de soluciones (rutas) aleatoriamente.
2. Calcular el fitness de cada individuo (ruta) considerando la distancia recorrida.
3. Para cada hormiga, realizar un recorrido siguiendo las reglas:
   - Eligiendo la siguiente ciudad visitada teniendo en cuenta la pheromona y la distancia.
   - Actualizar las pheromonas de acuerdo con la calidad de la solución encontrada.
4. Reemplazar la población anterior con la nueva generación.
5. Repetir los pasos 2-4 durante un número suficiente de iteraciones o hasta que se alcance una solución óptima.

### Introducción a las redes neuronales: el modelo de la neurona de los mamíferos

#### Problema 3: Perceptrones (Fácil)

**Enunciado:** Se tiene un conjunto de datos tabulares con características x y una etiqueta de salida y. Utilizar un perceptron simple para realizar la clasificación binaria.

**Solución:**
1. Inicializar los pesos w y el umbral b de manera aleatoria.
2. Para cada muestra (x, y) en el conjunto de entrenamiento:
   - Calcular la predicción z = wx + b.
   - Actualizar los pesos w y el umbral b siguiendo las reglas del aprendizaje por difusión:
     - Si la predicción es correcta (z > 0 para y = 1, z < 0 para y = -1), dejar los valores sin cambios.
     - Si la predicción está equivocada, actualizar w y b de manera proporcional al error para minimizarlo.

#### Problema 4: Backpropagation (Intermedio)

**Enunciado:** Utilizando una red neuronal feedforward con capas ocultas, realizar el problema de clasificación de imágenes digitales.

**Solución:**
1. Inicializar los pesos w de las conexiones y los umbrales b de las neuronas.
2. Para cada imagen (x, y) en el conjunto de entrenamiento:
   - Realizar la propagación hacia delante para calcular las predicciones z en cada capa oculta y en la salida.
   - Calcular el error en la salida E = (y - a)^2/2, donde a es la activación de la última neurona.
   - Propagar el error de regreso hacia la red utilizando la regla del delta:
     - Para la capa de salida: δi = E * (a_i - y_i) para cada neurona i.
     - Para las capas ocultas: δi = (δj * wji) * f'(net_i), donde δj es el error retropropagado en la neurona j, net_i es la entrada a la neurona i, y f'(net_i) es la derivada de la función activación.
   - Actualizar los pesos w y los umbrales b siguiendo las reglas:
     - Δwji = α * δj * a_i para cada conexión j -> i, donde α es el factor de aprendizaje.
     - Δbi = α * δi para cada neurona i.

### Aplicación de redes neuronales a datos tabulares

#### Problema 5: Regresión (Fácil)

**Enunciado:** Se tiene un conjunto de datos tabulares con características x y una etiqueta numérica y. Utilizar una red neuronal simple para realizar la regresión.

**Solución:**
1. Inicializar los pesos w y el umbral b de manera aleatoria.
2. Para cada muestra (x, y) en el conjunto de entrenamiento:
   - Calcular la predicción z = wx + b.
   - Actualizar los pesos w y el umbral b siguiendo las reglas del aprendizaje por difusión:
     - Si la predicción está equivocada, actualizar w y b de manera proporcional al error para minimizarlo.

#### Problema 6: Series de tiempo (Intermedio)

**Enunciado:** Dada una serie temporal de datos económicos, predecir el valor futuro utilizando una red neuronal recurrente.

**Solución:**
1. Inicializar los pesos w y los umbrales b de manera aleatoria.
2. Para cada paso temporal en la serie:
   - Calcular las predicciones z en función de las entradas x y los pesos w, teniendo en cuenta las conexiones recurrentes.
   - Actualizar los pesos w y los umbrales b siguiendo las reglas del aprendizaje por retropropagación:
     - Para cada neurona i, actualizar Δwi = α * δi * xi, donde δi es el error retropropagado en la neurona i y α es el factor de aprendizaje.

### Aprendizaje profundo y frameworks de trabajo

#### Problema 7: Aumentación de datos (Fácil)

**Enunciado:** Utilizar técnicas de augmentación para aumentar un conjunto de datos de imágenes digitales, permitiendo mejorar la robustez de las redes neuronales entrenadas.

**Solución:**
1. Para cada imagen original:
   - Realizar rotaciones.
   - Realizar traslaciones.
   - Cambiar el brillo y el contraste.
   - Aplicar guías de color.
   - Etc.

#### Problema 8: Redes neuronales convolucionales (Intermedio)

**Enunciado:** Utilizar una red neuronal convolutional para la clasificación de imágenes en un conjunto de datos de imagen con gran cantidad de clases.

**Solución:**
1. Inicializar los filtros w y los umbrales b de manera aleatoria.
2. Realizar las operaciones de convolución, pooling y activación en cada capa del modelo convolutional.
3. Unir las características extraídas por las convoluciones para realizar la clasificación final utilizando capas densas.

Espero que esto te ayude a entender mejor los conceptos presentados en este problema propuesto! Si tienes alguna duda o necesitas más detalles, no dudes en preguntar.