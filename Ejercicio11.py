"""11- Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores
deben elegir entre jugar tijera, papel o piedra.
Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a
piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
El ganador del juego es el primero que gane tres rondas.
Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el
marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres
rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra."""


marcador1=0
marcador2=0

def jugada(jugador1,jugador2):
    if(jugador1 == jugador2):
        return "empate"
    if((jugador1 == "piedra" and jugador2 == "tijera") or \
        (jugador1 == "papel" and jugador2 == "piedra") or \
        (jugador1 == "tijera" and jugador2 == "papel")):
        return "jugador1" 
    else:
        return "jugador2" 

    


print("juego de piedra papel o tijera")


while marcador1 < 3 and marcador2 < 3 :

    jugador1=input("Jugador1 elegir entre piedra , papel o tijera: ").lower()
    jugador2=input("Jugador2 elegir entre piedra , papel o tijera: ").lower()
    print(f"Jugador1= {jugador1}")
    print(f"Jugador2= {jugador2}")

    partida=jugada(jugador1,jugador2)
    if(partida == "jugador1"):
        marcador1+=1
    elif(partida == "jugador2"):
        marcador2+=1
    
    print(f"{marcador1} - {marcador2}")


    




 #   piedra>tijera  
 #   tijera>papel  
 #   papel>piedra   




    
