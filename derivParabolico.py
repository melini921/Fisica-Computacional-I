# -*- coding: utf-8 -*-
"""
Created on Fri May  9 12:22:22 2025

@author: Melissa Niño
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir símbolo
t = sp.Symbol('t')

# Función posición (parábola): y(t) = -5t^2 + 20t + 1
# Aquí: -5 representa -g/2, 20 es la velocidad inicial, y 1 la altura inicial
posicion = -5 * t**2 + 20 * t + 1

# Derivadas: velocidad y aceleración
velocidad = sp.diff(posicion, t)
aceleracion = sp.diff(velocidad, t)

# Convertir a funciones evaluables (lambda) -  Usando 'numpy' directamente
f_pos = sp.lambdify(t, posicion, 'numpy')
f_vel = sp.lambdify(t, velocidad, 'numpy')
f_acel = sp.lambdify(t, aceleracion, 'numpy')

# Crear dominio de tiempo
tiempo = np.linspace(0, 5, 400)

# Evaluar funciones
y_pos = f_pos(tiempo)
y_vel = f_vel(tiempo)
y_acel = f_acel(tiempo)

# Graficar - Mejorando la presentación
plt.figure(figsize=(10, 6))

plt.plot(tiempo, y_pos, label='Posición (m)', color='blue', linewidth=2)
plt.plot(tiempo, y_vel, label='Velocidad (m/s)', color='green', linewidth=2)
plt.plot(tiempo, y_acel, label='Aceleración (m/s²)', color='red', linewidth=2)

plt.title('Movimiento vertical de un proyectil', fontsize=14)
plt.xlabel('Tiempo (s)', fontsize=12)
plt.ylabel('Magnitud', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.5)

plt.tight_layout()  # Ajusta el espacio entre elementos
plt.show()
