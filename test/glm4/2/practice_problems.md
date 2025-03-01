### Problemas de Práctica con Soluciones

#### Problema 1: Algoritmos Evolutivos
**Dificultad:** Básico

**Descripción del problema:**
Un ingeniero está diseñando un algoritmo evolutivo para encontrar la solución óptima a un problema de asignación de recursos. La población inicial tiene 10 individuos y el genoma de cada individuo representa una posible solución para la asignación. El objetivo es maximizar el rendimiento del sistema.

**Ejercicio:**
Implemente una simple función de fitness para evaluar las soluciones y realice una generación de algoritmo evolutivo.

**Solución:**

```python
import random

# Definir la función de fitness
def fitness(solution):
    return sum(solution)

# Inicializar la población
population_size = 10
population = [[random.randint(0, 100) for _ in range(5)] for _ in range(population_size)]

# Evolución de una generación
new_population = []
for _ in range(population_size):
    parent1 = max(population, key=fitness)
    parent2 = max(population, key=lambda x: x if x != parent1 else min(population, key=fitness))
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    
    # Mutación
    mutation_rate = 0.01
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child[i] = random.randint(0, 100)
    
    new_population.append(child)

population = new_population

# Resultado final
best_solution = max(population, key=fitness)
print("Mejor solución:", best_solution)
```

#### Problema 2: Colonias de hormigas
**Dificultad:** Intermedio

**Descripción del problema:**
Un equipo de investigadores está utilizando el algoritmo de colonias de hormigas para resolver un problema de routed-based optimization. Se sabe que hay 5 puntos de interés y se desea encontrar la ruta más eficiente entre ellos.

**Ejercicio:**
Implemente una función que simule el comportamiento de las hormigas y encuentre la ruta óptima.

**Solución:**

```python
import random

# Definir los puntos de interés
points = [(0, 0), (1, 2), (3, 5), (4, 8), (6, 10)]

# Inicializar las feromonas y la ruta actual
pheromones = [[1.0 for _ in range(len(points))] for _ in range(len(points))]
current_route = [random.randint(0, len(points) - 1)]
visited_points = [current_route[0]]

# Función de costo para una ruta
def route_cost(route):
    return sum((points[route[i]] - points[route[i + 1]])**2 for i in range(len(route) - 1))

# Función para actualizar las feromonas
def update_pheromones(best_route, route):
    pheromone_factor = 0.5
    evaporation_rate = 0.5

    for i in range(len(points)):
        for j in range(len(points)):
            if i not in visited_points and j not in visited_points:
                if (i, j) in best_route:
                    pheromones[i][j] += pheromone_factor
                else:
                    pheromones[i][j] -= evaporation_rate

    return pheromones

# Función para encontrar la ruta mejorada
def find_better_route():
    global current_route, visited_points
    new_route = [current_route[-1]]
    
    while len(new_route) < len(points):
        next_point = random.choices(range(len(points)), weights=pheromones[current_route[-1]], k=1)[0]
        if next_point not in visited_points:
            visited_points.append(next_point)
            new_route.append(next_point)

    return new_route

# Evolución de las generaciones
best_cost = float('inf')
for _ in range(100):
    best_route = find_better_route()
    current_route = [points[best_route[0]][0], points[best_route[0]][1]]
    
    cost = route_cost(best_route)
    if cost < best_cost:
        best_cost = cost
        pheromones = update_pheromones(best_route, new_route)

print("Mejor ruta:", best_route)
```

#### Problema 3: Perceptrones y Backpropagation
**Dificultad:** Avanzado

**Descripción del problema:**
Se tiene un conjunto de datos de clasificación binaria con características discretas. El modelo es un perceptron simple para predecir la clase a la que pertenece cada ejemplo.

**Ejercicio:**
Implemente el algoritmo de backpropagation para entrenar el perceptrón y realice una predicción.

**Solución:**

```python
import numpy as np

# Conjunto de datos
X = np.array([[0, 1], [1, 1], [1, 0], [0, 0]])
y = np.array([0, 1, 1, 0])

# Inicializar los pesos y biases
np.random.seed(0)
weights = np.random.randn(2, 1)
bias = np.random.randn(1)

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función para calcular la predicción
def predict(X, weights, bias):
    return sigmoid(np.dot(X, weights) + bias)

# Función de pérdida cuadrática media
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred)**2).mean()

# Entrenamiento del perceptrón
learning_rate = 0.1
for _ in range(1000):
    # Predicción actual
    predictions = predict(X, weights, bias)
    
    # Error de la pérdida
    error = (y - predictions) * sigmoid_derivative(predictions)
    
    # Actualización de los pesos y biases
    weights += learning_rate * np.dot(X.T, error)
    bias += learning_rate * np.sum(error)

# Predicción final para un nuevo ejemplo
new_example = np.array([[1, 0]])
final_prediction = predict(new_example, weights, bias)
print("Predicción:", sigmoid(final_prediction))
```

#### Problema 4: Aplicación de Redes Neuronales a Datos Tabulares (Regresión)
**Dificultad:** Básico

**Descripción del problema:**
Se tiene un conjunto de datos con características numéricas y se desea predecir una variable continua.

**Ejercicio:**
Implemente una red neuronal simple para realizar la regresión lineal y realice una predicción.

**Solución:**

```python
import numpy as np

# Conjunto de datos
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3, 5, 7, 11])

# Inicializar los pesos y biases
np.random.seed(0)
weights = np.random.randn(1, 1)
bias = np.random.randn(1)

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función para calcular la predicción
def predict(X, weights, bias):
    return sigmoid(np.dot(X, weights) + bias)

# Entrenamiento del modelo
learning_rate = 0.01
for _ in range(1000):
    predictions = predict(X, weights, bias)
    
    # Error de la pérdida
    error = y - predictions
    
    # Actualización de los pesos y biases
    weights += learning_rate * np.dot(X.T, error)
    bias += learning_rate * np.sum(error)

# Predicción final para un nuevo ejemplo
new_example = np.array([[6]])
final_prediction = predict(new_example, weights, bias)
print("Predicción:", sigmoid(final_prediction))
```

#### Problema 5: Aplicación de Redes Neuronales a Datos Tabulares (Clasificación)
**Dificultad:** Avanzado

**Descripción del problema:**
Se tiene un conjunto de datos de clasificación con características numéricas y se desea predecir la clase a la que pertenece cada ejemplo.

**Ejercicio:**
Implemente una red neuronal para realizar la clasificación binaria y realice una predicción.

**Solución:**

```python
import numpy as np

# Conjunto de datos
X = np.array([[1, 2], [2, 3], [4, 5], [5, 6], [7, 8]])
y = np.array([0, 1, 1, 0, 1])

# Inicializar los pesos y biases
np.random.seed(0)
weights = np.random.randn(2, 1)
bias = np.random.randn(1)

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función para calcular la predicción
def predict(X, weights, bias):
    return sigmoid(np.dot(X, weights) + bias)

# Entrenamiento del modelo
learning_rate = 0.01
for _ in range(1000):
    predictions = predict(X, weights, bias)
    
    # Error de la pérdida
    error = (y - predictions) * sigmoid_derivative(predictions)
    
    # Actualización de los pesos y biases
    weights += learning_rate * np.dot(X.T, error)
    bias += learning_rate * np.sum(error)

# Predicción final para un nuevo ejemplo
new_example = np.array([[6, 7]])
final_prediction = predict(new_example, weights, bias)
print("Predicción:", sigmoid(final_prediction))
```

Estas soluciones proporcionan implementaciones básicas y avanzadas de diferentes algoritmos y técnicas en el campo del aprendizaje automático.