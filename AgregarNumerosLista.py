#Python3 

# ALgoritmo permite ingresar elementos a una lista vacia 

correcto = True
lista = []
print("Algoritmo que permite ingresar numeros a una lista, estos deben ser enteros, el ciclo se detiene cuando se ingresa algo diferente.")

#ciclo continua si se ingresan numeros enteros 
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
