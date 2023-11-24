# 4.1. FiguraGeometrica: Utilizar la clase FiguraGeometrica del ejercicio de
# abstracción y crear un método muestre información específica de la
# figura utilizando polimorfismo. Luego, crear una lista de figuras
# geométricas de diferentes tipos y utilizar el polimorfismo para imprimir
# su información.



from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio =radio

    def area(self):
        return f'Area del Círculo: {3.14 * self.radio **2}'
    
    def perimetro(self):
        return f'Perímetro del Círculo: {2 * 3.14 * self.radio}'

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f'Area del Rectángulo: {self.base * self.altura}'
    
    def perimetro(self):
        return f'Perímetro del Rectángulo: {2 * (self.base + self.altura)}'

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, a, b, c):
        self.base = base
        self.altura = altura
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        return f'Area del Triángulo: {(self.base * self.altura) / 2}'

    def perimetro(self):
        return f'Perímetro del Triángulo: {self.a + self.b + self.c}'


circulo = Circulo(100)
print(circulo.area())
print(circulo.perimetro())

rectangulo = Rectangulo(100, 200)
print(rectangulo.area())
print(rectangulo.perimetro())

triangulo = Triangulo(100, 200, 20, 20, 20)
print(triangulo.area())
print(triangulo.perimetro())



