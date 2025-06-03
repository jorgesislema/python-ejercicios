"""
Ejercicio 7: Gráfico con seaborn

Objetivo: Crear gráficos atractivos usando seaborn.

Instrucciones:
- Instala seaborn: pip install seaborn
- Crea un gráfico de distribución usando seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurar el estilo de seaborn
sns.set_style("whitegrid")

# Generar datos
np.random.seed(42)
datos = np.random.normal(100, 15, 1000)

# Crear el gráfico de distribución
plt.figure(figsize=(10, 6))
sns.histplot(datos, bins=30, kde=True, color='skyblue')
plt.title('Distribución de Datos con Seaborn')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
