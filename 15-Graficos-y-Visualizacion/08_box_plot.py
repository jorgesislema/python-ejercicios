"""
Ejercicio 8: Box plot (diagrama de caja)

Objetivo: Crear un diagrama de caja para analizar la distribución de datos.

Instrucciones:
- Crea un box plot para comparar las calificaciones de diferentes materias.
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos simulados de calificaciones
np.random.seed(42)
matematicas = np.random.normal(7.5, 1.5, 100)
ciencias = np.random.normal(8.0, 1.2, 100)
historia = np.random.normal(7.0, 1.8, 100)
literatura = np.random.normal(7.8, 1.3, 100)

datos = [matematicas, ciencias, historia, literatura]
etiquetas = ['Matemáticas', 'Ciencias', 'Historia', 'Literatura']

# Crear el box plot
plt.boxplot(datos, labels=etiquetas)
plt.title('Distribución de Calificaciones por Materia')
plt.ylabel('Calificación')
plt.grid(True, alpha=0.3)
plt.show()
