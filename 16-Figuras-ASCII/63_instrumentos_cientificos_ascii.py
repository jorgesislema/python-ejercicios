"""
EJERCICIO 63: Instrumentos Científicos ASCII

Objetivo:
- Crear figuras ASCII de instrumentos y equipos científicos
- Practicar la representación de herramientas de investigación
- Explorar el mundo de la ciencia y tecnología

Conceptos a practicar:
- Representación de instrumentos de precisión
- Uso de símbolos científicos y técnicos
- Creación de laboratorios y equipos
- Diseño de interfaces científicas
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🔬 INSTRUMENTOS CIENTÍFICOS ASCII 🔬")
    print("="*50)
    print("0. Salir")
    print("1. Microscopio 🔬")
    print("2. Telescopio 🔭")
    print("3. Balanza de precisión ⚖️")
    print("4. Probetas de laboratorio 🧪")
    print("5. Osciloscopio 📊")
    print("6. Centrifugadora 🌀")
    print("7. Espectrofotómetro 🌈")
    print("8. Termómetro digital 🌡️")
    print("9. ADN secuenciador 🧬")
    print("="*50)

def dibujar_microscopio():
    print("\n🔬 MICROSCOPIO")
    print("-" * 30)
    microscopio = """
    ╔══════════════════════╗
    ║ MICROSCOPIO ÓPTICO   ║
    ╚══════════════════════╝
    
         ╔═════╗ 👁️
         ║ 10x ║ ← Ocular
         ╚══╤══╝
            │
    ╔═══════╧═══════╗
    ║ ○ 4x  ○ 10x  ║ ← Objetivos
    ║ ○ 40x ○ 100x ║
    ╚═══════╤═══════╝
            │
        ╔═══╧═══╗
        ║ 🦠🦠🦠 ║ ← Muestra
        ╚═══════╝
    ╔═══════════════════╗
    ║ 💡 ILUMINACIÓN    ║
    ║    ⚪ ⚪ ⚪       ║
    ╚═══════════════════╝
    
    Aumento: 40x - 1000x 🔍
    """
    print(microscopio)
    print("Ventana al mundo microscópico invisible 🦠")

def dibujar_telescopio():
    print("\n🔭 TELESCOPIO")
    print("-" * 30)
    telescopio = """
    🌟 OBSERVATORIO ASTRONÓMICO 🌟
    
           ⭐ ⭐ ⭐ ⭐
             ╱
            ╱ 🔭
           ╱________
          ╱ ○ ○ ○ ○ ╲
         ╱ REFRACTOR  ╲
        ╱______________╲
       ╱                ╲
      ╱ ◯ LENTE 200mm ◯ ╲
     ╱____________________╲
    ╱ MONTURA ECUATORIAL  ╲
    ║ ⚙️ RA: 15°/h ⚙️     ║
    ║ ⚙️ DEC: ±90° ⚙️     ║
    ╚══════════════════════╝
         ╱│╲  ╱│╲  ╱│╲
    
    Observación: Galaxias y nebulosas 🌌
    """
    print(telescopio)
    print("Explorador del cosmos y las profundidades estelares ✨")

def dibujar_balanza_precision():
    print("\n⚖️ BALANZA DE PRECISIÓN")
    print("-" * 30)
    balanza = """
    ╔═══════════════════════════╗
    ║ BALANZA ANALÍTICA         ║
    ║ Precisión: 0.0001g        ║
    ╚═══════════════════════════╝
    
        ╔═══╗     ╔═══╗
        ║ ● ║     ║ ● ║
        ╚═╤═╝     ╚═╤═╝
          │         │
      ────┴─── = ───┴────
     ╱         ╲ ╱         ╲
    ╱   0.0000g ╲ 0.1234g  ╲
    ╲___________╱╲___________╱
           │         │
           └────╤────┘
    ╔═══════════╧═══════════╗
    ║ [TARA] [CAL] [PRINT]  ║
    ║                       ║
    ║  📊 0.1234 ± 0.0001g  ║
    ╚═══════════════════════╝
    
    Aplicación: Química analítica ⚗️
    """
    print(balanza)
    print("Medición ultra-precisa de masas mínimas 📏")

def dibujar_probetas_laboratorio():
    print("\n🧪 PROBETAS DE LABORATORIO")
    print("-" * 30)
    probetas = """
    ╔═══ MATERIAL VOLUMÉTRICO ═══╗
    
    ╱─╲   ╱─╲   ╱─╲   ╱─╲
   ╱ 🔴 ╲ ╱ 🟡 ╲ ╱ 🔵 ╲ ╱ 🟢 ╲
  ╱ 250ml╲ 500ml╲ 100ml╲ 1L  ╲
 ╱ ━━━━━ ╲━━━━━╲━━━━━╲━━━━━╲
 ║   25  ║  50  ║  10  ║ 100 ║
 ║ ━━━━━ ║━━━━━ ║━━━━━ ║━━━━━║
 ║   20  ║  40  ║   8  ║  80 ║
 ║ ━━━━━ ║━━━━━ ║━━━━━ ║━━━━━║
 ║   15  ║  30  ║   6  ║  60 ║
 ║ ■■■■■ ║■■■■■ ║■■■■■ ║■■■■■║
 ║ ■■■■■ ║■■■■■ ║■■■■■ ║■■■■■║
 ╚═══════╩═══════╩═══════╩═════╝
 
 Reactivos: HCl, NaOH, H₂SO₄, H₂O
 """
    print(probetas)
    print("Medición precisa de volúmenes en química ⚗️")

def dibujar_osciloscopio():
    print("\n📊 OSCILOSCOPIO")
    print("-" * 30)
    osciloscopio = """
    ╔══════════════════════════════╗
    ║ OSCILOSCOPIO DIGITAL 100MHz  ║
    ╠══════════════════════════════╣
    ║ ┌──────────────────────────┐ ║
    ║ │ ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿ │ ║
    ║ │ ∿     ∿     ∿     ∿    │ ║
    ║ │   ∿ ∿   ∿ ∿   ∿ ∿     │ ║
    ║ │  ┬───┬───┬───┬───┬───  │ ║
    ║ │  │   │   │   │   │     │ ║
    ║ └──────────────────────────┘ ║
    ║                              ║
    ║ CH1: 2V/div  TIME: 1ms/div   ║
    ║ [▲] [▼] [◀] [▶] [TRIG] [RUN] ║
    ╚══════════════════════════════╝
    
    Función: Análisis señales eléctricas ⚡
    """
    print(osciloscopio)
    print("Visualizador de ondas y señales eléctricas 📈")

def dibujar_centrifugadora():
    print("\n🌀 CENTRIFUGADORA")
    print("-" * 30)
    centrifugadora = """
    ╔═══════════════════════════╗
    ║ CENTRÍFUGA DE MESA        ║
    ║ Max: 15,000 RPM           ║
    ╚═══════════════════════════╝
         ╔═══════════════╗
         ║ [●] [START]   ║
         ║     [STOP]    ║
         ║ RPM: 12,000   ║
         ║ TIME: 05:30   ║
         ╚═══════════════╝
    ╔═══════════════════════════╗
    ║      🔄 ROTOR 🔄         ║
    ║   🧪     🧪     🧪      ║
    ║     🧪  🔄  🧪         ║
    ║   🧪     🧪     🧪      ║
    ║                           ║
    ║ ████████████████████████ ║
    ╚═══════════════════════════╝
    
    Separación: Densidad diferencial 📊
    """
    print(centrifugadora)
    print("Separador de componentes por fuerza centrífuga 💫")

def dibujar_espectrofotometro():
    print("\n🌈 ESPECTROFOTÓMETRO")
    print("-" * 30)
    espectrofotometro = """
    ╔══════════════════════════════╗
    ║ ESPECTROFOTÓMETRO UV-VIS     ║
    ╚══════════════════════════════╝
    
    💡 ─→ 🔍 ─→ 🧪 ─→ 🔍 ─→ 📊
    Fuente  Mono  Muestra  Detector
    
    ╔══════════════════════════════╗
    ║ λ (nm): 280  520  650  750   ║
    ║                              ║
    ║ ┌────────────────────────┐   ║
    ║ │ Abs: 0.854 ± 0.002    │   ║
    ║ │ 🔴██🟡██🟢██🔵██    │   ║
    ║ │ ▲      ▲      ▲       │   ║
    ║ │ │      │      │       │   ║
    ║ └────────────────────────┘   ║
    ║                              ║
    ║ [SCAN] [MEAS] [CAL] [PRINT]  ║
    ╚══════════════════════════════╝
    
    Análisis: Concentración molecular 🧬
    """
    print(espectrofotometro)
    print("Analizador de absorción de luz por moléculas 💡")

def dibujar_termometro_digital():
    print("\n🌡️ TERMÓMETRO DIGITAL")
    print("-" * 30)
    termometro = """
    ╔══════════════════════════╗
    ║ TERMÓMETRO INFRARROJO    ║
    ╚══════════════════════════╝
    
         ╔═══════════╗
         ║  🌡️ 36.7°C ║
         ║           ║
         ║ MAX: 42.1 ║
         ║ MIN: 35.2 ║
         ║ AVG: 36.8 ║
         ╚══════╤════╝
                │
        ╔═══════╧═══════╗
        ║ ● SENSOR IR ● ║
        ║  ············ ║ ← Radiación
        ║ 📏 Distancia  ║   térmica
        ║    5-15 cm    ║
        ╚═══════════════╝
         [ON] [°C/°F] [MEM]
    
    Precisión: ±0.1°C 📊
    Rango: -20°C a 500°C 🔥
    """
    print(termometro)
    print("Medidor sin contacto de temperatura corporal 🩺")

def dibujar_secuenciador_adn():
    print("\n🧬 ADN SECUENCIADOR")
    print("-" * 30)
    secuenciador = """
    ╔═══════════════════════════════╗
    ║ SECUENCIADOR DE ADN           ║
    ║ Tecnología: Sanger/NGS       ║
    ╚═══════════════════════════════╝
    
    🧬 ─→ ⚗️ ─→ 🌡️ ─→ ⚡ ─→ 💻
    ADN   PCR   Térm   Electr  Datos
    
    ╔═══════════════════════════════╗
    ║ Muestra: Homo sapiens chr.21  ║
    ║                               ║
    ║ A T G C G C T A G C A T G C   ║
    ║ ████▓▓▓▓████▓▓▓▓████▓▓▓▓     ║
    ║ 🔴🔵🟢🟡🟢🟡🔴🔵🟢🟡🔵🔴🟢🟡 ║
    ║                               ║
    ║ Longitud: 1,247 pb            ║
    ║ Calidad: Q30+ (99.9%)         ║
    ║ [ANALIZAR] [BLAST] [EXPORTAR] ║
    ╚═══════════════════════════════╝
    
    Función: Decodifica genoma 🧬
    """
    print(secuenciador)
    print("Descifrador del código genético de la vida 🔬")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar la ciencia con instrumentos ASCII! 🔬")
            break
        elif opcion == "1":
            dibujar_microscopio()
        elif opcion == "2":
            dibujar_telescopio()
        elif opcion == "3":
            dibujar_balanza_precision()
        elif opcion == "4":
            dibujar_probetas_laboratorio()
        elif opcion == "5":
            dibujar_osciloscopio()
        elif opcion == "6":
            dibujar_centrifugadora()
        elif opcion == "7":
            dibujar_espectrofotometro()
        elif opcion == "8":
            dibujar_termometro_digital()
        elif opcion == "9":
            dibujar_secuenciador_adn()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
