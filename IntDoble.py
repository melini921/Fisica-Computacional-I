# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 11:37:40 2025

@author: Melissa Niño
"""

import numpy as np

a = -100.0
b = 35.0
c = -20.0
d = 200.0

nx = 10000
ny = 10000

def trapecio_doble(f, a, b, c, d, nx, ny):
 

  hx = (b - a) / nx
  hy = (d - c) / ny

  suma = 0.0
  for i in range(nx + 1):
    for j in range(ny + 1):
      x = a + i * hx
      y = c + j * hy
      if (i == 0 or i == nx) and (j == 0 or j == ny):
        w = 1.0
      elif (i == 0 or i == nx) or (j == 0 or j == ny):
        w = 2.0
      else:
        w = 4.0
      suma += w * f(x, y)

  return suma * hx * hy / 4.0

def f(x, y):
  return x**2 + y**2


resultado_trapecio = trapecio_doble(f, a, b, c, d, nx, ny)

print("Resultado del método del trapecio:", resultado_trapecio)


def simpson_doble(f, a, b, c, d, nx, ny):


  hx = (b - a) / nx
  hy = (d - c) / ny

  suma = 0.0
  for i in range(nx + 1):
    for j in range(ny + 1):
      x = a + i * hx
      y = c + j * hy
      if (i == 0 or i == nx) and (j == 0 or j == ny):
        w = 1.0
      elif (i == 0 or i == nx) or (j == 0 or j == ny):
        if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
          w = 4.0
        else:
          w = 2.0
      else:
        if i % 2 == 0 and j % 2 == 0:
          w = 16.0
        elif (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
          w = 4.0
        else:
          w = 1.0
      suma += w * f(x, y)

  return suma * hx * hy / 9.0

def f(x, y):
  return x**2 + y**2


resultado_simpson = simpson_doble(f, a, b, c, d, nx, ny)

print("Resultado de la regla de Simpson:", resultado_simpson)

