Sources: https://machinelearningmastery.com/simulated-annealing-from-scratch-in-python/

# Gradient Descent and Simulated Annealing

This Python script demonstrates the implementation of two optimization algorithms: 
gradient descent and simulated annealing. The goal of both algorithms is to find 
the minimum point of a given function. 

If you have a bad guess, the naive gradient descent algorithm may converge to a local minimum. This is because the algorithm always moves in the direction of the negative gradient, and if the initial guess is close to a local minimum, then the algorithm will move towards that local minimum.



### 1. Gradient Descent

Gradient descent is an iterative optimization algorithm that uses the gradient of a function to find the minimum point. The script includes two versions of gradient descent:

    # a. Naive Gradient Descent

        The `naiveGradientDescent` function implements the gradient descent 
        algorithm using the exact gradient of the function. It iteratively updates
        the current coordinates `(xn, yn)` based on the negative gradient 
        direction multiplied by a step size `epsilon`. The process continues until 
        the change in position becomes smaller than a predefined threshold `epsilon`.

    # b. Approximate Gradient Descent

        The `approxNaiveGradientDescent` function implements a similar gradient 
        descent algorithm, but it approximates the gradient using the quotient rule. 
        This approximation can be useful when the exact gradient is challenging to 
        compute. The rest of the algorithm follows the same steps as the naive gradient 
        descent.

### 2. Simulated Annealing

        Simulated annealing is a probabilistic optimization algorithm inspired by the 
        annealing process in metallurgy. It mimics the slow cooling of a material to reach a 
        low-energy state. It perturbs the current coordinates `(xn, yn)` by adding random values 
        scaled by a temperature parameter `t`. The algorithm then evaluates the cost of the new 
        coordinates and decides whether to accept the new solution based on a Metropolis criterion. 
        The temperature is gradually decreased by multiplying it by a cooling rate `alpha` at each iteration.

        It's important to note that simulated annealing is a stochastic algorithm, meaning it introduces randomness 
        in its exploration of the search space. As a result, the algorithm may produce different results on different 
        runs, even for the same problem and parameters. Therefore, it's possible for the simulated annealing algorithm to 
        occasionally produce a minimum point with the wrong sign. This is due to the probabilistic nature of the algorithm and 
        the acceptance of solutions that increase the cost (based on the Metropolis criterion) to avoid getting trapped in local 
        optima. I reccommend running the program 3-5 times in order to get a contextual understanding of the nature of the algorithm 


## Usage

The script provides an example usage of the implemented algorithms. 
It demonstrates finding the minimum point of a function `f(x, y)`, defined as `x**2 + y**2 + x * math.sin(10 * y) + math.cos(4 * x)`.

1. Gradient Descent:

   - `initialGuess`: The initial guess for the minimum point.
   - `epsilon`: The threshold for the change in position to determine convergence.
   - `maxIterations`: The maximum number of iterations allowed.

   The script runs the naive gradient descent algorithm and the approximate gradient descent algorithm with the given parameters and prints the minimum point found by each algorithm.

2. Simulated Annealing:

   - `initialGuess`: The initial guess for the minimum point.
   - `maxIterations`: The maximum number of iterations allowed.
   - `t0`: The initial temperature.
   - `alpha`: The cooling rate.

   The script runs the simulated annealing algorithm with the given parameters and prints the minimum point found by the algorithm.

Feel free to modify the parameters and the objective function to experiment with different optimization scenarios.

## Additional Considerations

- The objective function `f(x, y)` and its gradient are hardcoded in the script. If you want to optimize a different 
- function, you need to modify the `f(x, y)` function and its corresponding gradient function.

- The convergence of the algorithms depends on the chosen parameters and the nature of the objective function. 
- Adjusting the parameters, such as step size `epsilon`, cooling rate `alpha`, and initial temperature `t0`, 
- may be required to achieve satisfactory results.

- The script uses the `math` and `random` 
