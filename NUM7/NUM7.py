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

n = 10
xi = xi(n)
yi = yi(xi)
    
print (xi)
print (yi)



plt.plot(xi, yi, label='f(x) = 1/(1 + 10*x^2)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = 1/(1 + 10*x^2)')
plt.legend()
plt.grid(True)
plt.show()