```markdown
# Práctica de problemas: Conocimientos Específicos

## 1. Sistemas bioinspirados: Algoritmos Evolutivos
### Problema Básico:
**Enunciado:** Diseñar un algoritmo evolutivo para optimizar la expresión matemática \( f(x) = x^2 + 5x + 10 \).  
**Solución:**  
1. Seleccionar una población inicial de 50 individuos con valores aleatorios entre -10 y 10.  
2. Aplicar el operador de mutación punto 1: \( x_{n+1} = x_n + \delta \), donde \( \delta \) es un valor pequeño aleatorio entre -0.5 y 0.5.  
3. Calcular la fitness de cada individuo usando la función \( f(x) \).  
4. Realizar operación de selección (ejemplo, el mejor de cada nacimiento).  
5. Repetir los pasos 2-4 por 100 generaciones y seleccionar el meilleur x que minimize \( f(x) \).

**Resultado Esperado:** Alrededor de x = -2.

---

### Problema Intermedio:
**Enunciado:** Implementar un algoritmo evolutivo para maximizar la altura de una torre usando los mismos coeficientes.  
**Solución:**  
1. Definir el mismo fitness function \( f(x) \).  
2. Implementar mutación y operadores de selección similares.  
3. Correr 50 runs de 100 generaciones y comparar la altura promedio.

**Resultado Esperado:** Alrededor de x = -2.1 con altura mayor a 10.

---

### Problema Avanzado:
**Enunciado:** Comparar los resultados de un algoritmo evolutivo vs. Backpropagation para la misma función \( f(x) \).  
**Solución:**  
1. Implementar ambos métodos.  
2. Correr 20 runs con parámetros ajustados para ambos.  
3. Comparar la precisión y velocidad en la búsqueda de x óptimo.

**Resultado Esperado:** Backpropagation será más precisa pero el algoritmo evolutivo tendrá menores recursos.

---

## 2. Redes Neuronales: Perceptrones y Backpropagation
### Problema Básico:
**Enunciado:** Implementar un perceptron para clasificar datos binarios (0/1).  
**Solución:**  
1. Definir dataset con 100 ejemplos de 0 y 1.  
2. Normalizar los ejemplos.  
3. Implementar una red simple con 1 neuroná.  
4. Ajustar el阈值 y weights using stochastic gradient descent.

**Resultado Esperado:** Acierto mayor al 70%.

---

### Problema Intermedio:
**Enunciado:** IMPLEMENTAR Backpropagation para predecir la clase de un dataset pequeño.  
**Solución:**  
1. Usar dataset de 50 ejemplos.  
2. Crear una red con 3 capas: entrada, oculta y salida.  
3. Entrenar con learning rate=0.01 y momentum=0.9.

**Resultado Esperado:** Accuracy >80%.

---

### Problema Avanzado:
**Enunciado:** Aplicar perceptrones en TensorFlow para regresión lineal.  
**Solución:**  
1. Usar dataset de regresión simple (ejemplo: ventas vs. día).  
2. Implementar modelo con 10 neurons en capa oculta.  
3. Training with batch size=32 y epochs=100.

**Resultado Esperado:** R² >0.8.

---

## 3. Aprendizaje Profundo y Frameworks
### Problema Básico:
**Enunciado:** Implementar una red neuronal convolucional para detectar círculos en imágenes.  
**Solución:**  
1. Crear dataset de imágenes de círculos y no-círculos.  
2. Configurar una red con 3 capas convoluciones: 5x5, 3x3, y 2x2.  
3. Training with labels using Adam optimizer.

**Resultado Esperado:** Accuracy >90%.

---

### Problema Intermedio:
**Enunciado:** Implementar un GAN (Generative Adversarial Network) para generar imágenes de círculos aleatorios.  
**Solución:**  
1. Configurar dos reds: discriminadora y generativa.  
2. Training alternado por 100 iteraciones.  
3. Monitorizar losses.

**Resultado Esperado:** Imágenes realistas con alta variación.

---

### Problema Avanzado:
**Enunciado:** Comparar performance de diferentes frameworks (TensorFlow, PyTorch) en un dataset pequeño.  
**Solución:**  
1. Usar dataset de regresión simple.  
2. Implementarredes similares en ambos frameworks.  
3. Training y comparar precision, time, y stability.

**Resultado Esperado:** PyTorch tendrá mejor performance pero dependiendo del dataset.
```