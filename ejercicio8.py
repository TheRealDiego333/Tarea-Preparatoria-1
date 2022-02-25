import sys
import os
import psycopg2
import time
print("Ejercicio #8")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)
SQL = "SELECT * FROM ejercicio8;"
INSERT = "INSERT INTO ejercicio8(año,kilometraje,accion) VALUES(%s,%s,%s);"


print("Clasificación de taxis")
texto = open('ejercicio8.txt','w')
while(True):
	try:
		año = int(input("Ingrese el año del automovil: "))
		kilometraje = float(input("Ingrese el kilometraje del automovil: "))
	except ValueError:
		print("Debe ingresar un número para el año del automovil o el kilometraje")
	estadoAuto = ""
	if (año<2007 and kilometraje>20000.00):
		estadoAuto= "debe renovarse";
		cursor = conexion.cursor()
		cursor.execute(INSERT,(año, kilometraje, estadoAuto))
		conexion.commit()
		texto.write('Debe renovarse\n')
		
	elif (año>=2007 and año<=2013) and  kilometraje>=20000.00:
		estadoAuto="debe recibir mantenimiento"
		cursor = conexion.cursor()
		cursor.execute(INSERT,(año, kilometraje, estadoAuto))
		conexion.commit()
		texto.write('Debe recibir mantenimiento\n')

	elif (año > 2013 and kilometraje<10000.00):
		estadoAuto= "se encuentra en condiciones óptimas"
		cursor = conexion.cursor()
		cursor.execute(INSERT,(año, kilometraje, estadoAuto))
		conexion.commit()
		texto.write('Se encuentra en condiciones optima\n')

	else:
		estadoAuto = "mecánico"

		cursor = conexion.cursor()
		cursor.execute(INSERT,(año, kilometraje, estadoAuto))
		conexion.commit()
		texto.write('Mecanico\n')


	if estadoAuto!= "mecánico":
		print("El automovil "+ estadoAuto)
	else:
		print(estadoAuto)
texto.close()
