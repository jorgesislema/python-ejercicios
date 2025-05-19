"""
Ejercicio: Métodos Estáticos y de Clase
--------------------------------------
Este ejercicio demuestra los métodos estáticos y métodos de clase en Python.
"""

class Calculadora:
    """
    Clase que proporciona métodos estáticos para operaciones matemáticas básicas.
    """
    
    @staticmethod
    def sumar(a, b):
        """
        Método estático para sumar dos números.
        
        Args:
            a (float): Primer número
            b (float): Segundo número
            
        Returns:
            float: Suma de los dos números
        """
        return a + b
    
    @staticmethod
    def restar(a, b):
        """
        Método estático para restar dos números.
        
        Args:
            a (float): Primer número
            b (float): Segundo número
            
        Returns:
            float: Resta de los dos números
        """
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        """
        Método estático para multiplicar dos números.
        
        Args:
            a (float): Primer número
            b (float): Segundo número
            
        Returns:
            float: Multiplicación de los dos números
        """
        return a * b
    
    @staticmethod
    def dividir(a, b):
        """
        Método estático para dividir dos números.
        
        Args:
            a (float): Numerador
            b (float): Denominador
            
        Returns:
            float: División de los dos números
            
        Raises:
            ZeroDivisionError: Si el denominador es cero
        """
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b
    
    @staticmethod
    def es_par(numero):
        """
        Método estático para determinar si un número es par.
        
        Args:
            numero (int): Número a comprobar
            
        Returns:
            bool: True si el número es par, False en caso contrario
        """
        return numero % 2 == 0
    
    @staticmethod
    def es_primo(numero):
        """
        Método estático para determinar si un número es primo.
        
        Args:
            numero (int): Número a comprobar
            
        Returns:
            bool: True si el número es primo, False en caso contrario
        """
        if numero <= 1:
            return False
        if numero <= 3:
            return True
        if numero % 2 == 0 or numero % 3 == 0:
            return False
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True

class Fecha:
    """
    Clase que representa una fecha y proporciona métodos estáticos y de clase
    para trabajar con fechas.
    """
    
    # Variable de clase para almacenar los días en cada mes
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def __init__(self, dia=1, mes=1, anio=2023):
        """
        Constructor de la clase Fecha.
        
        Args:
            dia (int, opcional): Día del mes
            mes (int, opcional): Mes del año (1-12)
            anio (int, opcional): Año
            
        Raises:
            ValueError: Si la fecha no es válida
        """
        if not Fecha.es_fecha_valida(dia, mes, anio):
            raise ValueError("Fecha no válida")
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    @classmethod
    def es_bisiesto(cls, anio):
        """
        Método de clase para determinar si un año es bisiesto.
        
        Args:
            anio (int): Año a comprobar
            
        Returns:
            bool: True si el año es bisiesto, False en caso contrario
        """
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
    
    @classmethod
    def dias_en_mes(cls, mes, anio):
        """
        Método de clase para determinar el número de días en un mes.
        
        Args:
            mes (int): Mes del año (1-12)
            anio (int): Año
            
        Returns:
            int: Número de días en el mes
            
        Raises:
            ValueError: Si el mes no es válido
        """
        if not 1 <= mes <= 12:
            raise ValueError("Mes no válido")
        
        dias = cls.dias_por_mes[mes]
        if mes == 2 and cls.es_bisiesto(anio):
            dias += 1
        
        return dias
    
    @classmethod
    def es_fecha_valida(cls, dia, mes, anio):
        """
        Método de clase para determinar si una fecha es válida.
        
        Args:
            dia (int): Día del mes
            mes (int): Mes del año (1-12)
            anio (int): Año
            
        Returns:
            bool: True si la fecha es válida, False en caso contrario
        """
        if not 1 <= mes <= 12:
            return False
            
        return 1 <= dia <= cls.dias_en_mes(mes, anio)
    
    @classmethod
    def desde_string(cls, fecha_str):
        """
        Método de clase (factory) para crear una instancia de Fecha a partir
        de un string en formato 'dd/mm/aaaa'.
        
        Args:
            fecha_str (str): String con la fecha en formato 'dd/mm/aaaa'
            
        Returns:
            Fecha: Nueva instancia de Fecha
            
        Raises:
            ValueError: Si el formato de la fecha no es válido o la fecha no es válida
        """
        try:
            dia, mes, anio = map(int, fecha_str.split('/'))
            return cls(dia, mes, anio)
        except:
            raise ValueError("Formato de fecha no válido. Use 'dd/mm/aaaa'")
    
    def __str__(self):
        """
        Representación en string de la fecha.
        
        Returns:
            str: Fecha en formato 'dd/mm/aaaa'
        """
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio:04d}"

# Ejemplo de uso
if __name__ == "__main__":
    # Uso de métodos estáticos
    print("Uso de métodos estáticos en Calculadora:")
    print(f"5 + 3 = {Calculadora.sumar(5, 3)}")
    print(f"5 - 3 = {Calculadora.restar(5, 3)}")
    print(f"5 * 3 = {Calculadora.multiplicar(5, 3)}")
    print(f"5 / 3 = {Calculadora.dividir(5, 3):.2f}")
    print(f"¿Es 10 un número par? {Calculadora.es_par(10)}")
    print(f"¿Es 7 un número primo? {Calculadora.es_primo(7)}")
    
    print("\nUso de métodos de clase en Fecha:")
    print(f"¿Es 2024 un año bisiesto? {Fecha.es_bisiesto(2024)}")
    print(f"¿Es 2023 un año bisiesto? {Fecha.es_bisiesto(2023)}")
    print(f"Días en febrero de 2024: {Fecha.dias_en_mes(2, 2024)}")
    print(f"Días en febrero de 2023: {Fecha.dias_en_mes(2, 2023)}")
    
    # Crear instancias de Fecha
    fecha1 = Fecha(15, 9, 2023)
    print(f"\nFecha creada con constructor: {fecha1}")
    
    fecha2 = Fecha.desde_string("25/12/2023")
    print(f"Fecha creada desde string: {fecha2}")
    
    # Validar fechas
    try:
        fecha_invalida = Fecha(31, 2, 2023)  # 31 de febrero no existe
    except ValueError as e:
        print(f"\nError al crear fecha inválida: {e}")
        
    try:
        fecha_invalida = Fecha.desde_string("31/02/2023")  # 31 de febrero no existe
    except ValueError as e:
        print(f"Error al crear fecha inválida desde string: {e}")
