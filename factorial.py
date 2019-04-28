

def factorial(x,n):

	if(n>0):
		# solo si es mayor a cero
		x=factorial(x,n-1)
		x=x*n
	else:
		x=1
	return x

try:
	num = int(raw_input("Digite un numero "))

	calculo=factorial(1,num)
	print "El factorial de %s es %s" % (num,calculo)
except:
	print "\n No es un valor numerico"
