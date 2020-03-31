#Python3

#Algoritmo para pasar numero entero a binario

dividendo = input("Ingrese el número que desea pasar a binario, para esto el número debe ser mayor que cero ")
dividendo = int(dividendo)

if (dividendo >= 0):
	binario = ""
	cociente = dividendo
	while (dividendo >0):
		cociente = dividendo // 2
		residuo = dividendo - (cociente*2)
		binario = str(residuo) + binario
		dividendo = cociente
		
	print ("El número transformado en binario es ", str(binario))		
	
else:
	print("No puedo pasar un número menor a cero a binario, lo lamento ")
