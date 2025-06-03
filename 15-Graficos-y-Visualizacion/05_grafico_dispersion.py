"""
Ejercicio 5: Gráfico de dispersión (scatter plot)

Objetivo: Crear un gráfico de dispersión para mostrar correlación entre variables.

Instrucciones:
- Crea un gráfico de dispersión que muestre la relación entre horas de estudio y calificaciones.
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos simulados
np.random.seed(42)
horas_estudio = np.random.uniform(0, 10, 50)
calificaciones = 5 + 0.8 * horas_estudio + np.random.normal(0, 1, 50)

# Crear el gráfico de dispersión
plt.scatter(horas_estudio, calificaciones, alpha=0.6, color='purple')
plt.title('Relación entre Horas de Estudio y Calificaciones')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación')
plt.grid(True, alpha=0.3)
plt.show()
