#Python3
#Algoritmo utilizando la definición de pascal para crear un triángulo

##### 			DEFINICIONES 				##### 
#Definición para colocar numeros en triangulo de pascal
def pascal(n, i):
	if (n==i) or (i==1):
		return 1
	else:
		return pascal(n-1, i-1) + pascal(n-1, i)

#Definicion para contablilizar el numero de filas para el triangulo
def fila_pascal(nivelfila):
	for indice in range (1, nivelfila+1):
		print (pascal(nivelfila, indice), end= "    ") 
	print ("")	

#Se crea la definición para crear el triángulo de pascal el cual contempla
#un triangulo de números enteros,infinito y simétrico.
#Se empieza con un 1 en la primera fila, 
#y en las filas siguientes se van colocando números de forma 
#que cada uno de ellos sea la suma de los dos números que tiene encima.
def trian_pascal(varios):
	for indice in range (1, varios+1):
		fila_pascal(indice)

##### 			IMPLEMENTACION				##### 
nivel = int(input("Digite la cantidad de niveles "))
trian_pascal(nivel)

