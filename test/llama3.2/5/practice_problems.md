**Problemas de Práctica**
==========================

### Sección 1: Optimización con métodos bioinspirados
-----------------------------------------------

#### a. Algoritmos Evolutivos

*   **Problema:** Implemente el algoritmo genético para encontrar la solución óptima a la función de costo `f(x) = x^2 + 10x + 5`.
    *   **Ingresos:**
        *   Población inicial: 100 individuos
        *   Número máximo de generaciones: 50
        *   Tasa de crossover: 0.7
        *   Tasa de mutación: 0.1
    *   **Solución:**
        *   Primero, inicializa la población aleatoriamente.
        *   Repite los siguientes pasos durante `n_max_generaciones`:
            *   Selecciona aleatoriamente a dos padres para el corte over.
            *   Genera los hijos mediante corte y mutación.
            *   Evalúa la función de costo en cada individuo.
            *   selecciona al individuo con menor costo como parte del conjunto de mejores soluciones.
        *   Finalmente, devuelve el mejor individuo encontrado.

#### b. Colonias de hormigas

*   **Problema:** Implemente una colonia de hormigas para resolver la función de costo `f(x) = 3x^2 - 4x + 1`.
    *   **Ingresos:**
        *   Número inicial de hormigas: 10
        *   Tasa de búsqueda: 0.5
        *   Número máximo de iteraciones: 100
    *   **Solución:**
        *   Primero, inicializa la colonia con las hormigas aleatoriamente.
        *   Repite los siguientes pasos durante `n_max_iteraciones`:
            *   Selecciona al hormiga más activa para realizar una búsqueda local.
            *   Evalúa la función de costo en el punto encontrado.
            *   Se mueve hacia el centro de la colonia si se encuentra con un mejor valor que el actual.
        *   Finalmente, devuelve el mejor individuo encontrado.

#### c. Inteligencia de enjambres

*   **Problema:** Implemente una red neuronal con un encaje lineal para predecir la función `f(x) = 2x + 1`.
    *   **Ingresos:**
        *   Número de neuronas en capa de entrada: 1
        *   Número de neuronas en capa oculta: 10
        *   Número de neuronas en capa de salida: 1
        *   Tasa de aprendizaje: 0.01
    *   **Solución:**
        *   Primero, inicializa las pesas aleatoriamente.
        *   Repite los siguientes pasos durante `n_max_iteraciones`:
            *   Selecciona al peso a ajustar.
            *   Calcula la salida de cada neurona en capa oculta usando una función de activación ligera (siendo 0 para neuronas no activadas y 1 para neuronas activadas).
            *   Calcule el error entre la salida deseada y la salida real.
            *   Ajuste las pesas utilizando gradient descendente y ajuste de aprendizaje.
        *   Finalmente, devuelve la red neuronal entrenada.

### Sección 2: Introducción a las redes neuronales
-------------------------------------------

#### a. Perceptrones

*   **Problema:** Implemente un perceptron simple para clasificar puntos en el plano (x, y) como pertenecientes a una clase o no.
    *   **Ingresos:**
        *   Punto de entrada $(x,y)$
        *   Clase deseada $c \in \{0, 1\}$
    *   **Solución:**
        *   Primero, inicializa las pesas y el sesgo aleatoriamente.
        *   Calcule la salida del perceptron usando una función de activación lineal:
            *   $f(x) = w_0x + w_1y + b$
            *   If $(w_0x + w_1y + b)\geq 1$: $f(x) = 1$ Else: $f(x) = 0$
        *   Ajuste las pesas y el sesgo utilizando gradient descendente.
        *   Finalmente, devuelve la clasificación del punto de entrada.

#### b. Backpropagation

*   **Problema:** Implemente backpropagation para minimizar la función de error `E` en una red neuronal simple con una capa oculta de neuronas lineales:
    *   **Ingresos:**
        *   Punto de entrada $(x,y)$
        *   Clase deseada $c \in \{0, 1\}$
    *   **Solución:**
        *   Primero, inicializa las pesas y el sesgo aleatoriamente.
        *   Calcule la salida del perceptron usando una función de activación lineal:
            *   $f(x) = w_0x + w_1y + b$
            *   If $(w_0x + w_1y + b)\geq 1$: $f(x) = 1$ Else: $f(x) = 0$
        *   Calcule el error de la salida usando una función de pérdida de errores (por ejemplo, error categórico)
            *   $E =  \frac{1}{2}[(1-f)^2 + (1-f)^2]$
        *   Calcula los gradientes del error con respecto a las pesas y el sesgo.
        *   Ajuste las pesas y el sesgo utilizando gradient descendente y ajuste de aprendizaje.
        *   Finalmente, devuelve la clasificación del punto de entrada.

#### c. Red neuronal oculta

*   **Problema:** Implemente una red neuronal oculta para predecir un valor continuo dado como entrada `x`.
    *   **Ingresos:**
        *   Valor de entrada $x$
    *   **Solución:**
        *   Primero, inicializa las pesas y el sesgo aleatoriamente.
        *   Repite los siguientes pasos durante `n_max_iteraciones`:
            *   Selecciona al peso a ajustar.
            *   Calcule la salida de cada neurona en capa oculta usando una función de activación lineal.
            *   Calcule el error entre la salida deseada y la salida real.
            *   Ajuste las pesas utilizando gradient descendente y ajuste de aprendizaje.
        *   Finalmente, devuelve la salida final.

### Sección 3: Red neuronal con encaje lineal
-----------------------------------------

*   **Problema:** Implemente una red neuronal con un encaje lineal para predecir el valor continuo `y = f(x)`.
    *   **Ingresos:**
        *   Valor de entrada $x$
    *   **Solución:**
        *   Primero, inicializa las pesas y el sesgo aleatoriamente.
        *   Calcule la salida del perceptron usando una función de activación lineal:
            *   $f(x) = w_0x + b$
        *   Ajuste las pesas y el sesgo utilizando gradient descendente.
        *   Finalmente, devuelve la predicción `y`.