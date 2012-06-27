#-*- coding:utf-8 -*-
#importando formulas y la libreria de conexion a BD
import sqlite3
import datetime
from formula import imc_calculo, consulta_imc
from formula import ica_calculo, consulta_ica
from formula import pgc_calculo, consulta_pgcm
from formula import pgc_calculo, consulta_pgcf
from formula import calculo_rutina, consulta_rutina
#importando libreria grafica
from Tkinter import *
import login

#funciones de procesamiento
def conectar(consulta):
	conexion = sqlite3.connect('gym.db')
	cursor = conexion.cursor()
	resultado = cursor.execute(consulta)
	conexion.commit()
	return resultado

def procesar():
	Fecha = str(datetime.datetime.now())
	Nombre_completo = nombrecompleto.get()
	Peso = peso.get()
	Altura = altura.get()
	Cintura = cintura.get()
	Cuello = cuello.get()
	Genero = genero.get()
	Cadera = cadera.get()

	registro_bd = "INSERT INTO persona VALUES (NULL,'%s','%s',%d, %d, %d, %d, %d, %d)" % (Nombre_completo,Fecha,Peso,Altura,Cintura,Cuello,Genero,Cadera)
	conectar(registro_bd)
	
	imc_valor = imc_calculo(Peso, Altura)
	ica_valor = ica_calculo(Cintura, Altura)
	pgc_valor = pgc_calculo(Cintura, Cuello, Altura, Genero, Cadera)
	imc.set("Su indice de masa corporal es "+str(imc_valor))
	ica.set("Su indice de cintura altura es "+str(ica_valor))
	pgc.set("Su porcentaje de grasa corporal es "+str(pgc_valor))
	
	imc_condicion = consulta_imc(imc_valor)
	imc_consulta_bd = "SELECT descripcion FROM imc_tabla WHERE valor='%s'" % (imc_condicion)
	imc_resultado = conectar(imc_consulta_bd) 
	for i in imc_resultado:
		condicion_imc.set("Su condicion es "+str(i[0]))
		
	ica_condicion2 = consulta_ica(ica_valor)
	ica_consulta_bd = "SELECT descripcion FROM ica_tabla WHERE valor='%s'" % (ica_condicion2)
	ica_resultado = conectar(ica_consulta_bd) 
	for i in ica_resultado:
		condicion2_ica.set("Ud está "+str(i[0]))
		
	#IMPRESION TEMPORAL DE PERSONAS
	busqueda_bd = "SELECT * FROM persona";
	resultado_busqueda = conectar(busqueda_bd)
	for persona in resultado_busqueda:
		print "%s se registro el %s con las medidas: " % (persona[1], persona[2])
		print "peso: %d " % (persona[3])
		print "altura: %d " % (persona[4])
		print "cintura: %d " % (persona[5])
		print "cuello: %d " % (persona[6])
		print "genero: %d " % (persona[7])
		print "cadera: %d " % (persona[8])

	#Calculando rutina
	calculo = calculo_rutina(imc_valor, ica_valor, pgc_valor, Genero)
	rutina_obtenida = consulta_rutina(calculo)
	rutina_bd = "SELECT * FROM ejercicios WHERE rutina='%s'" % rutina_obtenida
	resultado_rutina = conectar(rutina_bd)
	lista_rutina = ''
	for ejercicios in resultado_rutina:
		lista_rutina += ejercicios[2] + ": " + ejercicios[3]+"\n"
	resultadorutina.set(lista_rutina)


#Instancia de la clase Tk
ventana = Tk()
ventana.title('Generador de Rutinas')

#Variables que almacenarán los datos
nombrecompleto = StringVar()
peso = IntVar()
altura = IntVar()
cintura = IntVar()
cuello = IntVar()
genero = IntVar()
genero.set(1)
cadera = IntVar()
actividad = StringVar()
actividad.set("Sedentario")

#variables calculadas
imc = StringVar()
ica = StringVar()
pgc = StringVar()
condicion_imc = StringVar()
condicion2_ica = StringVar()
rutina = StringVar()
resultadorutina = StringVar()

#generación de widgets
#datos personales
etiqueta_nombre = Label(ventana, text='Nombre completo:')
entrada_nombre = Entry(ventana, textvariable=nombrecompleto)
etiqueta_nombre.grid(row=1, column=1)
entrada_nombre.grid(row=1, column=2)

#peso
etiqueta_peso = Label(ventana, text='Peso:')
entrada_peso = Entry(ventana, textvariable=peso)
etiqueta_peso.grid(row=2, column=1)
entrada_peso.grid(row=2, column=2)

#altura
etiqueta_altura = Label(ventana, text='Altura: ')
entrada_altura = Entry(ventana, textvariable=altura)
etiqueta_altura.grid(row=3, column=1)
entrada_altura.grid(row=3, column=2)

#cintura
etiqueta_cintura = Label(ventana, text='Cintura: ')
entrada_cintura = Entry(ventana, textvariable=cintura)
etiqueta_cintura.grid(row=4, column=1)
entrada_cintura.grid(row=4, column=2)

#cuello
etiqueta_cuello = Label(ventana, text='Cuello: ')
entrada_cuello = Entry(ventana, textvariable=cuello)
etiqueta_cuello.grid(row=5, column=1)
entrada_cuello.grid(row=5, column=2)

#genero
etiqueta_genero = Label(ventana, text='Genero: ')
entrada_genero_1 = Radiobutton(ventana, text='Masculino', variable=genero, value=1)
entrada_genero_2 = Radiobutton(ventana, text='Femenino', variable=genero, value=2)
etiqueta_genero.grid(row=6, column=1)
entrada_genero_1.grid(row=6, column=2)
entrada_genero_2.grid(row=7, column=2)

#cadera
etiqueta_cadera = Label(ventana, text='Cadera: ')
entrada_cadera = Entry(ventana, textvariable=cadera)
etiqueta_cadera.grid(row=8, column=1)
entrada_cadera.grid(row=8, column=2)

#actividad
etiqueta_actividad = Label(ventana, text='Actividad: ')
entrada_actividad = OptionMenu(ventana, actividad, "Sedentario", "Moderado", "Activo")
etiqueta_actividad.grid(row=9, column=1)
entrada_actividad.grid(row=9, column=2)
logo = PhotoImage(file='ratgym.gif')
etiqueta_espacio = Label(ventana, image=logo)
etiqueta_espacio.grid(row=10, column=1)

#botonprocesar
boton_procesar = Button(ventana, text='Procesar', command=procesar, width=20)
boton_procesar.grid(row=14, column=2)

#impresion resultado
etiqueta_resultado = Label(ventana, text='Resultado: ')
salida_imc = Label(ventana, textvariable=imc)
salida_ica = Label(ventana, textvariable=ica)
salida_pgc = Label(ventana, textvariable=pgc)
salida_condicion = Label(ventana, textvariable=condicion_imc)
salida_condicion2 = Label(ventana, textvariable=condicion2_ica)
etiqueta_resultado.grid(row=15, column=1)
salida_imc.grid(row=15, column=2) 
salida_ica.grid(row=16, column=2) 
salida_pgc.grid(row=17, column=2) 
salida_condicion.grid(row=18, column=2)
salida_condicion2.grid(row=19, column=2) 

#impresion rutina
etiqueta_rutina = Label(ventana, text='RUTINA')
salida_rutina = Label(ventana, text='Su rutina es...')
etiqueta_rutina.grid(row=20, column=2)
salida_rutina.grid(row=21, column=1)
etiqueta_resultado_rutina = Label(ventana, textvariable=resultadorutina, anchor=W, justify=LEFT)
etiqueta_resultado_rutina.grid(row=21, column=2)

#ejecución de ventana
ventana.mainloop()
