#se define una lista
lista = [25, 12, 15, 23, 24, 39, 13, 31, 19, 16]
#se ordenan los elementos de menor a mayor 
lista.sort()
#definimos una funcion que calcule la media de los elementos de la lista 
#es el numero medio de la lista de datos recorridos
def mediana(lista):
	mediana_calc = (lista[4] +lista[5])/2
	return mediana_calc
#definimos una funcion que calcule la media aritmetica de los elementos de la lista
#calcula el valor medio de todos los numeros, suma todos y los divide entre la cantidad total 
def media_arit(lista):
	n = len(lista)
	sumatoria = 0
	for indice in range (0, n):
		sumatoria = sumatoria + lista[indice]
	return sumatoria/n	
#definimos una funcion para varianza entre los elementos de la lista 
#el cuadrado de la desviación estándar, más adelante se define
#la desviación estandar.
def varianza(lista):
	n = len(lista)
	sumatoria = 0
	for indice in range (0, n):
		sumatoria = sumatoria + (media_arit(lista)-lista[indice])**2
	return sumatoria/n
#definimos la desviacion estandar
#La desviación estándar es la medida de dispersión más común,
#que indica qué tan dispersos están los datos con respecto a 
#la media. Mientras mayor sea la desviación estándar, mayor 
#será la dispersión de los datos.
def desvia_estan(lista):
	desvi = varianza(lista)**(1/2)
	return desvi
#se aplican las definiciones
mediana_calc = mediana(lista)
media_a = media_arit(lista)
varianza_calc = varianza(lista)
desvia_calc = desvia_estan(lista)
#se imprimen los resultados 
print ("Vector: ",lista)
print ("Mediana: ", mediana_calc)
print ("Media Aritmética: ", media_a) 	
#Beneficios de la varianza:
#1. Cuando existen diferencias entre los datos abismales es muy bueno elevar esta diferencia al cuadrando (recordando que 
#esta diferencia es la desviación estándar)
#2. Cuando puede que existan valores negativos entonces al elevar la difencia al cuadrado hace que sea positiva
print ("Varianza: ", varianza_calc)
print ("Desviación estándar: ",  desvia_calc)
