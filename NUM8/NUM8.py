import numpy as np
import matplotlib.pyplot as plt

def f1a(x):
    return 3 * np.sin(2 * x)
def f1b(x):
    return 2 * (x ** 3)
def f1c(x):
    return - np.exp(x)
real_a1 = [3, 2, -1]

def f2a(x):
    return 2 * np.cos(3 * x)
def f2b(x):
    return 4 * (x ** 3)
def f2c(x):
    return 5 * x
real_a2 = [2, 4, 5]

def f3a(x):
    return 7 * np.sqrt(x ** 3)
def f3b(x):
    return 3 * np.tan(x ** 5)
def f3c(x):
    return 9 * (x ** 2)
real_a3 = [7, 3, 9]

def metoda_najmniejszych_kwadratów(fa, fb, fc, real_a):

    n = 30
    sigma = 3
    sigma_y = np.random.normal(0, sigma, n)
    x = np.linspace(0, 2, n)
    
    real_f1 = real_a[0] * fa(x) + real_a[1] * fb(x) + real_a[2] * fc(x)
    y = real_f1 + sigma_y

    A = np.vstack([fa(x), fb(x), fc(x)]).T
    U, S, V = np.linalg.svd(A, full_matrices=False)

    a = np.dot(V.T, np.dot(np.diag(1/S), np.dot(U.T, y)))
    
    plt.plot(x, real_f1, label='Real function')
    plt.plot(x, a[0] * fa(x) + a[1] * fb(x) + a[2] * fc(x), label='Calculated function', linestyle = "--")
    plt.plot(x, y, label='Noisy data', linestyle = "None", marker = "o")
    plt.legend()
    plt.show()
    
    return a

print(f"Real a for f1: {real_a1}")
print(f"Calculated a for f1: {metoda_najmniejszych_kwadratów(f1a, f1b, f1c, real_a1)}")
print(f"Real a for f2: {real_a2}")
print(f"Calculated a for f2: {metoda_najmniejszych_kwadratów(f2a, f2b, f2c, real_a2)}")
print(f"Real a for f3: {real_a3}")
print(f"Calculated a for f3: {metoda_najmniejszych_kwadratów(f3a, f3b, f3c, real_a3)}")