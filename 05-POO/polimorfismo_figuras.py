"""
Ejercicio: Polimorfismo
----------------------
Este ejercicio demuestra el concepto de polimorfismo en la programación orientada a objetos,
usando figuras geométricas como ejemplo.
"""

import math

class Figura:
    """
    Clase base abstracta para figuras geométricas.
    """
    def area(self):
        """
        Método abstracto para calcular el área de la figura.
        
        Raises:
            NotImplementedError: Si la clase hija no implementa este método
        """
        raise NotImplementedError("Las clases hijas deben implementar este método")
    
    def perimetro(self):
        """
        Método abstracto para calcular el perímetro de la figura.
        
        Raises:
            NotImplementedError: Si la clase hija no implementa este método
        """
        raise NotImplementedError("Las clases hijas deben implementar este método")
    
    def describir(self):
        """
        Método que describe la figura y sus propiedades.
        """
        return f"Soy una figura con área {self.area()} y perímetro {self.perimetro()}"

class Circulo(Figura):
    """
    Clase que representa un círculo.
    """
    def __init__(self, radio):
        """
        Constructor de la clase Circulo.
        
        Args:
            radio (float): Radio del círculo
        """
        self.radio = radio
    
    def area(self):
        """
        Calcula el área del círculo.
        
        Returns:
            float: Área del círculo
        """
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        """
        Calcula el perímetro (circunferencia) del círculo.
        
        Returns:
            float: Perímetro del círculo
        """
        return 2 * math.pi * self.radio
    
    def describir(self):
        """
        Descripción específica del círculo.
        
        Returns:
            str: Descripción del círculo
        """
        return f"Soy un círculo de radio {self.radio}, área {self.area():.2f} y perímetro {self.perimetro():.2f}"

class Rectangulo(Figura):
    """
    Clase que representa un rectángulo.
    """
    def __init__(self, ancho, alto):
        """
        Constructor de la clase Rectangulo.
        
        Args:
            ancho (float): Ancho del rectángulo
            alto (float): Alto del rectángulo
        """
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        """
        Calcula el área del rectángulo.
        
        Returns:
            float: Área del rectángulo
        """
        return self.ancho * self.alto
    
    def perimetro(self):
        """
        Calcula el perímetro del rectángulo.
        
        Returns:
            float: Perímetro del rectángulo
        """
        return 2 * (self.ancho + self.alto)
    
    def describir(self):
        """
        Descripción específica del rectángulo.
        
        Returns:
            str: Descripción del rectángulo
        """
        return f"Soy un rectángulo de {self.ancho}x{self.alto}, área {self.area()} y perímetro {self.perimetro()}"

class Triangulo(Figura):
    """
    Clase que representa un triángulo.
    """
    def __init__(self, lado1, lado2, lado3):
        """
        Constructor de la clase Triangulo.
        
        Args:
            lado1 (float): Primer lado del triángulo
            lado2 (float): Segundo lado del triángulo
            lado3 (float): Tercer lado del triángulo
            
        Raises:
            ValueError: Si los lados no pueden formar un triángulo válido
        """
        # Comprobar si los lados pueden formar un triángulo
        if (lado1 + lado2 <= lado3) or (lado1 + lado3 <= lado2) or (lado2 + lado3 <= lado1):
            raise ValueError("Los lados proporcionados no pueden formar un triángulo válido")
            
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        """
        Calcula el área del triángulo usando la fórmula de Herón.
        
        Returns:
            float: Área del triángulo
        """
        # Semiperímetro
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        # Fórmula de Herón
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
    
    def perimetro(self):
        """
        Calcula el perímetro del triángulo.
        
        Returns:
            float: Perímetro del triángulo
        """
        return self.lado1 + self.lado2 + self.lado3
    
    def describir(self):
        """
        Descripción específica del triángulo.
        
        Returns:
            str: Descripción del triángulo
        """
        return f"Soy un triángulo con lados {self.lado1}, {self.lado2} y {self.lado3}, área {self.area():.2f} y perímetro {self.perimetro()}"

def calcular_area_total(figuras):
    """
    Función que demuestra el polimorfismo al calcular el área total de varias figuras,
    independientemente del tipo específico de cada una.
    
    Args:
        figuras (list): Lista de objetos que heredan de Figura
        
    Returns:
        float: Suma total de las áreas de todas las figuras
    """
    area_total = 0
    for figura in figuras:
        area_total += figura.area()
    return area_total

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de diferentes figuras
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    triangulo = Triangulo(3, 4, 5)
    
    # Mostrar descripciones específicas de cada figura
    print(circulo.describir())
    print(rectangulo.describir())
    print(triangulo.describir())
    
    # Demostrar polimorfismo
    figuras = [circulo, rectangulo, triangulo]
    area_total = calcular_area_total(figuras)
    print(f"\nEl área total de todas las figuras es: {area_total:.2f}")
