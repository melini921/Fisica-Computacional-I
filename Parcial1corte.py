# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 14:33:01 2025

@author: Melissa Niño
"""
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

def Fuerza(k):  
    v_scalar = lambda t: k * t**3
    v_array = lambda t: k * t**3
    return v_scalar, v_array  

class EntidadMatematica(ABC):
    @abstractmethod
    def Suma(self, other):
        pass
    @abstractmethod
    def Evaluar(self):
        pass
    @abstractmethod
    def Escalar(self, escalar):  
        pass

class Vector(EntidadMatematica):
    def __init__(self, components):  
        if len(components) != 1:
            raise ValueError("Un vector debe tener una dimension.")
        self.x = components[0]

    def Suma(self, other):
        return Vector([self.x + other.x])  

    def Escalar(self, escalar):
        return Vector([self.x * escalar])

class Funcion(EntidadMatematica):
    def __init__(self, func):
        self.func = func

    def Evaluar(self, x):
        return self.func(x)  

    def Representar(self, a, b):
        x_vals = np.linspace(a, b, 100)
        y_vals = [self.func(t) for t in x_vals]  

        plt.plot(x_vals, y_vals, label="Función")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfica de la función")
        plt.legend()
        plt.grid(True)
        plt.show()

def Factorial_Recursivo(n):
    if n == 0:
        return 1  
    elif n == 1:
        return 1
    else:
        return n * Factorial_Recursivo(n - 1)

def Aceleracion(t, Mass):
    fuerza_scalar, fuerza_array = Fuerza(t)  
    ace = fuerza_scalar(t) / Mass  
    return ace

def trapezoid_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def calcular_aceleracion(t, Mass, k):  
    fuerza_scalar, fuerza_array = Fuerza(k)
    ace = fuerza_scalar(t) / Mass
    return ace

def calcular_velocidad(aceleracion_func, a, b, n, Mass, k):
    x_vals = np.linspace(a, b, n + 1)
    v_vals = [trapezoid_rule(lambda t: calcular_aceleracion(t, Mass, k), a, t, n) for t in x_vals]
    return x_vals, v_vals

def calcular_posicion(velocidad_func, a, b, n, Mass, k):
    x_vals = np.linspace(a, b, n + 1)
    p_vals = [trapezoid_rule(lambda t: velocidad_func(t)[1][np.where(velocidad_func(t)[0] == t)[0][0]], a, t, n) for t in x_vals]
    return x_vals, p_vals

#ejemplo
Mass = 10  
k = 5  
a = 0  
b = 10  
n = 100  

aceleracion_func = lambda t: calcular_aceleracion(t, Mass, k)
velocidad_func = lambda t: calcular_velocidad(aceleracion_func, a, b, n, Mass, k)
posicion_func = lambda t: calcular_posicion(velocidad_func, a, b, n, Mass, k)

t_vals = np.linspace(a, b, n + 1)
a_vals = [aceleracion_func(t) for t in t_vals]
v_vals = [velocidad_func(t)[1] for t in t_vals]
p_vals = [posicion_func(t)[1] for t in t_vals]

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

axs[0].plot(t_vals, a_vals)
axs[0].set_title("Acceleration")
axs[0].set_xlabel("Time (t)")
axs[0].set_ylabel("Acceleration (a)")

axs[1].plot(t_vals, v_vals)
axs[1].set_title("Velocity")
axs[1].set_xlabel("Time (t)")
axs[1].set_ylabel("Velocity (v)")

axs[2].plot(t_vals, p_vals)
axs[2].set_title("Position")
axs[2].set_xlabel("Time (t)")
axs[2].set_ylabel("Position (x)")


plt.tight_layout()
plt.show()
        
        