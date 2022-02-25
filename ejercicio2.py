import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #2")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)
SQL = "SELECT * FROM ejercicio2;"
INSERT = "INSERT INTO ejercicio2(numero,divisores) VALUES(%s,%s);"


texto = open('ejercicio2.txt','w')
while(True):
	try:
		numero = int(input("Ingrese un número: "))
	except ValueError:
		print("Debe ingresar un número, no cualquier otro caracter")
	divisores=[]
	for x in range(1, numero+1):
		if numero % x == 0:
			divisores.append(x)
			print("El numero {:d} es divisor de {:d}".format(x, numero))			
			cursor = conexion.cursor()
			cursor.execute (INSERT,(numero,x))
			conexion.commit()
			texto.write('Divisores de ')
			texto.write(str(numero))
			texto.write(' son: ')
			texto.write(str(x))
			texto.write('\n')	
texto.close()

