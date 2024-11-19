import numpy as np
import time
import matplotlib.pyplot as plt


Ns = range(1, 121)
times = []

for N in Ns:
    A = np.ones((N, N))
    for i in range (N):
        A[i][i] = 5
        if i == N - 1:
            break
        A[i][i + 1] = 3

    b = np.zeros((N,1))
    for i in range(N):
        b[i] = 2
        
    y_numPy = np.linalg.solve(A, b)
    
    start = time.time()
    y = np.zeros((N,1))

    u = np.ones((N,1))
    vT = u.T

    A1 = A - u @ vT

    #odwracanie macierzy A1
    A1_inv = np.zeros((N, N))
    for i in range(N):
        for j in range(i, N):
            value = (-1.0) ** (j - i) / (4.0 ** (j - i + 1))
            A1_inv[i, j] = value

    z = A1_inv @ b
    q = A1_inv @ u

    y = z - ((vT @ z) / (1 + vT @ q)) * q
        
    end = time.time() - start
    times.append(end)
    
    if N == 120:
        print(y_numPy - y)
    
plt.figure(figsize=(10, 6))
plt.plot(Ns, times, label='Execution Time')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('Execution Time vs N')
plt.legend()
plt.show()
#print("NumPy: ", end_numPy)
#print("My: ", end)
#print(w)
#print (y_numPy - y)
#print(y)
#print(y_numPy)