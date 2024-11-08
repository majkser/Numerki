import numpy as np

N = 300
A = np.zeros((N, N))
X = np.zeros((N, 1))
L = np.zeros((N, N))
U = np.zeros((N, N))

for i in range(N): 
    if i < N:
        A[i][i] = 1.01
    if i < N - 1:
        A[i + 1][i] = 0.3
    if i < N - 1:
        A[i][i + 1] = 0.2 / (i + 1)
    if i < N - 2:
        A[i][i + 2] = 0.15 / (i + 1) ** 3
        
for i in range(N):
    X[i][0] = i + 1

np.set_printoptions(precision=4, suppress=True, linewidth=150, threshold=np.inf)
print(L)
#print(A)