"""
EJERCICIO 66: Tecnología y Robótica ASCII

Objetivo:
- Crear figuras ASCII de robots y tecnología avanzada
- Practicar la representación de elementos futuristas
- Explorar el mundo de la inteligencia artificial y automatización

Conceptos a practicar:
- Representación de formas mecánicas y tecnológicas
- Uso de caracteres para simular circuitos y componentes
- Creación de interfaces robóticas
- Diseño de elementos de ciencia ficción
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🤖 TECNOLOGÍA Y ROBÓTICA ASCII 🤖")
    print("="*50)
    print("0. Salir")
    print("1. Robot humanoide 🤖")
    print("2. Drone autónomo 🚁")
    print("3. Brazo robótico 🦾")
    print("4. Inteligencia artificial 🧠")
    print("5. Circuito integrado 💾")
    print("6. Robot industrial 🏭")
    print("7. Coche autónomo 🚗")
    print("8. Casa inteligente 🏠")
    print("9. Laboratorio de robótica 🔬")
    print("="*50)

def dibujar_robot_humanoide():
    print("\n🤖 ROBOT HUMANOIDE")
    print("-" * 30)
    robot = """
    ╔══════════════════════════╗
    ║ ANDROIDE SERIE RX-2000   ║
    ╚══════════════════════════╝
    
         ╔═══════════╗
         ║ ● LED ● ║ ← Sensores
         ║    ▼     ║   visuales
         ║   ___    ║
         ╚═════╤═════╝
    ╔══════════╧══════════╗
    ║ ⚡ PROCESADOR ⚡   ║ ← CPU
    ║ 🔋 BATERÍA 98% 🔋   ║   cuántico
    ╠══════════════════════╣
    ║ 🦾         🦾      ║ ← Brazos
    ║   ╲       ╱        ║   articulados
    ║    ╲_____╱         ║
    ║      |||           ║ ← Torso
    ║      |||           ║   blindado
    ║    ╱─────╲         ║
    ║   ╱ 🦵 🦵 ╲        ║ ← Piernas
    ║  ╱   |||   ╲       ║   hidráulicas
    ╚═╱════|||════╲══════╝
        🤖 ║ 🤖
    
    Estado: ACTIVO | Misión: ASISTENCIA
    """
    print(robot)
    print("Compañero artificial con inteligencia avanzada 🧠")

def dibujar_drone_autonomo():
    print("\n🚁 DRONE AUTÓNOMO")
    print("-" * 30)
    drone = """
    ╔══════════════════════════╗
    ║ DRON DE VIGILANCIA X-400 ║
    ╚══════════════════════════╝
    
    ⚙️──⚙️           ⚙️──⚙️
     ╲ │             │ ╱
      ╲│             │╱
    ┌───┴─────────────┴───┐
    │ 📡 GPS  📱 COMM 📡 │ ← Antenas
    │                     │   comunicación
    │ 📹 CAM  🧠 AI  📊  │ ← Cámara HD
    │                     │   IA integrada
    │ 🔋 BATERÍA: 85%     │ ← Sistema
    │ ⚡ ESTADO: PATRULLA  │   energético
    └───┬─────────────┬───┘
      ╱│             │╲
     ╱ │             │ ╲
    ⚙️──⚙️           ⚙️──⚙️
    
    Altitud: 150m | Velocidad: 45 km/h
    Misión: Reconocimiento área 🗺️
    """
    print(drone)
    print("Ojo electrónico que vigila desde las alturas 👁️")

def dibujar_brazo_robotico():
    print("\n🦾 BRAZO ROBÓTICO")
    print("-" * 30)
    brazo = """
    ╔══════════════════════════╗
    ║ BRAZO INDUSTRIAL RB-6000 ║
    ╚══════════════════════════╝
    
    🏭 BASE FIJA 🏭
    ████████████████
    ║ ⚡ MOTOR 1 ⚡ ║ ← Rotación
    ╚══════╤═══════╝   base 360°
           │
           ├─── ⚙️ ARTICULACIÓN 1
           │
    ╔══════╧═══════╗
    ║ ⚡ MOTOR 2 ⚡ ║ ← Elevación
    ╚══════╤═══════╝   brazo ±90°
           │
           ├─── ⚙️ ARTICULACIÓN 2
           │
    ╔══════╧═══════╗
    ║ ⚡ MOTOR 3 ⚡ ║ ← Extensión
    ╚══════╤═══════╝   antebrazo
           │
           ├─── ⚙️ ARTICULACIÓN 3
           │
         ╔═╧═╗
         ║🤏 ║ ← PINZA NEUMÁTICA
         ║ ⚡ ║   Fuerza: 500N
         ╚═══╝
    
    Precisión: ±0.1mm | Carga: 25kg
    """
    print(brazo)
    print("Extensión mecánica de precisión milimétrica 🎯")

def dibujar_inteligencia_artificial():
    print("\n🧠 INTELIGENCIA ARTIFICIAL")
    print("-" * 30)
    ia = """
    ╔══════════════════════════════╗
    ║ SISTEMA NEURAL AVANZADO v3.7 ║
    ╚══════════════════════════════╝
    
         🧠 RED NEURONAL 🧠
    ○─○─○─○─○  ○─○─○─○─○  ○─○─○─○─○
    │╲│╱│╲│╱│  │╲│╱│╲│╱│  │╲│╱│╲│╱│
    ○─○─○─○─○  ○─○─○─○─○  ○─○─○─○─○
    │╱│╲│╱│╲│  │╱│╲│╱│╲│  │╱│╲│╱│╲│
    ○─○─○─○─○  ○─○─○─○─○  ○─○─○─○─○
     INPUT     HIDDEN     OUTPUT
    
    ╔══════════════════════════════╗
    ║ 💾 MEMORIA: 500 TB           ║
    ║ ⚡ PROCESAMIENTO: 10^18 ops  ║
    ║ 🔍 ANÁLISIS: Tiempo real     ║
    ║ 🎯 PRECISIÓN: 99.7%          ║
    ║ 📊 APRENDIZAJE: Continuo     ║
    ╚══════════════════════════════╝
    
    FUNCIONES ACTIVAS:
    ✅ Reconocimiento de patrones
    ✅ Procesamiento de lenguaje natural
    ✅ Toma de decisiones autónomas
    """
    print(ia)
    print("Mente artificial capaz de aprender y razonar 🎓")

def dibujar_circuito_integrado():
    print("\n💾 CIRCUITO INTEGRADO")
    print("-" * 30)
    circuito = """
    ╔════════════════════════════════╗
    ║ MICROCHIP CUÁNTICO QC-2025     ║
    ╚════════════════════════════════╝
    
    ┌────────────────────────────────┐
    │ ╔══╗ ╔══╗ ╔══╗ ╔══╗ ╔══╗    │
    │ ║⚡║ ║⚡║ ║⚡║ ║⚡║ ║⚡║    │ ← Núcleos
    │ ╚══╝ ╚══╝ ╚══╝ ╚══╝ ╚══╝    │   procesamiento
    │ ═══════════════════════════    │
    │ ┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃┃    │ ← Buses
    │ ═══════════════════════════    │   datos
    │ 💾 CACHÉ L1: 64KB              │
    │ 💾 CACHÉ L2: 2MB               │ ← Memoria
    │ 💾 CACHÉ L3: 16MB              │   caché
    │ ═══════════════════════════    │
    │ ⚡ FRECUENCIA: 4.8 GHz         │
    │ 🌡️ TEMPERATURA: 35°C          │ ← Monitoreo
    │ 🔋 VOLTAJE: 1.2V              │   sistema
    └────────────────────────────────┘
    
    Arquitectura: 3nm | Transistores: 50B
    """
    print(circuito)
    print("Cerebro electrónico en chip de silicio 🔬")

def dibujar_robot_industrial():
    print("\n🏭 ROBOT INDUSTRIAL")
    print("-" * 30)
    robot_industrial = """
    ╔════════════════════════════════╗
    ║ ROBOT ENSAMBLAJE AUTO-3000     ║
    ╚════════════════════════════════╝
    
    🏭 LÍNEA DE PRODUCCIÓN 🏭
    ════════════════════════════════
    
         🤖 ESTACIÓN 1 🤖
    ┌─────────────────────────────┐
    │ SOLDADURA LÁSER ⚡         │ ← Proceso
    │ ╔═══╗  ╔═══╗  ╔═══╗       │   automatizado
    │ ║ 🔥 ║  ║ 🔥 ║  ║ 🔥 ║       │
    │ ╚═══╝  ╚═══╝  ╚═══╝       │
    │ ├─🦾─┤  ├─🦾─┤  ├─🦾─┤     │ ← Brazos
    └─────────────────────────────┘   múltiples
    
         ⬇️ CINTA TRANSPORTADORA ⬇️
    ╔═══════════════════════════════╗
    ║ 🔩🔧🔩 → → → 🔩🔧🔩 → → → ║ ← Piezas
    ╚═══════════════════════════════╝   en movimiento
    
    ESTADÍSTICAS:
    📊 Productividad: 1200 pzas/hora
    ⚡ Eficiencia: 98.5%
    🎯 Precisión: ±0.05mm
    """
    print(robot_industrial)
    print("Automatización masiva de procesos industriales ⚙️")

def dibujar_coche_autonomo():
    print("\n🚗 COCHE AUTÓNOMO")
    print("-" * 30)
    coche = """
    ╔════════════════════════════════╗
    ║ VEHÍCULO AUTÓNOMO NIVEL 5      ║
    ╚════════════════════════════════╝
    
    📡 SENSORES Y CÁMARAS 📡
    
    ╔══════════════════════════════╗
    ║ 📹 CAM  🎯 LIDAR  📱 5G  🛰️ ║ ← Sistemas
    ║                              ║   percepción
    ║  👥     🖥️ AI     ⚙️      ║ ← Pasajeros
    ║         PILOTO             ║   e IA
    ║  💺     AUTOMÁTICO   💺    ║
    ╚═════════════════════════════╝
    ⚫ 🔋              🔋 ⚫
    
    ESTADO DEL VIAJE:
    🗺️ Ruta: Optimizada GPS
    🎯 Destino: 15.3 km
    ⏱️ ETA: 18 minutos
    ⚡ Batería: 78%
    🚦 Semáforos: Sincronizado
    👥 Peatones: Detectados
    🚙 Tráfico: Fluido
    
    Modo: CONDUCCIÓN AUTÓNOMA ✅
    """
    print(coche)
    print("Transporte sin conductor con IA avanzada 🧠")

def dibujar_casa_inteligente():
    print("\n🏠 CASA INTELIGENTE")
    print("-" * 30)
    casa = """
    ╔════════════════════════════════╗
    ║ SMART HOME SISTEMA v4.2        ║
    ╚════════════════════════════════╝
    
           🛰️ IoT CONECTADO 🛰️
    ╔══════════════════════════════════╗
    ║ 🌡️23°C  💡AUTO  🔐SEGURO  📱APP ║ ← Panel
    ╠══════════════════════════════════╣   control
    ║ 🏠                              ║
    ║ COCINA    📺 SALA    🛏️ DORMIT ║
    ║ 🔥 AUTO   📱 ALEXA   🌡️ 22°C   ║ ← Zonas
    ║ ⏰ 18:30  🔊 ON      💡 DIM     ║   inteligentes
    ║                                 ║
    ║ 🚿 BAÑO   🏃‍♂️ GYM    🌿 JARDÍN  ║
    ║ 💧 38°C   💪 ACTIVO  💧 RIEGO   ║
    ║ 💡 AUTO   🎵 MUSIC   ⏰ AUTO    ║
    ╚═════════════════════════════════╝
    
    AUTOMATIZACIONES ACTIVAS:
    ✅ Climatización inteligente
    ✅ Iluminación adaptativa
    ✅ Seguridad perimetral
    ✅ Gestión energética
    """
    print(casa)
    print("Hogar conectado que se adapta a tus necesidades 🎯")

def dibujar_laboratorio_robotica():
    print("\n🔬 LABORATORIO DE ROBÓTICA")
    print("-" * 30)
    laboratorio = """
    ╔════════════════════════════════════╗
    ║ LABORATORIO DE IA Y ROBÓTICA       ║
    ╚════════════════════════════════════╝
    
    🔬 ÁREA DE DESARROLLO 🔬
    ┌────────────────────────────────────┐
    │ MESA 1: PROTOTIPADO               │
    │ 🤖 ⚡ 🔧 🔬 💾 🖥️ 📱            │ ← Prototipos
    │                                   │   desarrollo
    │ MESA 2: PROGRAMACIÓN IA           │
    │ 💻 🧠 📊 🎯 ⚙️ 📈 🔍            │ ← Algoritmos
    │                                   │   aprendizaje
    │ MESA 3: PRUEBAS                   │
    │ 🎮 📹 🎯 ⏱️ 📊 ✅ ❌            │ ← Testing
    └────────────────────────────────────┘   validación
    
    👨‍🔬 EQUIPO DE INVESTIGACIÓN 👩‍🔬
    ┌────────────────────────────────────┐
    │ Dr. GARCÍA    - JEFE PROYECTO      │
    │ 🤖 Ing. LÓPEZ  - ROBÓTICA         │ ← Especialistas
    │ 🧠 Dr. MARTÍN  - IA AVANZADA      │   multidisciplinar
    │ ⚡ Ing. PÉREZ  - ELECTRÓNICA      │
    └────────────────────────────────────┘
    
    PROYECTOS ACTIVOS: 12 | PRESUPUESTO: €2.5M
    """
    print(laboratorio)
    print("Centro de innovación donde nace el futuro 🚀")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar el futuro tecnológico! 🤖")
            break
        elif opcion == "1":
            dibujar_robot_humanoide()
        elif opcion == "2":
            dibujar_drone_autonomo()
        elif opcion == "3":
            dibujar_brazo_robotico()
        elif opcion == "4":
            dibujar_inteligencia_artificial()
        elif opcion == "5":
            dibujar_circuito_integrado()
        elif opcion == "6":
            dibujar_robot_industrial()
        elif opcion == "7":
            dibujar_coche_autonomo()
        elif opcion == "8":
            dibujar_casa_inteligente()
        elif opcion == "9":
            dibujar_laboratorio_robotica()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
