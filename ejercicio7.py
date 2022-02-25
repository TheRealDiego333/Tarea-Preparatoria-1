import numpy as np
import sys
import os
import psycopg2
from math import factorial
print("Ejercicio #7")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)
SQL = "SELECT * FROM ejercicio7;"
INSERT = "INSERT INTO ejercicio7(factorial) VALUES(%s);"
print("Factorial de un número")
texto = open('ejercicio7.txt','w')

while(True):
	try:
		numero = int(input("Ingrese el número: "))
	except ValueError:
		print("Debe ingresar un número, no cualquier otro caracter")
	if numero % 7 ==0:
		print ("Factorial is", factorial(numero))
		#para que sea una lista de 1 a el numero
#		nums = [x+1 for x in list(range(numero))]
#		factorial = np.prod(nums)
#		print("El factorial del número "+ str(numero)+ " es "+ str(factorial))
		fac = str(factorial(numero))
		cursor = conexion.cursor()
		cursor.execute (INSERT,(factorial(numero),))
		conexion.commit()

		texto.write('El factorial es: ')
		texto.write(str(factorial(numero)))
		texto.write('\n')

	else:
		print("El número no es multiplo de 7")
		cursor = conexion.cursor()
		cursor.execute (INSERT,(0,))
		conexion.commit()
texto.close()
