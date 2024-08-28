"""1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
número con los dígitos en orden inverso"""

def inverso(num):

    array=list(str(num))

    array.reverse()

    return "".join(array)
       


print(inverso(321))