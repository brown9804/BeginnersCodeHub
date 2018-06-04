#Writting first part
archivo = open("Himno.txt", "w")

archivo.write("¡Noble patria!, tu hermosa bandera\n") 
archivo.write("expresión de tu vida nos da;\n") 
archivo.write("bajo el límpido azul de tu cielo\n")
archivo.write("blanca y pura descansa la paz.\n")

archivo.close()

#Giving permission for reading
#archivo = open("Himno.txt", "r")

#for linea in archivo: 
	#print(linea)
#archivo.close()

#deleting \n
archivo = open("Himno.txt", "r")
for linea in archivo:
	hilera = linea.replace("\n","") 
	print(hilera)
archivo.close()

