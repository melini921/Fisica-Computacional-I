# -*- coding: utf-8 -*-
"""
Created on Fri May 16 15:12:14 2025

@author: Melissa Niño
"""

import matplotlib.pyplot as plt
import numpy as np

class Particula:
    def __init__(self):
        self.carga = 1.0
        self.masa = 1.0
        self.vel = np.array([0.0, 0.0])
        self.pos = np.array([0.0, 0.0])
        self.acc = np.array([0.0, 0.0])

    def set_pos(self, pos):
        self.pos = np.array(pos)

    def set_carga(self, carga):
        self.carga = carga

    def set_vel(self, vel):
        self.vel = np.array(vel)

    def set_acc(self, acc):
        self.acc = np.array(acc)

K = 9e9
dt = 1e-2
m_pas = 100

def coulomb(p1, p2):
    r = p2.pos - p1.pos
    d = np.linalg.norm(r)
    if d == 0:
        return np.array([0.0, 0.0])
    ru = r / d
    return (K * p1.carga * p2.carga / d**2) * ru

def update(p1, p2):
    f = coulomb(p1, p2)
    acc1 = f / p1.masa
    acc2 = -f / p2.masa

    v1 = p1.vel + acc1 * dt
    v2 = p2.vel + acc2 * dt

    x1 = p1.pos + p1.vel * dt + 0.5 * acc1 * dt**2
    x2 = p2.pos + p2.vel * dt + 0.5 * acc2 * dt**2

    p1.set_pos(x1)
    p2.set_pos(x2)
    p1.set_vel(v1)
    p2.set_vel(v2)
    p1.set_acc(acc1)
    p2.set_acc(acc2)

# Crear partículas con posiciones no alineadas
a = Particula()
b = Particula()
a.set_pos([0.0, 0.0])
b.set_pos([1.0, 1.0])
a.set_vel([0.0, 0.1])
b.set_vel([-0.1, 0.0])
a.set_carga(1.0)
b.set_carga(-1.0)

# Guardar trayectorias
trayectoria_a = [a.pos.copy()]
trayectoria_b = [b.pos.copy()]

for _ in range(m_pas):
    update(a, b)
    trayectoria_a.append(a.pos.copy())
    trayectoria_b.append(b.pos.copy())

trayectoria_a = np.array(trayectoria_a)
trayectoria_b = np.array(trayectoria_b)

# Graficar XY
plt.figure(figsize=(8, 6))
plt.plot(trayectoria_a[:, 0], trayectoria_a[:, 1], label='Partícula A', color='blue')
plt.plot(trayectoria_b[:, 0], trayectoria_b[:, 1], label='Partícula B', color='red')
plt.scatter(trayectoria_a[0, 0], trayectoria_a[0, 1], color='blue', marker='o', label='Inicio A')
plt.scatter(trayectoria_b[0, 0], trayectoria_b[0, 1], color='red', marker='o', label='Inicio B')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trayectoria XY de dos partículas cargadas')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

