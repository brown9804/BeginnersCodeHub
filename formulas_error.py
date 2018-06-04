lista = [25, 12, 15, 23, 24, 39, 13, 31, 19, 16]
lista.sort()
def mediana(lista):
	mediana_calc = (lista[4] +lista[5])/2
	return mediana_calc
def media_arit(lista):
	n = len(lista)
	sumatoria = 0
	for indice in range (0, n):
		sumatoria = sumatoria + lista[indice]
	return sumatoria/n	
	 
def varianza(lista):
	n = len(lista)
	sumatoria = 0
	for indice in range (0, n):
		sumatoria = sumatoria + (media_arit(lista)-lista[indice])**2
	return sumatoria/n

def desvia_estan(lista):
	desvi = varianza(lista)**(1/2)
	return desvi

mediana_calc = mediana(lista)
media_a = media_arit(lista)
varianza_calc = varianza(lista)
desvia_calc = desvia_estan(lista)

print ("Vector: ",lista)
print ("Mediana: ", mediana_calc)
print ("Media Aritmética: ", media_a) 	
print ("Varianza: ", varianza_calc)
print ("Desviación estándar: ",  desvia_calc)
