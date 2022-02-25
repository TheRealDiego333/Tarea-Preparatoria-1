import numpy as np
import sys
import os
import psycopg2
import math
print("Ejercicio #12")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio12;"
INSERT = "INSERT INTO ejercicio12(figura,area) VALUES(%s,%s);"
texto = open('ejercicio12.txt','w')

while (True):

	print ("""
		Figura a calcular?
		1)Circulo
		2)Triangulo
		3)Cuadrado
		4)Rectangulo
		""")

	figura = int(input("Seleccione figura: "))
	if figura == 1:
		print ("Circulo seleccionado")
		radio = float(input("Por favor ingrese radio: "))
		areacir = math.pi*pow(radio,2)
		print("El area del circulo es: ",areacir)
		cursor = conexion.cursor()
		cursor.execute (INSERT,("circulo",areacir))
		conexion.commit()
		texto.write('Circulo con area: ')
		texto.write(str(areacir))
		texto.write('\n')

	if figura == 2:
		print ("Triangulo seleccionado")
		base = float(input("Por favor ingrese base: "))
		altura = float(input("Por favor ingrese altura: "))
		areatri = (base*altura)/2 
		print("El area del triangulo es: ",areatri)
		cursor = conexion.cursor()
		cursor.execute (INSERT,("triangulo",areatri))
		conexion.commit()
		texto.write('Triangulo con area: ')
		texto.write(str(areatri))
		texto.write('\n')

	if figura == 3:
		print ("Cuadrado seleccionado")
		lado = float(input("Por favor ingrese un lado: "))
		areacuad =  lado*lado
		print("El area del cuadrado es: ",areacuad)
		cursor = conexion.cursor()
		cursor.execute (INSERT,("cuadrado",areacuad))
		conexion.commit()
		texto.write('Cuadrado con area: ')
		texto.write(str(areacuad))
		texto.write('\n')

	if figura == 4:
		print ("Rectangulo seleccionado")
		base = float(input("Por favor ingrese base: "))
		altura = float(input("Por favor ingrese altura: "))
		arearec = (base*altura)
		print("El area del rectangulo es: ",arearec)
		cursor = conexion.cursor()
		cursor.execute (INSERT,("rectangulo",arearec))
		conexion.commit()
		texto.write('Rectangulo con area: ')
		texto.write(str(arearec))
		texto.write('\n')


texto.close()
