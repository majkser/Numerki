import numpy as np
import time
import matplotlib.pyplot as plt


Ns = range(1, 1000)
times = []
times_numPy = []

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
    
    start_numPy = time.time()
    if N == 120:
        y_numPy_120 = np.linalg.solve(A, b)
    y_numPy = np.linalg.solve(A, b)
    end_numPy = time.time() - start_numPy
    times_numPy.append(end_numPy)
    
    start = time.time()
    y = np.zeros((N,1))

    u = np.ones((N,1))
    vT = u.T

    A1 = A - u @ vT

    A1_pasma = np.zeros((N, 2))
    
    for i in range(N):
        A1_pasma[i][0] = A1[i][i]
        if i == N - 1:
            break
        A1_pasma[i][1] = A1[i][i + 1]
    
    z = np.zeros((N,1))
    q = np.zeros((N,1))
    #Back substitution
    for i in range(N - 1, -1, -1):
        if i == N - 1:
            z[i][0] = b[i][0] / A1_pasma[i][0]
            q[i][0] = z[i][0] / A1_pasma[i][0]
        else:
            z[i][0] = (b[i][0] - A1_pasma[i][1] * z[i + 1][0]) / A1_pasma[i][0]
            q[i][0] = (1 - A1_pasma[i][1] * q[i + 1][0]) / A1_pasma[i][0]
    
    y = z - ((vT @ z) / (1 + (vT @ q))) * q
    
    
    end = time.time() - start
    times.append(end)
    
    if N == 120:
        diff = y_numPy_120 - y
        y = y.flatten()
        y_numPy_120 = y_numPy_120.flatten()
        print(y_numPy_120)

plt.figure(figsize=(10, 6))
plt.plot(Ns, times, label='Execution Time - custom method')
plt.plot(Ns, times_numPy, label='Execution Time - numPy')
plt.xlabel('N')
plt.ylabel('Time (seconds)')
plt.title('Execution Time vs N')
plt.legend()
plt.show()
