import math
import random

#Define function f(x, y)
def f(x, y):
    return x**2 + y**2 + x * math.sin(10 * y) + math.cos(4 * x) 

#The gradient is hardcoded 
def gradient(func, x, y):
    grad_x = 2 * x - 10 * y * math.sin(4 * x)
    grad_y = 2 * y + x * 10 * math.cos(10 * y)
    return grad_x, grad_y

#Computes approximate gradient of f(x, y) using qoutient rule
def approximateGradient(func, x, y, h=1e-6):
    grad_x = (func(x + h, y) - func(x - h, y)) / (2 * h)
    grad_y = (func(x, y + h) - func(x, y - h)) / (2 * h)
    return grad_x, grad_y

# Compute naive gradient descent using approximate gradient
def approxNaiveGradientDescent(func, initialGuess, epsilon, maxIterations):
    xn, yn = initialGuess

    for i in range(maxIterations):
        # Calculates the approximate gradient of the function.
        grad_x, grad_y = approximateGradient(func, xn, yn)

        # The following lines set delta x, delta y respectfully to the change in coordinate 
        # by multiplying the gradient with the step size epsilon with -1. We multiply
        # by -1 becuase it indicates that we are descending towards the minimum
        delta_xn = -epsilon * grad_x
        delta_yn = -epsilon * grad_y

        # The following lines updates the coordinates by adding the change in position calculated in
        # the previous step. 
        xn += delta_xn
        yn += delta_yn

        # Check distance from current point and previous point, if less than episolon (step size)
        # the calculation has reached desired accuracy
        if math.sqrt(delta_xn**2 + delta_yn**2) < epsilon:
            break

    return xn, yn


# This function is almost identical to the above, however, it uses exact gradient
def naiveGradientDescent(func, initialGuess, epsilon, maxIterations):
    xn, yn = initialGuess

    for i in range(maxIterations):
        # Initializes gradient of the function.
        grad_x, grad_y = gradient(func, xn, yn)

        # The following lines set delta x, delta y respectfully to the change in coordinate 
        # by multiplying the gradient with the step size epsilon with -1. We multiply
        # by -1 becuase it indicates that we are descending towards the minimum
        delta_xn = -epsilon * grad_x
        delta_yn = -epsilon * grad_y

        # The following lines updates the coordinates by adding the change in position calculated in
        # the previous step. 
        xn += delta_xn
        yn += delta_yn

        # Check distance from current point and previous point, if less than episolon (step size)
        # the calculation has reached desired accuracy
        if math.sqrt(delta_xn**2 + delta_yn**2) < epsilon:
            break
    
    return xn, yn


def simulatedAnnealing(func, initialGuess, maxIterations, t0, alpha):
    # Initial guess parameters.
    xn, yn = initialGuess

    # The initial tempurature. 
    t = t0

    
    for i in range(maxIterations):
        # Each iteration the current coord (xn, yn) is perturbed by adding random values 
        # which are scaled by temp. 
        xn_new = xn + random.uniform(-1, 1) * t
        yn_new = yn + random.uniform(-1, 1) * t

        # func() calculates the cost of the current coords and the new coords and adds it to 
        # delta 
        delta = func(xn_new, yn_new) - func(xn, yn)

        # if the new soluation has a lower cost than the current solution then it becomes the 
        # the new solution 
        # math.exp(-delta / t) - calculates the exponenetion term in the metropolis criterion
        if delta < 0 or random.random() < math.exp(-delta / t):
            xn = xn_new
            yn = yn_new

        # after each iteration t is updated by the cooling rate (alpha)
        t *= alpha

    return xn, yn

# Main program
initialGuess = (-1, 0)
episilon = 0.001
maxIterations = 1000

minX, minY = naiveGradientDescent(f, initialGuess, episilon, maxIterations)
print(f"Minimum point from exact gradient: ({minX}, {minY})")

initialGuess = (-1, 0)
epsilon = 0.001
maxIterations = 1000

minX, minY = approxNaiveGradientDescent(f, initialGuess, epsilon, maxIterations)
print(f"Minimum point from qoutient rule gradient: ({minX}, {minY})")


initialGuess = (2, 3)
maxIterations = 1000000
t0 = 2
alpha = 0.99

minX, minY = simulatedAnnealing(f, initialGuess, maxIterations, t0, alpha)
print(f"Minimum point from simulated annealing: ({minX}, {minY})")
