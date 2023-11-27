import os
import errno
import wikipediaapi

#-----Crear carpetas-----#
try:
    os.mkdir('Carpeta_1')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

try:
    os.mkdir('Carpeta_2')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
#------------------------#

#--------Formato---------#
def existe(b):
    if b:
        return "Si"
    else:
        return "No" 
#------------------------#

#--Filtro-y minusculas---#
def normalizado(s):
    remplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("— ",""),
        (" —"," "),
        ("—​ ", ""),
        ("/", " "),
    )
    for a, b in remplazos:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def filtro(string):
    caracteres_especiales = "'!?ˈ«»,.:;¿¡()}{[]$#º%=_+-²123456@°′″7890"+'"'
    for x in range(len(caracteres_especiales)):
        string = string.replace(caracteres_especiales[x], "")
    return normalizado(string.lower())
#------------------------#

#------Consumo api-------#
user_agent = 'T3SD (felipe.castro3@mail.udp.cl)'
wiki_wiki = wikipediaapi.Wikipedia(language='es', user_agent=user_agent)



# Temas (Solo funciona con temas sin acentos y de una palabra)
topicos = ["Python", "Apple", "Chile", "Facebook", "Automovil", "Mesa",
          "Videojuego", "Deporte", "Microsoft", "Google", "Zapatillas",
          "Robot", "Internet", "Satelite", "Universidad"]

topicos += ["Celular", "Musica", "Libro", "Cine", "Teclado",
          "Televisor", "Reloj", "Bicicleta", "Jardin", "Cocina",
          "Avion", "Barco", "Tren", "Guitarra", "Pintura"]
cont = 0

for topico in topicos:
    page_py = wiki_wiki.page(topico)

    print("El topico", topico, "existe?:", existe(page_py.exists()))
    
    if page_py.exists():
        folder = "Carpeta_1" if cont < 15 else "Carpeta_2"
        with open(os.path.join(folder, f"{topico}.txt"), "w") as arch:
            arch.write(filtro(page_py.text))
        cont += 1
