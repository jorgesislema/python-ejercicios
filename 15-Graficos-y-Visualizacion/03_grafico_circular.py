"""
Ejercicio 3: Gráfico circular (pie chart)

Objetivo: Crear un gráfico circular para mostrar proporciones.

Instrucciones:
- Crea un gráfico circular que muestre la distribución de sistemas operativos.
"""

import matplotlib.pyplot as plt

# Datos
sistemas = ['Windows', 'macOS', 'Linux', 'Otros']
porcentajes = [70, 20, 8, 2]
colores = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']

# Crear el gráfico circular
plt.pie(porcentajes, labels=sistemas, colors=colores, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Sistemas Operativos')
plt.axis('equal')  # Para que el círculo sea perfecto
plt.show()
