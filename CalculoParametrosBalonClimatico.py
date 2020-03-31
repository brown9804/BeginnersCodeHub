#Python3 
#Calculo de algunas propiedades de un balón climático

####### 			DEFINICIONES				#######

#Definición de velocidad para un balón climático
def velocidad(t):
	vel = -0.48*(t**3) + 36*(t**2) - 760*t + 4100
	return vel 
#Definición de la altitud para un balón climático
def altitud(t):
	alt =  -0.12*t*t*t*t + 12*t*t*t -380*t*t + 4100*t + 220
	return alt

def velocidadconv(t):
	v = t/3600
	return v 
#Avance en el proceso de algunas variables dependientes del tiempo
def proce(inicio, final, incremen):
	hmax = 0 
	horahmx = 0
	for indice in range (inicio, final +1, incremen):
		vel = velocidad(indice)
		alt = altitud(indice)
		velcn = velocidadconv(vel)
		if alt > hmax:
			hmax = alt
			horahmx = indice
		print("{0:2}h   {1:8.2f}m       {2:3.2f}m/s".format(indice, alt, velcn))
	print("La altura máxima se alcanzó a las", horahmx, "horas \n Esta altura máxima fue de ", hmax, "metros")


####### 			IMPLEMENTACION				#######

timei = int(input("Ingrese el tiempo inicial para calcular la velocidad y la altitud para este balón climático "))
timef = int(input("Digite el tiempo final "))
incre = int(input("Digite el incremento de horas "))

if (timei>=0) and (timef<48):
		proce(timei, timef, incre) 	
else:
	while (timei<0) and (timef>48):
		print("Debe digitar un tiempo inicial mayor o igual a cero y el tiempo final debe ser menor a las 48 horas")
		timei = int(input("Ingrese el tiempo inicial para calcular la velocidad y la altitud para este balón climático"))
		timef = int(input("Digite el tiempo final "))
	
