archivo = open("Himno.txt", "r")

lista = archivo.readlines()
for i in lista: 
	print(i)

archivo.close()
