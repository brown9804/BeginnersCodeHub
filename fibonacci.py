def fibo(s):
	if s == 0: 
		return 0
	elif s == 1:
		return 1
	else:
		return (fibo(s-1) +fibo(s-2))

n = int(input("Cuántos elementos desea?  "))
for indice in range(0, n+1):
	print(fibo(indice), end= " , ")
print( "...")

