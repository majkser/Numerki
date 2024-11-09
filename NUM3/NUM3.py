import numpy as np

N = 300
A = np.zeros((N, 4))
X = np.zeros((N, 1))
L = np.zeros((N, 2))
U = np.zeros((N, 3))

for i in range(N): 
    if i < N:
        A[i][1] = 1.01
    if i < N - 1:
        A[i][0] = 0.3
        A[i][2] = 0.2 / (i + 1)
    if i < N - 2:
        A[i][3] = 0.15 / (i + 1) ** 3
        
for i in range(N):
    X[i][0] = i + 1

for i in range(N):
    L[i][1] = 1        
    U[i][0] = A[i][1] - L[i - 1][0] * U[i - 1][1]    
    L[i][0] = A[i][0]/U[i][0]   
    U[i][1] = A[i][2] - L[i - 1][0] * U[i - 1][2]
    U[i][2] = A[i][3]

detA = 1
for i in range (N):
    detA *= U[i][0]

#forward sbustitution
Z = np.zeros((N , 1)) 
for i in range(N):
    if i == 0:
        Z[i][0] = X[i][0]
    else:
        Z[i][0] = X[i][0] - L[i-1][0] * Z[i - 1][0]

#back substitution
Y = np.zeros((N, 1))
for i in range(N - 1, -1, -1):
    if i == (N - 1):
        Y[i][0] = Z[i][0] / U[i][0]
    elif i == (N - 2):
        Y[i][0] = (Z[i][0] - U[i][1] * Y[i + 1][0]) / U[i][0]
    else:
        Y[i][0] = (Z[i][0] - U[i][1] * Y[i + 1][0] - U[i][2] * Y[i + 2][0]) / U[i][0]

np.set_printoptions(precision=3, suppress=True, linewidth=150, threshold=np.inf)
print(Y)