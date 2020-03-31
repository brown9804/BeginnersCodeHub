#Python3


#Muestra como leer lineas de un archivo de texto .txt 

#Abre archivo
archivo = open("Himno.txt", "r")

#Lee las lineas 
lista = archivo.readlines()

#Pasa por casa elemento de la lista
for i in lista: 
	print(i)
#Cierra el archivo
archivo.close()
