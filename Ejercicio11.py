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

def jugada(jugador1,jugador2,marcador1,marcador2):
    if(jugador1 == jugador2):
        return f"marcador {marcador1} - {marcador2}"
    if(jugador1 == "piedra" and jugador2 == "tijera"):
        marcador1 += 1
        return f"marcador {marcador1} - {marcador2}"
    elif( jugador1 == "tijera" and jugador2 == "piedra" ):
        marcador2 += 1
        return f"marcador {marcador1} - {marcador2}"
    elif(jugador1 == "papel" and jugador2 == "piedra"):
        marcador2 += 1
        return f"marcador {marcador1} - {marcador2}"
    elif(jugador1 == "piedra" and jugador2 == "papel"):
        marcador1 += 1
        return f"marcador {marcador1} - {marcador2}"
    elif(jugador1 == "tijera" and jugador2 == "papel"):
        marcador1 += 1
        return f"marcador {marcador1} - {marcador2}"
    elif(jugador1 == "papel" and jugador2 == "tijera"):
        marcador2 += 1
        return f"marcador {marcador1} - {marcador2}"



print("juego de piedra papel o tijera")


while marcador1 <= 3 or marcador2 <= 3:

    jugador1=input("elegir entre piedra , papel o tijera: ").lower()
    jugador2=input("elegir entre piedra , papel o tijera: ").lower()
    print(f"Jugador1= {jugador1}")
    print(f"Jugador2= {jugador2}")

    print(jugada(jugador1,jugador2,marcador1,marcador2))
    print(marcador1,marcador2)










 #   piedra>tijera  
 #   tijera>papel  
 #   papel>piedra   




    
