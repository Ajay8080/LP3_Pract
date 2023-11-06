
import numpy as np


def function(x):
    return x**4 - 3 * (x**3) + 2


def derivative(x):
    return 4 * (x**3) - 9 * (x**2)


def gradient_descent(initial_x, learning_rate, precision, max_iterations):
    x = initial_x
    iteration = 0

    while True:
        gradient = derivative(x)
        new_x = x - learning_rate * gradient

        if abs(new_x - x) < precision:
            print("Local minimum occurs at:", new_x)
            break

        x = new_x
        iteration += 1

        if iteration >= max_iterations:
            print("Exceeded the maximum number of iterations. No convergence.")
            break


initial_x = 6 
learning_rate = 0.01  
precision = 0.0001  
max_iterations = 10000  


gradient_descent(initial_x, learning_rate, precision, max_iterations)
