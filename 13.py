def bisiesto(year):
	if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
		return True
	else:
		return False
an1 = int(input("Digite el año mayor que desea comparar "))
an2 = int(input("Digite el año menor "))
dif = an1 - an2
cont = 0
for indice in range (an2, an1+1):
	if bisiesto(indice) == True:
		cont = cont + 1
print ("La diferencia entre ", an1, " y ", an2, " es de ", dif)
if (cont >0):
	print ("Entre este intervalo de años hay ", cont, " años bisiestos ")	
else: 
	print("No hay años bisiestos en este intervalo ")
