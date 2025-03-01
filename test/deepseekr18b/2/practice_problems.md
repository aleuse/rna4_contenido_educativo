#### Bioinspired Systems: 

1. **Problem:** *Understanding Conway's Game of Life Rules*  
   *Objective:* Apply the rules of Conway's Game of Life to determine the next generation of a simple grid.  
   *Instructions:* Given a 5x5 grid where each cell is either alive (1) or dead (0), apply the following rules:  
     - Any live cell with two or three live neighbors survives.  
     - Any dead cell with exactly three live neighbors becomes alive.  
     - All other cells die or stay dead.  

   *Expected Output:* A 5x5 grid showing the next state of the grid.  

   *Solution Steps:*  
   1. Identify all live cells (1s) in the current grid.  
   2. For each cell, count its live neighbors.  
   3. Apply the rules to determine if each cell is alive or dead in the next generation.  
   4. Compile these results into a new 5x5 grid.  

   Example Input:  
   ```
   0 1 0
   0 1 0
   1 1 0
   ```  
   Example Output:  
   ```
   1 1 0
   0 0 0
   0 0 0
   ```

2. **Intermediate Problem:** *Evolutionary Algorithm for Function Optimization*  
   *Objective:* Implement an evolutionary algorithm to find the maximum of a given function within a specified range.  

   *Instructions:* Define a fitness function \( f(x) = x^2 \). Use an evolutionary algorithm (e.g., genetic algorithm) with population size 10, mutation rate 0.05, and crossover probability 0.7. Run the algorithm for 50 generations and find the maximum value achieved.  

   *Expected Output:* The maximum value of \( f(x) \) found by the algorithm within the specified range.  

   *Solution Steps:*  
   1. Initialize a population of random numbers within the search space.  
   2. Evaluate each number using the fitness function.  
   3. Apply mutation and crossover operations to generate new offspring.  
   4. Keep track of the best solution found so far.  
   5. Repeat for 50 generations and output the maximum value achieved.  

3. **Advanced Problem:** *Ant Colony Optimization for Path Finding*  
   *Objective:* Use an ant colony optimization algorithm to find the shortest path in a graph with weighted edges.  

   *Instructions:* Define a graph with nodes A, B, C, D connected by edges AB (weight 2), BC (1), CD (3), and DA (4). The goal is to find the shortest path from A to D using ants that deposit pheromone on paths and preferentially follow it.  

   *Expected Output:* The shortest path from A to D, along with the total weight of this path.  

   *Solution Steps:*  
   1. Initialize each ant to start at node A.  
   2. Allow ants to move randomly through the graph, depositing pheromone on their paths.  
   3. After a certain number of iterations (e.g., 100), guide the ants along the paths with the most pheromone.  
   4. Update the best path found so far and repeat until convergence.  

#### Neural Networks:

1. **Problem:** *Perceptron Classification for Binary Data*  
   *Objective:* Train a perceptron to classify two classes (0 and 1) based on a given dataset.  

   *Instructions:* Given the following data points:  
   - (1,1), (2,3), (3,5), (-1,-2) for class 1  
   - (4,4), (6,2), (7,1), (8,0) for class 0  

   Train a perceptron with learning rate 0.1 and show the final weights that maximize classification accuracy.  

   *Expected Output:* The perceptron's weights after training and the classification accuracy.  

   *Solution Steps:*  
   1. Initialize weights randomly.  
   2. For each data point, compute the activation: \( a = \sum_{i=1}^{n} w_i x_i + b \).  
   3. Compute the error: \( e = y - a \).  
   4. Update weights using \( w_i := w_i + \eta x_i e \).  
   5. Repeat for 100 iterations or until convergence.  

2. **Intermediate Problem:** *Backpropagation Implementation for Digit Recognition*  
   *Objective:* Implement backpropagation to classify digits (0-9) based on a training dataset and test the model on unseen data.  

   *Instructions:* Use the MNIST dataset with 60 samples of each digit for training and 20 samples for testing. Build a neural network with one hidden layer of 6 neurons, using sigmoid activation functions. Implement backpropagation for weight updates. Achieve at least 90% accuracy on the test set.  

   *Expected Output:* The neural network's weights after training and the classification accuracy on the test set.  

   *Solution Steps:*  
   1. Preprocess the data: normalize to -1 to 1.  
   2. Initialize weights randomly within a small range.  
   3. Compute inputs, forward propagate through the network.  
   4. Compute error using the loss function (cross-entropy).  
   5. Backpropagate the error and update weights.  
   6. Repeat for 50 iterations or until accuracy stabilizes.  

3. **Advanced Problem:** *Using Transformers for Text Classification*  
   *Objective:* Implement a transformer-based model to classify text into categories (e.g., sentiment analysis).  

   *Instructions:* Use the IMDB dataset with reviews labeled as positive, negative, or neutral. Pretrain a transformer model (BERT) on a large corpus of text and fine-tune it on the IMDB dataset. Achieve at least 92% accuracy on the test set.  

   *Expected Output:* The transformer's outputs after fine-tuning and the classification accuracy.  

   *Solution Steps:*  
   1. Preprocess the data: remove special tokens, lowercase, etc.  
   2. Use BERT to encode text into token embeddings.  
   3. Fine-tune the model on IMDB dataset with learning rate 0.00005 and batch size 16.  
   4. Evaluate on a held-out test set and report accuracy.  

#### System Conclusion:
By solving these problems, you'll gain hands-on experience in implementing various machine learning algorithms, from traditional methods like perceptrons and ant colony optimization to modern approaches like neural networks and transformers.