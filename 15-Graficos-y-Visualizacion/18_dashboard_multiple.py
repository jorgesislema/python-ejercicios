"""
Ejercicio 18: Dashboard con múltiples gráficos

Objetivo: Crear un dashboard combinando diferentes tipos de visualizaciones.

Instrucciones:
- Crea un dashboard con 6 gráficos diferentes en una sola figura.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Configurar el estilo
plt.style.use('default')
sns.set_palette("husl")

# Generar datos simulados
np.random.seed(42)
fechas = pd.date_range('2023-01-01', periods=12, freq='M')
ventas = np.random.uniform(50, 150, 12)
gastos = np.random.uniform(30, 100, 12)
categorias = ['A', 'B', 'C', 'D', 'E']
valores_cat = np.random.uniform(10, 50, 5)
datos_dist = np.random.normal(100, 15, 1000)

# Crear la figura con subplots
fig = plt.figure(figsize=(16, 12))

# 1. Gráfico de líneas - Evolución temporal
ax1 = plt.subplot(2, 3, 1)
plt.plot(fechas, ventas, marker='o', label='Ventas', linewidth=2)
plt.plot(fechas, gastos, marker='s', label='Gastos', linewidth=2)
plt.title('Evolución de Ventas y Gastos')
plt.xlabel('Fecha')
plt.ylabel('Cantidad (miles €)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# 2. Gráfico de barras
ax2 = plt.subplot(2, 3, 2)
plt.bar(categorias, valores_cat, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Ventas')

# 3. Gráfico circular
ax3 = plt.subplot(2, 3, 3)
plt.pie(valores_cat, labels=categorias, autopct='%1.1f%%', startangle=90)
plt.title('Distribución por Categoría')

# 4. Histograma
ax4 = plt.subplot(2, 3, 4)
plt.hist(datos_dist, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Distribución de Datos')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# 5. Gráfico de dispersión
ax5 = plt.subplot(2, 3, 5)
x_scatter = np.random.randn(100)
y_scatter = 2 * x_scatter + np.random.randn(100)
plt.scatter(x_scatter, y_scatter, alpha=0.6, color='purple')
plt.title('Correlación X-Y')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')

# 6. Box plot
ax6 = plt.subplot(2, 3, 6)
datos_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(datos_box, labels=['Grupo 1', 'Grupo 2', 'Grupo 3'])
plt.title('Comparación de Grupos')
plt.ylabel('Valor')

# Ajustar el layout
plt.tight_layout()
plt.suptitle('Dashboard de Análisis de Datos', fontsize=16, y=0.98)
plt.show()
