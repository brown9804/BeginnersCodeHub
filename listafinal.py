correcto = True 
lista = []
while (correcto == True):
	try:
		num = ""
		while (num != 0):
			num = int(input("Digite números para una lista "))
			if (num != 0):
				lista.append (num)
		print (lista)
		
		for num in lista:
			print (num)

		consult = int(input("¿Cuál es el número que desea consultar? "))
		if (consult in lista):
			print ("El entero", consult, " digitado se encuentra en la lista ")
		else:
			print ("El número", consult, "no está en la lista " )
		correcto = False
	
	except ValueError as mistake:
		print ("No puedo leer variables ni números reales, su número debe ser entero ", mistake)
		
