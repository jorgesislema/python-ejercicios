"""
Ejercicio 6: Subgráficos (subplots)

Objetivo: Crear múltiples gráficos en una sola figura.

Instrucciones:
- Crea una figura con 4 subgráficos mostrando diferentes tipos de gráficos.
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
categorias = ['A', 'B', 'C', 'D']
valores = [23, 45, 56, 78]

# Crear subgráficos
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

# Gráfico 1: Línea
ax1.plot(x, y1, 'b-', label='sin(x)')
ax1.set_title('Función Seno')
ax1.grid(True)

# Gráfico 2: Línea
ax2.plot(x, y2, 'r-', label='cos(x)')
ax2.set_title('Función Coseno')
ax2.grid(True)

# Gráfico 3: Barras
ax3.bar(categorias, valores, color='green')
ax3.set_title('Gráfico de Barras')

# Gráfico 4: Dispersión
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
ax4.scatter(x_scatter, y_scatter, alpha=0.6)
ax4.set_title('Gráfico de Dispersión')

plt.tight_layout()
plt.show()
