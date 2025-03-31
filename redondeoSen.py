# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 11:38:43 2025

@author: Melissa Niño
"""

import math

def taylor_sin(x, terms):
    
    result = 0
    for n in range(terms):
        result += (((-1)**n) * (x**(2*n+1))) / math.factorial(2*n+1)
    return result

# True value of sin(45) using math.sin
x = 270.0  # Input in degrees
x_rad = math.radians(x)  # Convert to radians for math.sin
true_value = math.sin(x_rad)
print(f"True value of sin({x} degrees): {true_value}")


for terms in [2, 4, 6, 8, 10, 12, 14]:
    approx = taylor_sin(x_rad, terms)  # Use radians for the approximation
    truncation_error = true_value - approx
    print(f"Terms: {terms}, Approximation: {approx}, Truncation Error: {truncation_error}")