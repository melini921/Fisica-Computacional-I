# -*- coding: utf-8 -*-
"""
Created on Mon May 19 11:43:53 2025

@author: Melissa Niño
"""

import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.trajectory = []
        self.vel = np.array([0.0, 0.0])
        self.pos = np.array([0.0, 0.0])

    def set_pos(self, pos):
        self.pos = np.array(pos)

    def set_vel(self, vel):
        self.vel = np.array(vel)

    def update_pos(self, delta_t):
        self.pos = self.pos + self.vel * delta_t
        self.trajectory.append(self.pos.copy())  # Usamos copy() para no perder datos anteriores

# Crear partículas
particle_a = Particle()
particle_a.set_pos([-5, 1])
particle_a.set_vel([1, 0])

particle_b = Particle()
particle_b.set_pos([5, -1])
particle_b.set_vel([-1, 0])

# Parámetros de simulación
d_t = 1e-3
n_pasos = 1000  # Más pasos para ver movimiento más claro

# Simulación
for _ in range(n_pasos):
    particle_a.update_pos(d_t)
    particle_b.update_pos(d_t)

# Convertir trayectorias a arrays de NumPy
trayectoria_a = np.array(particle_a.trajectory)
trayectoria_b = np.array(particle_b.trajectory)

# Graficar trayectorias
plt.figure(figsize=(8, 6))
plt.plot(trayectoria_a[:, 0], trayectoria_a[:, 1], label="Partícula A", color='blue')
plt.plot(trayectoria_b[:, 0], trayectoria_b[:, 1], label="Partícula B", color='red')
plt.scatter(trayectoria_a[0, 0], trayectoria_a[0, 1], color='blue', label="Inicio A")
plt.scatter(trayectoria_b[0, 0], trayectoria_b[0, 1], color='red', label="Inicio B")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Trayectoria de dos partículas con velocidad constante")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()
