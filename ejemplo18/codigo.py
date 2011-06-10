#-*- coding:UTF-8 -*-
#Importar las librerias para gtk y MySQL
import gtk
import MySQLdb

class Ventana:
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file('ventanaprincipal.glade')
		self.ventana = self.builder.get_object('ventana1')
		self.entrada1 = self.builder.get_object('entrada1')
		self.entrada2 = self.builder.get_object('entrada2')
		self.entrada3 = self.builder.get_object('entrada3')
		self.etiqueta1 = self.builder.get_object('etiqueta1')
		self.ventana.show_all()
		self.builder.connect_signals(self)

	def promedio(self, widget):
		numero1 = float(self.entrada1.get_text())
		numero2 = float(self.entrada2.get_text())
		promedio = (numero1 + numero2)/2
		conectar = MySQLdb.connect('localhost','root','toor','ejemplo')
		cursor = conectar.cursor()
		sql = "INSERT INTO numeros VALUES (%f)" % promedio
		cursor.execute(sql)
		conectar.commit()
		cursor.close()
		conectar.close()
		self.entrada1.set_text('')
		self.entrada2.set_text('')

	def mensaje(self, widget):
		nombre = self.entrada3.get_text()
		mensaje = "Ojala que apruebes, "+nombre
		self.entrada3.set_text('')
		self.etiqueta1.set_text(mensaje)
		conectar = MySQLdb.connect('localhost','root','toor','ejemplo')
		cursor = conectar.cursor()
		sql = "INSERT INTO personas VALUES ('%s')" % nombre
		cursor.execute(sql)
		conectar.commit()
		cursor.close()
		conectar.close()
		
if __name__=="__main__":
	variable = Ventana()
	gtk.main()
