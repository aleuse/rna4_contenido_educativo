# Práctica de Problemas - Sistemas Bioinspirados y Redes Neuronales
=============================================

### Sección 1: Optimización con Métodos Bioinspirados

#### 1.1 Algoritmos Evolutivos

 Diseña un algoritmo evolutivo para resolver el problema del "juego de la vida" utilizando la función de fitness `fitness = num_vivos - num_muertos`. El algoritmo debe utilizar una población inicial de tamaño 100 y realizar 500 generaciones.

#### Solución
```markdown
# Algoritmo Evolutivo para Juego de la Vida

def fitness(individual):
    return len(individual) - len(set.individual)

def algoritmo_evolutivo(poblacion, num_generaciones):
    for i in range(num_generaciones):
        # Selección aleatoria
        seleccion = random.sample(poblacion, 20)
        
        # Crós y mutación
        new_individuals = []
        for individuo in seleccion:
            nuevo_individuo = individuo[:]
            for j in range(len(individuo)):
                if random.random() < 0.1:
                    nuevo_individuo[j] = 1 - individuo[j]
            new_individuals.append(nuevo_individuo)
        
        # Evaluación de fitness
        poblacion = [individual for individual in poblacion + new_individuals if fitness(individual) > 0]
    
    return poblacion

# Inicialización de la población
poblacion = [[1]*100] * 100

# Ejecución del algoritmo
num_generaciones = 500
poblacion_final = algoritmo_evolutivo(poblacion, num_generaciones)
```

#### Solución Adicional: Uso de Pandas para Optimización

```markdown
# Algoritmo Evolutivo con Pandas

import pandas as pd

def fitness(individual):
    return len(individual) - len(set.individual)

def algoritmo_evolutivo(poblacion, num_generaciones):
    for i in range(num_generaciones):
        # Selección aleatoria
        seleccion = random.sample(poblacion, 20)
        
        # Crós y mutación
        new_individuals = []
        for individuo in seleccion:
            nuevo_individuo = individuo[:]
            for j in range(len(individuo)):
                if random.random() < 0.1:
                    nuevo_individuo[j] = 1 - individuo[j]
            new_individuals.append(nuevo_individuo)
        
        # Creación de DataFrame
        df = pd.DataFrame(new_individuals, columns=range(100))
        
        # Evaluación de fitness
        poblacion = [individual for individual in poblacion + new_individuals if fitness(individual) > 0]
    
    return poblacion

# Inicialización de la población
poblacion = [[1]*100] * 100

# Ejecución del algoritmo
num_generaciones = 500
poblacion_final = algoritmo_evolutivo(poblacion, num_generaciones)
```

### Sección 2: Introducción a las Redes Neuronales - Perceptrones y Backpropagation

#### 2.1 Perceptrones Simples

Diseña un perceptrón simple para clasificar los datos `[(1, 0), (0, 1)]` en dos clases (`positivo` y `negativo`). El peso inicial es de 0.5.

#### Solución
```markdown
# Perceptrón Simple

def activacion_sigmoid(x):
    return 1 / (1 + exp(-x))

def perceptrone(x, pesos):
    # Calcular salida
    salida = sum([peso * elemento for peso, elemento in zip(pesos, x)])
    
    # Aplicar función de activación sigmoid
    return activacion_sigmoid(salida)

# Inicialización de pesos
pesos = [0.5]

# Dados de entrada
x = [(1, 0), (0, 1)]

# Clasificación
for elemento in x:
    salida = perceptrone(elemento, pesos)
    
    # Decidir la clase
    if salida > 0.5:
        print("Clase: positivo")
    else:
        print("Clase: negativo")
```

#### Solución Adicional: Uso de Matrices para Optimización

```markdown
# Perceptrón Simple con Matrices

import numpy as np

def activacion_sigmoid(x):
    return 1 / (1 + np.exp(-x))

def perceptrone(x, pesos):
    # Calcular salida
    salida = np.sum([peso * elemento for peso, elemento in zip(pesos, x)])
    
    # Aplicar función de activación sigmoid
    return activacion_sigmoid(salida)

# Inicialización de pesos
pesos = [0.5]

# Dados de entrada
x = [(1, 0), (0, 1)]

# Clasificación
for elemento in x:
    salida = perceptrone(elemento, pesos)
    
    # Decidir la clase
    if salida > 0.5:
        print("Clase: positivo")
    else:
        print("Clase: negativo")
```

### Sección 3: Aplicación de Redes Neuronales a Datos Tabulares - Regresión

#### 3.1 Regresión Lineal

Diseña una red neuronal para predecir la variable `salario` en función de las variables `edad` y `experiencia`. El algoritmo debe utilizar un perceptrón de retropropagación simple con una capa oculta con 2 neuronas.

#### Solución
```markdown
# Red Neuronal para Regresión Lineal

import numpy as np

def activacion_sigmoid(x):
    return 1 / (1 + np.exp(-x))

def regresion_lineal(edad, experiencia):
    # Salida del perceptrón
    salida = 0.5 * edad + 0.2 * experiencia
    
    # Aplicar función de activación sigmoid
    return activacion_sigmoid(salida)

# Dados de entrada
edad = [25, 30]
experiencia = [3, 5]

# Predicción
for i in range(len(edad)):
    salario = regresion_lineal(edad[i], experiencia[i])
    
    print(f"Salario para edad {edad[i]} y experiencia {experiencia[i]}: {salario}")
```

#### Solución Adicional: Uso de Matrices para Optimización

```markdown
# Red Neuronal para Regresión Lineal con Matrices

import numpy as np

def activacion_sigmoid(x):
    return 1 / (1 + np.exp(-x))

def regresion_lineal(edad, experiencia):
    # Salida del perceptrón
    salida = 0.5 * edad + 0.2 * experiencia
    
    # Aplicar función de activación sigmoid
    return activacion_sigmoid(salida)

# Dados de entrada
edad = np.array([25, 30])
experiencia = np.array([3, 5])

# Predicción
salarios = []
for i in range(len(edad)):
    salario = regresion_lineal(edad[i], experiencia[i])
    
    salarios.append(salario)

print(salarios)
```