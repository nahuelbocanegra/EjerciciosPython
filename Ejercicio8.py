"""8- Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011
en el campus Vitacura.
Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una."""

def tipo(tipo_producto):
    array_productos=[270,340,390]
    if(tipo_producto == "A"):
        return array_productos[0]
    elif(tipo_producto == "B"):
        return array_productos[1]
    elif(tipo_producto == "C"):
        return array_productos[2]



def cargar(producto):
    cant_monedas=0
    
    while True:
        monedas=int(input("Ingrese monedas: "))
        cant_monedas+=monedas;
        if(cant_monedas>=producto):
            return cant_monedas-producto;
            
            

def cambioMoneda(cambio):
    
    print("tu cambio: ")
    while cambio>0:
        if(cambio>100):
            cambio-=100
            print(100)
        elif(cambio<100 and cambio>50):
            cambio-=50
            print(50)
        else:
            cambio-=10
            print(10)


def main():
    tipo_producto=input("Ingrese el tipo de producto (A-B-C): ").upper()
    producto=tipo(tipo_producto)
    cambio=cargar(producto)
    cambioMoneda(cambio)



main()





