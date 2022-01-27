import math


def f(x):
    return math.e**(math.sin(3)*x) + x**6 - 2*x**4 - x**3 - 1

def Df (x):
    return 3 * math.e**(math.sin(x)**3) * math.cos(x) * math.sin(x)**2 + 6*x**5 - 4*x**3 - 3*x**2 


def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

print(newton(f,Df,0,1e-8,1000))

# exercise 7
"""
❯ python3 newton.py
Found solution after 28 iterations.
1.6074695772652305
❯ python3 newton.py
Found solution after 43 iterations.
-1.0872046018267927
❯ python3 newton.py
Found solution after 0 iterations.
0
"""