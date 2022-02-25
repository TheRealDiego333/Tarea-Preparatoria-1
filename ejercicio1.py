import numpy as np
import sys
import os
import psycopg2
print("Ejercicio #1")
conexion = psycopg2.connect(
	host = "localhost",
	port = "5432",
	user = "postgres",
	password = "lin_$$33",
	dbname = "Proyectos"
)

SQL = "SELECT * FROM ejercicio1;"
INSERT = "INSERT INTO ejercicio1(mensaje,operacion) VALUES(%s,%s);"

texto = open('ejercicio1.txt','w')

while(True):
	print("Ingrese 3 números: \n")
	numeros = []
	try:
	    numeros.append(int(input("Ingrese el primer número: ")))
	    numeros.append(int(input("Ingrese el segundo número: ")))
	    numeros.append(int(input("Ingrese el tercer número: ")))
	except ValueError:
	    print("Debe ingresar un número, no cualquier otro caracter")

	maxIndex=numeros.index(max(numeros))

	if len(set(numeros))== 2: #el objeto set no tiene repetidos, elimina los repetidos
	    num= 0
	    for x in numeros:
	      if numeros.count(x)==1:
	        num= x
	    print("El numero que no se repite es: "+ str(num))

	    cursor = conexion.cursor()
	    cursor.execute (INSERT,("El numero que no se repite",num))
	    conexion.commit()
	    
	    
	    texto.write('El numero que no se repite: ')
	    texto.write(str(num))
	    texto.write('\n')

	elif len(set(numeros))== 1:
		print("Todos son iguales")
		cursor = conexion.cursor()
		cursor.execute (INSERT,("Todos son iguales",numeros[0]))
		conexion.commit()

		texto.write('Todos son iguales\n')

	elif maxIndex ==0:
	    print("La suma de los tres numeros es : {:.2f}".format(sum(numeros)))
	    cursor = conexion.cursor()
	    cursor.execute (INSERT,("La suma de los tres numeros es: ",sum(numeros)))
	    conexion.commit()
            	    
	    
	    texto.write('La suma de los tres numeros es: ')
	    texto.write(str(sum(numeros)))
	    texto.write('\n')

	
	elif maxIndex ==1:
	    print("La multiplicacion de los tres numeros es : {:.2f}".format(np.prod(numeros)))
	    prod=numeros[0]*numeros[1]*numeros[2]

	    cursor = conexion.cursor()
	    cursor.execute (INSERT,("La multiplicacion de los tres numeros es: ",prod))
	    conexion.commit()
	    
	    
	    texto.write('La multiplicacion de los tres numeros es: ')
	    texto.write(str(prod))
	    texto.write('\n')

	elif maxIndex ==2:
	    conncat = ""
	    for num in numeros:
	        conncat+= str(num)
	    print("Los numeros concatenados son: "+conncat)

	    cursor = conexion.cursor()
	    cursor.execute (INSERT,("Los numeros concatenados son: ",int(conncat)))
	    conexion.commit()
            	    
	    
	    texto.write('Los numeros concatenados son: ')
	    texto.write(conncat)
	    texto.write('\n')
	
texto.close()
