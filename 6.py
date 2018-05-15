correcto = True 
while (correcto == True ):	
	try:
		num = int(input("Digite un número "))
		if (num %2 == 0 ):
			print ("El número:  ", num, " es entero")
		else:
			print ("El número: ", num, "es impar") 
		correcto = False 
	except ValueError as mistake:
		print ("No puedo trabajar con variables ni números que no sean enteros ", mistake)
	
