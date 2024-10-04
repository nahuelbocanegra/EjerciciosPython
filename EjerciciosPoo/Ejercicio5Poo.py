""" 5- Kilometraje Recorrido. Crea una clase vehículo que permita llevar el kilometraje
recorrido. Agrega atributos para definir color, marca, modelo y patente del vehículo y
métodos para: 1- conducir el auto (debe aceptar la cantidad de kilómetros y sumarlo
al kilometraje recorrido) y 2- muestre en pantalla los datos del vehículo y el
correspondiente kilometraje. Además, escribe una aplicación de consola que permita
al usuario conducir varios kilómetros y mostrar el kilometraje actual hasta que decida
detenerse. Al finalizar deberá mostrar los datos del vehículo y el kilometraje
recorrido."""

class Vehiculo: 
    def __init__(self,color, marca, modelo, patente ) -> None:
        self.color=color
        self.marca=marca
        self.modelo=modelo 
        self.patente=patente
        self.kilometraje=0

    def conducir(self,km_recoridos):
        self.kilometraje+=km_recoridos
        
    def datos(self):
        mensaje="datos: \n color:{} \n modelo:{} \n marca:{} \n patente:{} \n kilometraje:{}".format(self.color,self.modelo,self.marca,self.patente,self.kilometraje)
        return  mensaje



auto1=Vehiculo("rojo","renault","clio","AAA-222")

print(auto1.datos())