#Python3

#Permite analizar si el numero ingresado es par

correcto = True

#Ciclo para averiguar si los numeros digitados son par 
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
		print ("No puedo trabajar con variables ni números imaginarios ", error)
	except ZeroDivisionError  as mistake:
		print ("Ingrese otro valor que no sea cero ", mistake)
