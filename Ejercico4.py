""" Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0."""

def tramo():
    minutos=0
    horas=0
    
    while True :
        tramo=int(input("Ingresa la duracion del tramo en minutos: // ingreso 0 para terminar el proceso: "))
        minutos+= tramo
        if(tramo == 0):
            break
    
    print(minutos)
    horas=minutos//60
    minutos=minutos-horas*60

    return ("Tiempo de viaje:{}hs{} minutos".format(horas,minutos))

print(tramo())
    
