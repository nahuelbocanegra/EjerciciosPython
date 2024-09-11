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


for i in alfabeto:
    print(i)
