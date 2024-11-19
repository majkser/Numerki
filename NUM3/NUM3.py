import numpy as np
import matplotlib.pyplot as plt
import time

Ns = range(300, 1001, 10)
times = []

for N in Ns:

    A = np.zeros((N, 4))
    X = np.zeros((N, 1))
    L = np.zeros((N, 2))
    U = np.zeros((N, 3))
    Z = np.zeros((N, 1))    
    Y = np.zeros((N, 1))
    

    
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
        
    start_time = time.perf_counter()
    
    for i in range(N):
        L[i][1] = 1        
        U[i][0] = A[i][1] - L[i - 1][0] * U[i - 1][1]    
        L[i][0] = A[i][0] / U[i][0]   
        U[i][1] = A[i][2] - L[i - 1][0] * U[i - 1][2]
        if i < N - 2:
            U[i][2] = A[i][3]

    # Forward substitution
 
    for i in range(N):
        if i == 0:
            Z[i][0] = X[i][0]
        else:
            Z[i][0] = X[i][0] - L[i-1][0] * Z[i - 1][0]

    # Back substitution

    for i in range(N - 1, -1, -1):
        if i == (N - 1):
            Y[i][0] = Z[i][0] / U[i][0]
        elif i == (N - 2):
            Y[i][0] = (Z[i][0] - U[i][1] * Y[i + 1][0]) / U[i][0]
        else:
            Y[i][0] = (Z[i][0] - U[i][1] * Y[i + 1][0] - U[i][2] * Y[i + 2][0]) / U[i][0]

    end_time = time.perf_counter()
    times.append(end_time - start_time)
    
    if N == 300:    
        detA = 1
        for i in range(N):
            detA *= U[i][0] 
        print(Y)
        print(detA)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(Ns, times, label='Execution Time')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('Execution Time vs N')
plt.legend()
plt.show()