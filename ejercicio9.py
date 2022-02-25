import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #9")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio9;"
INSERT = "INSERT INTO ejercicio9(iteraciones) VALUES(%s);"
texto = open('ejercicio9.txt','w')

while(True):
	print("Numeros de 2 en 2")
	try:
		inicio = int(input("Ingrese número de inicio: "))
		fin = int(input("Ingrese número donde terminar: "))
		cursor = conexion.cursor()
		cursor.execute(INSERT,("Inicio",))
		conexion.commit()
		texto.write('Inicio ')



	except ValueError:
		print("Debe ingresar un número, no cualquier otro caracter")

	for i in range (inicio,fin,2):
		print (i)
		cursor = conexion.cursor()
		cursor.execute(INSERT,(str(i),))
		conexion.commit()
		texto.write(str(i))
		texto.write(" ")
		
	cursor = conexion.cursor()
	cursor.execute(INSERT,(str(fin),))
	conexion.commit()
	cursor = conexion.cursor()
	cursor.execute(INSERT,("Fin",))
	conexion.commit()
	texto.write("Fin")
texto.close()

