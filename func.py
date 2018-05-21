from math import pi
from math import sin 
def sinc(x):
	if x !=0 :
		result = (sin(pi*x))/(pi*x)	
	elif x == 0:
		result = 1
	return result 

def incre(a,b):
	inc = (b-a)/10
	return inc

def tabla(a, b):
	print("x                sinc(x)")
	for indice in range (0,11):
		incremento = incre(a, b)
		variable = a + (indice*incremento)
		seno = sinc(variable)
		print("{0:5.2f}           {1:4.20f}       ".format(variable, seno))
limsup = int(input("Digite el límite superior en el que desea evaluar la función "))
liminf = int(input("Ingrese el límite inferior en el que quiere evaluar la función ")) 	

tabla(limsup, liminf)	
