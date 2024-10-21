import numpy as np
import matplotlib.pyplot as plt

x1 = np.float32(0.2)
x2 = np.float64(0.2)

def f32(x):
    return np.float32(np.sin(x ** 3))

def f64(x):
    return np.float64(np.sin(x ** 3))

def fPrim32(x):
    return np.float32(3*x**2*np.cos(x**3))

def fPrim64(x):
    return np.float64(3*x**2*np.cos(x**3))

h1 =np.logspace(-8, 0, 400)
h2 =np.logspace(-16, 0, 400)

def derivative_a32(f, x, h):
    return np.float32((f(x + h) - f(x)) / h)

def derivative_a64(f, x, h):
    return np.float64((f(x + h) - f(x)) / h)

def derivative_b32(f, x, h):
    return  np.float32((f(x + h) - f(x - h)) / (2 * h))

def derivative_b64(f, x, h):
    return  np.float64((f(x + h) - f(x - h)) / (2 * h))

errors_a32_float32 = np.abs(derivative_a32(f32, x1, h1) - fPrim32(x1))
errors_a64_float64 = np.abs(derivative_a64(f64, x2, h2) - fPrim64(x2))

errors_b32_float32 = np.abs(derivative_b32(f32, x1, h1) - fPrim32(x1))
errors_b64_float64 = np.abs(derivative_b64(f64, x2, h2) - fPrim64(x2))


#############################################

plt.figure(figsize=(10, 6))
plt.plot(h1, errors_a32_float32, label='Errors A (float32)', color='blue')
plt.plot(h2, errors_a64_float64, label='Errors A (float64)', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Error')
plt.title('Errors in Numerical Derivatives (derivative_a)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(h1, errors_b32_float32, label='Errors B (float32)', color='green')
plt.plot(h2, errors_b64_float64, label='Errors B (float64)', color='orange')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Error')
plt.title('Errors in Numerical Derivatives (derivative_b)')
plt.legend()
plt.grid(True)
plt.show()

z1 = np.float32(0.5)
z2 = np.float64(0.5)

def g32(z):
    return np.float32(3**z)
def g64 (z):
    return np.float64(3**z)

def gPrim32(z):
    return np.float32(np.log(3)*3**z)
def gPrim64(z):
    return np.float64(np.log(3)*3**z)

errors_a32_float32 = np.abs(derivative_a32(g32, z1, h1) - gPrim32(z1))
errors_a64_float64 = np.abs(derivative_a64(g64, z2, h2) - gPrim64(z2))

errors_b32_float32 = np.abs(derivative_b32(g32, z1, h1) - gPrim32(z1))
errors_b64_float64 = np.abs(derivative_b64(g64, z2, h2) - gPrim64(z2))


plt.figure(figsize=(10, 6))
plt.plot(h1, errors_a32_float32, label='Errors A (float32)', color='blue')
plt.plot(h2, errors_a64_float64, label='Errors A (float64)', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Error')
plt.title('Errors in Numerical Derivatives (derivative_a)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(h1, errors_b32_float32, label='Errors B (float32)', color='green')
plt.plot(h2, errors_b64_float64, label='Errors B (float64)', color='orange')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('Error')
plt.title('Errors in Numerical Derivatives (derivative_b)')
plt.legend()
plt.grid(True)
plt.show()