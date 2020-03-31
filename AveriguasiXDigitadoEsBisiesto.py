#Python3 

#Sirve para averiguar si un año es bisiesto
print ("Vamos a averiguar si el año de su gusto es bisiesto o no")
year = input("Digite el año ")

if ((int(year)%400) == 0):
	if ((int(year)%4) == 0): 
		if ((int(year)%100) != 0):
			print ("El año " + str(year) + " es un año bisiesto")
		elif  ((int(year)%400) == 0) and ((int(year)%100) == 0):
			print("Sabemos que el año " +str(year) + " es bisiesto")
else:
	if ((int(year)%4) == 0):
		if((int(year)%100) != 0):
			print ("Año " +str(year) + " corresponde a un año bisiesto") 
		else:
			print("El año digitado " + str(year) + " no es bisiesto")
	else:
		print ("No es bisiesto el año " + str(year))
