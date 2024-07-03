#Python3 


#Se solicita datos
comp = input("Digite un año para averiguar cuánto tiempo ha transcurrido o cuánto falta para llegar ")

#Si la fecha está dentro del 2018
if (int(comp) == 2018):
	print("Estamos en el año que digitó, no falta tiempo para llegar al 2018 ")

#Procedimiento si es un año futuro, es decir, posterior al 2018
elif(int(comp) >= 2018):
	print("El año digitado es mayor al año en que estamos")
	falt = int(comp) - 2018
	print ("Faltan " +str(falt) +" años")
	if (falt == 1):
		print("Falta un año")

#si ya pasó el año
else:
	print("Vamos a calcular cuántos años han pasado ")
	hac = 2018 - int(comp)
	print("Pasaron " +str(hac) +" años")
	if (hac == 1):
		print ("Ha transcurrido un año ") 
