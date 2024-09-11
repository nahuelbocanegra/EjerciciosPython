
#Escriba las funciones necesarias para que el siguiente programa funcione

libros = [
('Papelucho programador', 'Marcela Paz', 1983),
('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
('Raw_input y Julieta', 'William Shakespeare', 1597),
('La tuplamorfosis', 'Franz Kafka', 1915),
# ...
]
autores = {
# autor: nacimiento, defunción, idioma
    'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
    'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
    'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
    'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español'),
# ...
}

titulo = input('Ingrese titulo del libro: ')



def obtener_autor(titulo):
    for  j in libros:
        if j[0].upper() == titulo.upper():
            return j[1]

def obtener_idioma(titulo):
    autor = obtener_autor(titulo)
    for j , x in autores.items():
        if j.upper() == autor.upper():
            return x[2]

def calcular_annos_antes_de_morir(titulo):
    autor = obtener_autor(titulo)
    for j , x in autores.items():
        if j.upper() == autor.upper():
           return x[1][0] - x[0][0]

print ('El libro fue escrito en', obtener_idioma(titulo)),
print ('por', obtener_autor(titulo))
print ('El autor fallecio', calcular_annos_antes_de_morir(titulo), 'años',)
print ('después de haber escrito el libro')