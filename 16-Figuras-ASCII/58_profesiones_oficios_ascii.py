"""
EJERCICIO 58: Profesiones y Oficios ASCII

Objetivo:
- Crear figuras ASCII representando diferentes profesiones
- Practicar la representación de personas y herramientas laborales
- Explorar la diversidad de trabajos y oficios

Conceptos a practicar:
- Representación de figuras humanas especializadas
- Uso de símbolos profesionales
- Creación de escenas laborales
- Diseño de ambientes de trabajo
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("👨‍💼 PROFESIONES Y OFICIOS ASCII 👩‍💼")
    print("="*50)
    print("0. Salir")
    print("1. Médico 👨‍⚕️")
    print("2. Bombero 👨‍🚒")
    print("3. Chef 👨‍🍳")
    print("4. Programador 👨‍💻")
    print("5. Profesor 👨‍🏫")
    print("6. Mecánico 👨‍🔧")
    print("7. Artista 👨‍🎨")
    print("8. Piloto ✈️")
    print("9. Científico 👨‍🔬")
    print("="*50)

def dibujar_medico():
    print("\n👨‍⚕️ MÉDICO")
    print("-" * 30)
    medico = """
        ╔═══════════════╗
        ║ 🏥 HOSPITAL   ║
        ╚═══════════════╝
    
           ╔═════╗
           ║ ● ● ║
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ ⚕️ + ⚕️ ║
        ║         ║
        ║ 🩺 📋 💊 ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║ 👤 PACIENTE ║
        ║    😷     ║
        ╚═══════════╝
    
    [DIAGNÓSTICO] 📊 [TRATAMIENTO] 💉
    """
    print(medico)
    print("Profesional de la salud que salva vidas 🩺")

def dibujar_bombero():
    print("\n👨‍🚒 BOMBERO")
    print("-" * 30)
    bombero = """
        🚨 EMERGENCIA 🚨
        
           ╔═════╗
           ║ ● ● ║
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ 🧯 🚒 🔥 ║
        ║         ║
        ║ ⛑️ 🪓 💧 ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║    🔥    ║
        ║ 🏠 💨 🔥 ║
        ╚═══════════╝
    
      🚒 ← ← ← ← 🔥🏠🔥
      
    [RESCATE] 🆘 [EXTINCIÓN] 💧
    """
    print(bombero)
    print("Héroe que combate incendios y rescata personas 🦸")

def dibujar_chef():
    print("\n👨‍🍳 CHEF")
    print("-" * 30)
    chef = """
        ╔═══════════════╗
        ║ 🍽️ RESTAURANTE ║
        ╚═══════════════╝
    
           ╔═════╗
           ║ ● ● ║
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ 👨‍🍳 🍽️ 🔪 ║
        ║         ║
        ║ 🥄 🍳 🧂 ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║ 🔥 🍲 🔥 ║
        ║ 🥕🍅🧄🧅 ║
        ╚═══════════╝
    
    [COCINANDO] 🔥 [PLATO LISTO] ✨
    """
    print(chef)
    print("Artista culinario que crea experiencias gastronómicas 🍽️")

def dibujar_programador():
    print("\n👨‍💻 PROGRAMADOR")
    print("-" * 30)
    programador = """
        ╔═══════════════╗
        ║ 💻 DEV OFFICE  ║
        ╚═══════════════╝
    
           ╔═════╗
           ║ ● ● ║ 👓
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ 💻 ⌨️ 🖱️ ║
        ║         ║
        ║ 📚 ☕ 🐛 ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║ 01010101 ║
        ║ def main():║
        ║   print("Hi")║
        ╚═══════════╝
    
    [CODING] ⚡ [DEBUGGING] 🔍
    """
    print(programador)
    print("Arquitecto digital que construye el futuro 🚀")

def dibujar_profesor():
    print("\n👨‍🏫 PROFESOR")
    print("-" * 30)
    profesor = """
        ╔═══════════════╗
        ║ 🏫 ESCUELA     ║
        ╚═══════════════╝
    
           ╔═════╗
           ║ ● ● ║ 👓
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ 📚 ✏️ 📝 ║
        ║         ║
        ║ 🍎 📖 🎓 ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║ 👨‍🎓👩‍🎓👨‍🎓👩‍🎓 ║
        ║   A B C   ║
        ║ 2 + 2 = 4 ║
        ╚═══════════╝
    
    [ENSEÑANDO] 📖 [APRENDIENDO] 🧠
    """
    print(profesor)
    print("Educador que forma las mentes del futuro 🌟")

def dibujar_mecanico():
    print("\n👨‍🔧 MECÁNICO")
    print("-" * 30)
    mecanico = """
        ╔═══════════════╗
        ║ 🔧 TALLER      ║
        ╚═══════════════╝
    
           ╔═════╗
           ║ ● ● ║
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ 🔧 🔩 ⚙️ ║
        ║         ║
        ║ 🛠️ 🔨 ⚒️ ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║   🚗     ║
        ║ ⚙️ 🔧 ⚙️ ║
        ╚═══════════╝
    
    [REPARANDO] 🔧 [FUNCIONAL] ✅
    """
    print(mecanico)
    print("Experto que mantiene las máquinas en funcionamiento ⚙️")

def dibujar_artista():
    print("\n👨‍🎨 ARTISTA")
    print("-" * 30)
    artista = """
        ╔═══════════════╗
        ║ 🎨 ESTUDIO     ║
        ╚═══════════════╝
    
           ╔═════╗
           ║ ● ● ║
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ 🎨 🖌️ 🖍️ ║
        ║         ║
        ║ 🎭 🖼️ ✨ ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║ 🌅 🏔️ 🌊 ║
        ║ 🎨 🖌️ 🎨 ║
        ╚═══════════╝
    
    [CREANDO] 🎨 [INSPIRACIÓN] 💫
    """
    print(artista)
    print("Creador de belleza y expresión visual 🌈")

def dibujar_piloto():
    print("\n✈️ PILOTO")
    print("-" * 30)
    piloto = """
        ╔═══════════════╗
        ║ ✈️ AEROPUERTO  ║
        ╚═══════════════╝
    
           ╔═════╗
           ║ ● ● ║ 🧢
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ ✈️ 🧭 📡 ║
        ║         ║
        ║ 🎙️ 📊 ⚖️ ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║    ✈️    ║
        ║ ☁️ 🌤️ ☁️ ║
        ╚═══════════╝
    
    [VOLANDO] ✈️ [DESTINO] 🌍
    """
    print(piloto)
    print("Navegador de los cielos que conecta el mundo 🌐")

def dibujar_cientifico():
    print("\n👨‍🔬 CIENTÍFICO")
    print("-" * 30)
    cientifico = """
        ╔═══════════════╗
        ║ 🔬 LABORATORIO ║
        ╚═══════════════╝
    
           ╔═════╗
           ║ ● ● ║ 👓
           ║  ▼  ║
           ╚═╤═══╝
        ╔════╧════╗
        ║ 🔬 ⚗️ 🧪 ║
        ║         ║
        ║ 📊 🧬 ⚛️ ║
        ╚═════════╝
            │ │
        ╔═══╧═╧═══╗
        ║ H₂O + CO₂ ║
        ║ 🧪⚗️🔬⚛️ ║
        ╚═══════════╝
    
    [INVESTIGANDO] 🔍 [DESCUBRIENDO] 💡
    """
    print(cientifico)
    print("Explorador del conocimiento y los misterios naturales 🌌")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por explorar las profesiones ASCII! 👨‍💼")
            break
        elif opcion == "1":
            dibujar_medico()
        elif opcion == "2":
            dibujar_bombero()
        elif opcion == "3":
            dibujar_chef()
        elif opcion == "4":
            dibujar_programador()
        elif opcion == "5":
            dibujar_profesor()
        elif opcion == "6":
            dibujar_mecanico()
        elif opcion == "7":
            dibujar_artista()
        elif opcion == "8":
            dibujar_piloto()
        elif opcion == "9":
            dibujar_cientifico()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
