# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 22:23:29 2025

@author: Melissa Niño
"""

import numpy as np
import matplotlib.pyplot as plt

K = 9e+9
DELTA_T = 1e-3
L = 5
N = 30  # Número de partículas
k_B = 1.38e-23

class Particle:
    def __init__(self, pos, vel, charge=0.0001, mass=0.1):
        self.mass = mass
        self.charge = charge
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.acc = np.array([0.0, 0.0])
        self.trajectory = [self.pos.copy()]

    def update_dynamics(self, force, delta_t):
        self.acc = force / self.mass
        self.vel += self.acc * delta_t
        self.pos += self.vel * delta_t
        self.apply_periodic_boundary_conditions(L)
        self.trajectory.append(self.pos.copy())

    def apply_periodic_boundary_conditions(self, L):
        self.pos = self.pos % L

def calculate_force(a, b):
    r = b.pos - a.pos
    r = r - L * np.round(r / L)  # condición de imagen mínima
    dist = np.linalg.norm(r)
    if dist == 0:
        return np.array([0.0, 0.0])
    f = K * a.charge * b.charge / (dist ** 3)
    return f * r

# Crear partículas con posiciones y velocidades aleatorias
particles = []
np.random.seed(0) 

for _ in range(N):
    pos = np.random.uniform(0, L, 2)
    vel = np.random.uniform(-1, 1, 2)
    particles.append(Particle(pos, vel))

kinetic_energies = []
potential_energies = []
temperaturas = []

# Simulación
dof = 2 * N
for _ in range(2000):
    forces = [np.array([0.0, 0.0]) for _ in particles]

    for i in range(N):
        for j in range(i + 1, N):
            f_ij = calculate_force(particles[i], particles[j])
            forces[j] += f_ij
            forces[i] -= f_ij  # acción y reacción

    for i in range(N):
        particles[i].update_dynamics(forces[i], DELTA_T)

    total_ke = 0.0
    for p in particles:
        v2 = np.dot(p.vel, p.vel)
        total_ke += 0.5 * p.mass * v2
    kinetic_energies.append(total_ke)

    T_inst = (2 * total_ke) / (dof * k_B)
    temperaturas.append(T_inst)

    total_pe = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            r = particles[j].pos - particles[i].pos
            r = r - L * np.round(r / L)
            dist = np.linalg.norm(r)
            if dist != 0:
                total_pe += K * particles[i].charge * particles[j].charge / dist
    potential_energies.append(total_pe)

# Graficar trayectorias
plt.figure(figsize=(8, 8))
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'cyan', 'magenta', 'gray', 'olive']

for i, p in enumerate(particles):
    traj = np.array(p.trajectory)
    plt.scatter(traj[:, 0], traj[:, 1], s=1, color=colors[i % len(colors)])
    plt.scatter(traj[0, 0], traj[0, 1], s=50, facecolors='none', edgecolors=colors[i % len(colors)], marker='o')

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Trayectorias de {N} partículas con condiciones periódicas")
plt.xlim(0, L)
plt.ylim(0, L)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.legend()
plt.show()

# Gráficos de energía
tiempos = np.arange(len(kinetic_energies)) * DELTA_T

plt.figure()
plt.plot(tiempos, kinetic_energies, label="Energía cinética")
plt.plot(tiempos, potential_energies, label="Energía potencial")
plt.plot(tiempos, np.array(kinetic_energies) + np.array(potential_energies), label="Energía total", linestyle='--')
plt.xlabel("Tiempo (s)")
plt.ylabel("Energía (J)")
plt.title("Energías del sistema")
plt.legend()
plt.grid(True)
plt.show()

# Temperaturas
T_final = temperaturas[-1]
T_avg = np.mean(temperaturas)

print(f"Temperatura final del sistema: {T_final:.2f} K")
print(f"Temperatura promedio del sistema: {T_avg:.2f} K")

plt.figure()
plt.plot(tiempos, temperaturas, label="Temperatura instantánea")
plt.axhline(y=T_avg, color='red', linestyle='--',
            label=f"Temperatura promedio ≈ {T_avg:.2f} K")
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura (K)")
plt.title("Evolución de la temperatura del sistema")
plt.grid(True)
plt.legend()
plt.show()

#  DISTRIBUCIÓN DE VELOCIDADES 

# Obtener las magnitudes de las velocidades finales
velocidades = [np.linalg.norm(p.vel) for p in particles]

# Histograma de velocidades
plt.figure()
count, bins, _ = plt.hist(velocidades, bins=10, density=True, color='skyblue', edgecolor='black', alpha=0.6, label="Simulación")

# Curva teórica de Maxwell-Boltzmann (2D)
v_vals = np.linspace(0, max(velocidades)*1.2, 200)
m = particles[0].mass
T = T_avg

f_MB = (m / (k_B * T)) * v_vals * np.exp(-m * v_vals**2 / (2 * k_B * T))
plt.plot(v_vals, f_MB, 'r-', lw=2, label="Maxwell-Boltzmann 2D")

plt.xlabel("Velocidad (m/s)")
plt.ylabel("Probabilidad normalizada")
plt.title("Distribución de velocidades")
plt.grid(True)
plt.legend()
plt.show()

