#-*- coding:UTF-8 -*-
#Ingresar a una base da datos el nombre completo, y el codigo de estudiante 
#de un alumno. El programa debe tener un menu para el ingreso de sus cursos
#y notas finales por cada curso. Al final el programa debe calcular el 
#promedio final de semestre

import MySQLdb
conexion = MySQLdb.connect('localhost','root','toor','pythonmysql')
cursor = conexion.cursor()
cursor.execute("select * from alumno")
if cursor.rowcount != 0:
    print "Elija una opcion:"
    print "1. Mostrar lista de alumnos, cursos y notas"
    print "2. Ingresar alumnos"
    print "3. Ingresar cursos"
    print "4. Ingresar notas"
    print "5. Salir"
    opcion = int(raw_input())
    if opcion == 1:
        sql = "select nombre_completo,nombre,nota from notas inner join alumno on alumno.codigo=notas.fk_alumno inner join curso on curso.id_curso=notas.fk_curso order by nombre_completo"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for i in resultado:
			print i[0],"|",i[1],"|",i[2]        
    elif opcion == 2:
		nombre = raw_input("Ingrese el nombre completo: ")
		codigo = raw_input("Ingrese el codigo: ")
		sql = "insert into alumno values ('%s','%s')" % (codigo,nombre)
		cursor.execute(sql)
		conexion.commit()
    elif opcion == 3:
        nombre = raw_input("Ingresa el nombre del curso: ")
        sql = "insert into curso values (null,'%s')" % (nombre)
        cursor.execute(sql)
        conexion.commit()
    elif opcion == 4:
		sql = "select * from alumno"
		cursor.execute(sql)
		alumno = cursor.fetchall()
		for i in alumno:
			print i[0]," => ",i[1]
		codigo = raw_input("Ingresa el codigo del alumno que deseas modificar su nota: ")
		sql = "select * from curso"
		cursor.execute(sql)
		curso = cursor.fetchall()
		for i in curso:
			print i[0]," => ",i[1]
		curso = int(raw_input("Ingresa el codigo del curso en el que deseas poner la nota: "))
		nota = int(raw_input("Ingresa la nota: "))
		sql = "insert into notas values (null,'%s',%d,%d)" % (codigo,curso,nota)
		cursor.execute(sql)
		conexion.commit()
    elif opcion == 5:
		quit()
    else:
		pass
else:
    print "No existen alumnos, debe ingresar al menos uno"
    nombre = raw_input("Ingrese el nombre completo: ")
    codigo = raw_input("Ingrese el codigo: ")
    sql = "insert into alumno values ('%s','%s')" % (codigo,nombre)
    cursor.execute(sql)
    conexion.commit()
