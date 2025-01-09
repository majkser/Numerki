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

def power_method(matrix, y0, error):
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

print(power_method(M, y0, error))

def power_method_plot(matrix, y0):
    y, Eigenvalue, number_of_itter, itter = power_method(matrix, y0, error)
    plt.plot(itter, label="diffrences in itterations for power method")
    plt.xlabel('Number of itterations')
    plt.ylabel('difference in logaritmic scale')
    plt.title('Power method')
    plt.grid()
    plt.legend()
    plt.show()
    
power_method_plot(M, y0)

def QR_algorithm(matrix, error):
    diff = np.inf
    itter_norm_upper_triangular_matrix = []
    itter_diag_A = []
    A = matrix
    
    while(diff > error):
        Q, R = np.linalg.qr(A)
        A = R @ Q
        diff = np.linalg.norm(np.abs(A - np.diag(np.diag(A))))
        itter_norm_upper_triangular_matrix.append(np.log10(diff))
        itter_diag_A.append(np.log10(np.diag(A)))
        
    return np.diag(A), itter_norm_upper_triangular_matrix, itter_diag_A

print(QR_algorithm(M, error))

def QR_algorithm_diff_in_itter_plot(matrix):
    Eigenvalues, itter_norm_upper_triangular_matrix, itter_diag_a = QR_algorithm(matrix, error)
    plt.plot(itter_norm_upper_triangular_matrix, label="diffrences in upper triangular matrixes in itterations for QR algorithm")
    plt.xlabel('Number of itterations')
    plt.ylabel('difference in logaritmic scale')
    plt.title('QR algorithm')
    plt.grid()
    plt.legend()
    plt.show()
    
QR_algorithm_diff_in_itter_plot(M)

def QR_algorithm_diff_in_diag_plot(matrix):
    Eigenvalues, itter_norm_upper_triangular_matrix, itter_diag_a = QR_algorithm(matrix, error)
    plt.plot(itter_diag_a, label=f"Eigenvalues in itterations for QR algorithm")
    plt.xlabel('Number of itterations')
    plt.ylabel('difference in logaritmic scale')
    plt.title('QR algorithm')
    plt.grid()
    plt.legend()
    plt.show()
    
QR_algorithm_diff_in_diag_plot(M)