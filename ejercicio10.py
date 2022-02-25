import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #10")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio10;"
INSERT = "INSERT INTO ejercicio10(lista) VALUES(%s);"

texto = open('ejercicio10.txt','w')
while (True):
	print("Lista de mayor a menor")
	try:
		num1 = int(input("Ingrese el primer numero: "))
		num2 = int(input("Ingrese el segundo numero: "))
	except ValueError:
		print("Debe ingresar un número, no cualquier caracter.")

	if num1 >num2:
		x=list(range(num2,num1+1))
		ordenada = sorted(x, reverse=True)
	else:
		x=list(range(num1,num2+1))
		ordenada = sorted(x, reverse=True)
	string =''
	for x in ordenada:
		string+=" "+ str(x)+ " "
	print(string)

	cursor = conexion.cursor()
	cursor.execute (INSERT,(string,))
	conexion.commit()

	texto.write('Lista de mayor a menor')
	texto.write(string)
	texto.write('\n')
texto.close()
