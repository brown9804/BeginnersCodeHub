#Python3 

#Algoritmo que representa la sucesión o serie de Fibonacci. La sucesión comienza con los números 0 y 1,2 a 
#partir de estos, cada término es la suma de los dos anteriores, es la relación de recurrencia que la define.

#####					DEFINICIONES 					#####

def fibo(s):
	if s == 0: 
		return 0
	elif s == 1:
		return 1
	else:
		return (fibo(s-1) +fibo(s-2))

#####					IMPLEMENTACION 					#####

n = int(input("Cuántos elementos desea?  "))
for indice in range(0, n+1):
	print(fibo(indice), end= " , ")
print( "...")

