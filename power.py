import numpy as numpy
A = numpy.array([[1,2],
[2,1]]
,float)
u = numpy.array([[1],[1]], float)
n = 100
eigenvalue = 0
for i in range(n):
    u = A@u
    eigenvalue = numpy.max(u)
    u = u/eigenvalue

print("eigenvector: \n", u)
print("neigenvalue =", eigenvalue)
