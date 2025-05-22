"""
Ejercicio 2: Formato de Cadenas Avanzado

Objetivo: Dominar técnicas avanzadas de formateo de cadenas en Python.

Instrucciones:
1. Explora diferentes métodos de formateo de cadenas (f-strings, str.format(), Template).
2. Implementa ejemplos de formateo con alineación, relleno y precisión.
3. Utiliza técnicas de localización y formateo específico de idioma.
4. Crea funciones para generar salidas formateadas complejas.
"""

import string
import locale
import datetime
import re
from string import Template

def main():
    # F-strings avanzados (Python 3.6+)
    print("=== F-strings Avanzados ===")
    
    nombre = "Ana"
    edad = 28
    altura = 1.75
    lenguajes = ["Python", "JavaScript", "Go"]
    
    # Expresiones dentro de f-strings
    print(f"Nombre en mayúsculas: {nombre.upper()}")
    print(f"Edad en 5 años: {edad + 5}")
    print(f"¿Mayor de edad? {'Sí' if edad >= 18 else 'No'}")
    
    # Formateo de números
    print(f"Altura con 1 decimal: {altura:.1f}")
    print(f"Edad en binario: {edad:#b}")
    print(f"Edad en formato: {edad:+}")
    
    # Alineación y relleno
    for lang in lenguajes:
        print(f"| {lang:<10} |")  # Alineado a la izquierda con ancho 10
    
    for i, lang in enumerate(lenguajes, 1):
        print(f"| {i:02d} | {lang:^15} |")  # Número con relleno de ceros y texto centrado
    
    # Usando variables de formato dentro de f-strings
    width = 15
    precision = 2
    print(f"Altura con ancho {width} y precisión {precision}: {altura:{width}.{precision}f}")
    
    # Método str.format() avanzado
    print("\n=== Método str.format() Avanzado ===")
    
    # Acceso por posición, nombre y atributos
    coords = (3, 5)
    punto = {'x': 10, 'y': 20}
    
    print("Coordenadas: ({0}, {1})".format(*coords))
    print("Punto: ({x}, {y})".format(**punto))
    
    # Alineación y formateo
    tabla = "{0:=^30}".format(" TABLA DE DATOS ")
    print(tabla)
    print("{0:<15}|{1:^15}".format("NOMBRE", "EDAD"))
    print("{0:-<30}".format(""))
    print("{0:<15}|{1:^15}".format("Ana", 28))
    print("{0:<15}|{1:^15}".format("Carlos", 35))
    
    # Formateo de fechas
    ahora = datetime.datetime.now()
    print("Fecha: {:%d/%m/%Y %H:%M}".format(ahora))
    print("Fecha: {:%A %d de %B de %Y}".format(ahora))
    
    # Acceso a elementos específicos
    datos = ["Python", 3.9, 2021]
    print("Lenguaje {0[0]}, versión {0[1]}, año {0[2]}".format(datos))
    
    # String Template
    print("\n=== String Template ===")
    
    # Template básico
    t = Template("$nombre tiene $edad años")
    resultado = t.substitute(nombre="Luis", edad=42)
    print(resultado)
    
    # Template con diccionario
    datos = {'nombre': 'María', 'edad': 33, 'profesion': 'Ingeniera'}
    t = Template("$nombre es $profesion y tiene $edad años")
    print(t.substitute(datos))
    
    # Template con delimitadores personalizados
    class CustomTemplate(Template):
        delimiter = '%'
        
    ct = CustomTemplate("%nombre trabaja en %empresa")
    print(ct.substitute(nombre="Juan", empresa="Google"))
    
    # Template seguro (safe_substitute)
    t = Template("$nombre trabaja en $empresa")
    print(t.safe_substitute(nombre="Pedro"))  # No da error si falta una variable
    
    # Localización y formateo regional
    print("\n=== Localización y Formateo Regional ===")
    
    # Configurar locale
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        print("Locale configurado para español (España)")
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'Spanish_Spain')
            print("Locale configurado para español (Windows)")
        except locale.Error:
            print("No se pudo configurar el locale para español, usando el predeterminado")
    
    # Formateo de fechas según locale
    fecha = datetime.datetime.now()
    try:
        fecha_local = fecha.strftime("%A, %d de %B de %Y")
        print(f"Fecha formateada según locale: {fecha_local}")
    except:
        print("Error al formatear fecha con locale")
    
    # Formateo de números según locale
    try:
        num = 1234567.89
        num_local = locale.format_string("%.2f", num, grouping=True)
        print(f"Número formateado según locale: {num_local}")
        
        moneda_local = locale.currency(num, grouping=True)
        print(f"Moneda formateada según locale: {moneda_local}")
    except:
        print("Error al formatear números con locale")
    
    # Restaurar locale predeterminado
    locale.setlocale(locale.LC_ALL, '')
    
    # Formateo de cadenas con expresiones regulares
    print("\n=== Formateo con Expresiones Regulares ===")
    
    # Reemplazar patrones en texto
    texto = "Mi teléfono es 123-456-789 y mi código postal es 28001"
    
    # Ocultar parte del número de teléfono
    patron_telefono = r'(\d{3})-(\d{3})-(\d{3})'
    telefono_oculto = re.sub(patron_telefono, r'\1-XXX-\3', texto)
    print(f"Teléfono parcialmente oculto: {telefono_oculto}")
    
    # Formatear códigos postales
    patron_cp = r'(\d{5})'
    cp_formateado = re.sub(patron_cp, r'CP: \1', texto)
    print(f"Código postal formateado: {cp_formateado}")
    
    # Ejemplos de uso práctico
    print("\n=== Ejemplos de Uso Práctico ===")
    
    # Generación de informes
    def generar_informe(titulo, datos, ancho=80):
        """Genera un informe formateado con título y datos."""
        linea = "=" * ancho
        titulo_centrado = f"{titulo:^{ancho}}"
        
        informe = [linea, titulo_centrado, linea]
        
        # Formatear cada línea de datos
        for key, value in datos.items():
            if isinstance(value, float):
                valor_fmt = f"{value:.2f}"
            elif isinstance(value, (list, tuple)):
                valor_fmt = ", ".join(str(v) for v in value)
            else:
                valor_fmt = str(value)
            
            informe.append(f"{key:<20}: {valor_fmt}")
        
        informe.append(linea)
        return "\n".join(informe)
    
    # Datos para el informe
    datos_informe = {
        "Nombre": "Proyecto X",
        "Presupuesto": 125000.75,
        "Equipo": ["Ana", "Luis", "Carlos", "María"],
        "Fecha inicio": "15/05/2022",
        "Duración (meses)": 6,
        "Estado": "En progreso"
    }
    
    informe = generar_informe("INFORME DE PROYECTO", datos_informe)
    print(informe)
    
    # Formateo de tabla de datos
    def crear_tabla(headers, rows, separador="|"):
        """Crea una tabla formateada con encabezados y filas de datos."""
        # Determinar el ancho de cada columna
        anchos = [len(h) for h in headers]
        for fila in rows:
            for i, celda in enumerate(fila):
                anchos[i] = max(anchos[i], len(str(celda)))
        
        # Crear líneas de la tabla
        formato_fila = separador + separador.join(f" {{:{anchos[i]}}} " for i in range(len(headers))) + separador
        separador_fila = "+" + "+".join("-" * (anchos[i] + 2) for i in range(len(headers))) + "+"
        
        # Construir la tabla
        tabla = [separador_fila]
        tabla.append(formato_fila.format(*headers))
        tabla.append(separador_fila)
        
        for fila in rows:
            tabla.append(formato_fila.format(*[str(celda) for celda in fila]))
        
        tabla.append(separador_fila)
        return "\n".join(tabla)
    
    # Datos para la tabla
    encabezados = ["Producto", "Cantidad", "Precio", "Total"]
    filas = [
        ["Laptop", 1, 999.99, 999.99],
        ["Mouse", 2, 25.50, 51.00],
        ["Monitor", 1, 249.99, 249.99]
    ]
    
    tabla_productos = crear_tabla(encabezados, filas)
    print("\nTabla de Productos:")
    print(tabla_productos)
    
    # Ejercicios para el usuario
    print("\n=== EJERCICIOS PARA PRACTICAR ===")
    print("1. Crea una función que genere un código de barras formateado (por ejemplo, ISBN) con guiones en posiciones específicas")
    print("2. Implementa una función que formatee fechas en diferentes estilos según el país (USA, Europa, Asia)")
    print("3. Desarrolla un generador de tarjetas de presentación con alineación y formateo personalizado")
    print("4. Crea una función que formatee automáticamente un texto para imprimirlo como un poema, con sangría y alineación específicas")

if __name__ == "__main__":
    main()
