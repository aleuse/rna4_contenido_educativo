**Problem Set: Bioinspired Optimization and Neural Networks**

1. **Genetic Algorithm Implementation**
   - *Objective*: Implement a genetic algorithm to find the minimum of a given function.
   - *Setup*: Use a binary representation for chromosomes, mutation rate 0.05, crossover probability 0.7, population size 50.
   - *Input Data*: Function to minimize (e.g., f(x) = x² + 2x + 3)
   - *Solution Code*:
     ```python
     import random

     # Define function to maximize/minimize
     def f(x):
         return x**2 + 2*x + 3

     # Genetic Algorithm parameters
     pop_size = 50
     mutation_rate = 0.05
     crossover_prob = 0.7
     generations = 100

     # Initialize population
     population = []
     for i in range(pop_size):
         chromosome = random.randint(0,1)
         population.append(chromosome)

     # Fitness calculation
     fitness = []
     for individual in population:
         fit = f(individual)
         fitness.append(fit)

     # Selection: Tournament selection
     selected = []
     for _ in range(pop_size//2):
         i1, i2 = random.randint(0, pop_size-1), random.randint(0, pop_size-1)
         if fitness[i1] < fitness[i2]:
             selected.append(i1)
         else:
             selected.append(i2)

     # Crossover: Single point crossover
     new_pop = []
     for i in range(0, pop_size, 2):
         child1 = selected[i]
         child2 = selected[i+1]
         if random.random() < crossover_prob:
             mid = random.randint(len(child1)*4 +1, len(child1)*4 +5)
             new_child1 = child1[:mid] + [0]* (len(child1) - mid)
             new_child2 = [0]*mid + child2[len(child2)-mid:]
             new_pop.append(new_child1)
             new_pop.append(new_child2)

     # Mutation
     for i in range(len(new_pop)):
         if random.random() < mutation_rate:
             pos = random.randint(0, len(new_pop[i])-1)
             new_pop[i] = list(new_pop[i])
             new_pop[i][pos], new_pop[i][pos] = new_pop[i][pos], new_pop[i][pos]

     # Evaluate and select
     fitness = [f(individual) for individual in new_pop]
     selected_indices = sorted(range(len(fitness)), key=lambda x: fitness[x], reverse=True)[:pop_size//2]
     population = [new_pop[i] for i in selected_indices]

     # End of loop
     return min(fit for fit in fitness)
     ```
   - *Expected Output*: The minimum value of the function with an error margin < 0.1.

2. **Ant Colony Algorithm for Path Finding**
   - *Objective*: Use the ant colony algorithm to find the shortest path between cities.
   - *Setup*: Cities represented as nodes, edges with weights (distance), initial pheromone value 1, evaporation rate 0.3, heuristic factor 0.2.
   - *Input Data*: Graph with nodes and edges
   - *Solution Code*:
     ```python
     import random

     # Define cities and edges
     cities = {'A': [ (1, 'B'), (4, 'D') ],
               'B': [ (2, 'C'), (5, 'E') ],
               'C': [ (3, 'F'), (6, 'G') ],
               'D': [ (7, 'H') ],
               'E': [ (8, 'I') ],
               'F': [],
               'G': [ (9, 'J') ],
               'H': [],
               'I': [ (10, 'K') ],
               'J': [],
               'K': []}

     # Initialize pheromone values
     pheromones = {city:1 for city in cities.keys()}

     # Parameters
     evaporation_rate = 0.3
     heuristic_factor = 0.2

     # Function to compute distance between cities
     def distance(cityA, cityB):
         for a in cities[cityA]:
             if a[1] == cityB:
                 return a[0]
         return float('inf')

     # Best fit neighborhood
     def best_fit_neighbors(current_city):
         neighbors = []
         max_distance = 0
         best_neighbor = None
         for city in cities[current_city]:
             distance = distance(current_city, city[1])
             if distance < max_distance:
                 max_distance = distance
                 best_neighbor = city
         return best_neighbor

     # Update pheromones
     def update_pheromones(current_city, next_city):
         pheromones[current_city] += 1/evaporation_rate
         pheromones[next_city] += heuristic_factor * distance(current_city, next_city)

     # Solve
     current_city = 'A'
     best_solution = float('inf')
     for _ in range(100):
         if current_city == 'K':
             break

         neighbors = [city for city in cities[current_city] if cities[city][1]]
         if not neighbors:
             break

         next_city = random.choice(neighbors)
         update_pheromones(current_city, next_city)
         current_city = next_city

         best_neighbor = best_fit_neighbors(current_city)
         if distance(current_city, best_neighbor) < best_solution:
             best_solution = distance(current_city, best_neighbor)

     print(f"Shortest path from A to K: {best_solution}")
     ```
   - *Expected Output*: The shortest path length.

3. **Neural Network Training using Backpropagation**
   - *Objective*: Train a neural network to classify handwritten digits.
   - *Setup*: 4 layers (input, hidden, output), activation functions (ReLU for hidden, sigmoid for output), learning rate 0.1, momentum 0.5
   - *Input Data*: Handwritten digits (0-9) in grayscale (20x20 pixels)
   - *Solution Code*:
     ```python
     import random
     from numpy import array

     # Load data
     training_data = array([[random.uniform(0,1)*20 + i for i in range(20)] for j in range(10)])
     test_data = array([[random.uniform(0,1)*20 + i for i in range(20)] for j in range(10)])

     # Define neural network
     weights_input_hidden = random.random() * 800
     weights_hidden_output = random.random() * 40

     def ReLU(x):
         return max(0, x)

     def sigmoid(z):
         return 1/(1+exp(-z))

     def forward_propagate(input_data):
         hidden_layer = ReLU(np.dot(input_data, weights_input_hidden))
         output_layer = sigmoid(np.dot(hidden_layer, weights_hidden_output))
         return output_layer

     # Backpropagation
     learning_rate = 0.1
     momentum = 0.5

     for epoch in range(100):
         selected_training_data = random.randint(0, len(training_data))
         input_data = training_data[selected_training_data]
         desired_output = training_data[selected_training_data][:, -1]

         # Forward pass
         output = forward_propagate(input_data)

         # Compute error
         error = abs(output - desired_output)
         print(f"Error: {error}")

         # Backward pass and update weights
         delta3 = (output - desired_output) * sigmoid'(z3), where z3 is output layer's pre-activation
         ...
         # Update weights using SGD with momentum

     print("Model trained")
     ```
   - *Expected Output*: Accuracy on test set.

**Note**: The provided code is for illustration only. In a real implementation, detailed data preprocessing and error handling would be required.
```