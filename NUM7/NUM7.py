import numpy as np
import matplotlib.pyplot as plt

def xi(n):
    x = [] 
    i = 0
    
    while True:
        if (-1 + 2*i/n > 1 or -1 + 2*i/n < -1):
            break
        
        x.append(-1 + 2*i/n)
        i += 1
    
    return x

def yi(x):
    y = []
    
    for i in range(len(x)):
        y.append(1/(1 + 10*(x[i]**2)))
        
    return y

n = 100
x = xi(n)
y = yi(x)

n_interp = 15
if (n_interp + 1) % 2 != 0:
    n_interp += 1
x_interp = xi(n_interp)
y_interp = yi(x_interp)

def lagrange(xs, x, y, n):
    li = []
    Wx = []
    
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (xs - x[j])/(x[i] - x[j])
        
        li.append(l)
        
    for i in range(n):
        Wx.append(y[i]*li[i])
    
    return sum(Wx) 
    
lagrange_y = []
lagrange_y = [lagrange(x, x_interp, y_interp, n_interp) for x in x]

def cubic_splain (x, y):
    n = len(x) - 1
    matrix = np.zeros((n + 1, n + 1))
    u = np.zeros(n + 1)
    
    #natural boundary conditions
    matrix[0][0] = 1
    matrix[n][n] = 1
    
    h = np.diff(x)
    
    for i in range(1, n):
        matrix[i][i - 1] = h[i - 1]
        matrix[i][i + 1] = h[i - 1]
        matrix[i][i] = 2*(h[i - 1] + h[i]) 
        u[i] = 6*(y[i+1] - y[i])/(h[i]) - 6*(y[i] - y[i-1])/(h[i-1])
        
    c = np.linalg.solve(matrix, u)
    
    a = y[:-1]
    b = np.zeros(n)
    d = np.zeros(n)
    
    for i in range(n):
        dx = x[i + 1] - x[i]
        b[i] = (y[i + 1] - y[i]) / dx - dx * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * dx)

    return a, b, c[:-1], d
        
def evaluate_spline(a, b, c, d, x, x_points):
    
    y_points = []
    for xp in x_points:
        for i in range(len(x) - 1):
            if x[i] <= xp <= x[i + 1]:
                dx = xp - x[i]
                y = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
                y_points.append(y)
                break
            
    return np.array(y_points)
    
a, b, c, d = cubic_splain(x_interp, y_interp)
splain_y = evaluate_spline(a, b, c, d, x_interp, x)


plt.plot(x, y, label='f(x) = 1/(1 + 10*x^2)')
plt.plot(x_interp, y_interp, 'ko', label='Interpolation points')
plt.plot(x, lagrange_y, '--',label='Lagrange Interpolation')
plt.plot(x, splain_y, label='Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 1/(1 + 10*x^2)')
plt.legend()
plt.grid(True)
plt.show()
