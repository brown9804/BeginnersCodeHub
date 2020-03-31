#Python3 

#Este ejemplo crea un archivo txt con los datos de una franquicia de tiendas, y manipula los datos 
# utilizando Object Oriented de Python

#Para crear el archivo
archivo = open("Datos.txt", "w")
archivo.write("Jacó, 2018/01/03, 45000\n")
archivo.write("Tamarindo, 2018/02/24, 20000\n")
archivo.write("Jacó, 2018/04/03, 5000\n")
archivo.write("Jacó, 2018/01/23, 145000\n")
archivo.write("Tamarindo, 2018/01/24, 213000\n")
archivo.write("Jacó, 2018/04/13, 5000\n")
archivo.write("Jacó, 2018/02/13, 25000\n")
archivo.write("Tamarindo, 2018/01/20, 23000\n")
archivo.close()

###### 				CLASES 				######

class Tienda():
	def __init__(self, nombre):
		self.nombre = nombre
		self.monto =[0,0]
		self.cantidad =[0,0]
	def sumar_venta(self, monto, mes):
		if (mes == 1) or (mes==12) or (mes==2) or (mes==7):
			self.cantidad[0] = self.cantidad[0] + 1.
			self.monto[0] = self.monto[0] + monto
		else:
			self.cantidad[1] = self.cantidad[1] +1
			self.monto[1] = self.monto[1] + monto 
	def imprimir_cantidad(self):
		print(self.nombre,"    	", self.cantidad[0],"		", self.cantidad[1])

	def imprimir_montos(self):
		print(self.nombre,"    	", self.monto[0],"	    ", self.monto[1])

	def imprimir_promedios(self):
		if (self.monto[0] == 0):
			promedio_baja = self.monto[1]/self.cantidad[1]
			print(self.nombre,  "	 0.00", promedio_baja)	
		elif  (self.monto[1]==0):
			promedio_alta = self.monto[0]/self.cantidad[0]
			print(self.nombre, promedio_alta, "	 0.00")
		elif (self.monto[0] ==0 and self.monto[1]==0):
			print(self.nombre, "	Su promedio de ventas es cero, lo lamento")
		else:
			promedio_baja = self.monto[1]/self.cantidad[1]
			promedio_alta = self.monto[0]/self.cantidad[0]		
			print(self.nombre,"	", promedio_alta,"	", promedio_baja)


class Negocio():
	def __init__(self, nombre):
		self.nombre = nombre
		self.jaco = Tienda("Jacó")
		self.tamarindo = Tienda("Tamarindo")
	def cargar_archivo(self, nombre_archivo):
		archivo= open(nombre_archivo, "r")
		for linea in archivo:
			tienda, fecha, monto = linea.split(",")
			if tienda == "Jacó":
				self.jaco.sumar_venta(float(monto),int(fecha[6:8]))
			elif tienda=="Tamarindo":
				self.tamarindo.sumar_venta(float(monto), int(fecha[6:8]))
		archivo.close()
	def mostrar_resultados(self):
		print("********************************")
		print(self.nombre)
		print("********************************")
		print()
		print("Cantidad de Ventas por Temporada")
		print("Tienda		Alta		Baja")
		self.jaco.imprimir_cantidad()
		self.tamarindo.imprimir_cantidad()
		print()
		print("Total de Ventas por temporada")
		print("Tienda		Alta		Baja")
		self.jaco.imprimir_montos()
		self.tamarindo.imprimir_montos()
		print()
		print("Promedio de Ventas por Temporada")
		print("Tienda		Alta		Baja")
		self.jaco.imprimir_promedios()
		self.tamarindo.imprimir_promedios()

		
###### 				IMPLEMENTACION 				######

artesanias = Negocio("   Artesanías de Costa Rica  ")
artesanias.cargar_archivo("Datos.txt")
artesanias.mostrar_resultados()

