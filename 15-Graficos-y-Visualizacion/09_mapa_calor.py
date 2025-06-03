"""
Ejercicio 9: Mapa de calor (heatmap)

Objetivo: Crear un mapa de calor para visualizar matrices de datos.

Instrucciones:
- Crea un mapa de calor que muestre la correlación entre variables.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Crear datos de ejemplo
np.random.seed(42)
datos = {
    'Temperatura': np.random.normal(25, 5, 100),
    'Humedad': np.random.normal(60, 10, 100),
    'Presión': np.random.normal(1013, 20, 100),
    'Viento': np.random.normal(15, 5, 100)
}

df = pd.DataFrame(datos)
correlacion = df.corr()

# Crear el mapa de calor
plt.figure(figsize=(8, 6))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f')
plt.title('Mapa de Calor - Correlación entre Variables Meteorológicas')
plt.show()
