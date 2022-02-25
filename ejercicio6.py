import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #6")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)
SQL = "SELECT * FROM ejercicio6;"
INSERT = "INSERT INTO ejercicio6(lado1,lado2,lado3,triangulo) VALUES(%s,%s,%s,%s);"

print("Ingrese los lados del triángulo: ")

texto = open('ejercicio6.txt','w')

while(True):
	numeros = []
	try:
		numeros.append(int(input("Ingrese el primer lado: ")))
		numeros.append(int(input("Ingrese el segundo lado: ")))
		numeros.append(int(input("Ingrese el tercer lado: ")))
	except ValueError:
		print("Debe ingresar un número, no cualquier otro caracter")

	tipoTriangulo = " "
	if len(set(numeros))== 2:
		tipoTriangulo = "Isósceles"
	elif len(set(numeros))== 3:
		tipoTriangulo = "Escaleno"
	elif len(set(numeros))== 1:
		tipoTriangulo = "Equilátero"
	print("El triángulo es de tipo "+ tipoTriangulo)  
	cursor = conexion.cursor()
	cursor.execute (INSERT,(numeros[0],numeros[1], numeros[2], tipoTriangulo))
	conexion.commit()
	texto.write('EL triangulo es de tipo '+tipoTriangulo+'\n')
texto.close()
