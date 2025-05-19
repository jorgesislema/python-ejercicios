"""
Ejercicio: Propiedades (Properties)
---------------------------------
Este ejercicio demuestra el uso de propiedades (@property) en Python como forma
moderna de implementar getter y setters.
"""

class Temperatura:
    """
    Clase para manejar conversiones de temperatura entre Celsius y Fahrenheit
    usando propiedades de Python.
    """
    def __init__(self, celsius=0):
        """
        Constructor de la clase Temperatura.
        
        Args:
            celsius (float, opcional): Temperatura inicial en grados Celsius
        """
        self._celsius = celsius
    
    @property
    def celsius(self):
        """
        Propiedad getter para obtener la temperatura en Celsius.
        
        Returns:
            float: Temperatura en grados Celsius
        """
        return self._celsius
        
    @celsius.setter
    def celsius(self, valor):
        """
        Propiedad setter para establecer la temperatura en Celsius.
        
        Args:
            valor (float): Nueva temperatura en grados Celsius
            
        Raises:
            ValueError: Si el valor es menor que el cero absoluto (-273.15°C)
        """
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto (–273.15°C)")
        self._celsius = valor
        
    @property
    def fahrenheit(self):
        """
        Propiedad getter para obtener la temperatura en Fahrenheit.
        
        Returns:
            float: Temperatura en grados Fahrenheit
        """
        return (self._celsius * 9/5) + 32
        
    @fahrenheit.setter
    def fahrenheit(self, valor):
        """
        Propiedad setter para establecer la temperatura en Fahrenheit.
        
        Args:
            valor (float): Nueva temperatura en grados Fahrenheit
            
        Raises:
            ValueError: Si el valor equivalente en Celsius es menor que el cero absoluto
        """
        celsius_equiv = (valor - 32) * 5/9
        if celsius_equiv < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto (–459.67°F)")
        self._celsius = celsius_equiv
        
    @property
    def kelvin(self):
        """
        Propiedad getter para obtener la temperatura en Kelvin.
        
        Returns:
            float: Temperatura en Kelvin
        """
        return self._celsius + 273.15
        
    @kelvin.setter
    def kelvin(self, valor):
        """
        Propiedad setter para establecer la temperatura en Kelvin.
        
        Args:
            valor (float): Nueva temperatura en Kelvin
            
        Raises:
            ValueError: Si el valor es menor que 0 (cero absoluto)
        """
        if valor < 0:
            raise ValueError("La temperatura en Kelvin no puede ser menor que 0")
        self._celsius = valor - 273.15
        
    def __str__(self):
        """
        Representación en string de la temperatura en las tres escalas.
        
        Returns:
            str: Representación en string de la temperatura
        """
        return f"{self._celsius:.2f}°C = {self.fahrenheit:.2f}°F = {self.kelvin:.2f}K"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia con una temperatura en Celsius
    temp = Temperatura(25)
    print(f"Temperatura inicial: {temp}")
    
    # Usar las propiedades de solo lectura
    print(f"En Celsius: {temp.celsius}°C")
    print(f"En Fahrenheit: {temp.fahrenheit}°F")
    print(f"En Kelvin: {temp.kelvin}K")
    
    # Cambiar la temperatura usando el setter de Celsius
    print("\nCambiando a 30°C:")
    temp.celsius = 30
    print(temp)
    
    # Cambiar la temperatura usando el setter de Fahrenheit
    print("\nCambiando a 68°F:")
    temp.fahrenheit = 68
    print(temp)
    
    # Cambiar la temperatura usando el setter de Kelvin
    print("\nCambiando a 300K:")
    temp.kelvin = 300
    print(temp)
    
    # Validación de errores
    try:
        print("\nIntentando establecer una temperatura imposible:")
        temp.celsius = -300
    except ValueError as e:
        print(f"Error capturado: {e}")
