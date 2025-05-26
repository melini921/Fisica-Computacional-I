# -*- coding: utf-8 -*-
"""
Created on Mon May 19 11:37:29 2025

@author: Melissa Niño
"""
import numpy as np
import matplotlib.pyplot as plt

# Clase para representar una partícula
class Particle:
    def __init__(self):
        self.pos = np.array([0.0, 0.0])
        self.vel = np.array([0.0, 0.0])
        self.acc = np.array([0.0, 0.0])
        self.masa = 1.0
        self.trajectory = []

    def set_pos(self, pos):
        self.pos = np.array(pos)

    def set_vel(self, vel):
        self.vel = np.array(vel)

    def update(self, delta_t):
        # Método de Verlet
        self.vel += 0.5 * self.acc * delta_t
        self.pos += self.vel * delta_t
        self.trajectory.append(self.pos.copy())

# Fuerza Lennard-Jones
def lennard_jones(p1, p2, epsilon=1.0, sigma=1.0):
    r_vec = p2.pos - p1.pos
    r = np.linalg.norm(r_vec)

    if r == 0:
        return np.array([0.0, 0.0])  # Para evitar división por cero

    r_unit = r_vec / r
    fuerza_magnitud = 24 * epsilon * (2 * (sigma / r)**12 - (sigma / r)**6) / r
    return fuerza_magnitud * r_unit

# Actualiza aceleraciones
def actualizar_aceleraciones(p1, p2, epsilon=1.0, sigma=1.0):
    f = lennard_jones(p1, p2, epsilon, sigma)
    p1.acc = f / p1.masa
    p2.acc = -f / p2.masa

# Configurar partículas
a = Particle()
b = Particle()

a.set_pos([1.0, 0.0])
b.set_pos([-1.0, 0.0])

a.set_vel([0.0, 0.5])
b.set_vel([0.0, -0.5])

# Parámetros de simulación
dt = 0.01
n_pasos = 1000

# Simulación
for _ in range(n_pasos):
    actualizar_aceleraciones(a, b)
    a.update(dt)
    b.update(dt)

# Convertir trayectorias a arrays
trayectoria_a = np.array(a.trajectory)
trayectoria_b = np.array(b.trajectory)

# Graficar trayectorias
plt.figure(figsize=(8, 6))
plt.plot(trayectoria_a[:, 0], trayectoria_a[:, 1], label="Partícula A", color="blue")
plt.plot(trayectoria_b[:, 0], trayectoria_b[:, 1], label="Partícula B", color="red")
plt.scatter(trayectoria_a[0, 0], trayectoria_a[0, 1], color="blue", label="Inicio A")
plt.scatter(trayectoria_b[0, 0], trayectoria_b[0, 1], color="red", label="Inicio B")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interacción Lennard-Jones entre dos partículas")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()

