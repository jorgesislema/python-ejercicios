"""
Ejercicio 13: Gráfico de violín

Objetivo: Crear un gráfico de violín para mostrar distribuciones de datos.

Instrucciones:
- Crea un gráfico de violín comparando diferentes grupos de datos.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Generar datos simulados
np.random.seed(42)
grupos = ['Grupo A', 'Grupo B', 'Grupo C', 'Grupo D']
datos = []

for i, grupo in enumerate(grupos):
    valores = np.random.normal(10 + i*2, 2 + i*0.5, 100)
    for valor in valores:
        datos.append({'Grupo': grupo, 'Valor': valor})

df = pd.DataFrame(datos)

# Crear el gráfico de violín
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='Grupo', y='Valor', palette='viridis')
plt.title('Distribución de Valores por Grupo (Gráfico de Violín)')
plt.ylabel('Valor')
plt.show()
