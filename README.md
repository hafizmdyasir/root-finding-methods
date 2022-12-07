# Root Finding Methods
A collection of python scripts that find the roots of given equation via different root finding algorithms. While each algorithm resides in a separate file, they can be conveniently accessed by running ```mainscreen.py```. 

## Supported Methods
1. Bisection Method
2. Regula-Falsi or False Position Method
3. Newton-Raphson Method
4. Secant Method

## How To Use
### Getting Started
The ```mainscreen.py``` file provides a convenient and user-friendly 'interface' for interacting with each of the scripts. Run this file and follow the on-screen prompts.

### Inputting functions
For function input, I have relied on the famous ```sympy``` module. Expressions of the form ```x**2 - 4*x + 9``` will work, as will the functions defined in Python's inbuilt ```math``` module, i.e., you can enter ```cos(x) + sin(x)``` and the program will work just fine.