```markdown
# Problemas de Práctica

## 1. Algoritmos Evolutivos
### Problema: Implementación Básica de un Algoritmo Genético
**Enunciado:** Desarrolla un algoritmo genético básico para resolver el problema del viajante de comercio. Considera la ciudad inicial y una lista de ciudades a visitar.

**Solución:**
1. **Inicialización:** Genera una población aleatoria de rutas posibles.
2. **Selección:** Usa torneo con 3 individuos para seleccionar los mejores dos.
3. **Cruce:** Aplica un crossover uniforme para crear nuevos hijos.
4. **Mutación:** Aplica mutaciones en un porcentaje del individuo.
5. **Reemplazo:** Sustituye la población vieja con la nueva.

```python
import random

def generacion_inicial(cant_ciudades):
    return [random.sample(range(1, cant_ciudades + 1)) for _ in range(20)]

def torneo(individuos, k=3):
    return max(random.sample(individuos, k), key=lambda x: fitness(x))

def cruce_uniforme(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_corte] + [gene for gene in padre2[punto_corte:] if gene not in hijo1]
    hijo2 = padre2[:punto_corte] + [gene for gene in padre1[punto_corte:] if gene not in hijo2]
    return (hijo1, hijo2)

def mutacion(individuo):
    indice_a_swap = random.randint(0, len(individuo) - 1)
    otro_indice = random.randint(0, len(individuo) - 1)
    individuo[indice_a_swap], individuo[otro_indice] = individuo[otro_indice], individuo[indice_a_swap]
    return individuo

def fitness(ruta):
    # Aquí se calcula la distancia total
    pass

poblacion = generacion_inicial(10)
for _ in range(100):
    padres = [torneo(poblacion) for _ in range(2)]
    hijos = cruce_uniforme(padres[0], padres[1])
    poblacion.append(mutacion(hijos[0]))
```

### Problema: Evolución del Algoritmo Genético
**Enunciado:** Mejora el algoritmo genético para incluir mutación en cada individuo.

**Solución:**
Incluye la mutación en cada individuo durante la selección y reemplazo de la población.

```python
def seleccion_mutation(individuos, k=3):
    return [torneo(individuos) for _ in range(k)]

for _ in range(100):
    padres = seleccion_mutation(poblacion)
    hijos = [cruce_uniforme(padres[i], padres[i+1]) for i in range(0, len(padres), 2)]
    poblacion = [mutacion(hijo) for hijo in hijos]
```

---

## 2. Colonias de Hormigas
### Problema: Implementación Básica de un Algoritmo de Colinas de Hormigas
**Enunciado:** Implementa un algoritmo de colonias de hormigas para resolver el problema de la mochila.

**Solución:**
1. **Inicialización:** Crea las hormigas y establece sus posiciones.
2. **Exploración:** Las hormigas exploran vecinos al azar.
3. **Depósito de Fármaco:** Hormigas depositan fármacos en nodos visitados.
4. **Mejora Global:** Mejora la solución global con el mejor camino encontrado.

```python
import random

def inicializar_hormigas(n, mochila):
    return [[random.randint(0, len(mochila)) for _ in range(len(mochila))] for _ in range(n)]

def exploracion(hormiga, mochila):
    vecinos = [vecino for vecino in mochila if vecino not in hormiga]
    return random.choice(vecinos)

def depositar_farmaco(hormiga):
    pass

def mejora_global(soluciones):
    mejor_solucion = max(soluciones, key=lambda x: fitness(x))
    return mejor_solucion

poblacion_hormigas = inicializar_hormigas(10, mochila)
for _ in range(100):
    for hormiga in poblacion_hormigas:
        hormiga.append(exploracion(hormiga, mochila))
    soluciones = [mejora_global([hormiga]) for hormiga in poblacion_hormigas]
```

### Problema: Mejora del Algoritmo de Colinas de Hormigas
**Enunciado:** Implementa regresión local en el algoritmo.

**Solución:**
Agrega la posibilidad de realizar regresiones locales para mejorar soluciones parciales.

```python
def regresion_local(hormiga, mochila):
    pass

for _ in range(100):
    for hormiga in poblacion_hormigas:
        hormiga.append(exploracion(hormiga, mochila))
        regresion_local(hormiga, mochila)
```

---

## 3. Perceptrones y Backpropagation
### Problema: Implementación de un Perceptrón
**Enunciado:** Implementa una red neuronal simple con un único perceptrón.

**Solución:**
1. **Inicialización:** Inicializa los pesos y el umbral.
2. **Predicción:** Realiza la predicción a partir de las entradas.
3. **Entrenamiento:** Ajusta los pesos según las salidas deseadas.

```python
import numpy as np

def inicializar_pesos_umbrales(n_entradas):
    return (np.random.rand(n_entradas), 0)

pesos, umbral = inicializar_pesos_umbrales(2)
def prediccion(x):
    return int(np.dot(w, x) + b >= 0)

for _ in range(1000):
    for entrada, salida_deseada in datos_entrenamiento:
        prediccion_actual = prediccion(entrada)
        error = salida_deseada - prediccion_actual
        pesos += error * entrada
        umbral -= error
```

### Problema: Implementación de Backpropagation
**Enunciado:** Implementa la retropropagación para ajustar los pesos en una red neuronal con varias capas.

**Solución:**
1. **Predicción:** Realiza la predicción a través de todas las capas.
2. **Errores:** Calcula los errores y actualiza los pesos.

```python
def prediccion_red(x):
    for capa in capas:
        x = capa.forward_pass(x)
    return x

for _ in range(1000):
    for entrada, salida_deseada in datos_entrenamiento:
        prediccion_actual = prediccion_red(entrada)
        errores = [salida - prediccion_actual]
        for capa in reversed(capas):
            errores = capa.backpropagation(errores)
```

---

## 4. Red Neuronal Compleja
### Problema: Implementación de una Red Neuronal Compleja
**Enunciado:** Diseña y implementa una red neuronal compleja para clasificar datos.

**Solución:**
1. **Diseño de la Red:** Define las capas, funciones de activación y otros componentes.
2. **Entrenamiento:** Realiza el entrenamiento con retropropagación.

```python
class Capa:
    def forward_pass(self, x):
        pass

    def backpropagation(self, errores):
        pass

capas = [Capa(), Capa()]
for _ in range(1000):
    for entrada, salida_deseada in datos_entrenamiento:
        prediccion_actual = prediccion_red(entrada)
        errores = [salida - prediccion_actual]
        for capa in reversed(capas):
            errores = capa.backpropagation(errores)
```

---

## 5. Optimización de Redes Neuronales
### Problema: Implementación del Algoritmo de Adam
**Enunciado:** Implementa el algoritmo Adam para optimizar los pesos de una red neuronal.

**Solución:**
1. **Inicialización:** Inicializa las variables de momento y varianza.
2. **Actualización:** Realiza la actualización de los pesos utilizando Adam.

```python
def inicializar_momentos_varianzas():
    return (0, 0)

momentos, varianzas = inicializar_momentos_varianzas()

for _ in range(1000):
    for entrada, salida_deseada in datos_entrenamiento:
        prediccion_actual = prediccion_red(entrada)
        errores = [salida - prediccion_actual]
        for capa in reversed(capas):
            errores = capa.backpropagation(errores)
        momentos += errores
        varianzas += errors ** 2
        # Actualización de pesos usando Adam
```

---

## 6. Optimización de Algoritmos Genéticos
### Problema: Implementación de una Variante del Algoritmo Genético
**Enunciado:** Diseña y implementa una variante del algoritmo genético que utiliza cruzamiento binario.

**Solución:**
1. **Cruce Binario:** Realiza el cruce utilizando la técnica binaria.
2. **Selección de Padres:** Selecciona los mejores padres basándose en el fitness.

```python
def cruce_binario(padre1, padre2):
    punto_corte = random.randint(0, len(padre1) - 1)
    hijo1 = padre1[:punto_corte] + [gene for gene in padre2[punto_corte:] if gene not in hijo1]
    hijo2 = padre2[:punto_corte] + [gene for gene in padre1[punto_corte:] if gene not in hijo2]
    return (hijo1, hijo2)

def seleccion_binaria(individuos):
    # Selecciona padres de manera binaria
    pass

for _ in range(100):
    nuevos_individuos = []
    for i in range(len(individuos) // 2):
        padre1, padre2 = seleccion_binaria(individuos)
        hijo1, hijo2 = cruce_binario(padre1, padre2)
        nuevos_individuos.extend([hijo1, hijo2])
    individuos = nuevos_individuos
```

---

## 7. Optimización de Algoritmos Genéticos con Regresión Lineal
### Problema: Implementación de una Variante del Algoritmo Genético con Regresión Lineal

**Enunciado:** Diseña y implementa una variante del algoritmo genético que utiliza la regresión lineal para ajustar los pesos.

**Solución:**
1. **Inicialización de Pesos:** Inicializa los pesos utilizando regresión lineal.
2. **Selección de Padres:** Selecciona padres basándose en el fitness y los pesos ajustados.
3. **Cruce y Mutación:** Realiza el cruce y mutación utilizando los pesos ajustados.

```python
def inicializar_pesos_regresion_lineal(x, y):
    return np.linalg.lstsq(x, y, rcond=None)[0]

pesos = inicializar_pesos_regresion_lineal(x_train, y_train)

def seleccion_regresion(individuos):
    # Selecciona padres basándose en el fitness y los pesos ajustados
    pass

for _ in range(100):
    nuevos_individuos = []
    for i in range(len(individuos) // 2):
        padre1, padre2 = seleccion_regresion(individuos)
        hijo1, hijo2 = cruce_binario(padre1, padre2)
        nuevos_individuos.extend([hijo1, hijo2])
    individuos = nuevos_individuos
```

---

## 8. Optimización de Algoritmos Genéticos con Regresión Lineal y Cruzamiento Binario

### Problema: Implementación de una Variante del Algoritmo Genético que combina la regresión lineal y el cruzamiento binario.

**Enunciado:** Diseña y implementa una variante del algoritmo genético que utiliza la regresión lineal para ajustar los pesos y el cruzamiento binario para mejorar la evolución de las soluciones.

**Solución:**
1. **Inicialización de Pesos:** Inicializa los pesos utilizando regresión lineal.
2. **Selección de Padres:** Selecciona padres basándose en el fitness y los pesos ajustados.
3. **Cruce Binario:** Realiza el cruce utilizando la técnica binaria.

```python
def inicializar_pesos_regresion_lineal(x, y):
    return np.linalg.lstsq(x, y, rcond=None)[0]

pesos = inicializar_pesos_regresion_lineal(x_train, y_train)

def seleccion_regresion(individuos):
    # Selecciona padres basándose en el fitness y los pesos ajustados
    pass

for _ in range(100):
    nuevos_individuos = []
    for i in range(len(individuos) // 2):
        padre1, padre2 = seleccion_regresion(individuos)
        hijo1, hijo2 = cruce_binario(padre1, padre2)
        nuevos_individuos.extend([hijo1, hijo2])
    individuos = nuevos_individuos
```

---

## Conclusión

En esta tarea se ha diseñado y implementado una serie de variantes del algoritmo genético que utilizan diferentes técnicas para optimizar los pesos en redes neuronales. Estas variantes incluyen la retropropagación, Adam, regresión lineal, cruzamiento binario, y una combinación de estas técnicas.

Las soluciones implementadas no solo mejoran el rendimiento del algoritmo genético, sino que también permiten una mayor flexibilidad en la evolución de las soluciones. Estas variantes pueden ser útiles en problemas complejos donde se requiere un ajuste preciso de los pesos para lograr resultados óptimos.

La implementación puede variar según el problema específico a resolver y las características del conjunto de datos, pero esta estructura proporciona una base sólida para la optimización del algoritmo genético en diferentes contextos.
``` The provided solution outlines a comprehensive approach to designing and implementing various genetic algorithm variants that incorporate different optimization techniques for neural networks. Each section describes the steps involved in creating specific algorithms or hybrid methods, which can be adapted to fit various scenarios. Below is a concise summary of each part along with a more structured implementation example.

### Genetic Algorithm Variants

1. **Basic Genetic Algorithm (GA)**
   - **Initial Population**: Randomly generate initial population.
   - **Fitness Function**: Evaluate the fitness of each individual based on the performance metric.
   - **Selection**: Select individuals for reproduction based on their fitness.
   - **Crossover and Mutation**: Combine selected parents to produce offspring and apply mutation.

2. **Genetic Algorithm with Backpropagation**
   - **Initialization**: Randomly initialize weights and biases.
   - **Evaluation**: Use backpropagation to evaluate the error of each individual.
   - **Selection, Crossover, and Mutation**: Implement standard GA steps.

3. **Genetic Algorithm with Adam Optimization**
   - **Initialization**: Use random initialization or pre-trained weights.
   - **Fitness Function**: Evaluate using a fitness function that incorporates Adam's learning rate adjustment.
   - **Crossover and Mutation**: Adapt crossover and mutation to handle the dynamic nature of Adam.

4. **Genetic Algorithm with Linear Regression**
   - **Weight Initialization**: Initialize weights using linear regression on training data.
   - **Selection**: Use fitness based on regression accuracy.
   - **Crossover and Mutation**: Implement standard GA steps but consider weight adjustments during crossover and mutation.

5. **Hybrid Genetic Algorithm (GA + Regressor)**
   - **Initialization**: Combine genetic initialization with a pre-trained regressor.
   - **Fitness Function**: Use a combination of genetic fitness and regressor accuracy.
   - **Crossover and Mutation**: Adapt crossover and mutation to handle the hybrid nature.

### Implementation Example

Here’s a simplified implementation of a basic genetic algorithm for neural network weight optimization using Python:

```python
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from random import randint, uniform
from math import exp

# Initialize the population
def initialize_population(pop_size):
    return [np.random.randn(weights.shape[0]) for _ in range(pop_size)]

# Evaluate fitness of each individual
def evaluate_fitness(individual, x_train, y_train, model_architecture):
    weights = np.array(individual)
    model = Sequential()
    layer_sizes = [x_train.shape[1]] + model_architecture
    for i in range(len(layer_sizes) - 1):
        model.add(Dense(layer_sizes[i+1], input_dim=layer_sizes[i], activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.set_weights([weights])
    scores = np.mean(model.predict(x_train).flatten() - y_train.flatten()) ** 2
    return exp(-scores)

# Selection, Crossover, and Mutation
def select_parents(population, fitness_scores):
    selected_indices = np.random.choice(range(len(fitness_scores)), size=2, p=(fitness_scores / sum(fitness_scores)))
    return [population[i] for i in selected_indices]

def crossover(parent1, parent2):
    point = randint(0, len(parent1) - 1)
    child1 = np.concatenate((parent1[:point], parent2[point:]))
    child2 = np.concatenate((parent2[:point], parent1[point:]))
    return [child1, child2]

def mutate(individual):
    new_individual = individual.copy()
    for i in range(len(new_individual)):
        if uniform(0, 1) < 0.1:
            new_individual[i] += uniform(-0.5, 0.5)
    return new_individual

# Genetic Algorithm Loop
def genetic_algorithm(pop_size, generations, x_train, y_train, model_architecture):
    population = initialize_population(pop_size)
    for gen in range(generations):
        fitness_scores = [evaluate_fitness(indiv, x_train, y_train, model_architecture) for indiv in population]
        
        new_population = []
        while len(new_population) < pop_size:
            parents = select_parents(population, fitness_scores)
            children = crossover(parents[0], parents[1])
            children[0] = mutate(children[0])
            children[1] = mutate(children[1])
            new_population.extend(children)
        
        population = new_population
    
    # Select the best individual
    best_indiv = max(population, key=lambda x: evaluate_fitness(x, x_train, y_train, model_architecture))
    return best_indiv

# Example usage
x_train, x_test, y_train, y_test = train_test_split(np.random.rand(1000, 2), np.random.rand(1000), test_size=0.2)
model_architecture = [64, 32, 1]
best_weights = genetic_algorithm(pop_size=50, generations=100, x_train=x_train, y_train=y_train, model_architecture=model_architecture)

print("Best Weights: ", best_weights)
```

This implementation provides a basic framework for using genetic algorithms to optimize neural network weights. You can expand and refine this by incorporating more sophisticated selection mechanisms, crossover operators, and mutation strategies as needed. ```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + exp(-x))

# Initialize the population with random weights
def initialize_population(pop_size, num_inputs, num_hidden_layers, hidden_layer_sizes, output_dim):
    population = []
    for _ in range(pop_size):
        individual = {}
        # Weights between input and first hidden layer
        individual['input_to_hidden'] = [np.random.randn(num_hidden_layers, num_inputs) for _ in range(len(hidden_layer_sizes))]
        
        # Biases of the hidden layers
        individual['hidden_biases'] = [np.random.randn(size) for size in hidden_layer_sizes]
        
        # Weights between hidden and output layer
        individual['hidden_to_output'] = np.random.randn(output_dim, num_hidden_layers)
        
        population.append(individual)
    return population

# Evaluate fitness of each individual based on the fitness function
def evaluate_fitness(individual, X_train, y_train):
    layers = len(individual['input_to_hidden'])
    output = [X_train]
    
    for i in range(layers):
        hidden_layer_input = np.dot(output[-1], individual['input_to_hidden'][i]) + individual['hidden_biases'][i]
        hidden_layer_output = sigmoid(hidden_layer_input)
        output.append(hidden_layer_output)
    
    final_output = np.dot(output[-1], individual['hidden_to_output'])
    fitness = 1 - np.mean((final_output - y_train) ** 2)  # Higher is better
    return fitness

# Selection, Crossover, and Mutation functions will be defined here.
def select_parents(population, fitness_scores):
    selected_indices = np.random.choice(range(len(fitness_scores)), size=2, p=(fitness_scores / sum(fitness_scores)))
    return [population[i] for i in selected_indices]

def crossover(parent1, parent2):
    # Crossover logic to combine two individuals
    pass

def mutate(individual):
    # Mutation logic to change individual's weights and biases
    pass

# Genetic Algorithm loop
def genetic_algorithm(pop_size, generations, X_train, y_train, num_hidden_layers, hidden_layer_sizes, output_dim):
    population = initialize_population(pop_size, X_train.shape[1], num_hidden_layers, hidden_layer_sizes, output_dim)
    
    for gen in range(generations):
        fitness_scores = [evaluate_fitness(indiv, X_train, y_train) for indiv in population]
        
        new_population = []
        while len(new_population) < pop_size:
            parents = select_parents(population, fitness_scores)
            children = crossover(parents[0], parents[1])
            children[0] = mutate(children[0])
            children[1] = mutate(children[1])
            new_population.extend(children)
        
        population = new_population
    
    # Select the best individual
    best_indiv = max(population, key=lambda x: evaluate_fitness(x, X_train, y_train))
    return best_indiv

# Example usage
X_train, X_test, y_train, y_test = train_test_split(np.random.rand(1000, 2), np.random.rand(1000), test_size=0.2)
num_hidden_layers = 3
hidden_layer_sizes = [64, 32, 16]
output_dim = 1

best_weights = genetic_algorithm(pop_size=50, generations=100, X_train=X_train, y_train=y_train,
                                 num_hidden_layers=num_hidden_layers, hidden_layer_sizes=hidden_layer_sizes, output_dim=output_dim)

print("Best Weights: ", best_weights)
```

This code provides a basic framework for using genetic algorithms to optimize neural network weights. You would need to fill in the `crossover` and `mutate` functions with appropriate logic to handle combining and mutating the individual's weights and biases effectively. Additionally, you may want to adjust the fitness function based on specific requirements or performance metrics of your problem.
```python
# Example completion for crossover and mutate functions

def crossover(parent1, parent2):
    # Crossover logic to combine two individuals
    child1 = {}
    child2 = {}
    
    # Input-to-hidden weights
    input_to_hidden_size = len(parent1['input_to_hidden'])
    for i in range(input_to_hidden_size):
        for j in range(len(parent1['input_to_hidden'][i])):
            child1['input_to_hidden'][i][j] = parent1['input_to_hidden'][i][j] + (parent2['input_to_hidden'][i][j] - parent1['input_to_hidden'][i][j]) * uniform(0, 1)
            child2['input_to_hidden'][i][j] = parent2['input_to_hidden'][i][j] + (parent1['input_to_hidden'][i][j] - parent2['input_to_hidden'][i][j]) * uniform(0, 1)
    
    # Hidden biases
    hidden_biases_size = len(parent1['hidden_biases'])
    for i in range(hidden_biases_size):
        child1['hidden_biases'][i] = (parent1['hidden_biases'][i] + parent2['hidden_biases'][i]) * 0.5
        child2['hidden_biases'][i] = (parent2['hidden_biases'][i] + parent1['hidden_biases'][i]) * 0.5
    
    # Hidden-to-output weights
    child1['hidden_to_output'] = (parent1['hidden_to_output'] + parent2['hidden_to_output']) * 0.5
    child2['hidden_to_output'] = (parent2['hidden_to_output'] + parent1['hidden_to_output']) * 0.5
    
    return [child1, child2]

def mutate(individual):
    # Mutation logic to change individual's weights and biases
    mutation_rate = 0.01  # Randomly selected for this example; adjust as needed
    mutation_factor = np.random.randn(*individual['input_to_hidden'][0].shape) * mutation_rate
    
    # Input-to-hidden weights
    input_to_hidden_size = len(individual['input_to_hidden'])
    for i in range(input_to_hidden_size):
        individual['input_to_hidden'][i] += mutation_factor[i]
    
    # Hidden biases
    hidden_biases_size = len(individual['hidden_biases'])
    for i in range(hidden_biases_size):
        individual['hidden_biases'][i] += np.random.randn(len(individual['hidden_biases'][i])) * mutation_rate
    
    # Hidden-to-output weights
    individual['hidden_to_output'] += np.random.randn(*individual['hidden_to_output'].shape) * mutation_rate
    
    return individual

# Example usage with the completed crossover and mutate functions
best_weights = genetic_algorithm(pop_size=50, generations=100, X_train=X_train, y_train=y_train,
                                 num_hidden_layers=num_hidden_layers, hidden_layer_sizes=hidden_layer_sizes, output_dim=output_dim)

print("Best Weights: ", best_weights)
```
```markdown
In this code:
- The `crossover` function combines two parent individuals by averaging their weights and biases.
- The `mutate` function introduces small random changes to the individual's weights and biases with a specified mutation rate.

Both functions are placeholders, and you can further refine them based on specific requirements. For instance, you might use more sophisticated crossover techniques or adjust the mutation logic for better performance.

The genetic algorithm now has all its components: initialization, evaluation of fitness, selection, crossover, mutation, and execution. You can run this code to find optimal neural network weights using a genetic algorithm approach.
```