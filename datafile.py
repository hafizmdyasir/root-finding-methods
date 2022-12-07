import newtonraphson
import falseposition
import bisection
import secantmethod

class Method:
    def __init__(self, name, call):
        self.name = name
        self.call = call

methods = (
    Method("Regula Falsi (False Position) Method", falseposition.regulaFalsi), 
    Method("Bisection Method", bisection.bisection),
    Method("Newton Raphson Method", newtonraphson.newtonRaphson),
    Method("Secant Method", secantmethod.secantMethod))