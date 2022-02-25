import numpy as np
import sys
import os
import psycopg2
import re
print("Ejercicio #11")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio11;"
INSERT = "INSERT INTO ejercicio11(vocal,veces) VALUES(%s,%s);"

texto = open('ejercicio11.txt','w')

print("Contador de ocurrencias de vocales")
while(True):

	try:
		palabra = input("Ingrese una palabra: ")
	except ValueError:
		print("Debe ingresar una palabra")
	vocales = ['A','E','I','O','U']
	#$4diccionario llave: vocal, valor: cantidad de apariciones
	vocalesCantidad = {}
	for voc in vocales:
		cantidad=len(re.findall(voc, str(palabra.upper())))
		vocalesCantidad[voc] = cantidad
		print(voc+"= "+str(cantidad))
		cursor = conexion.cursor()
		cursor.execute (INSERT,(voc,str(cantidad)))
		conexion.commit()
		texto.write(voc)
		texto.write('=')
		texto.write(str(cantidad))
		texto.write('\n')
texto.close()
