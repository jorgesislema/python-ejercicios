"""
Ejercicio 4: Histograma

Objetivo: Crear un histograma para mostrar la distribución de datos.

Instrucciones:
- Crea un histograma que muestre la distribución de edades de una población.
"""

import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios de edades
np.random.seed(42)
edades = np.random.normal(35, 10, 1000)  # Media 35, desviación 10, 1000 datos

# Crear el histograma
plt.hist(edades, bins=30, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True, alpha=0.3)
plt.show()
