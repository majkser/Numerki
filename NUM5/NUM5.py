import matplotlib.pyplot as plt
import numpy as np

result = np.zeros((200, 1))
x = np.zeros((200 ,1))
A = np.zeros((200, 5))

A_for_check = np.zeros((200, 200))
for i in range(200):
    A_for_check[i][i] = 2
    if i == 199:
        break
    A_for_check[i][i + 1] = 0.5
    A_for_check[i + 1][i] = 0.5
    if i < 198:
        A_for_check[i][i + 2] = 0.1
        A_for_check[i + 2][i] = 0.1
        


for i in range (200):
    result[i][0] = i + 1
    A[i][0] = 0.1
    A[i][1] = 0.5
    A[i][2] = 2
    A[i][3] = 0.5
    A[i][4] = 0.1
    

max_iter = 1000
for j in range(max_iter):      
    prev = np.copy(x)
    for i in range(200):        
        if i == 0:
            x[i][0] = (result[i][0] - (A[i][3] * x[i + 1][0]) - (A[i][4] * x[i + 2][0]))/A[i][2]
        elif i == 1:
            x[i][0] = (result[i][0] - (A[i][1] * x[i - 1][0]) - (A[i][3] * x[i + 1][0]) - (A[i][4] * x[i + 2][0]))/A[i][2]
        elif i == 198:
            x[i][0] = (result[i][0] - (A[i][0] * x[i - 2][0]) - (A[i][1] * x[i - 1][0]) - (A[i][3] * x[i + 1][0]))/A[i][2]
        elif i == 199:
            x[i][0] = (result[i][0] - (A[i][0] * x[i - 2][0]) - (A[i][1] * x[i - 1][0]))/A[i][2]
        else:
            x[i][0] = (result[i][0] - (A[i][0] * x[i - 2][0]) - (A[i][1] * x[i - 1][0]) - (A[i][3] * x[i + 1][0]) - (A[i][4] * x[i + 2][0]))/A[i][2]  
            #for j in range(200):
    if np.array_equal(x, prev):
        break

x_for_check = np.linalg.solve(A_for_check, result)

print(x - x_for_check)