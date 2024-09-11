"""16- Código Morse. Crea un programa que sea capaz de transformar texto natural a
código morse y viceversa.
● Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
● En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos
espacios entre palabras " "."""


alfabeto={
        0:"— — — — —",
        1:	"· — — — —",
        2:"· · — — —",
        3:"· · · — —",
        4:"· · · · —",
        5:"· · · · ·",
        6:"— · · · ·",
        7:"— — · · ·",
        8:"— — — · ·",
        9:"— — — — ·",
        "A":"· —",
        "N":"— ·",	 	
        "B":"— · · ·",
        "Ñ":"— — · — —",
        "C":"— · — ·",	 
        "O":"— — —",	 	
        "CH":"— — — —",	 	
        "P":"· — — ·",	 	
        "D":"— · ·",	
        "Q":"— — · —",
        "E":"·",	 	
        "R":"· — ·",	 	
        "F":"· · — ·",	 	
        "S":"· · ·"	, 	
        "G":"— — ·"	, 	
        "T":"—",	 	
        "H":"· · · ·",	 	
        "U":"· · —",	 	
        "I":"· ·",	 	
        "V":"· · · —",	 	
        "J":"· — — —",	 	
        "W":"· — —",	 	
        ".":"· — · — · —",
        "K":"— · —",	 	
        "X":"— · · —",	 	
        ",":"— — · · — —" ,
        "L":"· — · ·",	
        "Y":"— · — —",	 	
        "?":"· · — — · ·",
        "M":"— —",	 	
        "Z":"— — · ·",	 	
        ":":"· — · · — ·", 	
        "/":"— · · — ·",
}

def traducir(*frase):
    codigo=""
    for z in frase:
        if(z.count("a") or z.count("e") or z.count("i") or z.count("o") or z.count("u")):
            for i in z.upper():
                codigo += alfabeto[i] +"  "
    else:
        for z in frase:
           for i,j in alfabeto.items():
                if(j == z):
                    codigo+=i +" "
                    
                                            
    return codigo;
    

print(traducir("hola"))


