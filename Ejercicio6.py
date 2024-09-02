"""6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el
usuario"""

def triangulo():
    e=""
    renglon=int(input("Ingrese el numero de renglones: "))
    index=renglon
    for j in range(renglon):
        for i in range(index,renglon):
           e+=f"{i} "
        e+="\n"
        index-=1

    return e

print(triangulo())
