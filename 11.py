def impr (anch):
	print("*" * anch)
ancho = int(input("Digite el ancho para el de asteriscos "))
for indice in range (1, ancho + 1):
	impr(ancho)


def anchofig(anc,sym):
	print (sym*anc)
ancho = int(input("Digite el ancho que desea para la figura "))
alto = int(input("Digite el alto que desea para la figura "))
symbol = input("Digite el símbolo con el que desea contruir la figura ")
for indice in range (1, alto+1):
	anchofig(ancho,symbol)
