# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 11:48:51 2025

@author: Melissa Niño
"""
import numpy as np
import matplotlib.pyplot as plt

def integrando(x):
    """Función de la campana de Gauss."""
    return np.exp(-x**2)

a = -10  
b = 10  

N = 1000

h = (b - a) / N

x = np.linspace(a, b, N + 1)
y = integrando(x)

suma = y[0] + y[-1]  

for i in range(1, N):
    if i % 2 == 0:
        suma += 2 * y[i]  
    else:
        suma += 4 * y[i]

resultado_simpson = (h / 3) * suma

print("Resultado de la regla de Simpson implementada:", resultado_simpson)

x = np.linspace(-5, 5, 400)
y = integrando(x)

plt.plot(x, y, label='e^{-x^2}')
plt.fill_between(x, y, alpha=0.3)
plt.title('Campana de Gauss')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()