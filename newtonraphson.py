from sympy import symbols, lambdify, diff
import math


def newtonRaphson():
    print("\n")
    
    x = symbols('x')
    functionString = str(input("Enter the function in the form \'x**3 - 5*x - 9\': "))
    expression = lambdify(x, functionString, "math")
    derivative = lambdify(x, diff(functionString), "math")

    maxIterations = int(input("Enter maximum number of iterations: "))
    accuracy = float(input("Enter the desired tolerance: "))
    x0 = float(input("Enter the initial guess: "))
    
    count = 0
    fx1 = 0.0
    x1 = 0.0

    print("\nS. No.\tx0\t\tx1\t\tf(x1)")
    while True:
        x1 = x0 - (expression(x0) / derivative(x0))
        fx1 = expression(x1)
        print("{0}\t{1:.8f}\t{2:.8f}\t{3}".format(count+1, x0, x1, fx1))

        x0 = x1
        count += 1

        if (abs(fx1) < accuracy) or (count > maxIterations):
            break
        
    print("\nAfter {0} iterations, the root of the given equation is\n   x = {1}\nf(x) = {2}\n\n".format(count, x1, fx1))
    return True