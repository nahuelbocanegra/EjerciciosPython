"""2. Área y Perímetro. Crea una clase Rectángulo que permita calcular su área y su
perímetro. Además, crea en una aplicación de consola que permita al usuario crear
un objeto Perímetro y realizar los cálculos. ."""

class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area (self):
        return self.base*self.altura
    
    def perimetro(self):
        return 2 * self.base + 2 * self.altura 
    
    
        