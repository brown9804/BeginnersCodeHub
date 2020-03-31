#Python3

#Algoritmo que muestra las diferentes secciones en las que se divide el resultado de una division.
print ("Hola, favor ingrese lo que se le solicita ")
numero1 = input("Ingrese  un número entero que desee dividir: ")
numero2 = input("Ingrese la cantidad por la que desea dividir el número anterior ")

if (int(numero2) == 0):
	print ("Favor digite otro número que no sea cero, ya que no se admite este valor en el denominador debido a que la función se indefine ") #devuelve mensaje ya que no denominador no puede ser cero
 #si el denominador no es cero entoces porsigue a hacer la división
else:
	division = int(numero1) / int(numero2)
	coci = int(numero1) // int(numero2)
	resto = int(numero1) % int(numero2)
	#este procedimiento si el residuo es cero entonces sabe que es exacta
	if (resto == 0):
		print ("Es una división exacta ")
		print ("El cociente de la división es " + str(coci))
		print ("Y su residuo es " + str(resto))
	
 	#Si el residuo o resto es distinto de cero entonces sabe que es no es exacta
	else:
		print ("La división no es exacta ")
		print ("Su cociente es : " + str(coci))
		print ("El residuo es " + str(resto))

