import math
from sympy import *


xs = [1, 2, 3, 4, 5, 6]

f = lambda x: math.exp(-x**2)

#ys = [f(i) for i in xs]
ys = [10,10,10,10,10,15]

iV = 0

x = symbols('x')

#lagrange interpolation formula
def lagrange(x,xs,ys):
    n = len(xs)
    result = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x - xs[j])/(xs[i] - xs[j])
        result += ys[i]*L
    return expand(result)



print(lagrange(x, xs,ys))

p  = lambda x: x**5/24 - 5*x**4/8 + 85*x**3/24 - 75*x**2/8 + 137*x/12 + 5
print(p(7))