"""
EJERCICIO 68: Sistemas del Cuerpo Humano ASCII

Objetivo:
- Crear figuras ASCII de los sistemas del cuerpo humano
- Practicar la representación de anatomía y fisiología
- Explorar el funcionamiento del organismo humano

Conceptos a practicar:
- Representación de estructuras anatómicas
- Uso de caracteres para simular órganos y sistemas
- Creación de diagramas médicos educativos
- Diseño de interfaces de salud y medicina
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🫀 SISTEMAS DEL CUERPO HUMANO ASCII 🫀")
    print("="*50)
    print("0. Salir")
    print("1. Sistema circulatorio ❤️")
    print("2. Sistema respiratorio 🫁")
    print("3. Sistema nervioso 🧠")
    print("4. Sistema digestivo 🍽️")
    print("5. Sistema esquelético 🦴")
    print("6. Sistema muscular 💪")
    print("7. Sistema endocrino 🩺")
    print("8. Sistema inmunitario 🛡️")
    print("9. ADN y células 🧬")
    print("="*50)

def dibujar_sistema_circulatorio():
    print("\n❤️ SISTEMA CIRCULATORIO")
    print("-" * 30)
    circulatorio = """
    🫀 BOMBEO CARDÍACO 🫀
    
         🧠 CEREBRO 🧠
           ↗️ ↙️ ← Flujo
         ╔═══╧═══╗  sanguíneo
         ║ ○ ○ ○ ║  cerebral
         ╚═══════╝
             │
    ╔════════╧════════╗
    ║ ♥️ CORAZÓN ♥️   ║
    ║ ╔═══╗   ╔═══╗   ║ ← Aurículas
    ║ ║ AD ║   ║ AI ║   ║   derecha/izquierda
    ║ ╚═╤═╝   ╚═╤═╝   ║
    ║   ║       ║     ║
    ║ ╔═╧═╗   ╔═╧═╗   ║ ← Ventrículos
    ║ ║ VD ║   ║ VI ║   ║   derecho/izquierdo
    ║ ╚═══╝   ╚═══╝   ║
    ╚══════════════════╝
         │       │
    🫁 PULMONES │ CUERPO 💪
    ═══════════════════════
    
    Frecuencia: 60-100 latidos/min 📊
    Volumen: 5 litros sangre 🩸
    Presión: 120/80 mmHg 📈
    """
    print(circulatorio)
    print("Red de transporte vital que nutre todo el organismo 🚛")

def dibujar_sistema_respiratorio():
    print("\n🫁 SISTEMA RESPIRATORIO")
    print("-" * 30)
    respiratorio = """
    🌬️ INTERCAMBIO GASEOSO 🌬️
    
           👃 NARIZ 👃
           ║       ║ ← Fosas
           ║ ░░░░░ ║   nasales
           ╚═══╤═══╝
               │
        ╔══════╧══════╗
        ║ 😮 FARINGE  ║ ← Garganta
        ╚══════╤══════╝
               │
        ╔══════╧══════╗
        ║ ░ LARINGE ░ ║ ← Cuerdas
        ║   🎵🎵🎵   ║   vocales
        ╚══════╤══════╝
               │
        ╔══════╧══════╗
        ║ │ TRÁQUEA │ ║ ← Tubo
        ║ │ ═══════ │ ║   principal
        ║ │ ═══════ │ ║
        ╚══════╤══════╝
               │
           ╔═══╧═══╗
    🫁 ╔═══╧═╗ ╔═╧═══╗ 🫁
       ║ ○○○ ║ ║ ○○○ ║ ← Pulmones
       ║ ○○○ ║ ║ ○○○ ║   con alvéolos
       ║ ○○○ ║ ║ ○○○ ║
       ╚═════╝ ╚═════╝
    
    Respiración: 12-20 veces/min 🔄
    Capacidad: 6 litros aire 💨
    """
    print(respiratorio)
    print("Sistema que intercambia oxígeno por dióxido de carbono 🌱")

def dibujar_sistema_nervioso():
    print("\n🧠 SISTEMA NERVIOSO")
    print("-" * 30)
    nervioso = """
    ⚡ CONTROL Y COMUNICACIÓN ⚡
    
    ╔═══════════════════════════╗
    ║ 🧠 CEREBRO 🧠            ║
    ║ ╔═══╗ ╔═══╗ ╔═══╗       ║ ← Lóbulos
    ║ ║ F ║ ║ P ║ ║ O ║       ║   cerebrales
    ║ ╚═══╝ ╚═══╝ ╚═══╝       ║
    ║        ╔═══╗             ║
    ║        ║ T ║             ║ ← Temporal
    ║        ╚═══╝             ║
    ╚═══════════╤═════════════╝
                │
    ╔═══════════╧═════════════╗
    ║ 🧠 CEREBELO 🧠          ║ ← Equilibrio
    ║    ▓▓▓▓▓▓▓▓▓▓▓         ║   coordinación
    ╚═══════════╤═════════════╝
                │
    ║ MÉDULA ESPINAL ║ ← Columna
    ║ ⚡⚡⚡⚡⚡⚡⚡⚡⚡ ║   vertebral
    ║ ⚡⚡⚡⚡⚡⚡⚡⚡⚡ ║
    ║ ⚡⚡⚡⚡⚡⚡⚡⚡⚡ ║
    ╚═══════════════════╝
           │   │   │
       🦾 ─┴─ ─┴─ ─┴─ 🦾 ← Nervios
          PERIFÉRICOS    periféricos
    
    Velocidad: 120 m/s impulsos ⚡
    Neuronas: 86 mil millones 🧮
    """
    print(nervioso)
    print("Red de control que coordina todas las funciones 🎮")

def dibujar_sistema_digestivo():
    print("\n🍽️ SISTEMA DIGESTIVO")
    print("-" * 30)
    digestivo = """
    🍴 PROCESAMIENTO DE ALIMENTOS 🍴
    
           😮 BOCA 😮
           ║ 🦷🦷🦷 ║ ← Dientes
           ║   👅   ║   lengua
           ╚═══╤═══╝   saliva
               │
        ╔══════╧══════╗
        ║   ESÓFAGO   ║ ← Tubo
        ║ ░░░░░░░░░░░ ║   muscular
        ║ ░░░░░░░░░░░ ║   25cm
        ╚══════╤══════╝
               │
    ╔══════════╧══════════╗
    ║ 🍽️ ESTÓMAGO 🍽️     ║ ← Digestión
    ║ ╔═══════════════╗   ║   ácida
    ║ ║ 🍕 → 🥣 → 💧 ║   ║   pH 1.5-3.5
    ║ ╚═══════════════╝   ║
    ╚══════════╤══════════╝
               │
    ╔══════════╧══════════╗
    ║ INTESTINO DELGADO   ║ ← Absorción
    ║ ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿ ║   nutrientes
    ║ ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿ ║   6-7 metros
    ╚══════════╤══════════╝
               │
    ╔══════════╧══════════╗
    ║ INTESTINO GRUESO    ║ ← Absorción
    ║ ████████████████    ║   agua
    ║ ████████████████    ║   1.5 metros
    ╚═════════════════════╝
    
    Digestión completa: 24-72 horas ⏰
    """
    print(digestivo)
    print("Fábrica que convierte alimentos en energía vital ⚡")

def dibujar_sistema_esqueletico():
    print("\n🦴 SISTEMA ESQUELÉTICO")
    print("-" * 30)
    esqueletico = """
    💀 ESTRUCTURA Y SOPORTE 💀
    
        ╔═══════════╗
        ║ 💀 CRÁNEO ║ ← Protección
        ║  ◉    ◉  ║   cerebral
        ║     ∧    ║   22 huesos
        ║    ___   ║
        ╚═════╤═════╝
              │
    ╔═════════╧═════════╗
    ║ ╔═══╗     ╔═══╗   ║ ← Clavículas
    ║ ║   ║     ║   ║   ║   y escápulas
    ║ ╚═══╝     ╚═══╝   ║
    ║                   ║
    ║ ╔═══════════════╗ ║ ← Caja torácica
    ║ ║ 🫀 ║ ║ ║ 🫁 ║ ║   12 costillas
    ║ ║ ═══ ═══ ═══ ║ ║
    ║ ╚═══════════════╝ ║
    ║                   ║
    ║ ╔═══╗     ╔═══╗   ║ ← Brazos
    ║ ║ ⚡ ║     ║ ⚡ ║   ║   húmero, radio
    ║ ╚═══╝     ╚═══╝   ║   cúbito
    ║                   ║
    ║ ╔═══╗     ╔═══╗   ║ ← Piernas
    ║ ║ ⚡ ║     ║ ⚡ ║   ║   fémur, tibia
    ║ ╚═══╝     ╚═══╝   ║   peroné
    ╚═══════════════════╝
    
    Total huesos: 206 en adulto 🧮
    Médula ósea: Produce células sanguíneas 🩸
    """
    print(esqueletico)
    print("Armazón que sostiene y protege el cuerpo humano 🏗️")

def dibujar_sistema_muscular():
    print("\n💪 SISTEMA MUSCULAR")
    print("-" * 30)
    muscular = """
    🏋️ MOVIMIENTO Y FUERZA 🏋️
    
    ╔═══════════════════════════╗
    ║ 💪 TIPOS DE MÚSCULO 💪   ║
    ╚═══════════════════════════╝
    
        ╔═══════════╗
        ║ 🧠 CONTROL ║ ← Sistema
        ║   NEURAL   ║   nervioso
        ╚═════╤═════╝
              │ ⚡
    ╔═════════╧═════════╗
    ║ ▓ MÚSCULO LISO ▓  ║ ← Involuntario
    ║ ░ órganos ░░░░░░░ ║   digestión
    ╠═══════════════════╣
    ║ ♥️ MÚSCULO CARDÍACO ║ ← Corazón
    ║ ♥️♥️♥️♥️♥️♥️♥️♥️♥️ ║   automático
    ╠═══════════════════╣
    ║ 💪 ESQUELÉTICO 💪  ║ ← Voluntario
    ║ ╔═══╗     ╔═══╗   ║   movimiento
    ║ ║▓▓▓║     ║▓▓▓║   ║   bíceps
    ║ ║░░░║     ║░░░║   ║   tríceps
    ║ ║▓▓▓║     ║▓▓▓║   ║   cuádriceps
    ║ ╚═══╝     ╚═══╝   ║
    ║ ╔═══╗     ╔═══╗   ║ ← Piernas
    ║ ║▓▓▓║     ║▓▓▓║   ║   gemelos
    ║ ╚═══╝     ╚═══╝   ║   isquiotibiales
    ╚═══════════════════╝
    
    Total músculos: +600 💪
    Contracción: Ca²⁺ + ATP = Movimiento ⚡
    """
    print(muscular)
    print("Motor biológico que genera movimiento y postura 🚀")

def dibujar_sistema_endocrino():
    print("\n🩺 SISTEMA ENDOCRINO")
    print("-" * 30)
    endocrino = """
    🧪 MENSAJEROS QUÍMICOS 🧪
    
    ╔═══════════════════════════╗
    ║ 🧠 HIPOTÁLAMO 🧠         ║ ← Control
    ║   ↓ HORMONAS ↓           ║   maestro
    ║ 🫘 HIPÓFISIS 🫘          ║   7 hormonas
    ╚═══════════╤═════════════╝
                │
    ╔═══════════╧═════════════╗
    ║ 🦋 TIROIDES 🦋          ║ ← Metabolismo
    ║    T3, T4, CALCITONINA   ║   crecimiento
    ╠═════════════════════════╣
    ║ 🫀 SUPRARRENALES 🫀     ║ ← Estrés
    ║   ADRENALINA, CORTISOL   ║   respuesta
    ╠═════════════════════════╣
    ║ 🥞 PÁNCREAS 🥞          ║ ← Glucosa
    ║   INSULINA, GLUCAGÓN     ║   control
    ╠═════════════════════════╣
    ║ 🌸 GÓNADAS 🌸           ║ ← Reproducción
    ║   TESTOSTERONA/ESTRÓGENO ║   sexual
    ╚═════════════════════════╝
    
    ╔═══════════════════════════╗
    ║ FUNCIONES REGULADAS:      ║
    ║ • Crecimiento 📏          ║
    ║ • Metabolismo ⚡          ║ ← Homeostasis
    ║ • Reproducción 👶         ║   corporal
    ║ • Estrés 😰              ║
    ║ • Sueño 😴               ║
    ╚═══════════════════════════╝
    """
    print(endocrino)
    print("Sistema de comunicación química del organismo 📡")

def dibujar_sistema_inmunitario():
    print("\n🛡️ SISTEMA INMUNITARIO")
    print("-" * 30)
    inmunitario = """
    ⚔️ DEFENSA CORPORAL ⚔️
    
    ╔═══════════════════════════╗
    ║ 🛡️ LÍNEAS DE DEFENSA 🛡️  ║
    ╚═══════════════════════════╝
    
    ╔═══════════════════════════╗
    ║ 1️⃣ BARRERA FÍSICA        ║
    ║ 👁️ Piel, mucosas, lágrimas ║ ← Primera
    ║ 🫧 pH ácido, enzimas      ║   línea
    ╠═══════════════════════════╣
    ║ 2️⃣ INMUNIDAD INNATA      ║
    ║ 🦠 → 👮‍♂️ MACRÓFAGOS      ║ ← Segunda
    ║ 🔥 Inflamación, fiebre    ║   línea
    ╠═══════════════════════════╣
    ║ 3️⃣ INMUNIDAD ADAPTATIVA  ║
    ║ 🎯 LINFOCITOS B → 🅰️      ║ ← Tercera
    ║ ⚔️ LINFOCITOS T → 🔫      ║   línea
    ║ 🧠 MEMORIA INMUNITARIA    ║   especializada
    ╚═══════════════════════════╝
    
    ╔═══════════════════════════╗
    ║ ÓRGANOS LINFOIDES:        ║
    ║ 🍯 Médula ósea           ║ ← Producción
    ║ 🧠 Timo                  ║   células
    ║ 🫘 Bazo                  ║   inmunes
    ║ 🔗 Ganglios linfáticos   ║
    ╚═══════════════════════════╝
    
    Eficacia: 99.9% vs patógenos 🎯
    """
    print(inmunitario)
    print("Ejército microscópico que protege la salud 🏥")

def dibujar_adn_celulas():
    print("\n🧬 ADN Y CÉLULAS")
    print("-" * 30)
    adn_celulas = """
    🧬 INFORMACIÓN GENÉTICA 🧬
    
    ╔═══════════════════════════╗
    ║ 🔬 CÉLULA EUCARIOTA 🔬   ║
    ╚═══════════════════════════╝
    
    ╔═════════════════════════════╗
    ║ 🧱 MEMBRANA CELULAR 🧱     ║ ← Barrera
    ║ ╔═══════════════════════╗   ║   selectiva
    ║ ║ 🧬 NÚCLEO 🧬          ║   ║
    ║ ║ ┌─────────────────┐   ║   ║ ← Control
    ║ ║ │ ADN: A-T, G-C   │   ║   ║   genético
    ║ ║ │ 🧬═══🧬═══🧬    │   ║   ║
    ║ ║ │ 23 CROMOSOMAS   │   ║   ║
    ║ ║ └─────────────────┘   ║   ║
    ║ ╚═══════════════════════╝   ║
    ║ 🔋 MITOCONDRIAS 🔋         ║ ← Energía
    ║ ⚡ ATP ⚡ ATP ⚡ ATP        ║   celular
    ║                             ║
    ║ 🏭 RIBOSOMAS 🏭             ║ ← Síntesis
    ║ 🧪 PROTEÍNAS 🧪             ║   proteínas
    ╚═════════════════════════════╝
    
    ╔═══════════════════════════╗
    ║ CÓDIGO GENÉTICO:          ║
    ║ 🧬 3 mil millones de pares ║ ← Secuencia
    ║ 📚 20,000-25,000 genes    ║   información
    ║ 🔄 Replicación: DNA→DNA   ║
    ║ 📝 Transcripción: DNA→RNA ║
    ║ 🏭 Traducción: RNA→Proteína║
    ╚═══════════════════════════╝
    """
    print(adn_celulas)
    print("Unidad básica de la vida con instrucciones genéticas 📖")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar el cuerpo humano! 🫀")
            break
        elif opcion == "1":
            dibujar_sistema_circulatorio()
        elif opcion == "2":
            dibujar_sistema_respiratorio()
        elif opcion == "3":
            dibujar_sistema_nervioso()
        elif opcion == "4":
            dibujar_sistema_digestivo()
        elif opcion == "5":
            dibujar_sistema_esqueletico()
        elif opcion == "6":
            dibujar_sistema_muscular()
        elif opcion == "7":
            dibujar_sistema_endocrino()
        elif opcion == "8":
            dibujar_sistema_inmunitario()
        elif opcion == "9":
            dibujar_adn_celulas()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
