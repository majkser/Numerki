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

n_interp = 10
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

plt.plot(x, y, label='f(x) = 1/(1 + 10*x^2)')
plt.plot(x_interp, y_interp, 'ko', label='Interpolation points')
plt.plot(x, lagrange_y, '--',label='Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 1/(1 + 10*x^2)')
plt.legend()
plt.grid(True)
plt.show()
