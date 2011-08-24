#-*- coding:UTF-8 -*-
# 1. Ingresar a una base de datos el nombre, apellido y correo electronico de las personas, 
# mediante un programa que pida continuar o no. Al final el programa debe imprimir la lista 
# total de la tabla
import MySQLdb
conexion = MySQLdb.connect('localhost','root','toor','pythonmysql')
cursor = conexion.cursor()

continuar = 's'
while continuar == 's':
	nombre = raw_input("Ingrese el nombre: ")
	apellido = raw_input("Ingrese el apellido: ")
	correo = raw_input("Ingrese el correo electronico: ")
	
	sql = "INSERT INTO persona VALUES (null,'%s','%s','%s')" % (nombre,apellido,correo)
	cursor.execute(sql)
	conexion.commit()
	
	continuar = ''
	while continuar != 's' and continuar != 'n':
		continuar = raw_input("¿Desea continuar (s/n)?")

sql = "SELECT * FROM persona"
cursor.execute(sql)
resultado = cursor.fetchall()
for persona in resultado:
    print "Nombre: ",persona[1],"| Apellidos: ",persona[2],"| email: ",persona[3]

cursor.close()

