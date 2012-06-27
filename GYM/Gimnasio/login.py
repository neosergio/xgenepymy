#-*- coding:utf-8 -*-
import md5
import sqlite3
import getpass
import sys

def conectar(consulta):
	conexion = sqlite3.connect('gym.db')
	cursor = conexion.cursor()
	resultado = cursor.execute(consulta)
	conexion.commit()
	return resultado

usuario = raw_input("Ingresa tu usuario: ")
clave = getpass.getpass(prompt='Ingrese su clave: ')
clave_cifrada = md5.new()
clave_cifrada.update(clave)
clave_cifrada = str(clave_cifrada.hexdigest())

consulta = "SELECT id FROM usuario WHERE usuario = '%s' and clave='%s'" % (usuario, clave_cifrada)
resultado = conectar(consulta).fetchone()
try:
	cantidad = len(resultado)
	if cantidad == 1:
		print "Acceso concedido"
except:
	sys.exit("El usuario no existe")
	