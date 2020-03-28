#Este código permite averiguar si un número ingresado es entero, siendo par o bien impar dado que se debide entre dos y se
#observa su sobrante. Este programa pregunta el número hasta que se ingrese un número impar


#Se ejecuta mediante el comando:
# python3 AveriguaEntero_o_Impar.py


#Se establece una condición de verdadero
correcto = True 
#Ciclo, mientras la condicicón siga siendo verdadera
while (correcto == True ):	
	try:
		#se obtiene dato mediante su ingreso en una variable
		num = int(input("Digite un número "))
		# Se calcula su resto y si es igual a cero es par
		#ejemplo si 50/2 = 25 y no tiene decimales entonces 
		# el número 50 es par
		if (num %2 == 0 ):
			print ("El número:  ", num, " es entero")
		#si no sicede la condición anterior
		else:
			print ("El número: ", num, "es impar") 
		# se cambia el estado de la variable correcto para que el ciclo termine 
		correcto = False 
	except ValueError as mistake:
		print ("No puedo trabajar con variables ni números que no sean enteros (int) ", mistake)
	
