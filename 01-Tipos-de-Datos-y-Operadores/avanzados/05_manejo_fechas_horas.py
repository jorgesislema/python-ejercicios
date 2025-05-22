"""
Ejercicio 5: Manejo de Fechas y Horas

Objetivo: Aprender a trabajar con fechas, horas y zonas horarias en Python.

Instrucciones:
1. Utilizar los módulos datetime, time y calendar para manipular fechas y horas.
2. Realizar operaciones como suma, resta y comparación de fechas.
3. Formatear fechas y horas en diferentes formatos de presentación.
4. Trabajar con zonas horarias utilizando el módulo pytz.
"""

import datetime
import time
import calendar
import locale
try:
    import pytz
    pytz_available = True
except ImportError:
    print("Nota: El módulo pytz no está instalado. Algunas funcionalidades de zona horaria no estarán disponibles.")
    pytz_available = False

def main():
    # Módulo datetime
    print("=== Módulo datetime ===")
    
    # Crear objetos date
    fecha_actual = datetime.date.today()
    fecha_especifica = datetime.date(2025, 5, 21)
    
    print(f"Fecha actual: {fecha_actual}")
    print(f"Fecha específica: {fecha_especifica}")
    
    # Atributos de date
    print(f"Año: {fecha_actual.year}")
    print(f"Mes: {fecha_actual.month}")
    print(f"Día: {fecha_actual.day}")
    
    # Crear objetos time
    hora_actual = datetime.datetime.now().time()
    hora_especifica = datetime.time(14, 30, 45)
    
    print(f"Hora actual: {hora_actual}")
    print(f"Hora específica: {hora_especifica}")
    
    # Atributos de time
    print(f"Hora: {hora_especifica.hour}")
    print(f"Minuto: {hora_especifica.minute}")
    print(f"Segundo: {hora_especifica.second}")
    print(f"Microsegundo: {hora_especifica.microsecond}")
    
    # Crear objetos datetime
    dt_actual = datetime.datetime.now()
    dt_especifico = datetime.datetime(2025, 5, 21, 14, 30, 45)
    
    print(f"Datetime actual: {dt_actual}")
    print(f"Datetime específico: {dt_especifico}")
    
    # Operaciones con fechas
    print("\n=== Operaciones con Fechas ===")
    
    # Diferencia entre fechas
    delta = fecha_especifica - fecha_actual
    print(f"Días de diferencia: {delta.days}")
    
    # Sumar días a una fecha
    manana = fecha_actual + datetime.timedelta(days=1)
    print(f"Mañana: {manana}")
    
    # Restar días a una fecha
    ayer = fecha_actual - datetime.timedelta(days=1)
    print(f"Ayer: {ayer}")
    
    # Operaciones más complejas con timedelta
    una_semana_despues = dt_actual + datetime.timedelta(weeks=1)
    dos_horas_antes = dt_actual - datetime.timedelta(hours=2)
    tiempo_personalizado = dt_actual + datetime.timedelta(days=10, hours=5, minutes=30)
    
    print(f"Una semana después: {una_semana_despues}")
    print(f"Dos horas antes: {dos_horas_antes}")
    print(f"Tiempo personalizado: {tiempo_personalizado}")
    
    # Comparación de fechas
    print("\n=== Comparación de Fechas ===")
    
    es_anterior = fecha_actual < fecha_especifica
    es_posterior = fecha_actual > fecha_especifica
    es_igual = fecha_actual == fecha_especifica
    
    print(f"¿Fecha actual es anterior a fecha específica? {es_anterior}")
    print(f"¿Fecha actual es posterior a fecha específica? {es_posterior}")
    print(f"¿Fecha actual es igual a fecha específica? {es_igual}")
    
    # Formateo de fechas
    print("\n=== Formateo de Fechas ===")
    
    # Método strftime para formatear fechas
    formato_fecha = dt_actual.strftime("%d/%m/%Y")
    formato_hora = dt_actual.strftime("%H:%M:%S")
    formato_completo = dt_actual.strftime("%A, %d de %B de %Y a las %H:%M:%S")
    
    print(f"Formato fecha (dd/mm/aaaa): {formato_fecha}")
    print(f"Formato hora (hh:mm:ss): {formato_hora}")
    print(f"Formato completo: {formato_completo}")
    
    # Códigos de formato comunes
    print("\n=== Códigos de Formato Comunes ===")
    print(f"%d - Día del mes: {dt_actual.strftime('%d')}")
    print(f"%m - Mes (número): {dt_actual.strftime('%m')}")
    print(f"%B - Mes (nombre): {dt_actual.strftime('%B')}")
    print(f"%y - Año (2 dígitos): {dt_actual.strftime('%y')}")
    print(f"%Y - Año (4 dígitos): {dt_actual.strftime('%Y')}")
    print(f"%H - Hora (formato 24h): {dt_actual.strftime('%H')}")
    print(f"%I - Hora (formato 12h): {dt_actual.strftime('%I')}")
    print(f"%M - Minutos: {dt_actual.strftime('%M')}")
    print(f"%S - Segundos: {dt_actual.strftime('%S')}")
    print(f"%A - Día de la semana: {dt_actual.strftime('%A')}")
    print(f"%a - Día de la semana (abreviado): {dt_actual.strftime('%a')}")
    print(f"%p - AM/PM: {dt_actual.strftime('%p')}")
    
    # Formateo según el locale
    print("\n=== Formateo según el Locale ===")
    
    # Intentar establecer el locale para español
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        print("Locale configurado para español (España)")
    except locale.Error:
        try:
            locale.setlocale(locale.LC_TIME, 'Spanish_Spain')
            print("Locale configurado para español (Windows)")
        except locale.Error:
            print("No se pudo configurar el locale para español, usando el predeterminado")
    
    # Formateo con locale
    formato_local = dt_actual.strftime("%A, %d de %B de %Y")
    print(f"Fecha en formato local: {formato_local}")
    
    # Restaurar locale predeterminado
    locale.setlocale(locale.LC_TIME, '')
    
    # Análisis (parsing) de fechas
    print("\n=== Análisis (Parsing) de Fechas ===")
    
    # Convertir string a objeto datetime
    fecha_str = "21/05/2025 14:30:45"
    fecha_parseada = datetime.datetime.strptime(fecha_str, "%d/%m/%Y %H:%M:%S")
    print(f"String de fecha: '{fecha_str}'")
    print(f"Fecha parseada: {fecha_parseada}")
    
    # Módulo time
    print("\n=== Módulo time ===")
    
    # Timestamp (tiempo Unix)
    timestamp_actual = time.time()
    print(f"Timestamp actual: {timestamp_actual}")
    
    # Convertir timestamp a datetime
    dt_desde_timestamp = datetime.datetime.fromtimestamp(timestamp_actual)
    print(f"Datetime desde timestamp: {dt_desde_timestamp}")
    
    # Convertir datetime a timestamp
    timestamp_desde_dt = dt_actual.timestamp()
    print(f"Timestamp desde datetime: {timestamp_desde_dt}")
    
    # time.sleep para pausar la ejecución
    print("Pausa de 1 segundo...")
    time.sleep(1)
    print("Continuando después de la pausa")
    
    # Módulo calendar
    print("\n=== Módulo calendar ===")
    
    # Obtener el calendario de un mes
    cal = calendar.month(2025, 5)
    print(f"Calendario de Mayo 2025:\n{cal}")
    
    # Verificar si un año es bisiesto
    es_bisiesto_2024 = calendar.isleap(2024)
    es_bisiesto_2025 = calendar.isleap(2025)
    print(f"¿2024 es bisiesto? {es_bisiesto_2024}")
    print(f"¿2025 es bisiesto? {es_bisiesto_2025}")
    
    # Obtener el día de la semana
    # 0 = Lunes, 1 = Martes, ..., 6 = Domingo
    dia_semana = calendar.weekday(2025, 5, 21)
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print(f"21/05/2025 cae en: {dias[dia_semana]}")
    
    # Trabajar con zonas horarias
    if pytz_available:
        print("\n=== Zonas Horarias con pytz ===")
        
        # Listar algunas zonas horarias disponibles
        zonas = ["America/New_York", "Europe/London", "Europe/Madrid", "Asia/Tokyo", "Australia/Sydney"]
        print("Algunas zonas horarias disponibles:")
        for zona in zonas:
            print(f"- {zona}")
        
        # Obtener la hora actual en diferentes zonas horarias
        print("\nHora actual en diferentes zonas:")
        for zona in zonas:
            tz = pytz.timezone(zona)
            dt_zona = datetime.datetime.now(tz)
            print(f"{zona}: {dt_zona.strftime('%H:%M:%S %Z%z')}")
        
        # Convertir entre zonas horarias
        madrid_tz = pytz.timezone("Europe/Madrid")
        tokyo_tz = pytz.timezone("Asia/Tokyo")
        
        # Crear un datetime con zona horaria
        dt_madrid = madrid_tz.localize(datetime.datetime.now())
        print(f"\nHora en Madrid: {dt_madrid.strftime('%H:%M:%S %Z%z')}")
        
        # Convertir a hora de Tokyo
        dt_tokyo = dt_madrid.astimezone(tokyo_tz)
        print(f"La misma hora en Tokyo: {dt_tokyo.strftime('%H:%M:%S %Z%z')}")
        
        # Trabajar con UTC
        dt_utc = datetime.datetime.now(pytz.UTC)
        print(f"Hora UTC: {dt_utc.strftime('%H:%M:%S %Z%z')}")
        
        # Convertir UTC a hora local
        dt_local = dt_utc.astimezone()
        print(f"Hora local desde UTC: {dt_local.strftime('%H:%M:%S %Z%z')}")
    
    # Ejemplos prácticos
    print("\n=== Ejemplos Prácticos ===")
    
    # Calcular edad
    def calcular_edad(fecha_nacimiento):
        hoy = datetime.date.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad
    
    fecha_nacimiento = datetime.date(1990, 5, 15)
    edad = calcular_edad(fecha_nacimiento)
    print(f"Fecha de nacimiento: {fecha_nacimiento}")
    print(f"Edad actual: {edad} años")
    
    # Calcular días hasta un evento
    navidad = datetime.date(datetime.date.today().year, 12, 25)
    if navidad < datetime.date.today():
        navidad = datetime.date(datetime.date.today().year + 1, 12, 25)
    
    dias_hasta_navidad = (navidad - datetime.date.today()).days
    print(f"Días hasta Navidad: {dias_hasta_navidad}")
    
    # Cronómetro simple
    def cronometrar_operacion():
        inicio = time.time()
        
        # Simulación de una operación que toma tiempo
        time.sleep(0.5)
        
        fin = time.time()
        return fin - inicio
    
    tiempo_ejecucion = cronometrar_operacion()
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Crea una función que calcule la diferencia en días, horas, minutos y segundos entre dos fechas")
    print("2. Implementa un programa que muestre un calendario del mes actual, resaltando el día de hoy")
    print("3. Desarrolla una función que convierta una fecha entre diferentes formatos (ISO, americano, europeo)")
    print("4. Crea un programa que muestre la hora actual en tres zonas horarias diferentes simultáneamente")

if __name__ == "__main__":
    main()
