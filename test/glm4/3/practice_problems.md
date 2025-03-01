```markdown
## Práctica de Problemas de Sistemas Bioinspirados y Redes Neuronales

### Problema 1 (Fácil)
**Descripción:** Implementa el algoritmo Evolutivo para resolver un problema de optimización. Supongamos que deseamos encontrar el valor óptimo de la función f(x) = x^2 en el rango [0,10].

**Solución:**
```python
import random

# Función objetivo
def f(x):
    return x ** 2

# Parámetros del algoritmo
num_generaciones = 100
poblacion_inicial = 50
mascara_mutacion = 0.1
tolerancia = 0.001

# Inicialización de la población
poblacion = [random.uniform(0, 10) for _ in range(poblacion_inicial)]

for generacion in range(num_generaciones):
    # Evaluación de la función
    fitness = [f(individuo) for individuo in poblacion]
    
    # Selección
    seleccionados = random.choices(poblacion, weights=fitness, k=poblacion_inicial)
    
    # Cruza y mutación
    nueva_poblacion = []
    for i in range(0, len(seleccionados), 2):
        padre1 = seleccionados[i]
        madre1 = seleccionados[i+1]
        
        if random.random() < 0.5:
            hijo1 = (padre1 + madre1) / 2
        else:
            hijo1 = (madre1 + padre1) / 2
        
        if random.random() < mascara_mutacion:
            hijo1 += random.uniform(-tolerancia, tolerancia)
        
        nueva_poblacion.append(hijo1)
    
    poblacion = nueva_poblacion

print("Valor óptimo:", min(poblacion, key=f))
```

### Problema 2 (Intermedio)
**Descripción:** Implementa el algoritmo Colonias de hormigas para resolver un problema de paths optimizados en un grafo no dirigido.

**Solución:**
```python
import numpy as np

# Grafo
grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 1},
    'D': {'B': 4, 'C': 1}
}

# Inicialización de las colonias
colonia = ['A'] * 10

# Tamaño del caminar
tamanho_caminho = len(colonia)

while True:
    caminho = np.random.choice(list(grafo.keys()), size=tamanho_caminho)
    custo = sum([grafo[antecessor][proximo] for antecessor, proximo in zip(caminho[:-1], caminh[1:])])
    
    if custo < 100: # Suponemos que um caminho ótimo não passa de 100
        break

print("Caminho ótimo:", caminho)
```

### Problema 3 (Difícil)
**Descripción:** Implementa un modelo simple de Perceptron para la regresión lineal. Supongamos que deseamos predecir el valor de y a partir de x, con los datos: [(1, 2), (2, 4), (3, 6)].

**Solución:**
```python
def perceptron(X, y, learning_rate=0.01, iterations=100):
    weights = [0 for _ in X[0]]
    
    for _ in range(iterations):
        for xi, yi in zip(X, y):
            output = sum([weights[x] * xi[x] for x in xi])
            
            if output <= 0:
                weights = [weights[x] + learning_rate * xi[y] for x in range(len(xi))]
    
    return weights

# Datos
X = [[1], [2], [3]]
y = [2, 4, 6]

weights = perceptron(X, y)
print("Peso óptimo:", weights)
```

### Problema 4 (Avanzado)
**Descripción:** Implementa un modelo de red neuronal con backpropagation para predecir la clase de una serie de datos de clasificación binaria.

**Solución:**
```python
import numpy as np

# Función de activación sigmoidea
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoidea
def derivative_sigmoid(x):
    return x * (1 - x)

# Función de error cuadrático medio
def mse(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

# Entrenamiento del modelo
def train_model(X, y, weights, iterations=1000, learning_rate=0.01):
    for _ in range(iterations):
        for xi, yi in zip(X, y):
            output = sigmoid(sum([weights[j] * xi[j] for j in range(len(xi))]))
            
            error = yi - output
            d_error = derivative_sigmoid(output) * error
            
            weights = [weights[j] + learning_rate * error * xi[j] for j in range(len(weights))]
    
    return weights

# Datos
X = np.array([[1, 0], [0, 1], [1, 1], [1, 0]])
y = np.array([1, 0, 1, 0])

weights = train_model(X, y, [0.1, 0.1])
print("Peso óptimo:", weights)
```

### Problema 5 (Experto)
**Descripción:** Implementa un modelo de Aprendizaje por Refuerzo para resolver el problema del laberinto con rewards y penalties.

**Solución:**
```python
import numpy as np

# Laberinto
laberinto = {
    'start': {'up': 'wall', 'right': 'wall', 'down': 'end', 'left': 'wall'},
    'A': {'up': 'start', 'right': 'B', 'down': 'wall', 'left': 'C'},
    'B': {'up': 'A', 'right': 'D', 'down': 'end', 'left': 'E'},
    'C': {'up': 'A', 'right': 'F', 'down': 'end', 'left': 'wall'},
    'D': {'up': 'B', 'right': 'G', 'down': 'wall', 'left': 'end'},
    'E': {'up': 'A', 'right': 'wall', 'down': 'end', 'left': 'F'},
    'F': {'up': 'C', 'right': 'wall', 'down': 'end', 'left': 'G'},
    'G': {'up': 'D', 'right': 'end', 'down': 'F', 'left': 'wall'},
    'end': {'up': 'wall', 'right': 'wall', 'down': 'wall', 'left': 'wall'}
}

# Reinforcement Learning
def reinforcement_learning(q_table, state):
    actions = list(laberinto[state].keys())
    next_action = np.argmax(q_table[state, actions])
    
    if laberinto[state][actions[next_action]] == 'end':
        return 1, laberinto[state][actions[next_action]]
    
    return 0, laberinto[state][actions[next_action]]

# Tabela de ações
q_table = np.zeros((len(laberinto), len(laberinto['start'].keys())))

state = 'start'
reward = 0

while state != 'end':
    reward, next_state = reinforcement_learning(q_table, state)
    
    if reward:
        print("Concluído!")
        break
    
    q_table[state, list(laberinto[state].keys()).index(next_state)] += 1
    state = next_state
```
```