#Python3

#Ejemplifica el uso de la propiedad de Object Oriented de Python

########				CLASES				########
class Estacion():
	def __init__(self, nombre):
		self.nombre = nomnbre
		self.veces = [0,0]
		self.cantidad = [0,0]
	def sumar_veces(self,cantidad, mes):
		if (mes==12) or (mes==1) or (mes==2) or (mes==3) or (mes==4) or (mes==5):
			self.veces[0] = self.veces[0] +1
			self.cantidad[0] = self.cantidad[0] + cantidad
		else:
			self.veces[1] = self.veces[1] +1 
			self.cantidad[1] = self.camtidad[1] + cantidad
	def imprimir_veces(self):
		print(self.nombre, "	", self.veces[0], "	", self.veces[1])

	def imprimir_cantidad(self):
		print(self.nombre, "	", self.cantidad[0],"	", self.cantidad[1])

	def imprimir_promedios(self):
		if self.cantidad[0]==0:
			promedio_seca = self.cantidad[1]/self.veces[1]
			print(self.nombre,"	", "0.00", promedio_seca)
		elif(self.cantidad[1]==0):
			promedio_lluvioso = self.cantidad[0]/self.veces[0]
			print(self.nombre, promedio_lluvioso, "0.00")
		elif(self.cantidad[0] == 0 and self.cantidad[1]==0):
			print("El promedio de precipitación es cero, no ha llovido")
		else:
			promedio_seca = self.cantidad[1]/self.veces[1]
			promedio_lluvioso = self.cantidad[0]/self.veces[0]
			print(self.nombre, promedio_lluvioso, promedio_seca)

class Inst.m():
	def __init__(self,nombre):
		self.nom = nombre
		self.san_pedro = Estacion("San Pedro")
		self.chirripo = Estacion("Chirripó")
		self.liberia = Estacion("Liberia")
	def cargar_archivo(self, nombre_archivo):
		archivo = open(nombre_archivo, "r")
		for linea in archivo:
			lugar, fecha, cantidad = linea.split(",")
			if lugar == "San Pedro":
				self.san_pedro.sumar_veces(float(cantidad), int(fecha[5:7]))
			elif lugar == "Chirripó":
				self.chirripo.sumar_veces(float(cantidad), int(fecha[5:7])
			elif lugar == "Libreria":
				self.liberia.sumar_veces(float(cantidad), int(fecha[5:7]))
	def mostrar_resultados(self):
		print("**************************")
		print(self.nombre)
		print("**************************")
		print()
		print("Cantidad de lluvia por temporada")
		print("Lugar 	Alta 	Baja")
		self.san_pedro.imprimir_veces()
		self.chirripo.imprimir_veces()
		self.liberia.imprimir_veces()
		print("Precipitación por temporada")
		print("Lugar    Alta    Baja")
		self.san_pedro.imprimir_cantidad()
		self.chirripo.imprimir_cantidad()
		self.san_pedro.imprimir_cantidad()
		print()
		print("Promedio de precipitación")
		print("Lugar    Alta    Baja")
		self.san_pedro.imprimir_promedio()
		self.chirripo.imprimir_promedio()
		self.liberia.imprimir_promedio()

########				IMPLEMENTACION				########

place= Inst.m("Precipación por temporada")
#esta linea es para cargar el arhivo que desea leer place.cargar_archivo("nombre del archivo.txt")
place.mostrar_resultados()

