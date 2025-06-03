"""
Ejercicio 17: Gráfico de burbujas

Objetivo: Crear un gráfico de burbujas para mostrar tres dimensiones de datos.

Instrucciones:
- Crea un gráfico de burbujas donde el tamaño de la burbuja represente una tercera variable.
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos simulados - países
np.random.seed(42)
paises = ['País A', 'País B', 'País C', 'País D', 'País E', 'País F', 'País G', 'País H']
pib_per_capita = np.random.uniform(20000, 80000, len(paises))  # PIB per cápita
esperanza_vida = np.random.uniform(65, 85, len(paises))        # Esperanza de vida
poblacion = np.random.uniform(5, 150, len(paises))             # Población (millones)

# Crear el gráfico de burbujas
plt.figure(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(paises)))

for i, pais in enumerate(paises):
    plt.scatter(pib_per_capita[i], esperanza_vida[i], 
               s=poblacion[i]*20,  # Tamaño de la burbuja
               alpha=0.6, 
               color=colors[i],
               label=pais)

plt.xlabel('PIB per cápita (USD)')
plt.ylabel('Esperanza de vida (años)')
plt.title('Relación entre PIB, Esperanza de Vida y Población\n(Tamaño de burbuja = Población)')
plt.grid(True, alpha=0.3)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
