import numpy as np

N = 300
A = np.zeros((N, N))
X = np.zeros((N, 1))

j = 0
for i in range(N): 
    if (i == j): 
        A[i][j] = 1.01
        j = j + 1
    else :
        j = j + 1

j = 0
for i in range(1,N):
    if (i - j == 1):
        A[i][j] = 0.3
        j = j + 1
    else:
        j = j + 1

j = 1
for i in range(N-1):
    if (j - i == 1):
        A[i][j] = 0.2/j
        j = j + 1
    else:   
        j = j + 1

j = 2
for i in range(N-2):
    if (j - i == 2):
        A[i][j] = 0.15/(i+1)**3
        j = j + 1
    else:   
        j = j + 1
        
for i in range(N):
    X[i][0] = i + 1
    
np.set_printoptions( suppress=True, linewidth=150, threshold=np.inf)
print(X)
print(A)