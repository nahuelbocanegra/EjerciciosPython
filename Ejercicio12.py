"""12- Torneo de Tenis. Escriba un programa para simular un campeonato de tenis.
Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación,
debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El
ganador de cada partido avanza a la ronda siguiente.
El programa debe continuar preguntando ganadores de partidos hasta que quede un
único jugador, que es el campeón del torneo.
7"""

def inscripciones():
    
    jugador1=input("Ingrese el nombre del primer jugador: ")
    jugador2=input("Ingrese el nombre del segundo jugador: ")
    jugador3=input("Ingrese el nombre del tercero jugador: ")
    jugador4=input("Ingrese el nombre del cuarto jugador: ")
    jugador5=input("Ingrese el nombre del quinto jugador: ")
    jugador6=input("Ingrese el nombre del sexto jugador: ")
    jugador7=input("Ingrese el nombre del septimo jugador: ")
    jugador8=input("Ingrese el nombre del octavo jugador: ")
    
    return [jugador1,jugador2,jugador3,jugador4,jugador5,jugador6,jugador7,jugador8]

cuartos=inscripciones();

semifinal=[]
final=[]

print("Primera ronda: ")

for i in range(0,8,2):
    ganador=input(f"a-{cuartos[i]} vs b-{cuartos[i+1]}: ")
    if(ganador == "a"):
        print(f"el ganador es: {cuartos[i]}")
        semifinal.append(cuartos[i])
    else:
        print(f"el ganador es: {cuartos[i+1]}")
        semifinal.append(cuartos[i+1])
print(semifinal)

for i in range(0,4,2):
    ganador=input(f"a-{semifinal[i]} vs b-{semifinal[i+1]}: ")
    if(ganador == "a"):
        print(f"el ganador es: {semifinal[i]}")
        final.append(semifinal[i])
    else:
        print(f"el ganador es: {semifinal[i+1]}")
        final.append(semifinal[i+1])


ganador=input(f"a-{final[i]} vs b-{final[i+1]}: ")
if(ganador == "a"):
    print(f"el ganador es: {final[i]}")
print(f"el ganador es: {final[i+1]}")
        


        


