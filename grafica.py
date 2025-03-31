# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 07:50:43 2025

@author: Melissa Niño
"""

from astroquery.simbad import Simbad


#Configurar columnas a obtener
Simbad.add_votable_fields('distance', 'sptype', 'flux(V)', 'flux(B)')

#Consultar datos de la estrella Betelgeuse
result = Simbad.query_object("Betelgeuse")

#Convertir a DataFrame
df = result.to_pandas()
print(df)

import matplotlib.pyplot as plt

# Datos de las estrellas
estrellas = [
    {"nombre": "Sirio", "distancia_AL": 8.6, "longitud_onda_nm": 450},  
    {"nombre": "Canopus", "distancia_AL": 310, "longitud_onda_nm": 530}, 
    {"nombre": "Vega", "distancia_AL": 25, "longitud_onda_nm": 480}, 
    {"nombre": "Betelgeuse", "distancia_AL": 642, "longitud_onda_nm": 700}, 
    {"nombre": "Rigel", "distancia_AL": 860, "longitud_onda_nm": 450}, 
    {"nombre": "Altair", "distancia_AL": 16.7, "longitud_onda_nm": 430}, 
    {"nombre": "Antares", "distancia_AL": 550, "longitud_onda_nm": 700}, 
    {"nombre": "Arcturus", "distancia_AL": 36.7, "longitud_onda_nm": 600}, 
    {"nombre": "Aldebarán", "distancia_AL": 65, "longitud_onda_nm": 625}, 
    {"nombre": "Procyon", "distancia_AL": 11.5, "longitud_onda_nm": 530} 
]


for estrella in estrellas:
    print(f"{estrella['nombre']}: {estrella['distancia_AL']} AL, {estrella['longitud_onda_nm']} nm")


nombres = [estrella['nombre'] for estrella in estrellas]
distancias = [estrella['distancia_AL'] for estrella in estrellas]
longitudes_onda = [estrella['longitud_onda_nm'] for estrella in estrellas]


colores = ['blue' if lo < 480 else 
           'lightblue' if lo < 530 else
           'yellow' if lo < 600 else
           'orange' if lo < 650 else
           'red' for lo in longitudes_onda]


plt.figure(figsize=(10, 6))
plt.scatter(distancias, longitudes_onda, s=100, c=colores, edgecolors="black")  


plt.xlabel('Distancia (AL)')
plt.ylabel('Longitud de Onda (nm)')
plt.title('Longitud de Onda de Estrellas vs. Distancia')


for i, nombre in enumerate(nombres):
    plt.annotate(nombre, (distancias[i], longitudes_onda[i]), 
                 textcoords="offset points", xytext=(5, 5), ha='center')


plt.grid(True)
plt.show()
