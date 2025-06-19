#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 87: Inventos que Cambiaron el Mundo ASCII
===================================================

Objetivo:
- Crear representaciones de inventos revolucionarios usando ASCII
- Explorar la historia de la innovación humana
- Comprender el impacto de la tecnología en la sociedad

Conceptos aplicados:
- Historia de la tecnología
- Innovación humana
- Revolución industrial
- Impacto social de los inventos
"""

import time
import random

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("💡 GENERADOR DE INVENTOS REVOLUCIONARIOS ASCII 💡")
    print("="*60)
    print("1. 💡 Bombilla eléctrica")
    print("2. 📞 Teléfono")
    print("3. 🚗 Automóvil")
    print("4. ✈️ Avión")
    print("5. 📺 Televisión")
    print("6. 💻 Computadora")
    print("7. 🌐 Internet")
    print("8. 📱 Teléfono móvil")
    print("9. 🧬 Microscopio")
    print("0. 🚪 Salir")
    print("-"*60)

def bombilla():
    """Crea una bombilla eléctrica de Edison"""
    print("💡 BOMBILLA ELÉCTRICA 💡")
    print("Thomas Edison (1879) - Iluminó el mundo moderno")
    print()
    
    bombilla_ascii = [
        "        ⚡⚡⚡⚡⚡⚡⚡",
        "      ⚡⚡⚡⚡⚡⚡⚡⚡⚡",
        "     ⚡⚡             ⚡⚡",
        "    ⚡⚡               ⚡⚡",
        "   ⚡⚡                 ⚡⚡",
        "  ⚡⚡     🔥🔥🔥🔥🔥     ⚡⚡",
        " ⚡⚡      🔥🔥🔥🔥🔥🔥     ⚡⚡",
        "⚡⚡       🔥🔥💡🔥🔥      ⚡⚡",
        " ⚡⚡      🔥🔥🔥🔥🔥🔥     ⚡⚡",
        "  ⚡⚡     🔥🔥🔥🔥🔥     ⚡⚡",
        "   ⚡⚡                 ⚡⚡",
        "    ⚡⚡               ⚡⚡",
        "     ⚡⚡             ⚡⚡",
        "      ⚡⚡⚡⚡⚡⚡⚡⚡⚡",
        "        ████████████",
        "        ████████████",
        "         ||      ||",