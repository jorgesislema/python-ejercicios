"""
Ejercicio 12: Animación con matplotlib

Objetivo: Crear una animación simple.

Instrucciones:
- Crea una animación de una función seno en movimiento.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Configurar la figura
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Animación de Función Seno')
ax.grid(True)

# Función de animación
def animate(frame):
    y = np.sin(x + frame * 0.1)
    line.set_ydata(y)
    return line,

# Crear la animación
anim = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Mostrar la animación
plt.show()

# Para guardar como GIF (opcional):
# anim.save('seno_animado.gif', writer='pillow', fps=20)
