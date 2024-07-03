#Python3 

# Permite ejemplificar como agregar lineas de texto a un archivo extension .txt

#Agregando lineas a un archivo de texto
archivo = open("Himno.txt", "w")

archivo.write("¡Noble patria!, tu hermosa bandera\n") 
archivo.write("expresión de tu vida nos da;\n") 
archivo.write("bajo el límpido azul de tu cielo\n")
archivo.write("blanca y pura descansa la paz.\n")

archivo.close()

#Cediendo permisos para leer el archivo
#archivo = open("Himno.txt", "r")

#for linea in archivo: 
	#print(linea)
#archivo.close()

#Eliminando los saltos de linea \n
archivo = open("Himno.txt", "r")
for linea in archivo:
	hilera = linea.replace("\n","") 
	print(hilera)
archivo.close()

