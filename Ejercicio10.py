"""
10- Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
desplazarse:
Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
una torre, e indique cuál pieza captura a la otra:

"""
tablero=""

fila_torre=int(input("Ingrese la fila en la que se encuentra la torre: "))
columna_torre=int(input("Ingrese la columna en la que se encuentra la torre: "))
fila_alfil=int(input("Ingrese la fila en la que se encuentra el alfil: "))
columna_alfil=int(input("Ingrese la columna en la que se encuentra el alfil: "))






if( columna_torre == columna_alfil  or fila_torre == fila_alfil):
    
    print("gana torre")


for i in range(8):
    for j in range(8):
        if(i == columna_torre and j == fila_torre):
            tablero+="("f"torre"")"
        if(i == columna_alfil and j == fila_alfil):
            tablero+="("f"alfil"")"
        else:
            tablero+="("f"{i}" + f" {j}"")"

    tablero+="\n"
    
print(tablero)
