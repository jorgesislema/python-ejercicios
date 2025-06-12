"""
EJERCICIO 59: Festivales y Celebraciones ASCII

Objetivo:
- Crear figuras ASCII de festivales y celebraciones mundiales
- Practicar la representación de eventos culturales
- Explorar tradiciones y festividades de diferentes culturas

Conceptos a practicar:
- Representación de elementos festivos
- Uso de colores y símbolos culturales
- Creación de atmósferas celebrativas
- Diseño de escenas multiculturales
"""

def mostrar_menu():
    print("\n" + "="*50)
    print("🎉 FESTIVALES Y CELEBRACIONES ASCII 🎉")
    print("="*50)
    print("0. Salir")
    print("1. Carnaval 🎭")
    print("2. Día de los Muertos 💀")
    print("3. Festival de Luces 🪔")
    print("4. Oktoberfest 🍺")
    print("5. Festival de Fuegos Artificiales 🎆")
    print("6. Año Nuevo Chino 🐉")
    print("7. Festival de Música 🎵")
    print("8. La Tomatina 🍅")
    print("9. Festival de Holi 🌈")
    print("="*50)

def dibujar_carnaval():
    print("\n🎭 CARNAVAL")
    print("-" * 30)
    carnaval = """
    🎉🎊🎉🎊🎉🎊🎉🎊🎉🎊🎉
    
       🎭        🎭        🎭
      ╱ ╲      ╱ ╲      ╱ ╲
     ╱   ╲    ╱   ╲    ╱   ╲
    👤     👤     👤
    ╱│╲   ╱│╲   ╱│╲
   🌈 │ 🌈 │ 🌈 │
     ╱│╲  ╱│╲  ╱│╲
    🎺🎷🥁🎺🎷🥁🎺🎷🥁
    
    ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫
    
    🎪═══════════════════🎪
    ║ 🎠 🎡 🎢 🎯 🍭   ║
    ║                   ║
    ║ 👨‍👩‍👧‍👦 🎈 👨‍👩‍👧‍👦 🎈   ║
    🎪═══════════════════🎪
    """
    print(carnaval)
    print("Explosión de color, música y alegría comunitaria 🎊")

def dibujar_dia_muertos():
    print("\n💀 DÍA DE LOS MUERTOS")
    print("-" * 30)
    dia_muertos = """
    🌺 OFRENDA 🌺
    
    ╔═══════════════════════════╗
    ║ 🕯️ 💀 🕯️ 💀 🕯️ 💀 🕯️ ║
    ║                           ║
    ║ 🌺 🍞 🌺 🍞 🌺 🍞 🌺   ║
    ║                           ║
    ║ 💀   👨‍👩‍👧‍👦   👵   💀     ║
    ║  FAMILIA ETERNA           ║
    ║                           ║
    ║ 🌮 🌽 🥖 🍊 🍎 🌶️ 🥃   ║
    ║                           ║
    ║ 🌺 🌺 🌺 🌺 🌺 🌺 🌺   ║
    ╚═══════════════════════════╝
    
    "Los que se van, nunca se olvidan" 💝
    """
    print(dia_muertos)
    print("Celebración mexicana honrando a los ancestros 🌺")

def dibujar_festival_luces():
    print("\n🪔 FESTIVAL DE LUCES")
    print("-" * 30)
    festival_luces = """
    ✨ DIWALI ✨
    
    🪔 🪔 🪔 🪔 🪔 🪔 🪔 🪔 🪔
      ✨   ✨   ✨   ✨   ✨
    
    ╔═════════════════════════════╗
    ║ 🏠 ○ ○ ○ ○ ○ ○ ○ ○ 🏠   ║
    ║   ●   ●   ●   ●   ●       ║
    ║                           ║
    ║ 🪔 👨‍👩‍👧‍👦 🙏 🪔 👨‍👩‍👧‍👦 🪔   ║
    ║                           ║
    ║   🎆   🎇   🎆   🎇       ║
    ║                           ║
    ╚═════════════════════════════╝
    
    🌟 La luz vence a la oscuridad 🌟
    """
    print(festival_luces)
    print("Festival hindú de luces y renovación espiritual 🕯️")

def dibujar_oktoberfest():
    print("\n🍺 OKTOBERFEST")
    print("-" * 30)
    oktoberfest = """
    🇩🇪 PROST! 🇩🇪
    
       🎪🎪🎪🎪🎪🎪🎪
      ╱               ╲
     ╱ BIER FEST MÜNCHEN ╲
    ╱___________________╲
    
    🍺 👨 🍺 👩 🍺 👨 🍺
      ║   ║   ║   ║
    ╔═╧═╤═╧═╤═╧═╤═╧═╗
    ║   │   │   │   ║
    ║ 🥨 │ 🌭 │ 🥨 │ 🌭 ║
    ║   │   │   │   ║
    ╚═══╧═══╧═══╧═══╝
    
    🎵 Ein Prosit, ein Prosit! 🎵
    🎺 🎷 🥨 🍺 🎺 🎷 🥨
    """
    print(oktoberfest)
    print("Festival alemán de cerveza y tradiciones bávaras 🥨")

def dibujar_fuegos_artificiales():
    print("\n🎆 FESTIVAL DE FUEGOS ARTIFICIALES")
    print("-" * 30)
    fuegos = """
    ✨ HANABI MATSURI ✨
    
      ★     ✦     ⭐     ✧
        ╲   │   ╱
         ╲  │  ╱
    ✦ ─── ⚡ ─── ✦
         ╱  │  ╲
        ╱   │   ╲
      ★     ✦     ⭐     ✧
    
    🎆 ╱│╲ 🎇 ╱│╲ 🎆 ╱│╲ 🎇
       │     │     │
    
    👥👥👥👥👥👥👥👥👥👥
    ═════════════════════
    🏮 🏮 🏮 🏮 🏮 🏮 🏮
    
    "Flores de fuego en el cielo" 🌸
    """
    print(fuegos)
    print("Espectáculo pirotécnico japonés lleno de arte 🎋")

def dibujar_ano_nuevo_chino():
    print("\n🐉 AÑO NUEVO CHINO")
    print("-" * 30)
    ano_chino = """
    🏮 恭喜发财 🏮
    
       🐉🐉🐉🐉🐉🐉🐉
      ╱               ╲
     👤👤👤👤👤👤👤
    
    🧧 💰 🧧 💰 🧧 💰 🧧
    
    ╔═══════════════════════╗
    ║ 🥟 🍜 🥢 🍤 🦆 🍊 ║
    ║                       ║
    ║   👨‍👩‍👧‍👦 🍵 👨‍👩‍👧‍👦     ║
    ║                       ║
    ║ 🎇 🎆 🎋 🎇 🎆 🎋   ║
    ╚═══════════════════════╝
    
    🥠 "Fortuna y prosperidad" 🥠
    """
    print(ano_chino)
    print("Celebración lunar china de renovación y abundancia 🌙")

def dibujar_festival_musica():
    print("\n🎵 FESTIVAL DE MÚSICA")
    print("-" * 30)
    festival_musica = """
    🎤 MUSIC FEST 2024 🎤
    
        🎪🎪🎪🎪🎪🎪🎪
       ╱ ESCENARIO PRINCIPAL ╲
      ╱_____________________╲
    
    🎸 👨‍🎤 🥁 👩‍🎤 🎹 👨‍🎤 🎸
      ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫
    
    ═════════════════════════
    🙋‍♂️🙋‍♀️🙋‍♂️🙋‍♀️🙋‍♂️🙋‍♀️🙋‍♂️🙋‍♀️
    ═════════════════════════
    
    🎵 Rock 🎵 Pop 🎵 Jazz 🎵
    🎪 Comida 🎪 Arte 🎪
    
    "Donde la música une corazones" 💕
    """
    print(festival_musica)
    print("Encuentro musical que celebra la diversidad sonora 🎶")

def dibujar_tomatina():
    print("\n🍅 LA TOMATINA")
    print("-" * 30)
    tomatina = """
    🇪🇸 BUÑOL, VALENCIA 🇪🇸
    
    🍅 ╱ ╲ 🍅 ╱ ╲ 🍅 ╱ ╲ 🍅
      ╱   ╲   ╱   ╲   ╱
    🍅     🍅     🍅
    
    👤🍅👤🍅👤🍅👤🍅👤
     ╲│╱ ╲│╱ ╲│╱ ╲│╱
      🍅   🍅   🍅   🍅
    
    ════🍅════🍅════🍅════
    🍅 SPLASH! 🍅 SPLAT! 🍅
    ════🍅════🍅════🍅════
    
    👥🍅💦🍅👥🍅💦🍅👥
    
    "¡Guerra de tomates!" 💥
    """
    print(tomatina)
    print("Festival español de diversión y tomates voladores 🎯")

def dibujar_holi():
    print("\n🌈 FESTIVAL DE HOLI")
    print("-" * 30)
    holi = """
    🇮🇳 HOLI HAI! 🇮🇳
    
    🌈 ░░░ ▓▓▓ ░░░ ▓▓▓ 🌈
      🔴 🟡 🔵 🟢 🟣 🟠
    
    👤💨🌈 👤💨🌈 👤💨🌈
     ╲│╱   ╲│╱   ╲│╱
    💙💚💛💜💙💚💛💜
    
    ═══🌈═══🌈═══🌈═══
    🎨 ░ ▓ ░ ▓ ░ ▓ 🎨
    ═══🌈═══🌈═══🌈═══
    
    👨‍👩‍👧‍👦🌈👨‍👩‍👧‍👦🌈👨‍👩‍👧‍👦
    
    "El triunfo del bien sobre el mal" ✨
    """
    print(holi)
    print("Festival hindú de colores y renovación primaveral 🌸")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (0-9): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por celebrar con nosotros! 🎉")
            break
        elif opcion == "1":
            dibujar_carnaval()
        elif opcion == "2":
            dibujar_dia_muertos()
        elif opcion == "3":
            dibujar_festival_luces()
        elif opcion == "4":
            dibujar_oktoberfest()
        elif opcion == "5":
            dibujar_fuegos_artificiales()
        elif opcion == "6":
            dibujar_ano_nuevo_chino()
        elif opcion == "7":
            dibujar_festival_musica()
        elif opcion == "8":
            dibujar_tomatina()
        elif opcion == "9":
            dibujar_holi()
        else:
            print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
