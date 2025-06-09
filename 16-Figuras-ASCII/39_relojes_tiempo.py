"""
Ejercicio 39: Relojes y Tiempo ASCII

Objetivo:
- Crear diferentes tipos de relojes ASCII
- Mostrar hora actual en ASCII
- Incluir relojes analógicos y digitales
- Crear cronómetros y temporizadores

Conceptos:
- Manejo de tiempo en Python
- Representación visual de números
- Algoritmos de posicionamiento de manecillas
- Interfaz de usuario temporal
"""

import time
import datetime
import os

def reloj_digital_basico():
    """Reloj digital básico con números ASCII"""
    print("🕐 RELOJ DIGITAL BÁSICO 🕐")
    print("═" * 50)
    
    # Obtener hora actual
    ahora = datetime.datetime.now()
    hora = ahora.strftime("%H:%M:%S")
    
    # Números ASCII grandes
    numeros = {
        '0': [
            "▓▓▓▓▓",
            "▓   ▓",
            "▓   ▓",
            "▓   ▓",
            "▓▓▓▓▓"
        ],
        '1': [
            "  ▓  ",
            " ▓▓  ",
            "  ▓  ",
            "  ▓  ",
            "▓▓▓▓▓"
        ],
        '2': [
            "▓▓▓▓▓",
            "    ▓",
            "▓▓▓▓▓",
            "▓    ",
            "▓▓▓▓▓"
        ],
        '3': [
            "▓▓▓▓▓",
            "    ▓",
            "▓▓▓▓▓",
            "    ▓",
            "▓▓▓▓▓"
        ],
        '4': [
            "▓   ▓",
            "▓   ▓",
            "▓▓▓▓▓",
            "    ▓",
            "    ▓"
        ],
        '5': [
            "▓▓▓▓▓",
            "▓    ",
            "▓▓▓▓▓",
            "    ▓",
            "▓▓▓▓▓"
        ],
        '6': [
            "▓▓▓▓▓",
            "▓    ",
            "▓▓▓▓▓",
            "▓   ▓",
            "▓▓▓▓▓"
        ],
        '7': [
            "▓▓▓▓▓",
            "    ▓",
            "   ▓ ",
            "  ▓  ",
            " ▓   "
        ],
        '8': [
            "▓▓▓▓▓",
            "▓   ▓",
            "▓▓▓▓▓",
            "▓   ▓",
            "▓▓▓▓▓"
        ],
        '9': [
            "▓▓▓▓▓",
            "▓   ▓",
            "▓▓▓▓▓",
            "    ▓",
            "▓▓▓▓▓"
        ],
        ':': [
            "     ",
            "  ▓  ",
            "     ",
            "  ▓  ",
            "     "
        ]
    }
    
    # Mostrar hora en ASCII
    for i in range(5):
        linea = ""
        for char in hora:
            if char in numeros:
                linea += numeros[char][i] + "  "
        print(linea)
    
    print(f"\nHora actual: {hora}")
    print(f"Fecha: {ahora.strftime('%d/%m/%Y')}")

def reloj_analogico():
    """Reloj analógico ASCII"""
    print("🕐 RELOJ ANALÓGICO 🕐")
    print("═" * 40)
    
    ahora = datetime.datetime.now()
    hora = ahora.hour % 12
    minuto = ahora.minute
    
    # Base del reloj
    reloj = [
        "    12    ",
        "  ╭─────╮ ",
        "9 │     │ 3",
        "  │  •  │ ",
        "  │     │ ",
        "  ╰─────╯ ",
        "     6    "
    ]
    
    # Mostrar reloj base
    for linea in reloj:
        print(linea)
    
    print(f"\nHora: {ahora.strftime('%I:%M %p')}")
    print("Manecilla corta: hora")
    print("Manecilla larga: minutos")

def cronometro_ascii():
    """Cronómetro ASCII funcional"""
    print("⏱️ CRONÓMETRO ASCII ⏱️")
    print("═" * 40)
    
    print("Presiona Enter para iniciar/pausar")
    print("Escribe 'reset' para reiniciar")
    print("Escribe 'salir' para terminar")
    
    tiempo_inicio = None
    tiempo_pausado = 0
    pausado = True
    
    while True:
        if not pausado and tiempo_inicio:
            tiempo_actual = time.time() - tiempo_inicio - tiempo_pausado
            minutos = int(tiempo_actual // 60)
            segundos = int(tiempo_actual % 60)
            centesimas = int((tiempo_actual % 1) * 100)
            
            # Limpiar pantalla
            os.system('cls' if os.name == 'nt' else 'clear')
            print("⏱️ CRONÓMETRO ASCII ⏱️")
            print("═" * 40)
            print(f"⏰ {minutos:02d}:{segundos:02d}.{centesimas:02d} ⏰")
            print("\n🔥 CRONÓMETRO EN MARCHA 🔥")
            print("Enter: pausar | 'reset': reiniciar | 'salir': terminar")
        
        # Verificar entrada sin bloquear
        try:
            import select
            import sys
            
            if select.select([sys.stdin], [], [], 0.01) == ([sys.stdin], [], []):
                entrada = input().strip().lower()
                
                if entrada == '':
                    if pausado:
                        if tiempo_inicio is None:
                            tiempo_inicio = time.time()
                        pausado = False
                        print("¡Cronómetro iniciado!")
                    else:
                        tiempo_pausado += time.time() - tiempo_inicio - tiempo_pausado
                        pausado = True
                        print("Cronómetro pausado")
                elif entrada == 'reset':
                    tiempo_inicio = None
                    tiempo_pausado = 0
                    pausado = True
                    print("Cronómetro reiniciado")
                elif entrada == 'salir':
                    break
        except:
            # Para Windows sin select
            print("Presiona Enter para interactuar:")
            entrada = input().strip().lower()
            
            if entrada == '':
                if pausado:
                    if tiempo_inicio is None:
                        tiempo_inicio = time.time()
                    pausado = False
                    print("¡Cronómetro iniciado!")
                else:
                    pausado = True
                    print("Cronómetro pausado")
            elif entrada == 'reset':
                tiempo_inicio = None
                tiempo_pausado = 0
                pausado = True
                print("Cronómetro reiniciado")
            elif entrada == 'salir':
                break
        
        time.sleep(0.01)

def reloj_mundial():
    """Relojes de diferentes zonas horarias"""
    print("🌍 RELOJES MUNDIALES 🌍")
    print("═" * 60)
    
    import pytz
    
    zonas = [
        ('Mexico/General', 'CIUDAD DE MÉXICO', '🇲🇽'),
        ('US/Eastern', 'NUEVA YORK', '🇺🇸'),
        ('Europe/London', 'LONDRES', '🇬🇧'),
        ('Europe/Paris', 'PARÍS', '🇫🇷'),
        ('Asia/Tokyo', 'TOKIO', '🇯🇵'),
        ('Australia/Sydney', 'SÍDNEY', '🇦🇺')
    ]
    
    try:
        for zona, ciudad, bandera in zonas:
            tz = pytz.timezone(zona)
            tiempo_local = datetime.datetime.now(tz)
            print(f"{bandera} {ciudad:15} {tiempo_local.strftime('%H:%M:%S')} {tiempo_local.strftime('%d/%m/%Y')}")
    except ImportError:
        print("Para mostrar zonas horarias, instala: pip install pytz")
        # Alternativa sin pytz
        ahora = datetime.datetime.now()
        print(f"🇲🇽 CIUDAD DE MÉXICO  {ahora.strftime('%H:%M:%S')} {ahora.strftime('%d/%m/%Y')}")

def temporizador_ascii():
    """Temporizador cuenta regresiva"""
    print("⏲️ TEMPORIZADOR ASCII ⏲️")
    print("═" * 40)
    
    try:
        minutos = int(input("Ingresa minutos: "))
        segundos = int(input("Ingresa segundos adicionales: "))
        
        total_segundos = minutos * 60 + segundos
        
        print(f"\n⏲️ Iniciando cuenta regresiva: {minutos:02d}:{segundos:02d}")
        time.sleep(2)
        
        while total_segundos > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("⏲️ TEMPORIZADOR ASCII ⏲️")
            print("═" * 40)
            
            mins = total_segundos // 60
            secs = total_segundos % 60
            
            print(f"\n⏰ {mins:02d}:{secs:02d} ⏰")
            
            if total_segundos <= 10:
                print("🔥 ¡ÚLTIMOS SEGUNDOS! 🔥")
            elif total_segundos <= 60:
                print("⚠️  Menos de un minuto ⚠️")
            
            time.sleep(1)
            total_segundos -= 1
        
        # Alarma
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🚨 ¡TIEMPO TERMINADO! 🚨")
        print("⏰ 00:00 ⏰")
        print("🔔 ¡RING RING RING! 🔔")
        
    except ValueError:
        print("❌ Por favor ingresa números válidos")

def reloj_binario():
    """Reloj en código binario"""
    print("💻 RELOJ BINARIO 💻")
    print("═" * 40)
    
    ahora = datetime.datetime.now()
    hora = ahora.hour
    minuto = ahora.minute
    segundo = ahora.second
    
    def a_binario(numero):
        return format(numero, '06b')  # 6 bits
    
    print("Hora en binario (24h):")
    print(f"Hora:    {hora:02d} = {a_binario(hora)}")
    print(f"Minuto:  {minuto:02d} = {a_binario(minuto)}")
    print(f"Segundo: {segundo:02d} = {a_binario(segundo)}")
    
    print("\nRepresentación visual:")
    print("H H M M S S")
    print("5 4 5 4 5 4  <- Posición del bit")
    print("│ │ │ │ │ │")
    
    # Crear representación visual
    h_bin = a_binario(hora)
    m_bin = a_binario(minuto)
    s_bin = a_binario(segundo)
    
    for i in range(6):
        h_bit = "●" if h_bin[i] == '1' else "○"
        m_bit = "●" if m_bin[i] == '1' else "○"
        s_bit = "●" if s_bin[i] == '1' else "○"
        print(f"{h_bit} {h_bit} {m_bit} {m_bit} {s_bit} {s_bit}")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "═" * 50)
        print("🕐 RELOJES Y TIEMPO ASCII 🕐")
        print("═" * 50)
        print("1. Reloj digital básico")
        print("2. Reloj analógico")
        print("3. Cronómetro ASCII")
        print("4. Relojes mundiales")
        print("5. Temporizador cuenta regresiva")
        print("6. Reloj binario")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            reloj_digital_basico()
        elif opcion == "2":
            reloj_analogico()
        elif opcion == "3":
            cronometro_ascii()
        elif opcion == "4":
            reloj_mundial()
        elif opcion == "5":
            temporizador_ascii()
        elif opcion == "6":
            reloj_binario()
        elif opcion == "0":
            print("¡Hasta luego! 🕐")
            break
        else:
            print("Opción no válida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
