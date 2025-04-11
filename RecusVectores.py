# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 15:16:17 2025

@author: Melissa Niño
"""

from abc import ABC, abstractmethod


class Vector(ABC):
  @abstractmethod
  def __init__(self, components):
    pass

  @abstractmethod
  def suma(self, other):
    pass

class Vector2D(Vector):
  def __init__(self, components):
    if len(components) != 2:
      raise ValueError("Un vector 2D debe tener dos componentes.")
    self.x = components[0]
    self.y = components[1]

  def suma(self, other):
    if not isinstance(other, Vector2D):
      raise TypeError("Se puede sumar un Vector2D solo con otro Vector2D")
    return Vector2D([self.x + other.x, self.y + other.y])

  def __str__(self):
    return f"({self.x}, {self.y})"


class Vector3D(Vector):
  def __init__(self, components):
    if len(components) != 3:
      raise ValueError("Un vector 3D debe tener tres componentes.")
    self.x = components[0]
    self.y = components[1]
    self.z = components[2]

  def suma(self, other):
    if not isinstance(other, Vector3D):
      raise TypeError("Se puede sumar un Vector3D solo con otro Vector3D")
    return Vector3D([self.x + other.x, self.y + other.y, self.z + other.z])

  def __str__(self):
    return f"({self.x}, {self.y}, {self.z})"
  
def suma_vectores_recursiva(vectores: Vector):
  if len(vectores) == 0:
    return None  # O lanzar una excepción, según sea apropiado
  elif len(vectores) == 1:
    return vectores[0]
  else:
    primer_vector = vectores[0]
    resto_vectores = vectores[1:]
    suma_resto = suma_vectores_recursiva(resto_vectores)
    
    if isinstance(primer_vector, Vector2D) and isinstance(suma_resto, Vector2D):
        return primer_vector.suma(suma_resto)
    elif isinstance(primer_vector, Vector3D) and isinstance(suma_resto, Vector3D):
        return primer_vector.suma(suma_resto)
    else:
        raise TypeError("Todos los vectores deben ser del mismo tipo (2D o 3D)")
        
vec1 = Vector2D([2,4])
vec2 = Vector2D([3,5])
vec3 = Vector3D([-1,4,2])
vec4 = Vector3D([-1,-3,6])

print(suma_vectores_recursiva([vec1, vec2]))
print(suma_vectores_recursiva([vec3, vec4]))