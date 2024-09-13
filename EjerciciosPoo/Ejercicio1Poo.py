""". Persona. crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:

a. Un constructor, donde los datos pueden estar vacíos.
b. Los setters y getters para cada uno de los atributos. 
Hay que validar las entradas de datos.
c. mostrar(): Muestra los datos de la persona.
d. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
Además, crea en una aplicación de consola que permita al usuario crear un objeto
Persona y evaluar si es mayo o menor de edad..
"""
class Persona:
    def __init__(self,nombre="", edad="",dni=""):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

    def mostrar(self):
        if self.nombre:
            return "hola,mi nombre es {} , mi documento es: {} y tengo {} años".format(self.nombre,self.dni,self.edad);
        return "tiene que darnos informacion"

    def es_mayor(self):
         return self.edad >= 18
    

persona1=Persona()

print(persona1.mostrar())


       