"""
Ejercicio 16: Gráfico de radar (spider chart)

Objetivo: Crear un gráfico de radar para comparar múltiples variables.

Instrucciones:
- Crea un gráfico de radar mostrando las habilidades de diferentes jugadores.
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo - habilidades de jugadores
categorias = ['Velocidad', 'Fuerza', 'Técnica', 'Resistencia', 'Inteligencia']
jugador1 = [8, 6, 9, 7, 8]
jugador2 = [7, 9, 6, 8, 7]

# Número de variables
N = len(categorias)

# Ángulos para cada categoría
angulos = [n / float(N) * 2 * np.pi for n in range(N)]
angulos += angulos[:1]  # Completar el círculo

# Agregar el primer valor al final para cerrar el polígono
jugador1 += jugador1[:1]
jugador2 += jugador2[:1]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))

# Plotear los datos
ax.plot(angulos, jugador1, 'o-', linewidth=2, label='Jugador 1', color='blue')
ax.fill(angulos, jugador1, alpha=0.25, color='blue')
ax.plot(angulos, jugador2, 'o-', linewidth=2, label='Jugador 2', color='red')
ax.fill(angulos, jugador2, alpha=0.25, color='red')

# Configurar las etiquetas
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(categorias)
ax.set_ylim(0, 10)
ax.set_title('Comparación de Habilidades - Gráfico de Radar', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
ax.grid(True)

plt.show()
