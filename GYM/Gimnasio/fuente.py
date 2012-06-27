#-*- coding:utf-8 -*-
# Programa generador de rutinas de ejercicios....
# autores: Blas, Bustamante, Ortega
#importando la formula y la libreria de conexion
import sqlite3
from formula import imc_calculo, consulta_imc
from formula import ica_calculo, consulta_ica
from formula import pgc_calculo, consulta_pgcm
from formula import pgc_calculo, consulta_pgcf
from formula import calculo_rutina, consulta_rutina
#from formula import consulta_actividad
#from formula import mcm_calculo, consulta_mcm

#ingreso de datos
peso = int(raw_input("Ingrese su peso: (kg)"))
altura = int(raw_input("Ingrese su altura: (cm)"))
cintura = int(raw_input("Ingrese el perimetro de cintura: (cm)"))
cuello = int(raw_input("Ingrese el perimetro de cuello: (cm)"))
sexo = raw_input("Ingrese su genero: (M/F) ")
#actividad = raw_input("Ingrese su actividad (1. sedentario, 2. moderado, 3. activo)")


#en caso de ser femenino se le pide medida de cadera
if sexo == "F":
	cadera = int(raw_input("Ingrese el perimetro de cadera: (cm)"))
else:
	cadera = 0
	


#rango = consulta_actividad(actividad)
#print "Su actividad fisica es: " + str(actividad) 

imc = imc_calculo(peso, altura)
rango = consulta_imc(imc)
print "Su Indice de Masa Corporal es: " + str(imc) 

ica = ica_calculo(cintura, altura)
rango = consulta_ica(ica)
print "Su Indice Cintura Altura es: " + str(ica) 

pgc = pgc_calculo(cintura, cuello, altura, sexo, cadera)
print "Su Porcentaje de Grasa Corporal es: " + str(pgc) 
#en caso de ser femenino se le pide medida de cadera
if sexo == "F":
	rango = consulta_pgcf(pgc)
elif sexo == "M":
    rango = consulta_pgcm(pgc)
    

#mcm = mcm_calculo(pgc, peso, sexo, cadera = 0)
#rango = mcm_calculo(pgcm, pgcf, peso, sexo, cadera = 0)
#en caso de ser femenino se le pide medida de cadera
#if sexo == "F":
#	cadera = int(raw_input("Ingrese el perimetro de cadera: (cm)"))
#    rango = consulta_pcgf
#elif sexo == "M"
#    rango = consulta_pgcm


#calculo = calculo_rutina(imc, ica, pgc, sexo, actividad)
calculo = calculo_rutina(imc, ica, pgc, sexo)
rutina = consulta_rutina(calculo)

#consulta a la base de datos pgcm
conexion = sqlite3.connect('gym.db')
cursor = conexion.cursor()
consulta = "SELECT descripcion FROM pgcm_tabla WHERE valor='%s'" % (rango)
#print consulta
resultadodb = cursor.execute(consulta)
for i in resultadodb:
	print i[0]


#consulta a la base de datos pgcf
conexion = sqlite3.connect('gym.db')
cursor = conexion.cursor()
consulta = "SELECT descripcion FROM pgcf_tabla WHERE valor='%s'" % (rango)
#print consulta
resultadodb = cursor.execute(consulta)
for i in resultadodb:
	print i[0]


#consulta a la base de datos ica
conexion = sqlite3.connect('gym.db')
cursor = conexion.cursor()
consulta = "SELECT descripcion FROM ica_tabla WHERE valor='%s'" % (rango)
#print consulta
resultadodb = cursor.execute(consulta)
for i in resultadodb:
	print i[0]
	
#consulta a la base de datos imc
conexion = sqlite3.connect('gym.db')
cursor = conexion.cursor()
consulta = "SELECT descripcion FROM imc_tabla WHERE valor='%s'" % (rango)
#print consulta
resultadodb = cursor.execute(consulta)
for i in resultadodb:
	print i[0]

	
consulta = "SELECT * FROM ejercicios WHERE rutina='%s'" % rutina
resultadorutina = cursor.execute(consulta)
for i in resultadorutina:
	print i[2] + i[3]
