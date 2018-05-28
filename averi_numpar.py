correcto = True
while (correcto == True):
	try:
		num = int(input("Digite un número: "))  
		if(num != 0) and (num % 2 == 0):
			print ("El número: ", num, " es par")
		elif (num == 0):
			num = num // 0
			raise ZeroDivisionError
		else:
			print ("El número: ", num, " es impar")
		correcto = False
	except ValueError as error:
		print ("No puedo trabajar con variables ni números reales ", error)
	except ZeroDivisionError  as mistake:
		print ("Ingrese otro valor que no sea cero ", mistake)
