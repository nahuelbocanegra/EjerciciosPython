"""14- Signo zodiacal. El signo zodiacal de una persona está determinado por su día de
nacimiento.
El diccionario de signos asocia a cada signo el período del año que le corresponde. Cada
período es una tupla con la fecha de inicio y la fecha de término, y cada fecha es una
tupla (mes, dia)

Por ejemplo, para que una persona sea de signo libra debe haber nacido entre el 24 de
septiembre y el 23 de octubre.
Escriba la función determinar_signo(fecha_de_nacimiento) que reciba como
parámetro la fecha de nacimiento de una persona, representada como una tupla (año,
mes, dia), y que retorne el signo zodiacal de la persona:
"""

signos = {
    'aries': (( 3, 21), ( 4, 20)),
    'tauro': (( 4, 21), ( 5, 21)),
    'geminis': (( 5, 22), ( 6, 21)),
    'cancer': (( 6, 22), ( 7, 23)),
    'leo': (( 7, 24), ( 8, 23)),
    'virgo': (( 8, 24), ( 9, 23)),
    'libra': (( 9, 24), (10, 23)),
    'escorpio': ((10, 24), (11, 22)),
    'sagitario': ((11, 23), (12, 21)),
    'capricornio': ((12, 22), ( 1, 20)),
    'acuario': (( 1, 21), ( 2, 19)),
    'piscis': (( 2, 20), ( 3, 20)),
}

def determinar_signo(fecha):
    for j in signos.values():
            if(j[0][0]== fecha[1]):
                print(list(signos.keys()))[11]

    


determinar_signo((1997,11,30))




