import numpy as np
import sys
import os
import psycopg2
import re

print("Ejercicio #3")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio3;"
INSERT = "INSERT INTO ejercicio3(palabra,vocales) VALUES(%s,%s);"

texto = open('ejercicio3.txt','w')

print("Contador de vocales")
while (True):
	try:
		palabra = input("Ingrese una palabra: ")
	except ValueError:
		print("Debe ingresar una palabra")

	#'[aeiou]' es una expresion regular para hacer match con las vocales y el str es por si meten un numero
	vocales = re.findall('[aeiou]', str(palabra))

	print("La palabra " + str(palabra) +" tiene " + str(len(vocales)) +" vocales")
	cursor = conexion.cursor()
	cursor.execute (INSERT,(str(palabra),len(vocales)))
	conexion.commit()

	texto.write('La palabra ')
	texto.write(str(palabra))
	texto.write(' tiene ')
	texto.write(str(len(vocales)))
	texto.write(' vocales\n')   
texto.close()
