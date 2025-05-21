"""
Quiz de Autoevaluación sobre Manejo de Errores en Python

Este script proporciona un quiz interactivo para evaluar 
los conocimientos sobre manejo de errores en Python.
"""

import random
import time
import os

# Lista de preguntas y respuestas para el quiz
preguntas = [
    {
        "pregunta": "¿Qué bloque se ejecuta siempre, ocurra o no una excepción?",
        "opciones": ["try", "except", "else", "finally"],
        "respuesta": "finally",
        "explicacion": "El bloque 'finally' siempre se ejecuta, independientemente de si ocurre una excepción o no."
    },
    {
        "pregunta": "¿Qué excepción se lanza cuando intentamos dividir por cero?",
        "opciones": ["ValueError", "ArithmeticError", "ZeroDivisionError", "TypeError"],
        "respuesta": "ZeroDivisionError",
        "explicacion": "ZeroDivisionError se lanza cuando el segundo operando de una división o módulo es cero."
    },
    {
        "pregunta": "¿Qué palabra clave se usa para lanzar manualmente una excepción?",
        "opciones": ["throw", "raise", "except", "error"],
        "respuesta": "raise",
        "explicacion": "La palabra clave 'raise' se utiliza para lanzar una excepción manualmente."
    },
    {
        "pregunta": "¿Qué sucede si una excepción no es capturada por ningún bloque except?",
        "opciones": ["Se ignora", "El programa continúa normalmente", "El programa termina", "Se guarda en un log"],
        "respuesta": "El programa termina",
        "explicacion": "Si una excepción no es capturada, se propaga hacia arriba en la pila de llamadas hasta terminar el programa."
    },
    {
        "pregunta": "¿Cuál es la clase base de todas las excepciones en Python?",
        "opciones": ["Error", "Exception", "BaseException", "StandardError"],
        "respuesta": "BaseException",
        "explicacion": "BaseException es la clase base para todas las excepciones integradas en Python."
    },
    {
        "pregunta": "¿Qué se utiliza para crear un manejador de contexto personalizado?",
        "opciones": ["Decorador @context", "Métodos __enter__ y __exit__", "Clase ContextManager", "Función with_context()"],
        "respuesta": "Métodos __enter__ y __exit__",
        "explicacion": "Para crear un manejador de contexto personalizado, se implementan los métodos __enter__ y __exit__ en una clase."
    },
    {
        "pregunta": "¿Cuál de las siguientes NO es una buena práctica en el manejo de errores?",
        "opciones": ["Capturar excepciones específicas", "Registrar información de errores", "Usar except: sin especificar la excepción", "Proporcionar mensajes de error claros"],
        "respuesta": "Usar except: sin especificar la excepción",
        "explicacion": "Capturar todas las excepciones sin especificar el tipo puede ocultar errores inesperados y dificultar la depuración."
    },
    {
        "pregunta": "¿Qué función se utiliza comúnmente para validar condiciones y lanzar una excepción si no se cumplen?",
        "opciones": ["validate()", "check()", "assert", "verify()"],
        "respuesta": "assert",
        "explicacion": "La declaración 'assert' evalúa una condición y lanza una AssertionError si la condición es falsa."
    },
    {
        "pregunta": "¿En qué caso es más adecuado crear excepciones personalizadas?",
        "opciones": ["Nunca, siempre se deben usar las excepciones estándar", "Para representar errores específicos del dominio de la aplicación", "Solo para errores de sintaxis", "Solo para proyectos grandes"],
        "respuesta": "Para representar errores específicos del dominio de la aplicación",
        "explicacion": "Las excepciones personalizadas son útiles para representar errores específicos del dominio o lógica de negocio."
    },
    {
        "pregunta": "¿Qué función permite obtener información sobre la excepción actual en el bloque except?",
        "opciones": ["get_error()", "sys.exc_info()", "exception.info()", "traceback()"],
        "respuesta": "sys.exc_info()",
        "explicacion": "sys.exc_info() devuelve una tupla con información sobre la excepción que se está manejando actualmente."
    },
    {
        "pregunta": "¿Qué sucede en un bloque 'else' después de un try-except?",
        "opciones": ["Se ejecuta si ocurre alguna excepción", "Se ejecuta si no ocurre ninguna excepción", "Se ejecuta siempre", "Se ejecuta solo para ciertos tipos de excepciones"],
        "respuesta": "Se ejecuta si no ocurre ninguna excepción",
        "explicacion": "El bloque 'else' se ejecuta solo si no se produce ninguna excepción en el bloque 'try'."
    },
    {
        "pregunta": "¿Cuál es la ventaja principal de usar with para manejar recursos?",
        "opciones": ["Es más rápido", "Garantiza que los recursos se liberan adecuadamente", "Evita todos los errores", "Reduce el consumo de memoria"],
        "respuesta": "Garantiza que los recursos se liberan adecuadamente",
        "explicacion": "El uso de 'with' garantiza que los recursos (como archivos) se cierren adecuadamente, incluso si ocurren excepciones."
    },
    {
        "pregunta": "¿Qué excepción se lanza cuando intentamos acceder a una clave que no existe en un diccionario?",
        "opciones": ["IndexError", "KeyError", "LookupError", "ValueError"],
        "respuesta": "KeyError",
        "explicacion": "KeyError se lanza cuando intentamos acceder a una clave que no existe en un diccionario."
    },
    {
        "pregunta": "¿Cuál es el método más seguro para verificar si una clave existe en un diccionario?",
        "opciones": ["dict.has_key()", "key in dict", "dict.contains(key)", "try-except con KeyError"],
        "respuesta": "key in dict",
        "explicacion": "El operador 'in' es la forma más clara y eficiente de verificar si una clave existe en un diccionario."
    },
    {
        "pregunta": "¿Qué módulo proporciona funciones para capturar y formatear trazas de pila de excepción?",
        "opciones": ["sys", "traceback", "errorhandler", "exception"],
        "respuesta": "traceback",
        "explicacion": "El módulo 'traceback' proporciona funciones para extraer, formatear y mostrar trazas de pila de excepciones."
    }
]

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_cabecera():
    """Muestra la cabecera del quiz."""
    limpiar_pantalla()
    print("=" * 70)
    print("QUIZ DE AUTOEVALUACIÓN: MANEJO DE ERRORES EN PYTHON".center(70))
    print("=" * 70)
    print("\nEvalúa tus conocimientos sobre manejo de errores en Python.")
    print("Responde las siguientes preguntas seleccionando la opción correcta.\n")

def realizar_quiz():
    """Realiza el quiz y muestra la puntuación final."""
    mostrar_cabecera()
    
    # Mezclar las preguntas
    preguntas_quiz = random.sample(preguntas, min(10, len(preguntas)))
    puntuacion = 0
    total_preguntas = len(preguntas_quiz)
    
    for i, pregunta_data in enumerate(preguntas_quiz, 1):
        print(f"Pregunta {i} de {total_preguntas}:")
        print(f"\n{pregunta_data['pregunta']}\n")
        
        # Mostrar opciones mezcladas
        opciones = pregunta_data['opciones'].copy()
        random.shuffle(opciones)
        
        # Guardar la posición de la respuesta correcta
        respuesta_correcta_index = None
        for j, opcion in enumerate(opciones, 1):
            print(f"{j}. {opcion}")
            if opcion == pregunta_data['respuesta']:
                respuesta_correcta_index = j
        
        # Obtener respuesta del usuario
        try:
            respuesta = input("\nTu respuesta (número): ")
            respuesta_num = int(respuesta)
            
            if respuesta_num < 1 or respuesta_num > len(opciones):
                print("\n❌ Respuesta inválida. Debe ser un número entre 1 y", len(opciones))
            else:
                if opciones[respuesta_num-1] == pregunta_data['respuesta']:
                    print("\n✅ ¡Correcto! " + pregunta_data['explicacion'])
                    puntuacion += 1
                else:
                    print(f"\n❌ Incorrecto. La respuesta correcta es: {respuesta_correcta_index}. {pregunta_data['respuesta']}")
                    print(pregunta_data['explicacion'])
        except ValueError:
            print("\n❌ Entrada inválida. Debes ingresar un número.")
        
        # Pausa antes de la siguiente pregunta
        input("\nPresiona Enter para continuar...")
        mostrar_cabecera()
    
    # Mostrar puntuación final
    porcentaje = (puntuacion / total_preguntas) * 100
    print("\n" + "=" * 70)
    print(f"PUNTUACIÓN FINAL: {puntuacion}/{total_preguntas} ({porcentaje:.1f}%)".center(70))
    
    if porcentaje >= 90:
        mensaje = "¡Excelente! Tienes un dominio excepcional del manejo de errores."
    elif porcentaje >= 70:
        mensaje = "¡Muy bien! Tienes buen conocimiento del manejo de errores."
    elif porcentaje >= 50:
        mensaje = "Bien. Has aprendido lo básico, pero puedes mejorar."
    else:
        mensaje = "Necesitas repasar más. Revisa los ejercicios y la documentación."
    
    print(mensaje.center(70))
    print("=" * 70)

def menu_principal():
    """Muestra el menú principal del quiz."""
    while True:
        mostrar_cabecera()
        print("\n1. Iniciar Quiz")
        print("2. Salir")
        
        opcion = input("\nSelecciona una opción (1-2): ")
        
        if opcion == "1":
            realizar_quiz()
        elif opcion == "2":
            print("\n¡Gracias por usar el quiz de autoevaluación!")
            break
        else:
            print("\nOpción no válida.")
            time.sleep(1)

if __name__ == "__main__":
    menu_principal()
