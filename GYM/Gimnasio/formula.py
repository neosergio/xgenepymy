#importando librerias
import math

#consulta de Actividad
#def consulta_actividad (actividad):
#	if actividad = 1:
#		respuesta = 'Sedentario'
#	elif actividad = 2:
#		respuesta = 'Moderado'
#	elif actividad = 3:
#		respuesta = 'Activo'
#	else:
#		respuesta = null
#	return respuesta


#calculo del IMC
def imc_calculo(peso, altura):
	altura = float(altura)/100
	resultado = float(peso)/float(altura*altura)
	return resultado

#Calculo de rango IMC
def consulta_imc(imc):
	if imc < 15:
		respuesta = '<15'
	elif imc >= 15 and imc < 18.5:
		respuesta = '>15y<18.5'
	elif imc >= 18.5 and imc < 25:
		respuesta = '>18.5y<25'
	elif imc >= 25 and imc < 30:
		respuesta = '>25y<30'
	elif imc >= 30 and imc < 40:
		respuesta = '>30y<40'
	elif imc >= 40:
		respuesta = '>40'
	else:
		respuesta = null
	return respuesta


#calculo del ICA
def ica_calculo(cintura, altura):
	cintura = float(cintura)
	altura = float(altura)
	resultado = float(cintura)/float(altura)
	return resultado

#Calculo de rango ICA
def consulta_ica(ica):
	if ica < 0.5:
		respuesta = '<0.5'
	elif ica >= 0.5:
		respuesta = '>0.5'
	else:
		respuesta = null
	return respuesta

#porcentaje de grasa corporal
def pgc_calculo(cintura, cuello, altura, sexo, cadera = 0):
	if sexo == 1:
		resultado = ((495)/((1.0324-(0.19077*math.log10(float(cintura-cuello))))+(0.15456*math.log10(float(altura))))) - 450
		return resultado
	elif sexo == 2:
		resultado = ((495)/((1.29579-(0.35004*math.log10(float(cintura+cadera-cuello))))+(0.22100*math.log10(float(altura)))))-450
		return resultado
		
#Calculo de rango PGC masculino
def consulta_pgcm(pgc):
	if pgc < 2:
		respuesta = '<2'
	if pgc >= 2 and pgc < 6:
		respuesta = '>=2y<6'
	elif pgc >= 6 and pgc < 14:
		respuesta = '>=6y<14'
	elif pgc >= 14 and pgc < 18:
		respuesta = '>=14y<18'
	elif pgc >= 18 and pgc < 26:
		respuesta = '>=18y<26'
	elif pgc >= 26:
		respuesta = '>=26'
	else:
		respuesta = null
	return respuesta


#Calculo de rango PGC femenino
def consulta_pgcf(pgc):
	if pgc < 10:
		respuesta = '<10'
	if pgc >= 10 and pgc < 14:
		respuesta = '>=10y<14'
	elif pgc >= 14 and pgc < 21:
		respuesta = '>=14y<21'
	elif pgc >= 21 and pgc < 25:
		respuesta = '>=21y<25'
	elif pgc >= 25 and pgc < 32:
		respuesta = '>=25y<32'
	elif pgc >= 32:
		respuesta = '>=32'
	else:
		respuesta = False
	return respuesta
	
	
#calculo de Masa Corporal Magra
#def mcm_calculo(pgc, peso, sexo, cadera = 0):
#	if sexo == 'M':
#		#altura = float(altura)/100
#		resultado = float(peso)*(100-float(pgc)
#		return resultado
#	elif sexo == 'F':
#		altura = float(altura)/100
#		resultado = float(peso)*(100-float(pgc)
#		return resultado
#	else:
#		return null
#
#Calculo de MCM
#def consulta_mcm(mcm):
#	if pgmf >= 10 and pgmf < 14:
#		respuesta = '>10y<14'
#	elif pgmf >= 14 and pgmf < 21:
#		respuesta = '>14y<21'
#	elif pgmf >= 21 and pgmf < 25:
#		respuesta = '>21y<25'
#	elif pgmf >= 25 and pgmf < 32:
#		respuesta = '>25y<32'
#	elif pgmf >= 32:
#		respuesta = '>32'
#	else:
#		respuesta = null
#	return respuesta

def calculo_rutina(imc, ica, pgc, sexo):
	if imc < 15:
		imc_consulta = "IMC1"
	elif imc >= 15 and imc <18.5:
		imc_consulta = "IMC2"
	elif imc >= 18.5 and imc <25:
		imc_consulta = "IMC3"
	elif imc >= 25 and imc <30:
		imc_consulta = "IMC4"
	elif imc >= 30 and imc <40:
		imc_consulta = "IMC5"
	elif imc >= 40:
		imc_consulta = "IMC6"
	else:
		imc_consulta = "ERROR IMC"
	
	
	if ica < 0.5:
		ica_consulta = "ICA1"
	elif ica >= 0.5:
		ica_consulta = "ICA2"
	else:
		ica_consulta = "ERROR ICA"
	
	if sexo == 2:
		sexo_text = 'F'
		#rango pgc FEMENINO
		if pgc >= 10 and pgc < 14:
			pgc_consulta = "PGC1"
		elif pgc >= 14 and pgc <21:
			pgc_consulta = "PGC2"
		elif pgc >= 21 and pgc <25:
			pgc_consulta = "PGC3"
		elif pgc >= 25 and pgc <32:
			pgc_consulta = "PGC4"
		elif pgc >= 32:
			pgc_consulta = "PGC5"
		else:
			pgc_consulta = "ERROR PGCF"
	elif sexo == 1:
		sexo_text = 'M'
		#rango pgc masculino
		if pgc >= 2 and pgc < 6:
			pgc_consulta = "PGC1"
		elif pgc >= 6 and pgc <14:
			pgc_consulta = "PGC2"
		elif pgc >= 14 and pgc <18:
			pgc_consulta = "PGC3"
		elif pgc >= 18 and pgc <26:
			pgc_consulta = "PGC4"
		elif pgc >= 26:
			pgc_consulta = "PGC5"
		else:
			pgc_consulta = "ERROR PGCM"


	resultado = str(imc_consulta) + str(ica_consulta) + str(pgc_consulta) + sexo_text
	return resultado

def consulta_rutina(resultado):
	if resultado == 'IMC1ICA1PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC1ICA1PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC1ICA1PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC1ICA1PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC1ICA1PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC1ICA1PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC1ICA1PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC1ICA1PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC1ICA1PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC1ICA1PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC1ICA1PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC1ICA1PGC6F':
		rutina = 'RUT6F'
		
		
#		---
	elif resultado == 'IMC1ICA2PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC1ICA2PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC1ICA2PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC1ICA2PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC1ICA2PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC1ICA2PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC1ICA2PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC1ICA2PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC1ICA2PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC1ICA2PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC1ICA2PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC1ICA2PGC6F':
		rutina = 'RUT6F'
#####

	elif resultado == 'IMC2ICA1PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC2ICA1PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC2ICA1PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC2ICA1PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC2ICA1PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC2ICA1PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC2ICA1PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC2ICA1PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC2ICA1PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC2ICA1PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC2ICA1PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC2ICA1PGC6F':
		rutina = 'RUT6F'
		
#		---
	elif resultado == 'IMC2ICA2PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC2ICA2PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC2ICA2PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC2ICA2PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC2ICA2PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC2ICA2PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC2ICA2PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC2ICA2PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC2ICA2PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC2ICA2PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC2ICA2PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC2ICA2PGC6F':
		rutina = 'RUT6F'
#####

	elif resultado == 'IMC3ICA1PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC3ICA1PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC3ICA1PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC3ICA1PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC3ICA1PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC3ICA1PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC3ICA1PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC3ICA1PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC3ICA1PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC3ICA1PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC3ICA1PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC3ICA1PGC6F':
		rutina = 'RUT6F'
		
#		---
	elif resultado == 'IMC3ICA2PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC3ICA2PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC3ICA2PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC3ICA2PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC3ICA2PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC3ICA2PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC3ICA2PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC3ICA2PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC3ICA2PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC3ICA2PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC3ICA2PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC3ICA2PGC6F':
		rutina = 'RUT6F'	
		
#####

	elif resultado == 'IMC4ICA1PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC4ICA1PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC4ICA1PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC4ICA1PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC4ICA1PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC4ICA1PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC4ICA1PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC4ICA1PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC4ICA1PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC4ICA1PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC4ICA1PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC4ICA1PGC6F':
		rutina = 'RUT6F'
		
#		---
	elif resultado == 'IMC4ICA2PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC4ICA2PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC4ICA2PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC4ICA2PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC4ICA2PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC4ICA2PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC4ICA2PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC4ICA2PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC4ICA2PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC4ICA2PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC4ICA2PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC4ICA2PGC6F':
		rutina = 'RUT6F'	
		
#####
	
	elif resultado == 'IMC5ICA1PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC5ICA1PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC5ICA1PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC5ICA1PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC5ICA1PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC5ICA1PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC5ICA1PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC5ICA1PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC5ICA1PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC5ICA1PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC5ICA1PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC5ICA1PGC6F':
		rutina = 'RUT6F'
		
#		---
	elif resultado == 'IMC5ICA2PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC5ICA2PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC5ICA2PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC5ICA2PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC5ICA2PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC5ICA2PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC5ICA2PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC5ICA2PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC5ICA2PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC5ICA2PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC5ICA2PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC5ICA2PGC6F':
		rutina = 'RUT6F'
		
	
#####

	elif resultado == 'IMC6ICA1PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC6ICA1PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC6ICA1PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC6ICA1PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC6ICA1PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC6ICA1PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC6ICA1PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC6ICA1PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC6ICA1PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC6ICA1PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC6ICA1PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC6ICA1PGC6F':
		rutina = 'RUT6F'
		
#		---
	elif resultado == 'IMC6ICA2PGC1M':
		rutina = 'RUT1M'
		
	elif resultado == 'IMC6ICA2PGC1F':
		rutina = 'RUT1F'
	
	elif resultado == 'IMC6ICA2PGC2M':
		rutina = 'RUT2M'
	
	elif resultado == 'IMC6ICA2PGC2F':
		rutina = 'RUT2F'
	
	elif resultado == 'IMC6ICA2PGC3M':
		rutina = 'RUT3M'
	
	elif resultado == 'IMC6ICA2PGC3F':
		rutina = 'RUT3F'
		
	elif resultado == 'IMC6ICA2PGC4M':
		rutina = 'RUT4M'
	
	elif resultado == 'IMC6ICA2PGC4F':
		rutina = 'RUT4F'
		
	elif resultado == 'IMC6ICA2PGC5M':
		rutina = 'RUT5M'
	
	elif resultado == 'IMC6ICA2PGC5F':
		rutina = 'RUT5F'
		
	elif resultado == 'IMC6ICA2PGC6M':
		rutina = 'RUT6M'
	
	elif resultado == 'IMC6ICA2PGC6F':
		rutina = 'RUT6F'
		
	else:
		print resultado
		rutina = 'NO COINCIDE'
#####
	
	return rutina

