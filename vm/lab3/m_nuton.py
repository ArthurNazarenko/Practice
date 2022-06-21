from sympy import *
import numpy as np
import math
EPS = 0.0001

def f(x):
    return x**3 - 2*x + 1

def derivative():
    x = Symbol('x')
    y = f(x)
    x = y.diff(x)
    print(x)
    return x
#derivative()

def newton(x):
    delta = abs(f(x))
    EPS = 0.0001
    while (EPS < delta):
        x = x - f(x)/derivative(x)
        delta = abs(f(x))
    return x

print(newton(0.1))    #2.0