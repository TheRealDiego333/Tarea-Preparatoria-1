import numpy as np
import sys
import os
import psycopg2
import time
print("Ejercicio #5")
conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "lin_$$33",
        dbname = "Proyectos"
)
SQL = "SELECT * FROM ejercicio5;"
INSERT = "INSERT INTO ejercicio5(numeros_Impares) VALUES(%s);"

print("Numeros impares")
texto = open('ejercicio5.txt','w')
for x in range(0,100,1):
	if x%2 !=0 :
		print (x)
		cursor = conexion.cursor()
		cursor.execute (INSERT,(x,))
		conexion.commit()
		texto.write('Los numeros impares son: ')
		texto.write(str(x))
		texto.write('\n')
texto.close()
