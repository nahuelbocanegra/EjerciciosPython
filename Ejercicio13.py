"""3- El diccionario países asocia cada persona con el conjunto de los países que ha
visitado:
Escriba una función cuantos_en_comun(a, b), que indique cuántos países en común han
visitado la persona a y la persona b:
"""

def cuantos_en_comun(a,b):
    paises = {
        'Pepito': {'Chile', 'Argentina'},
        'Yayita': {'Francia', 'Suiza', 'Chile'},
        'John': {'Chile', 'Italia', 'Francia', 'Peru'},
    }

    en_comun=[]

    for x in paises[a]:
        for j in paises[b]:
            if(j == x):
                print(j)
                en_comun.append(j)

    return en_comun
        

cuantos_en_comun("John","Yayita") 