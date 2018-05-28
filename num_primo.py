def primo_o_no(num, fac):
	if (num % fac == 0):
		return True
	else:
		return False
numero = int(input("Digite un número para verificar si es primo o no "))
cont = 0
for factor in range (2, numero):
	if primo_o_no(numero, factor) == True:
		print ("El número ", numero, "es divisible ", factor)
		cont = cont + 1	
if (cont >0):
	print ("El número digitado ", numero, " no es primo")
else:
	print ("El número ", numero, "es primo ")	
