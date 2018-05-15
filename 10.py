num = input ("Ingrese el número de tabla de multiplicar que desea imprimir: ")

while (int(num) >= 0):
	print ("Tabla del " + num)	
	for multi in range (1,13):
		resultado = int(num)*multi
		print (int(num), "*" , multi, "= ", resultado)
	print ("Se ha mostrado la tabla del número digitado multiplicado desde el 1 al 12")
	num = input("Ahora cuál número quiere imprimir? ")
else:
	print ("No le puedo mostrar las tablas de multiplicación de un número menor a cero")

		
		
