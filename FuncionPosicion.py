# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 14:34:30 2025

@author: Melissa Niño
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definimos la función de velocidad
v_scalar = lambda t: 5*t**3 - 4*t + 7
v_array = lambda t: 5*t**3 - 4*t + 7

# Intervalo de integración
a, b = 0, 50
exact_value, _ = quad(v_scalar, a, b)

# Implementación de la Regla del Trapecio
def trapezoid_rule(f, _a, _b, n):
    x = np.linspace(_a, _b, n + 1)
    y = f(x)
    h = (_b - _a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

# Implementación de la Regla de Simpson
def simpson_rule(f, _a, _b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser par para la regla de Simpson")
    x = np.linspace(_a, _b, n + 1)
    y = f(x)
    h = (_b - _a) / n
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

# Rango de valores para n
ns = np.arange(2, 100, 2)
trap_errors = [abs(trapezoid_rule(v_array, a, b, n) - exact_value) for n in ns]
simp_errors = [abs(simpson_rule(v_array, a, b, n) - exact_value) for n in ns]

# Gráfica de comparación de errores
#plt.plot(ns, trap_errors, label="Error Regla del Trapecio")
#plt.plot(ns, simp_errors, label="Error Regla de Simpson")
#plt.yscale("log")
#plt.xlabel("Número de subintervalos (n)")
#plt.ylabel("Error absoluto")
#plt.title("Comparación de errores numéricos para la función de velocidad")
#plt.legend()
#plt.grid(True)
#plt.show()

# Cálculo de x(t) integrando v(t)
def position_function(f, _a, _b):
    x_vals = np.linspace(_a, _b, 100)
    x_t = [quad(f, _a, t)[0] for t in x_vals]
    return x_vals, x_t

# Obtener x(t)
x_vals, x_t = position_function(v_scalar, a, b)

# Graficar x(t)
plt.plot(x_vals, x_t, label="Posición x(t)")
plt.xlabel("Tiempo (t)")
plt.ylabel("Posición (x)")
plt.title("Gráfica de la función de posición x(t)")
plt.legend()
plt.grid(True)
plt.show()
