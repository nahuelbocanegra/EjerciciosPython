"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no"""

def primo():
    num=int(input("Ingrese un numero:"))
    divisible=0

    for i in range(1,num +1 ):
        if(num % i == 0):
            divisible +=1

    if(divisible>2):
        return "no es primo"
    
    return "Es primo"

print(primo())