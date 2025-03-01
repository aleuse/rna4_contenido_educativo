```markdown
# Practica de Sistemas Bioinspirados y Redes Neuronales

## Problema 1: Algoritmos Evolutivos
**Enunciado**: Dado un problema de optimización, se desea encontrar los valores óptimos para dos parámetros \( x \) e \( y \). Se decide usar un algoritmo evolutivo con una población inicial de 50 individuos. Los parámetros están restringidos a: \( -10 \leq x \leq 10 \), \( -5 \leq y \leq 5 \).

**Solución**: 
1. **Inicialización**: Generar 50 individuos aleatorios dentro de los límites del problema.
2. **Evaluación Fitness**: Calcular el fitness de cada individuo usando la función objetivo.
3. **Selección**: Seleccionar individuos para el proceso de cruce y mutación en base a su fitness.
4. **Cruce (Reproducción)**: Combinar los genes de dos padres para formar hijos.
5. **Mutación**: Introducir pequeñas variaciones en los genes de los nuevos individuos.
6. **Nueva Población**: Sustituir a la población anterior con la nueva generación.

**Ejemplo**: Si la función objetivo es \( f(x, y) = (x - 2)^2 + (y - 3)^2 \), después de varias generaciones, podríamos encontrar que los valores óptimos son \( x^* \approx 2.0 \) e \( y^* \approx 3.0 \).

---

## Problema 2: Colinas de Hormigas
**Enunciado**: Se desea resolver un problema de optimización utilizando el algoritmo de colonias de hormigas. El problema es encontrar los minimos locales en una función bidimensional \( f(x, y) = x^3 - 6x^2 + 4xy - 10 \).

**Solución**:
1. **Inicialización**: Se establecen las reglas para la exploración del espacio de búsqueda (por ejemplo, número de hormigas, límites).
2. **Construcción de Soluciones**: Cada hormiga construye una solución basándose en el olor y la calidad de los caminos recorridos anteriormente.
3. **Actualización del Olor**: Mejores soluciones son fortalecidas con un mayor nivel de pheromona, lo que guía a futuras hormigas hacia ellas.
4. **Iteración**: Este proceso se repite por un número determinado de iteraciones.

**Ejemplo**: Después de varias iteraciones, podríamos encontrar que el valor óptimo es aproximadamente \( (x^*, y^*) = (3, 2) \).

---

## Problema 3: Perceptrones
**Enunciado**: Diseñar un perceptrón simple para clasificar datos linealmente separables.

**Solución**:
1. **Inicialización**: Seleccionar pesos iniciales y el sesgo.
2. **Entrenamiento**: Para cada dato, ajustar los pesos usando la regla de aprendizaje del perceptrón.
3. **Predicción**: Utilizar los pesos finales para hacer predicciones sobre nuevos datos.

**Ejemplo**: Si se tienen dos clases de datos separadas por una recta y se usan pesos iniciales, después del entrenamiento, el perceptrón puede clasificar correctamente todos los datos sin errores.

---

## Problema 4: Redes Neuronales Convolucionales
**Enunciado**: Diseñar una red neuronal convolucional para reconocer objetos en imágenes.

**Solución**:
1. **Capa de Entrada**: La imagen se divide en sub-imágenes (patches).
2. **Convolución**: Usar filtros de convolución para extraer características.
3. **Pooligación**: Reducir la dimensión de las características.
4. **Fully Connected Layer**: Conectar los resultados de la pooligación a una capa completamente conectada.

**Ejemplo**: Se puede diseñar una arquitectura simple como VGG16 o ResNet y entrenarla en un conjunto de datos de imagen para reconocer objetos.

---

## Problema 5: Redes Neuronales Recurrentes
**Enunciado**: Diseñar una red neuronal recurrente (RNN) para predecir la siguiente palabra en una oración basada en las anteriores palabras.

**Solución**:
1. **Ingresos y Ocultos**: Se inicializan los estados ocultos.
2. **Predicción de Palabras**: Para cada palabra, se predice la siguiente usando el estado oculto actualizado.
3. **Actualización del Estado Oculto**: El estado oculto es actualizado usando la nueva información.

**Ejemplo**: Usando un conjunto de datos como el de texto en "IMDB Reviews", una RNN puede predecir correctamente las próximas palabras y categorizar reseñas positivas vs negativas.

---

## Problema 6: Aprendizaje Profundo con Difusión Estable
**Enunciado**: Diseñar un modelo de difusión estable para generar imágenes a partir de ruido.

**Solución**:
1. **Inverso del Modelo**: Crear el inverso del modelo que genera ruido desde una imagen real.
2. **Entrenamiento del Inverso**: Entrenar este inverso usando gradientes invertidos y los datos reales.
3. **Generación de Imágenes**: Usar el inverso entrenado para generar nuevas imágenes a partir de ruido.

**Ejemplo**: Usando Stable Diffusion, se puede generar una imagen realista a partir de texto de entrada, como "una flor en un jardín" o "un perro corriendo en la playa".

---

## Problema 7: Redes Neuronales Recurrentes con Transformers
**Enunciado**: Diseñar una arquitectura que combine redes neuronales recurrentes (RNN) y transformers para mejorar el procesamiento de secuencias.

**Solución**:
1. **Inserción de Tokens Especiales**: Añadir tokens especiales al inicio y final de la secuencia.
2. **Atención Múltiple**: Utilizar múltiples capas de atención en las neuronas recurrentes para capturar dependencias a largo plazo.
3. **Fusión de Información**: Combinar información de RNN y transformers para mejorar el procesamiento.

**Ejemplo**: Se puede diseñar una arquitectura como BERT o T5 que combina RNN y transformers para realizar tareas como la traducción, el resumen de textos u otras tareas de lenguaje natural.
```

This document includes 7 practice problems covering a wide range of topics in machine learning and deep learning, each with a brief explanation of the problem statement and solution approach. ``` This comprehensive set of practice problems covers various key concepts in machine learning and deep learning, including perceptrons, convolutional neural networks (CNNs), recurrent neural networks (RNNs), transformers, and more advanced techniques like stable diffusion models.

Here's an overview of each problem:

1. **Perceptron Design**: Focuses on designing a simple perceptron to classify linearly separable data.
2. **Convolutional Neural Networks (CNN)**: Covers the design and training process for CNNs used in image recognition tasks.
3. **Recurrent Neural Networks (RNN)**: Introduces RNNs for sequence prediction, such as predicting words in a sentence.
4. **Stable Diffusion Models**: Explores the creation of generative models that can produce realistic images from noise.
5. **Transformers with RNNs**: Describes combining transformers and RNNs to enhance sequence processing.

Each problem includes an explanation of the task, key steps involved in solving it, and examples of what can be achieved. This should serve as a useful resource for students or practitioners looking to deepen their understanding of these topics. ```