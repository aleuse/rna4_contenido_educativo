# Problemas de práctica - Sistemas bioinspirados y optimización

## 1. Juego de la vida (Fácil)
**Descripción:**  
Analice el siguiente estado del juego de la vida y determine cuál será el próximo estado aplicando las reglas del juego.  
*Estado actual:*  
0 1 0  
1 0 1  
0 1 0  

**Solución:**  
- Primero, identifiquemos las células actuales que están vivas (1) y muertas (0).  
- En el centro, hay una célula viva. Las reglas del juego de la vida son:
  - Una célula muerta produce una viva si tiene exactamente dos células vivas en su vecindad inmediata.
  - Las demás combinaciones no generan vida.  
- Aplicando la regla: La célula central muerta tiene exactamente *dos* células vivas (las superiores y posteriores), por lo que se convierte en viva.  
**Estado siguiente:**  
1 0 0  
0 1 0  
0 1 0  

## 2. Algoritmos Evolutivos (Difícil)
**Descripción:**  
Implemente un algoritmo evolutivo simple para buscar la función fitness óptima en una población dada. Proporcióne y compare las probabilidades de supervivencia de los individuos más aptos.  

**Solución:**  
- **Población inicial:** 100 individuos aleatorios.  
- **Función fitness:** Cuanto mayor es la suma de sus coordenadas x² + y², mejor es el individuo.  
- **Selección natural:** Eliminarán los menos aptos durante varias generaciones.  
- *Resultados:* El algoritmo mostrará que las probabilidades de supervivencia se incrementan seleccionando a los mejores cromosomas.

## 3. Redes Neuronales Básicas (Intermedia)
**Descripción:**  
Determine qué es el modelo de la neurona de los mamíferos y cómo transmiten las señales neuronales.  

**Solución:**  
- Las neuronas mamíferas transmiten señales químicas a través de sinapsis.  
- La información se procesa en cascada, desde las percepciones hasta la corteza cerebral.

## 4. Perceptrones y Backpropagation (Difícil)
**Descripción:**  
Implemente un perceptron y aplique backpropagation para predecir si una imagen es de gatos o perros usando datos de entrenamiento.  

**Solución:**  
- **Datos de entrenamiento:** 500 imágenes de gatos y 500 de perros.  
- **Red:** Perceptron hidden layer con 20 neuronas y salida binaria.  
- *Ajustes:* Aumentar el learning rate si no se logra buen rendimiento.

## 5. Aplicación a Datos Tabulares (Intermedia)
**Descripción:**  
Crea un perceptron que predica la edad de una persona basada en sus características como altura y peso.  

**Solución:**  
- **Datos de entrenamiento:** Edades y características de 30 personas.  
- **Modelo:** Perceptron con una capa oculta de 4 neuronas.  
- *Predicción:* Márgenes de error menores a 5 años.

## 6. Series de Tiempo (Dífico)
**Descripción:**  
Predeca un modelo de series de tiempo usando Redes Neuronales y pruebe su eficacia en datos reales de stocks.  

**Solución:**  
- **Datos:** Series diarias de precios de acción de 10 años.  
- **Modelo:** RNN con 50 neuronas en la capa oculta.  
- *Resultados:* Precisiones superiores a 90% en pronósticos a largo plazo.

# Problemas de práctica - Optimización y avances

## 7. Aprendizaje por Refuerzo (Avanzado)
**Descripción:**  
Implemente un método de aprendizaje por refuerzo para optimizar una función usando experiencia interna.  

**Solución:**  
- **Ensamble:** Agregue ponderaciones a cada muestra basada en su contribución a la caída de la función.  
- *Resultados:* Mejora constante en la precisión de las predicciones.

## 8. Difusión Estandar (Avanzado)
**Descripción:**  
Determine cómo aplicar difusión estandar para distribuir calor en una habitación y minimizar el error cuadrático.  

**Solución:**  
- **Matriz de Covarianza:** Calcula la matriz de covarianzas de las observaciones.  
- *Ajuste:* Añadir la matriz de covarianzas al inverso de la matriz de datos para obtener la difusión.

## 9. Redes Neuronales Recurrentes (Avanzado)
**Descripción:**  
Crea un modelo de RNN para predecir secuencias de texto usando transformers.  

**Solución:**  
- **Datos:** Textos enteros con marcas de posición.  
- **Modelo:** RNN con capas de atención multimodal.  
- *Entrenamiento:* Utilice dataset grandes y variedad de temas.

## 10. Transformadores (Avanzado)
**Descripción:**  
Explique cómo los transformers aprenden a traducir texto usando atención múltiple.  

**Solución:**  
- **Aprendizaje:** Los transformers aprenden que la atención múltiple captura relaciones en el texto.  
- *Aplicación:* Traducción, sumarios, etc.

# Conclusión
Estos problemas abarcan desde la introducción básica hasta aplicaciones avanzadas de IA, fomentando el desarrollo de habilidades en modelado y optimización.
```