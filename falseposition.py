from sympy import symbols, lambdify
import math


def regulaFalsi():
    print("\n")
    
    x = symbols('x')
    functionString = str(input("Enter the function in the form \'x**3 - 5*x - 9\': "))
    expression = lambdify(x, functionString, "math")

    maxIterations = int(input("Enter maximum number of iterations: "))
    accuracy = float(input("Enter the desired tolerance: "))
    x1 = float(input("Enter the first guess: "))
    x2 = float(input("Enter the second guess: "))
    
    if expression(x1) * expression(x2) > 0:
        print("The expression has the same sign on both the given points. Please choose another pair of starting points.\nPress enter to cotinue")
        delay = input()
        return False

    count = 0
    fx3 = 0.0
    x3 = 0.0

    print("\nS. No.\tx1\t\tx2\t\tx3\t\tf(x3)")
    while True:
        x3 = x1 - ((x2 - x1) * expression(x1)) / (expression(x2) - expression(x1))
        fx3 = expression(x3)
        print("{0}\t{1:.8f}\t{2:.8f}\t{3:.8f}\t{4:.8f}".format(count+1, x1, x2, x3, fx3))

        if expression(x1) * fx3 < 0:
            x2 = x3
        else:
            x1 = x3
        count += 1

        if (abs(fx3) < accuracy) or (count >= maxIterations):
            break
        
    print("\nAfter {0} iterations, the root of the given equation is\n   x = {1}\nf(x) = {2}\n\n".format(count, x3, fx3))
    return True