import sqlite3
from sqlite3 import Error
import os
import wikipediaapi
contenido = os.listdir('/home/hadoop/Outputs')
col=[]
for i in range(len(contenido)):
	col.append("doc_"+str(i))

cols = " integer , ".join(col)
cols2 = ", ".join(col)
conn = None
try:
    conn = sqlite3.connect("db")
    print("Se creo la bd")
except Error as e:
    print(e)

#conn.execute("drop table palabras")
try:
    conn.execute("create table palabras (palabra text primary key,"+cols+" integer)")
    print("se creo la tabla Palabras")                        
except sqlite3.OperationalError:
    print("La tabla Palabras ya existe")

aux = ["?"] * len(contenido)
aux = ",".join(aux)

arch = open("salida.txt")
for linea in arch:
	linea = linea.strip().split("\t\t")
	temp = [0] * len(contenido)
	for tupla in linea[1].split(";"):
		tupla=tupla.replace("(","")
		tupla=tupla.replace(")","")
		tupla=tupla.split(" ")
		temp[int(tupla[0])] = int(tupla[1])
	temp = [linea[0]] + temp
	conn.execute("insert into palabras (palabra,"+cols2+") values (?,"+aux+")", temp)
arch.close()
print("Se insertaron todas las palabras")
while True:
	consulta = input("Ingrese la palabra que desea buscar (para salir presione Ctrl+c): ")

	cursor = conn.execute("select * from palabras where palabra='%s';" % consulta)
	for fila in cursor:
	    fila = fila.index(max(fila[1:])) - 1
	
	wiki_wiki = wikipediaapi.Wikipedia('es') #Lenguaje español
	pagina = contenido[fila].replace(".txt", "")
	page_py = wiki_wiki.page(pagina)
	print(page_py.fullurl)
	
#conn.close()
