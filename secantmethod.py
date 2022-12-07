from sympy import symbols, lambdify, diff
import math


def secantMethod():
    print("\n")
    
    x = symbols('x')
    functionString = str(input("Enter the function in the form \'x**3 - 5*x - 9\': "))
    expression = lambdify(x, functionString, "math")

    maxIterations = int(input("Enter maximum number of iterations: "))
    accuracy = float(input("Enter the desired tolerance: "))
    x0 = float(input("Enter the first point x0: "))
    x1 = float(input("Enter the second point x: "))

    count = 0
    fxi = 0.0
    xi = 0.0

    print("\nS. No.\tx_i-1\t\tx_i-2\t\tx_i\t\tfx_i")
    while True:
        fx0 = expression(x0)
        fx1 = expression(x1)

        xi = ((x0 * fx1) - (x1 * fx0)) / (fx1 - fx0)
        fxi = expression(xi)
        
        print("{0}\t{1:.8f}\t{2:.8f}\t{3:.8f}\t{4}".format(count+1, x1, x0, xi, fxi))

        x0 = x1
        x1 = xi
        count += 1

        if (abs(fxi) < accuracy) or (count > maxIterations):
            break
        
    print("\nAfter {0} iterations, the root of the given equation is\n   x = {1}\nf(x) = {2}\n\n".format(count, xi, fxi))
    return True