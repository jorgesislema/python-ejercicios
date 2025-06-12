"""
EJERCICIO 65: Arte y Cultura ASCII

Objetivo:
- Crear figuras ASCII representando arte y manifestaciones culturales
- Practicar la representación de obras artísticas
- Explorar diferentes formas de expresión cultural

Conceptos a practicar:
- Representación de obras de arte famosas
- Uso de caracteres para crear texturas artísticas
- Creación de escenas culturales
- Diseño de elementos artísticos
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🎨 ARTE Y CULTURA ASCII 🎨")
    print("="*50)
    print("0. Salir")
    print("1. La Mona Lisa 🖼️")
    print("2. Teatro griego 🎭")
    print("3. Escultura de David 🗿")
    print("4. Pintura abstracta 🎨")
    print("5. Ballet clásico 🩰")
    print("6. Ópera 🎼")
    print("7. Arte callejero 🏙️")
    print("8. Cerámica tradicional 🏺")
    print("9. Galería de arte 🏛️")
    print("="*50)

def dibujar_mona_lisa():
    print("\n🖼️ LA MONA LISA")
    print("-" * 30)
    mona_lisa = """
    ╔══════════════════════════╗
    ║ "LA GIOCONDA" - DA VINCI ║
    ╚══════════════════════════╝
    
    ╔══════════════════════════╗
    ║ ░░░░░░░░░░░░░░░░░░░░░░░░ ║
    ║ ░░░░░╔═══════╗░░░░░░░░░ ║
    ║ ░░░░░║ ◉ ◉ ║░░░░░░░░░ ║
    ║ ░░░░░║   ▼   ║░░░░░░░░░ ║
    ║ ░░░░░║   ∩   ║░░░░░░░░░ ║
    ║ ░░░░░╚═══════╝░░░░░░░░░ ║
    ║ ░░░░░╔═══════╗░░░░░░░░░ ║
    ║ ░░░░░║ 👗👗👗 ║░░░░░░░░░ ║
    ║ ░░░░░║ 👗👗👗 ║░░░░░░░░░ ║
    ║ ░░░░░╚═══════╝░░░░░░░░░ ║
    ║ ░░░░░░░░░░░░░░░░░░░░░░░░ ║
    ╚══════════════════════════╝
    
    Museo: Louvre, París 🇫🇷
    Año: 1503-1519 📅
    """
    print(mona_lisa)
    print("La sonrisa más enigmática del arte renacentista 😊")

def dibujar_teatro_griego():
    print("\n🎭 TEATRO GRIEGO")
    print("-" * 30)
    teatro = """
    🏛️ EPIDAURO - SIGLO IV a.C. 🏛️
    
              🎭 ESCENARIO 🎭
    ╔═══════════════════════════════╗
    ║ 👨‍🎭 ACTOR  👩‍🎭 CORO 👨‍🎭 ACTOR ║
    ╚═══════════════════════════════╝
         ╱ ╲               ╱ ╲
        ╱   ╲             ╱   ╲
       ╱ 👥👥 ╲           ╱ 👥👥 ╲
      ╱ 👥👥👥 ╲         ╱ 👥👥👥 ╲
     ╱ 👥👥👥👥 ╲       ╱ 👥👥👥👥 ╲
    ╱ 👥👥👥👥👥 ╲     ╱ 👥👥👥👥👥 ╲
   ╱ 👥👥👥👥👥👥 ╲   ╱ 👥👥👥👥👥👥 ╲
  ╱ 👥👥👥👥👥👥👥 ╲ ╱ 👥👥👥👥👥👥👥 ╲
    
    Capacidad: 14,000 espectadores 🎪
    Acústica: Perfecta sin amplificación 🔊
    """
    print(teatro)
    print("Anfiteatro clásico donde nació el drama occidental 🎼")

def dibujar_escultura_david():
    print("\n🗿 ESCULTURA DE DAVID")
    print("-" * 30)
    david = """
    🏛️ MIGUEL ÁNGEL - 1504 🏛️
    
         ╔═══════╗
         ║ ◉ ◉ ║ ← Mirada
         ║   ▼   ║   determinada
         ║   ∩   ║
         ╚═══╤═══╝
    ╔═══════╧═══════╗
    ║ 💪         💪 ║ ← Musculatura
    ║               ║   detallada
    ║ 🎯         🎯 ║
    ║               ║
    ║       🏹      ║ ← Honda
    ║               ║
    ╚═══════════════╝
         ║ ║ ║
         ║ ║ ║ ← Piernas
         ║ ║ ║   proporcionadas
    ═════╧═╧═╧═════
    
    Material: Mármol blanco 🏔️
    Altura: 5.17 metros 📏
    """
    print(david)
    print("Símbolo renacentista de la perfección humana 💪")

def dibujar_pintura_abstracta():
    print("\n🎨 PINTURA ABSTRACTA")
    print("-" * 30)
    abstracta = """
    🖼️ ESTILO KANDINSKY 🖼️
    
    ╔══════════════════════════╗
    ║ ▲🔴▲ ○🟡○ ▲🔵▲ ○🟢○  ║
    ║ 🔴○🔴 ▲🟡▲ 🔵○🔵 ▲🟢▲ ║
    ║                          ║
    ║ ～～～🟣～～～🟠～～～     ║
    ║   ╱╲  ◆  ╱╲  ◇  ╱╲    ║
    ║  ╱  ╲   ╱  ╲   ╱  ╲   ║
    ║                          ║
    ║ ●●●●●   ▪▪▪▪▪   ■■■■■ ║
    ║ ○○○○○   ▫▫▫▫▫   □□□□□ ║
    ║                          ║
    ║ ～～～～～～～～～～～～～ ║
    ╚══════════════════════════╝
    
    Movimiento: Expresionismo abstracto 🌈
    Emociones: Color y forma pura 💫
    """
    print(abstracta)
    print("Expresión libre de forma, color y emoción 🎭")

def dibujar_ballet_clasico():
    print("\n🩰 BALLET CLÁSICO")
    print("-" * 30)
    ballet = """
    🎭 EL LAGO DE LOS CISNES 🎭
    
       🎼 MÚSICA: TCHAIKOVSKY 🎼
    
    ╔═══════════════════════════════╗
    ║           🩰                  ║
    ║          ╱│╲  ← Prima         ║
    ║         ╱ │ ╲   ballerina     ║
    ║           │                   ║
    ║   🩰   🩰 │ 🩰   🩰          ║
    ║  ╱│╲  ╱│╲│╱│╲  ╱│╲ ← Cuerpo ║
    ║ ╱ │ ╲ ╱│ ╲╱│╲ ╱ │ ╲  de     ║
    ║   │    │  │  │   │     baile  ║
    ╚═══════════════════════════════╝
    
      👥👥👥 AUDIENCIA 👥👥👥
    ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫
    
    Técnica: En pointe, grand jeté 🩰
    Historia: Corte de Luis XIV 👑
    """
    print(ballet)
    print("Danza clásica de elegancia y técnica suprema 👑")

def dibujar_opera():
    print("\n🎼 ÓPERA")
    print("-" * 30)
    opera = """
    🏛️ TEATRO DE LA ÓPERA 🏛️
    
    ╔═══════════════════════════════╗
    ║ 🎤 SOPRANO 🎤 TENOR 🎤       ║
    ║  👩‍🎤 "AIDA" 👨‍🎤 ARIA       ║
    ║                               ║
    ║ 🎻🎺🥁🎹🎷🎻🎺🥁🎹🎷      ║
    ║ ← ORQUESTA SINFÓNICA          ║
    ╚═══════════════════════════════╝
           🎼 GIUSEPPE VERDI 🎼
    
    ╔═══════════════════════════════╗
    ║ PALCOS VIP                    ║
    ║ 👑 👑 👑 👑 👑              ║
    ╠═══════════════════════════════╣
    ║ 👥👥👥👥👥👥👥👥👥👥👥   ║
    ║ 👥👥👥👥👥👥👥👥👥👥👥   ║
    ╚═══════════════════════════════╝
    
    Duración: 3 actos, 2.5 horas ⏰
    """
    print(opera)
    print("Fusión suprema de música, teatro y drama vocal 🎭")

def dibujar_arte_callejero():
    print("\n🏙️ ARTE CALLEJERO")
    print("-" * 30)
    arte_callejero = """
    🏙️ MURAL URBANO - BANKSY 🏙️
    
    ████████████████████████████
    ██ ░░░░░░░░░░░░░░░░░░░░░░ ██
    ██ ░ 🕊️ PEACE & LOVE 🕊️ ░ ██
    ██ ░░░░░░░░░░░░░░░░░░░░░░ ██
    ██                        ██
    ██ 🎨 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 🎨 ██
    ██    ▓ 👤  HOPE  👤 ▓    ██
    ██    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ██
    ██                        ██
    ██ #STREETART #REVOLUTION ██
    ████████████████████████████
         🚶‍♂️    🚶‍♀️    🚶‍♂️
    
    Técnica: Plantilla, spray 🎨
    Mensaje: Crítica social 📢
    """
    print(arte_callejero)
    print("Arte urbano que transforma muros en lienzos 🎨")

def dibujar_ceramica_tradicional():
    print("\n🏺 CERÁMICA TRADICIONAL")
    print("-" * 30)
    ceramica = """
    🏺 ALFARERÍA ANCESTRAL 🏺
    
        ╔═══════════════╗
        ║ TORNO ALFARERO ║
        ╚═══════════════╝
    
           ╔═══╗
          ╱ 🏺 ╲ ← Vasija
         ╱ ○○○ ╲   en 
        ╱ ○○○○○ ╲  formación
       ╱ ○○○○○○○ ╲
      ╱ ○○○○○○○○○ ╲
     ╱_____________╲
     ║ 👐 ARTESANO 👐 ║
     ╚═══════════════╝
         🔥 HORNO 🔥
    
    ╔═══════════════════════════╗
    ║ 🏺 🏺 🏺 🏺 🏺 🏺 🏺   ║
    ║ PRODUCTOS TERMINADOS      ║
    ╚═══════════════════════════╝
    
    Material: Arcilla natural 🌍
    Técnica: Milenaria 📅
    """
    print(ceramica)
    print("Arte milenario de moldear la tierra con las manos 👐")

def dibujar_galeria_arte():
    print("\n🏛️ GALERÍA DE ARTE")
    print("-" * 30)
    galeria = """
    🏛️ MUSEO DE ARTE MODERNO 🏛️
    
    ╔═══════════════════════════════╗
    ║ SALA PRINCIPAL                ║
    ║                               ║
    ║ 🖼️      🖼️      🖼️         ║
    ║ [1]     [2]     [3]          ║
    ║                               ║
    ║      👥 👥 👥                ║
    ║   VISITANTES                  ║
    ║                               ║
    ║ 🖼️      🖼️      🖼️         ║
    ║ [4]     [5]     [6]          ║
    ║                               ║
    ║     🚶‍♂️ GUÍA 📖              ║
    ╚═══════════════════════════════╝
    
    Exposición: "Vanguardias del S.XX" 🎨
    Artistas: Picasso, Dalí, Miró 🖌️
    """
    print(galeria)
    print("Espacio sagrado donde el arte dialoga con el alma 🎭")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar el arte y la cultura! 🎨")
            break
        elif opcion == "1":
            dibujar_mona_lisa()
        elif opcion == "2":
            dibujar_teatro_griego()
        elif opcion == "3":
            dibujar_escultura_david()
        elif opcion == "4":
            dibujar_pintura_abstracta()
        elif opcion == "5":
            dibujar_ballet_clasico()
        elif opcion == "6":
            dibujar_opera()
        elif opcion == "7":
            dibujar_arte_callejero()
        elif opcion == "8":
            dibujar_ceramica_tradicional()
        elif opcion == "9":
            dibujar_galeria_arte()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
