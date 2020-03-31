#Python3 

#Manipula datos de una base de un curso por medio de definiciones. Obtiene los valores de un archivo de texto.

######					DEFINICIONES 					######
def leer_notas(nombre_archi):
	notas = [ ]
	archivo = open(nombre_archi, "r")
	for linea in archivo:
		carnet, nota = linea.split(",")
		notas.append([carnet, int(nota)])
	archivo.close()
	return notas

def imprimir_notas(mat):
	if mat == [ ]:
		print("- ")
	else:
		for indi in mat:
			print(indi[0], indi[1])

def promedio_notas(mat):
	n = len(mat)
	sumatoria = 0
	for indice in range (0, n):
		sumatoria = sumatoria + mat[indice][1]
	promedio = sumatoria/n
	return promedio

def mejores_promedios(mat):
	mejor_nota = 0
	for i in range (len(mat)):
		nota_max = mat[i][1]
		if  (int(nota_max) >= mejor_nota):
			mejor_nota = nota_max
	honor = [ ]
	for indice in mat:
		if mejor_nota == indice[1]:
			honor.append(indice)
	return honor
	
def a_ampliacion(mat):
	ampli = [ ]
	for i in mat:
		nota = (int(i[1]))
		if ((nota>=60) and (nota<=70)):
			ampli.append(i)
	return ampli



def repetir_curso(mat):
	repe = [ ]
	for i in mat:
		nota = (int(i[1]))
		if nota<60:
			repe.append(i)
	return repe


######					CREANDO ARCHIVO DE TEXTO 					######

archivo = open("Notas.txt", "w")

archivo.write("B607777, 50\n") 
archivo.write("B602222, 95\n") 
archivo.write("B602345, 80\n")
archivo.write("B502340, 95\n")
archivo.write("B502345, 80\n")
archivo.write("B622222, 60\n")
archivo.write("B555555, 65\n")
archivo.write("B601234, 85\n") 

archivo.close()

######					IMPLEMENTACION 					######


mat = leer_notas("Notas.txt")
print("Carnet	Nota")
imprimir_notas(mat)
print()

promedio = promedio_notas(mat)
print ("Promedio: ", promedio)

print()
print ("Los mejores promedios: ")
honor = mejores_promedios(mat)
imprimir_notas(honor)

print()
print ("Van a ampliación: ")
ampliacion = a_ampliacion(mat)
imprimir_notas(ampliacion)
 
print()
print ("Perdieron el curso: ")
repite = repetir_curso(mat)
imprimir_notas(repite)
