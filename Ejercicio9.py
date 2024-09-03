"""9 - Anagrama. Escribe una función que reciba dos palabras y retorne
verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama."""

def anagrama(palabra1,palabra2):

    palabra2=palabra2.lower()
    palabra1=palabra1.lower()

    if(len(palabra1) != len(palabra2)):
        return False
    return sorted(palabra1) == sorted(palabra2)

print(anagrama("olaa","aola"))