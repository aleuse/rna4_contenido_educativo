1. Problema: Implemente un algoritmo evolutivo para minimizar la función objetivo f(x) = (x - 4)^2, donde x es una variable real.
Solución:
a. Definir la población inicial aleatoriamente dentro del rango [0, 10].
b. Calcular las aptitudes de cada individuo usando la función objetivo.
c. Realizar la selección de reproducción utilizando un torneo.
d. Aplicar los operadores de mutación y crossover.
e. Reemplazar la población anterior con la nueva generación.
f. Repetir desde el paso b hasta que se alcance el criterio de parada (por ejemplo, un número máximo de generaciones).
g. Reportar el individuo con la mejor aptitud después del proceso evolutivo.

2. Problema: Utilizando el modelo de colonias de hormigas para resolver el problema del viajante de comercio en una instancia pequeña.
Solución:
a. Inicializar las colonias de hormigas aleatoriamente en ciudades diferentes.
b. Calcular la distancia entre todas las parejas de ciudades.
c. En cada iteración, escoger un camino de ciudad a ciudad siguiendo las reglas de la pheromona.
d. Actualizar las fórmulas de pheromona después de cada recorrido.
e. Repetir desde el paso c hasta que se alcance el criterio de parada (por ejemplo, un número máximo de iteraciones).
f. Encontrar el recorrido con la menor distancia total usando las colonias de hormigas.

3. Problema: Construya un perceptron para clasificar los puntos en un plano cartesiano si son por encima o debajo de la línea y = 0.5x + 0.7.
Solución:
a. Preprocesar los datos, asignando -1 a los puntos debajo de la línea y 1 a los puntos encima.
b. Entrenar el perceptron utilizando un learning rate adecuado.
c. Calcular el peso w y el sesgo b que minimizan la condición de error (x * w + b - t)^2.
d. Realizar predicciones usando el modelo entrenado y evaluar su precisión.

4. Problema: Aplicar una red neuronal para predecir las ventas semanales de un producto a partir del historial de precios y volúmenes de venta.
Solución:
a. Preprocesar los datos, normalizando los valores e ingresando el tiempo como variables adicionales.
b. Dividir los datos en conjuntos de entrenamiento y prueba adecuados.
c. Diseñar la arquitectura de la red neuronal apropiada (por ejemplo, una sola capa oculta).
d. Entrenar la red con backpropagation y un learning rate adecuado.
e. Hacer predicciones usando el modelo entrenado y compararlas con las ventas reales en el conjunto de prueba.

5. Problema: Implementar un sistema de aprendizaje profundo para reconocimiento de cifras en imágenes utilizando Redes Neuronales Convolutionales (CNN).
Solución:
a. Preprocesar las imágenes, normalizando los valores y rotulando correctamente.
b. Dividir los datos en conjuntos de entrenamiento, validación y prueba adecuados.
c. Diseñar la arquitectura de la CNN apropiada con varias capas convolucionales y max-pooling.
d. Entrenar la CNN utilizando un learning rate adecuado y una función de pérdida apropiada (por ejemplo, cross-entropy).
e. Hacer predicciones usando el modelo entrenado y evaluar su precisión en el conjunto de prueba.

Este conjunto de problemas prácticos aborda los conceptos fundamentales del curso, como la optimización bioinspirada, redes neuronales y aprendizaje profundo, proporcionando ejercicios escalonados desde niveles básicos hasta aplicaciones avanzadas. Cada problema viene acompañado de una solución detallada que guía al estudiante a través del proceso de resolución, reforzando sus conocimientos teóricos con práctica relevante y rigurosa.