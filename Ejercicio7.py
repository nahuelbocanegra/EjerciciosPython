"""7- La secuencia de Collatz de un número entero se construye de la siguiente forma:
● si el número es par, se lo divide por dos;
● si es impar, se le multiplica tres y se le suma uno;"""

def collatz():

    num=int(input("Ingrese un numero entero: "))
    cadena=f"{num} "

    while True:
        if(num % 2 == 0):
            num=num//2
            cadena += f"{num} "   
        elif(num % 2 != 0):
            num = num*3+1
            cadena += f"{num} "
        if(num == 1):
            break


    return cadena;
    

print(collatz())
