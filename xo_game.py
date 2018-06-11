def crear_matriz(i, j):
	mat = [["-" for jjjj in range (j)] for iiii in range(i)]
	return mat	


def celda_libre(mat, i, j):
		if mat[i][j] == "-":
			return True
		else:
			return  False


def celda_valid(i, j):
	if ((i >=0) and (i<= 3)) and ((j>=0) and (j<=3)):
		return True 
	else: 
		return False


def  desplegar(matriz):
	for i in range (len(matriz)):
		for j in range (len(matriz[i])):
 			print(matriz[i][j],end = "	")
		print()


def asignar_jugada(mat, i, j, jugador):
	if jugador == 1:
		mat[i][j] = "X"
	else:
		mat[i][j] ="O" 
		

def revisa_ganador(mat, jugador):
	if jugador == 1: 
		marca = "X"
	else:
		marca = "O"	
	filas = revisa_filas(mat, marca)
	columnas = revisa_columnas(mat, marca)
	diagonales = revisa_diagonales(mat, marca)
	if filas or columnas or diagonales:
		return True 
	else:
		return False
	return filas or columnas or diagonales


def revisa_filas(mat, marca):
	for i in range(len(mat)):
		if ((mat[i][0] == marca) and (mat[i][1] == marca) and (mat[i][2] == marca)):	
			return True
		else:
			return False

def revisa_columnas(mat, marca):
	for i in range (len(mat)):
		if ((mat[0][i] == marca) and (mat[1][i] == marca) and (mat[2][i] == marca)):
			return True
		else:
			return False


def revisa_diagonales(mat, marca):
	if (mat[0][0] == marca  and mat[1][1] == marca and mat[2][2] == marca):
		return True
	elif (mat[2][0] == marca and mat[1][1] == marca and mat[0][2] == marca):
		return True



def leer_jugada(mat, jugador):
	jugada_invalida = True
	while (jugada_invalida):
		print()
		print("Jugador -> ", jugador)
		pos_i = int(input("Digite fila 0, 1, 2: "))
		pos_j = int(input("Digite columna 0, 1, 2: "))
		if celda_valid(pos_i, pos_j) and celda_libre(mat, pos_i, pos_j):
			jugada_invalida = False
			asignar_jugada(mat, pos_i, pos_j, jugador)
			return revisa_ganador(mat, jugador)
		else:
			print("Celda inválida u ocupada, intente de nuevo")

cantidad_jugadas = 1
matriz = crear_matriz(3,3)
desplegar(matriz)
quien_juega = 1
while cantidad_jugadas <= 9:
	hay_ganador = leer_jugada(matriz, quien_juega)
	desplegar(matriz)
	if hay_ganador:
		print(">>> El jugador", quien_juega, "ganó!!!")
		cantidad_jugadas = 10
	else:
		cantidad_jugadas += 1
		if quien_juega == 1:
			quien_juega = 2
		else:
			quien_juega = 1
