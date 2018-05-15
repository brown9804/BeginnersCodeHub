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
		correcto = False	
	except ValueError  as err:
		print ("No puedo leer variables ni números reales ")
