"""2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
entero de horas h, que indique qué hora marcará el reloj dentro de h horas:"""



def marcaHora():
    horaActual=int(input("hora Actual: "));
    horas=int(input("Cantidad de horas: "));
    for i in range(horas):
        horaActual+=1
       
        if(horaActual == 24):
            horaActual = 0
    
    return horaActual;

print(marcaHora())




