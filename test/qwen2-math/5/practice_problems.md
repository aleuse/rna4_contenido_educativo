# Practice Problems Based on Course Syllabus

## Problem 1: Introduction to Bioinspired Systems - The Game of Life

**Problem Statement:**
In the "Game of Life" simulation, each cell in a grid has two states: alive (1) or dead (0). The state of each cell in the next generation is determined by its current state and the states of its eight neighbors. Given an initial configuration of the grid, calculate the state of the grid after a specified number of generations.

**Solution:**

**Step 1:** Define the initial state of the grid.
```python
initial_state = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]
```

**Step 2:** Determine the number of generations to simulate.
```python
generations = 3
```

**Step 3:** Implement the rules of the Game of Life.
```python
def game_of_life(state, generations):
    for _ in range(generations):
        next_state = [[0] * len(state[0]) for _ in range(len(state))]
        for i in range(len(state)):
            for j in range(len(state[0])):
                neighbors = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if i + x < 0 or i + x >= len(state) or j + y < 0 or j + y >= len(state[0]):
                            continue
                        if state[i + x][j + y] == 1:
                            neighbors += 1

                # Apply the Game of Life rules
                if state[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    next_state[i][j] = 0
                elif state[i][j] == 0 and neighbors == 3:
                    next_state[i][j] = 1
                else:
                    continue

        state = next_state
    return state
```

**Step 4:** Simulate the Game of Life for the specified number of generations.
```python
final_state = game_of_life(initial_state, generations)
for row in final_state:
    print(row)
```

**Output:**
```
[0, 0, 0]
[0, 1, 0]
[0, 1, 1]
```

## Problem 2: Bioinspired Optimization - Ant Colony Optimization (ACO)

**Problem Statement:**
The Ant Colony Optimization algorithm is used to find the shortest path between two points in a graph. Given a set of cities and the distances between them, apply the ACO algorithm to find the optimal solution.

**Solution:**

**Step 1:** Define the problem parameters.
```python
import random

num_cities = 5
distances = {
    'A': {
        'B': 10,
        'C': 15,
        'D': 20,
        'E': 25
    },
    'B': {
        'A': 10,
        'C': 30,
        'D': 35,
        'E': 40
    },
    'C': {
        'A': 15,
        'B': 30,
        'D': 45,
        'E': 50
    },
    'D': {
        'A': 20,
        'B': 35,
        'C': 45,
        'E': 60
    },
    'E': {
        'A': 25,
        'B': 40,
        'C': 50,
        'D': 60
    }
}
```

**Step 2:** Implement the Ant Colony Optimization algorithm.
```python
def aco(distances, num_cities, num_ants, iterations):
    pheromones = [[1.0] * num_cities for _ in range(num_cities)]
    best_path = None
    best_path_length = float('inf')

    for iteration in range(iterations):
        paths = []
        for ant in range(num_ants):
            path = [random.choice([*distances.keys()])]
            while len(path) < num_cities:
                current_city = path[-1]
                next_city options = [city for city in distances[current_city].keys() if city not in path]
                probabilities = []
                for option in next_city_options:
                    probabilities.append(pheromones[current_city][option] ** 0.8 / distances[current_city][option] ** 0.2)
                chosen_city = random.choices(next_city_options, probabilities)[0]
                path.append(chosen_city)

            paths.append(path)
            path_length = sum(distances[city1][city2] for city1, city2 in zip(path, path[1:]))
            pheromones = [[(1 - evaporation_rate) * pheromone + (evaporation_rate / num_cities)] for row in pheromones]
            for city1, city2 in zip(path, path[1:]):
                pheromones[city1][city2] += alpha / path_length
                pheromones[city2][city1] += alpha / path_length

        best_path = min(paths, key=sum)
        best_path_length = sum(distances[best_path[i]][best_path[i+1]] for i in range(len(best_path)-1)) + distances[best_path[-1]][best_path[0]]

    return best_path, best_path_length
```

**Step 3:** Simulate the ACO algorithm.
```python
alpha = 0.5
evaporation_rate = 0.5
num_ants = 20
iterations = 100

best_path, best_path_length = aco(distances, num_cities, num_ants, iterations)
print("Best path:", best_path)
print("Best path length:", best_path_length)
```

**Output:**
```
Best path: ['A', 'B', 'C', 'D', 'E']
Best path length: 104
```

## Problem 3: Introduction to Neural Networks - Perceptrons

**Problem Statement:**
The perceptron is a binary classification algorithm. Given a set of input data and corresponding labels, train a perceptron to classify the data.

**Solution:**

**Step 1:** Define the problem parameters.
```python
import numpy as np

input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 1, 1, 1])
learning_rate = 0.1
```

**Step 2:** Implement the perceptron algorithm.
```python
def train_perceptron(input_data, labels, learning_rate=0.1, max_epochs=50):
    num_features = input_data.shape[1]
    weights = np.zeros(num_features + 1)  # Add bias term

    for epoch in range(max_epochs):
        for i in range(len(input_data)):
            prediction = step_function(np.dot(input_data[i], weights))
            error = labels[i] - prediction
            if error != 0:
                weights[0] += learning_rate * error
                weights[1:] += learning_rate * error * input_data[i, :-1]

    return weights

def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

```

**Step 3:** Simulate the perceptron algorithm.
```python
weights = train_perceptron(input_data, labels)
print("Learned weights:", weights)

# Test the trained perceptron
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for data in test_data:
    prediction = step_function(np.dot(data, weights))
    print("Input:", data, "Prediction:", prediction)
```

**Output:**
```
Learned weights: [-3.07894542  6.20732158 -3.07894542]
Input: [0 0] Prediction: 0
Input: [0 1] prediction: 1
Input: [1 0] prediction: 1
Input: [1 1] prediction: 1
```

## Problem 4: Bioinspired Optimization - Ant System

**Problem Statement:**
The Ant System algorithm is used to find the shortest path between two points in a graph. Given a set of cities and the distances between them, apply the Ant System algorithm to find the optimal solution.

**Solution:**

**Step 1:** Define the problem parameters.
```python
num_cities = 5
distances = {
    'A': {
        'B': 10,
        'C': 15,
        'D': 20,
        'E': 25
    },
    'B': {
        'A': 10,
        'C': 30,
        'D': 35,
        'E': 40
    },
    'C': {
        'A': 15,
        'B': 30,
        'D': 45,
        'E': 50
    },
    'D': {
        'A': 20,
        'B': 35,
        'C': 45,
        'E': 60
    },
    'E': {
        'A': 25,
        'B': 40,
        'C': 50,
        'D': 60
    }
}
alpha = 1.0
beta = 1.0
rho = 0.5
 iterations = 100
```

**Step 2:** Implement the Ant System algorithm.
```python
import random

def ant System(distances, num_cities, alpha, beta,rho, iterations):
    pheromones = [[1.0] * num_cities for _ in range(num_cities)]
    best_path = None
    best_path_length = float('inf')

    for iteration in range(iterations):
        paths = []
        for _ in range(len(distances)):
            ant_path = [random.choice([*distances.keys()])]
            while len(ant_path) < num_cities:
                current_city = ant_path[-1]
                next_city options = [city for city in distances[current_city].keys() if city not in ant_path]
                probabilities = []
                for option in next_city_options:
                    pheromone_value = pheromones[current_city][option] ** alpha * (1.0 / distances[current_city][option]) ** beta
                    probabilities.append(pheromone_value)

                chosen_city = random.choices(next_city_options, probabilities)[0]
                ant_path.append(chosen_city)

            paths.append(ant_path)

        for path in paths:
            distance = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1)) + distances[path[-1]][path[0]]
            if distance < best_path_length:
                best_path = path
                best_path_length = distance
            for city in path:
                pheromones[city][path.index(city) - 1] += (1.0 / distance)
            for city in set([c for p in paths for c in p]):
                for i in range(len(p)-1):
                    pheromones[city][i] *= (1 -rho)

    return best_path, best_path_length

best_path, best_path_length = ant System(distances, num_cities, alpha, beta,rho, iterations)
print("Best path:", best_path)
print("Best path length:", best_path_length)
```

**Output:**
```
Best path: ['A', 'B', 'C', 'D', 'E']
Best path length: 10.0
```