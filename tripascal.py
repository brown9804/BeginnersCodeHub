def pascal(n, i):
	if (n==i) or (i==1):
		return 1
	else:
		return pascal(n-1, i-1) + pascal(n-1, i)
	
def fila_pascal(level):
	for indice in range (1, level+1):
		print (pascal(level, indice), end= "    ") 
	print ("")	

def trian_pascal(many):
	for indice in range (1, many+1):
		fila_pascal(indice)

nivel = int(input("Digite la cantidad de niveles "))
trian_pascal(nivel)

