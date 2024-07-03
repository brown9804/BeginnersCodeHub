#Se crea un gato 3x3 es decir de 3 filas con 3 columnas. Se realiza mediante definiciones sucesivo a su implementación.

#Se ejcuta mediante el comando python3 JuegoGato_XO.py


#Se crea una una matriz nxn 
#abajo se define como 3x3 
def crear_matriz(i, j):
	mat = [["-" for jjjj in range (j)] for iiii in range(i)]
	return mat	


#Para verificar si la celda está ocupada o se encuentra vacía 
def celda_libre(mat, i, j):
		if mat[i][j] == "-":
			return True
		else:
			return  False


#Si la celda es válida es cuando se encuentra entre el rango de filas y columnas asignadas, esta definición
#se encarga de revisar eso
def celda_valid(i, j):
	if ((i >=0) and (i<= 3)) and ((j>=0) and (j<=3)):
		return True 
	else: 
		return False

#muestra en pantalla la matriz que se posee en el momento, es decir se puede ver como están marcadas las casillas 
def  desplegar(matriz):
	for i in range (len(matriz)):
		for j in range (len(matriz[i])):
 			print(matriz[i][j],end = "	")
		print()

#Para asignarle al primer jugador en ingresar la X, en síntensis funciona 
#para asignarle una figura ya sea X o O a los jugadores
def asignar_jugada(mat, i, j, jugador):
	if jugador == 1:
		mat[i][j] = "X"
	else:
		mat[i][j] ="O" 

		
#Revisa si existe una fila en la cual todas sus casillas contienen la misma figura
def revisa_filas(mat, marca):
	for i in range(len(mat)):
		if ((mat[i][0] == marca) and (mat[i][1] == marca) and (mat[i][2] == marca)):	
			return True
		else:
			return False
		
#Revisa si existe una columna en la cual todas sus casillas contienen la misma figura
def revisa_columnas(mat, marca):
	for i in range (len(mat)):
		if ((mat[0][i] == marca) and (mat[1][i] == marca) and (mat[2][i] == marca)):
			return True
		else:
			return False

#Revisa si existe una diagonal en la cual todas sus casillas contienen la misma figura
def revisa_diagonales(mat, marca):
	if (mat[0][0] == marca  and mat[1][1] == marca and mat[2][2] == marca):
		return True
	elif (mat[2][0] == marca and mat[1][1] == marca and mat[0][2] == marca):
		return True

							
#Funciona para revisar si existe una fila, columna o bien por medio de diagonal llena de una sola figura, 
# es decir, revisa si las reglas paras ganar se cumplen pero lo hace por medio de la implementación de las definiciones anteriores.
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


#Esto para digirir la posición de la figura a ingresar
def leer_jugada(mat, jugador):
	jugada_invalida = True
	while (jugada_invalida):
		print()
		print("Jugador -> ", jugador)
		pos_i = int(input("Digite la fila donde desea marcar con su figura, tenemos las filas 0, 1, 2. Usted ha digitado:	 "))
		pos_j = int(input("Digite columna donde desea marcar con su figura, tenemos las columnas 0, 1, 2. Ha ingresado: 	"))
		if celda_valid(pos_i, pos_j) and celda_libre(mat, pos_i, pos_j):
			jugada_invalida = False
			asignar_jugada(mat, pos_i, pos_j, jugador)
			return revisa_ganador(mat, jugador)
		else:
			print("Celda inválida u ocupada, intente de nuevo")

			
##### Inicio del programa	
#Se define que cada jugar tiene una jugada por turno
cantidad_jugadas = 1
# Se establece que la matriz va a ser 3x3
matriz = crear_matriz(3,3)
#Se muestra el "tablero" creado
desplegar(matriz)
#Se inicia el juego con el primer jugador ingresado a la partida
quien_juega = 1
#Ciclo dado que tenemos 3 casillas necesarias y por persona es un turno 
#Considerando que las casillas en total son 9 donde 3*3 =9 se crea un ciclo para el cual 
#realiza lo solicitado hasta que ya no hayan más jugadas. Del mismo modo, toma en cuenta que si el jugador gana 
#antes de las 9 jugadas mínimas entonces se le asigan el valor de 10 para que el ciclo termine.
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
