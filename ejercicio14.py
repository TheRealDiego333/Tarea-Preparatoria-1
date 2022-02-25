import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #14")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio14;"
INSERT = "INSERT INTO ejercicio14(año,bisiesto) VALUES(%s,%s);"

texto = open('ejercicio14.txt','w')

def paso5 ():
	print("No es un año bisiesto")
	cursor = conexion.cursor()
	cursor.execute (INSERT,(año, "No es bisiesto"))
	conexion.commit()
	texto.write(str(año))
	texto.write(' No es bisiesto\n')


def paso4 ():
	print("Es un año bisiesto")
	cursor = conexion.cursor()
	cursor.execute (INSERT,(año, "Es bisiesto"))
	conexion.commit()
	texto.write(str(año))
	texto.write(' Es bisiesto\n')


while (True):
	año=int(input("Ingrese un año: "))
	if (año > 0):
		if año%4 == 0:
			if año%100 ==0:
				if año%400 ==0:
					paso4()
				else:
					paso5()
			else:
				paso4()
		else:
			paso5()
	else:
		print("Ingrese un año valido")

texto.close()
