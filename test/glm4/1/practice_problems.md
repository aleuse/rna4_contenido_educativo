### Practice Problems on Bio-Inspired Systems and Neural Networks

#### Problem 1: Optimization with Ant Colony Algorithm - Easy Level
**Problem Statement:** Solve the TSP (Travelling Salesman Problem) using the Ant Colony Algorithm. Given n cities, find the shortest possible route that visits each city once and returns to the starting city.

**Solution Steps:**
1. Initialize the pheromone levels on all paths between cities.
2. For a number of iterations:
   - Generate paths by selecting cities based on the pheromone levels and heuristic information.
   - Update the pheromone levels based on the quality of each path found.
3. The shortest path at the end of the iterations is the solution.

```python
# Example pseudo-code for Ant Colony Algorithm
def ant_colony_tsp(num_cities):
    # Initialize pheromones and heuristic information
    # ...
    
    # For number of iterations:
    for _ in range(iterations):
        paths = []
        # Generate paths
        # ...
        
        # Update pheromone levels
        # ...

    return shortest_path_found

# Example call
shortest_path = ant_colony_tsp(5)
```

#### Problem 2: Perceptron Learning Rule - Medium Level
**Problem Statement:** Implement the perceptron learning rule to classify a set of data points into two classes.

**Solution Steps:**
1. Initialize weights and biases.
2. For each training example:
   - Compute the output using the linear model (weighted sum of inputs).
   - If the prediction is incorrect, update the weights and bias accordingly.
3. Continue this process until the weights no longer change significantly or a predefined number of iterations has been reached.

```python
# Example pseudo-code for Perceptron Learning Rule
def perceptron_learning(data_points, labels):
    # Initialize weights and biases
    weights = [0] * num_features
    bias = 0
    
    # Iterate over training data points
    for x, y in zip(data_points, labels):
        output = dot_product(weights, x) + bias
        if (output * y) <= 0:
            weights += learning_rate * y * x
            bias += learning_rate * y

# Example call
perceptron_learning(training_data, training_labels)
```

#### Problem 3: Neural Network Regression - Hard Level
**Problem Statement:** Use a neural network to predict housing prices based on input features such as number of bedrooms and bathrooms.

**Solution Steps:**
1. Preprocess the data, normalizing numerical inputs.
2. Define a neural network with input layer, one or more hidden layers, and an output layer.
3. Train the neural network using backpropagation to minimize the error between predicted and actual housing prices.
4. Evaluate the performance of the trained model.

```python
# Example pseudo-code for Neural Network Regression
import numpy as np

def neural_network_regression(X_train, y_train):
    # Define the neural network architecture
    # ...
    
    # Training using backpropagation
    for epoch in range(num_epochs):
        # Forward pass
        # ...
        
        # Backward pass
        # ...

    return model

# Example call
model = neural_network_regression(X_train, y_train)
```

#### Problem 4: Convolutional Neural Networks - Medium Level
**Problem Statement:** Use a convolutional neural network to classify images from the MNIST dataset.

**Solution Steps:**
1. Preprocess the images, converting them into a suitable format for input into a CNN.
2. Define a CNN architecture with convolutional layers, pooling layers, and fully connected layers.
3. Train the CNN using backpropagation with the appropriate loss function (e.g., cross-entropy) and optimizer.
4. Evaluate the model's accuracy on a test dataset.

```python
# Example pseudo-code for Convolutional Neural Networks
import tensorflow as tf

def create_cnn_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        # Additional layers...
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Example call
model = create_cnn_model()
```

#### Problem 5: Recurrent Neural Networks - Hard Level
**Problem Statement:** Implement a simple RNN to predict the next number in a sequence of integers.

**Solution Steps:**
1. Preprocess the input sequences into a suitable format for an RNN.
2. Define a recurrent neural network with LSTM or GRU layers.
3. Train the model using backpropagation through time to predict the next number in the sequence.
4. Evaluate the model's performance.

```python
# Example pseudo-code for Recurrent Neural Networks
import tensorflow as tf

def create_rnn_model():
    model = tf.keras.Sequential([
        tf.keras.layers.SimpleRNN(50, input_shape=(timesteps, features)),
        tf.keras.layers.Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Example call
model = create_rnn_model()
```

### Note: The provided code snippets are in pseudo-code and should be implemented using appropriate libraries like TensorFlow or PyTorch for actual execution.