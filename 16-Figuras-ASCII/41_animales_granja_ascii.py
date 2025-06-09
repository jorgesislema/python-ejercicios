"""
Ejercicio 41: Animales de Granja ASCII

Objetivo:
- Crear representaciones ASCII de animales de granja
- Incluir variantes: vaca, cerdo, gallina, oveja, caballo, pato
- Permitir personalización y animaciones simples

Conceptos:
- Arte ASCII de animales
- Menú interactivo
- Uso de funciones y cadenas multilinea
"""

def vaca_ascii():
    print("🐄 VACA ASCII 🐄\n" + "═"*30)
    print(r"""
         ^__^
         (oo)\_______
         (__)\       )\/\
             ||----w |
             ||     ||
    """)

def cerdo_ascii():
    print("🐖 CERDO ASCII 🐖\n" + "═"*30)
    print(r"""
      ^-----^
     ( ' o ' )
     (  -  )
     (     )
      """""" 
    """)

def gallina_ascii():
    print("🐔 GALLINA ASCII 🐔\n" + "═"*30)
    print(r"""
      _
     (o>
\\_//)
 \_/_)
  _|_  
    """)

def oveja_ascii():
    print("🐑 OVEJA ASCII 🐑\n" + "═"*30)
    print(r"""
      __  
    (oo)\_______
    (__)\       )\/\
        ||----w |
        ||     ||
    """)

def caballo_ascii():
    print("🐎 CABALLO ASCII 🐎\n" + "═"*30)
    print(r"""
      ,--.  
     /    \
    /_/|__|
    ( o_o )
     `---' 
    """)

def pato_ascii():
    print("🦆 PATO ASCII 🦆\n" + "═"*30)
    print(r"""
     __
   <(o )___
    ( ._> /
     `---' 
    """)

def menu_principal():
    while True:
        print("\n" + "═"*40)
        print("🐄 ANIMALES DE GRANJA ASCII 🐖")
        print("═"*40)
        print("1. Vaca")
        print("2. Cerdo")
        print("3. Gallina")
        print("4. Oveja")
        print("5. Caballo")
        print("6. Pato")
        print("0. Salir")
        print("═"*40)
        opcion = input("Selecciona un animal: ")
        if opcion == "1":
            vaca_ascii()
        elif opcion == "2":
            cerdo_ascii()
        elif opcion == "3":
            gallina_ascii()
        elif opcion == "4":
            oveja_ascii()
        elif opcion == "5":
            caballo_ascii()
        elif opcion == "6":
            pato_ascii()
        elif opcion == "0":
            print("¡Hasta luego, granjero! 🐄")
            break
        else:
            print("Opción no válida")
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
