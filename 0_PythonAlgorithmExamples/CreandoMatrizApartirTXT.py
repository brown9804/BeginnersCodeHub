#Se requiere utilizar pyhton3

#importando paquetes
import numpy as np
import sys

#Dado que las instrucciones solicitan imprimir la matriz en la linea de comandos utilizando el archivo facilitado.
#se considera que no se conoce el numero de filas o columnas

#Se requiere leer un archivo

def leerArchivo(nombreArchivo, columnas, filas):
    arreglo = []
    try:
        archivo = open(nombreArchivo,"r")
        for linea in archivo:
            linea_nueva =linea.split(",")
            for i in range(len(filas)):
                for j in range(len(columnas)):
                    arreglo.append(linea_nueva)
                    #print(arreglo[int(filas)][int(columnas)], end = " ")
        archivo.close()

    except(FileNotFoundError):
        print("Archivo No encontrado")
    except(ValueError):
        print("Error en los tipos-valores de datos")
    return arreglo



#Dado que el archivo ya existe lo unico que se necesita es imprimir la matriz
#para lo cual se debe crear una funcion

arhivoAExtraer = input("Digite el nombre del archivo a leer junto con su extensión siendo esta (.txt)\n")
filas = input("Digite la cantidad de elementos por oración en el archivo (.txt)\n")
columnas = input("Digite el numero de oraciones que posee el (.txt)\n")

matriz = leerArchivo(arhivoAExtraer,columnas,filas)
print("Matriz solicitada orden NxM")
matriz_con_corchetas = np.matrix(matriz)
matriz_sin_corchetas = str(matriz_con_corchetas)[1:-1]
print (matriz_sin_corchetas)
print()
