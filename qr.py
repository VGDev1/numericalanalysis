import numpy as np

def qr_factorization(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            q = Q[:, i].T
            R[i, j] = np.dot(q, v)
            v -= np.dot(R[i, j], q)
        norm = np.linalg.norm(v)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R

def back_substitution(U, y):
    #source https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html
    #Number of rows
    n = U.shape[0]
    #Allocating space for the solution vector
    x = np.zeros_like(y, dtype=np.double);
    #Here we perform the back-substitution.  
    #Initializing with the last row.
    x[-1] = y[-1] / U[-1, -1]
    #Looping over rows in reverse (from the bottom up), 
    #starting with the second to last row, because the 
    #last row solve was completed in the last step.
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    return x

A = np.array([[1, 0.0,1], [1, 0,1], [1, 1,0], [1,1,0], [1, 1,2]])
B = np.array([3., 2., 3., 4., 6.])

#decompose
#Q, R = qr_factorization(A)
Q, R = np.linalg.qr(A)
#Q.TB
y = np.dot(Q.T, B)
#solve for x, code for back_substitution is from here https://gist.github.com/RRisto/2cddc23d829877248915d66ecbe09a39
print(back_substitution(R, y))

print(np.linalg.solve(R, y))