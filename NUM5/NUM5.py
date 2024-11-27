import numpy as np
import matplotlib.pyplot as plt
import time

result = np.zeros((200, 1))
x = np.zeros((200, 1))
x2 = np.zeros((200, 1))
A = np.zeros((200, 5))
A_for_check = np.zeros((200, 200))

def matrix_builder(d):
    for i in range(200):
        result[i][0] = i + 1
        A[i][0] = 0.1
        A[i][1] = 0.5
        A[i][2] = d
        A[i][3] = 0.5
        A[i][4] = 0.1
        A_for_check[i][i] = d
        if i < 198:
            A_for_check[i][i + 2] = 0.1
            A_for_check[i + 2][i] = 0.1
        if i < 199:
            A_for_check[i][i + 1] = 0.5
            A_for_check[i + 1][i] = 0.5

max_iter = 10000
tolerance = 1e-10  # Convergence tolerance

def Gauss_Seidel(x_for_check):
    differences = []
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
        differences.append(np.linalg.norm(x - x_for_check, ord=np.inf))
        if np.linalg.norm(x - prev, ord=np.inf) < tolerance:
            print("Gauss-Seidel converged in", j + 1, "iterations")
            print(x.flatten())
            break
    return differences

def Jacobi(x_for_check):
    differences = []
    for j in range(max_iter):      
        prev = np.copy(x2)
        for i in range(200):        
            if i == 0:
                x2[i][0] = (result[i][0] - (A[i][3] * prev[i + 1][0]) - (A[i][4] * prev[i + 2][0]))/A[i][2]
            elif i == 1:
                x2[i][0] = (result[i][0] - (A[i][1] * prev[i - 1][0]) - (A[i][3] * prev[i + 1][0]) - (A[i][4] * prev[i + 2][0]))/A[i][2]
            elif i == 198:
                x2[i][0] = (result[i][0] - (A[i][0] * prev[i - 2][0]) - (A[i][1] * prev[i - 1][0]) - (A[i][3] * prev[i + 1][0]))/A[i][2]
            elif i == 199:
                x2[i][0] = (result[i][0] - (A[i][0] * prev[i - 2][0]) - (A[i][1] * prev[i - 1][0]))/A[i][2]
            else:
                x2[i][0] = (result[i][0] - (A[i][0] * prev[i - 2][0]) - (A[i][1] * prev[i - 1][0]) - (A[i][3] * prev[i + 1][0]) - (A[i][4] * prev[i + 2][0]))/A[i][2]  
        differences.append(np.linalg.norm(x2 - x_for_check, ord=np.inf))
        if np.linalg.norm(x2 - prev, ord=np.inf) < tolerance:
            print("Jacobi converged in", j + 1, "iterations")
            print(x2.flatten())
            break
    return differences

# Plotting the results for different matrices
def plot_differences(d):
    matrix_builder(d)
    x_for_check = np.linalg.solve(A_for_check, result)
    
    gauss_seidel_differences = Gauss_Seidel(x_for_check)
    jacobi_differences = Jacobi(x_for_check)
    
    plt.figure(figsize=(10, 6))
    plt.plot(gauss_seidel_differences, label='Gauss-Seidel')
    plt.plot(jacobi_differences, label='Jacobi')
    plt.xlabel('Iteration')
    plt.yscale('log')
    plt.ylabel('Difference from exact solution')
    plt.title(f'Convergence Comparison: Jacobi vs Gauss-Seidel (d={d})')
    plt.legend()
    plt.show()

# Plot for different matrix values
for d in [1.2001, 2, 3, 4]:
    plot_differences(d)