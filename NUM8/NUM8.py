import numpy as np
import matplotlib.pyplot as plt

M = np.array([[9, 2, 0 , 0],
     [2, 4, 1, 0],
     [0, 1, 3, 1],
     [0, 0, 1, 2]])

print(M)

error = 10e-8
y0 = np.random.rand(4)
print(y0)

def power_method(matrix, y0):
    itter = []
    diff = np.inf
    number_of_itter = 0
    while(diff > error):
        y = matrix @ y0
        Eigenvalue = np.max(np.abs(y))
        y = y / Eigenvalue
        diff = np.linalg.norm(np.abs(y - y0))
        y0 = y
        number_of_itter += 1
        itter.append(np.log10(diff))
        
    return y, Eigenvalue, number_of_itter, itter

print(power_method(M, y0))

def power_method_plot(matrix, y0):
    y, Eigenvalue, number_of_itter, itter = power_method(matrix, y0)
    plt.plot(itter, label="diffrences in itterations for power method")
    plt.xlabel('Number of itterations')
    plt.ylabel('difference in logaritmic scale')
    plt.title('Power method')
    plt.grid()
    plt.legend()
    plt.show()
    
power_method_plot(M, y0)
