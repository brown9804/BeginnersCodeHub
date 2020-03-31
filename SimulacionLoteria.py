#Python3 

#Este algoritmo permite representar la forma en la que se realiza el sorteo de loteria, grosso modo cualquier sorteo.

###### 					IMPORTANDO PAQUETES 					######
from random import *


###### 					IMPLEMENTANDO 					######

num = input("Digite el número que desea jugar ")

if int(num) in range (0,100):
	veces = input("Cuántos sorteos desea jugar? ")
	veces = int(veces)
	if (veces >=1) and (veces<=10000):
		ganadas = 0
		for veces in range (1, veces+1):
			num_gan = randint(0,100)
			if (int(num) == num_gan):
				ganadas = ganadas + 1
		beneficio = ganadas*50000
		paga = veces*1000
		balance = beneficio - paga
		print ("Veces jugadas: ", veces)
		print ("Veces ganadas: ", ganadas)
		print ("Ha invertido: ", paga)
		print ("Total ganado: ", beneficio)
		print ("Balance ", balance)
	else: 
		print ("No puede jugar cero veces ni más de 10000 veces")		
else: 
 	print("Para poder jugar debe escoger un número entre elque vaya desde cero hasta el 99")

