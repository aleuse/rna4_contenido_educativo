```markdown
# Problemas Prácticos

## 1. Optimización con Algoritmos Evolutivos
**Enunciado:**
Diseña un algoritmo evolutivo para resolver un problema de optimización de funciones reales en un espacio bidimensional.

**Solución:**
1. **Inicialización:** Genera una población inicial aleatoria de soluciones.
2. **Evaluación:** Calcula el valor de la función objetivo para cada solución.
3. **Selección:** Usa un método como torneo o ruleta para seleccionar padres.
4. **Cruce:** Aplica un operador de cruce, por ejemplo, punto fijo.
5. **Mutación:** Introduce pequeñas variaciones en las soluciones hijas.
6. **Reemplazo:** Reemplaza a los individuos viejos con nuevos hijos si son mejores.

**Ejemplo:**
- Función objetivo: \(f(x,y) = (x^2 + y - 11)^2 + (x + y^2 -7)^2\)
- Población inicial de 50 soluciones.
- Máximo número de generaciones: 100.

---

## 2. Colonias de Hormigas
**Enunciado:**
Implementa un algoritmo basado en colonias de hormigas para resolver el problema del viajante del comercio (TSP).

**Solución:**
1. **Inicialización:** Crea una colonia de hormigas y inicializa las feromonas.
2. **Constructión:** Las hormigas construyen rutas eligiendo probabilísticamente entre ciudades.
3. **Actualización:** Actualiza la feromona en función del rendimiento de las soluciones encontradas.

**Ejemplo:**
- Ciudades: Madrid, Barcelona, Valencia, Sevilla.
- Longitud máxima de las rutas: 200 km.
- Número de hormigas: 50.
- Factor evaporation: 0.1.

---

## 3. Perceptrones y Backpropagation
**Enunciado:**
Implementa un perceptrón simple para clasificar datos linealmente separables en un conjunto de entrenamiento dado.

**Solución:**
1. **Inicialización:** Inicializa pesos y el sesgo.
2. **Entrenamiento:** Usa backpropagation para ajustar los pesos.
3. **Prueba:** Evalúa la precisión del perceptrón en un conjunto de prueba.

**Ejemplo:**
- Entradas: \(x_1, x_2\).
- Salidas deseadas: 0 o 1.
- Tasa de aprendizaje: 0.3.
- Número de iteraciones: 500.

---

## 4. Regresión con Redes Neuronales
**Enunciado:**
Entrena una red neuronal simple para realizar regresión en un conjunto de datos dado.

**Solución:**
1. **Preprocesamiento:** Normaliza los datos.
2. **Estructura de la red:** Usa una arquitectura con una capa oculta y una salida.
3. **Entrenamiento:** Usa el método del gradiente descendente para ajustar los pesos.
4. **Prueba:** Evalúa la precisión en un conjunto de prueba.

**Ejemplo:**
- Entradas: 10 features.
- Salida deseada: 1 real value.
- Tasa de aprendizaje: 0.1.
- Número de iteraciones: 5000.

---

## 5. Redes Neuronales Recurrentes
**Enunciado:**
Implementa una RNN para predecir series temporales a partir de un conjunto de datos dado.

**Solución:**
1. **Preprocesamiento:** Normaliza los datos y crea secuencias.
2. **Estructura de la red:** Usa un modelo LSTM o GRU.
3. **Entrenamiento:** Entrena el modelo con backpropagation a través del tiempo (BPTT).
4. **Prueba:** Evalúa el rendimiento en una serie temporal futura.

**Ejemplo:**
- Datos de entrenamiento: 100 datos de series temporales.
- Tamaño de secuencia: 20.
- Número de neuronas: 50.
- Número de épocas: 1000.
```
```