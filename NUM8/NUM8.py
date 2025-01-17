import numpy as np
import matplotlib.pyplot as plt

def f1a(x):
    return 3 * np.sin(2 * x)
def f1b(x):
    return 2 * (x ** 3)
def f1c(x):
    return - np.exp(x)

real_a1 = [3, 2, -1]

def metoda_najmniejszych_kwadratów(fa, fb, fc, real_a):

    n = 100
    sigma = 3
    sigma_y = np.random.normal(0, sigma, n)
    x = np.linspace(0, 2, n)

    real_f1 = real_a[0] * fa(x) + real_a[1] * fb(x) + real_a[2] * fc(x)
    y = real_f1 + sigma_y

    A = np.vstack([fa(x), fb(x), fc(x)]).T
    U, S, V = np.linalg.svd(A, full_matrices=False)

    a = np.dot(V.T, np.dot(np.diag(1/S), np.dot(U.T, y)))
    
    return a

print(f"Real a: {real_a1}")
print(f"Calculated a: {metoda_najmniejszych_kwadratów(f1a, f1b, f1c, real_a1)}")