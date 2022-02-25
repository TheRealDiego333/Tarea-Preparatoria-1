import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #13")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio13;"
INSERT = "INSERT INTO ejercicio13(promedio,Nota) VALUES(%s,%s);"
texto = open('ejercicio13.txt','w')
while (True):
	n1=int(input("Primera nota: "))
	n2=int(input("Segunda nota: "))
	n3=int(input("Tercera nota: "))
	promedio = (n1+n2+n3)/3
	if promedio >= 60:
		print("Aprobado")
		cursor = conexion.cursor()
		cursor.execute (INSERT,(promedio,"Aprobado"))
		conexion.commit()
		texto.write('Aprobado con nota: ')
		texto.write(str(promedio))
		texto.write('\n')
	else:
		print("Reprobado")
		cursor = conexion.cursor()
		cursor.execute (INSERT,(promedio,"Reprobado"))
		conexion.commit()
		texto.write('Reprobado con nota: ')
		texto.write(str(promedio))
		texto.write('\n')
texto.close()
