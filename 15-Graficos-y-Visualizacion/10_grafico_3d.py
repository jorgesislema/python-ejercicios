"""
Ejercicio 10: Gráfico 3D

Objetivo: Crear gráficos tridimensionales.

Instrucciones:
- Crea un gráfico 3D de superficie usando matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Crear datos para la superficie
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Crear el gráfico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear la superficie
superficie = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfico 3D - Superficie')

# Agregar barra de colores
fig.colorbar(superficie)
plt.show()
