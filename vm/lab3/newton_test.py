from sympy import *
EPS = 0.0001
import math

def f(x):
    return x ** 2 - 3
    #return 3 * x ** 4 - 8 * x ** 3 - 18 * x ** 2 + 2


def df(x):
    x = Symbol('x')
    y = f(x)
    dy = y.diff(x)
    print(dy)
    return dy

def newton1(x):
    y = f(x)
    delta = 1e-10
    while abs(y) > EPS:
        dy = (f(x + delta) - y)/delta
        x = x - y/dy
        y = f(x)
    return x

def newton(x):
    delta = math.fabs(f(x))
    while (delta > EPS):
        x = x - f(x) / df(x)
        delta = abs(f(x))
    return x
#print(newton(1))
print(newton1(2)) #2.0

