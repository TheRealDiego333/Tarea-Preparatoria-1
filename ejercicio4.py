import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #4")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)
SQL = "SELECT * FROM ejercicio4;"
INSERT = "INSERT INTO ejercicio4(numero,suma) VALUES(%s,%s);"

print("Suma de los numeros anteriores hasta el numero dado")
texto = open('ejercicio4.txt','w')

while (True):

	try:
		numero = int(input("Ingrese un número: "))
	except ValueError:
		print("Debe ingresar un número, no cualquier otro caracter")

	nums = [x+1 for x in list(range(numero))]

	print("La suma de los numeros hasta " + str(numero) + " es "+ str(sum(nums)))
	cursor = conexion.cursor()
	cursor.execute (INSERT,(numero,sum(nums)))
	conexion.commit()

	texto.write('La suma es: ')
	texto.write(str(sum(nums)))
	texto.write('\n')   
texto.close()
	
