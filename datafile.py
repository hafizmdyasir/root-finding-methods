###########################################
'''
File Name: datafile.py
Author: Mohammad Yasir

This module creates a list of Method instances which are accessed by the mainscreen module for easy access and management.
'''
###########################################


import newtonraphson
import falseposition
import bisection
import secantmethod

class Method:
    '''
    Describes a root-finding method (hence the name). The call property stores reference to the function which must be called to perform calculations of the given method. These functions return True or False depending on whether the calculations were succesful or not.
    '''
    def __init__(self, name, call):
        self.name = name
        self.call = call

methods = (
    Method("Regula Falsi (False Position) Method", falseposition.regulaFalsi), 
    Method("Bisection Method", bisection.bisection),
    Method("Newton Raphson Method", newtonraphson.newtonRaphson),
    Method("Secant Method", secantmethod.secantMethod))