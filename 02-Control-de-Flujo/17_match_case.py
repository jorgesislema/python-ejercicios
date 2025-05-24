"""
Ejercicio 17: match-case (Python 3.10+)

Objetivo: Usar la estructura match-case para múltiples condiciones.

Instrucciones:
- Escribe un programa que pida un día de la semana y muestre si es laborable o fin de semana usando match-case.
"""

dia = input("Introduce un día de la semana: ").lower()

match dia:
    case "lunes" | "martes" | "miércoles" | "miercoles" | "jueves" | "viernes":
        print("Es un día laborable.")
    case "sábado" | "sabado" | "domingo":
        print("Es fin de semana.")
    case _:
        print("Día no reconocido.")
