"""
Ejercicio 15: Gráfico polar

Objetivo: Crear un gráfico en coordenadas polares.

Instrucciones:
- Crea un gráfico polar mostrando datos en forma circular.
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos para el gráfico polar
theta = np.linspace(0, 2*np.pi, 100)
r = 1 + 0.5 * np.sin(5*theta)

# Crear el gráfico polar
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

# Plotear los datos
ax.plot(theta, r, 'b-', linewidth=2)
ax.fill(theta, r, alpha=0.3, color='blue')

# Configurar el gráfico
ax.set_title('Gráfico Polar - Rosa de 5 Pétalos', pad=20)
ax.set_ylim(0, 2)
ax.grid(True)

plt.show()
