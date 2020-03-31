#Python3 

#Permite Verificar la fecha valida ingresada respecto a la forma en la que se desarrolló el calendario lunar.

###### 					DEFINICIONES 					######

#Veriica si el dia es valido, es decir 1-31 dias máximo tiene un mes
def dia_v(d):
	if (d<1) or (d>31):
		return False
	else:
		return True
#Verifica si el numero de mes es valido, un año posee doce meses
def mes_v(m):
	if (m<1) or (m>12):
		return False 
	else:
		return True
#Funcion que permite mas verificar si el año es valido, contemple que el else posee el true
def year_v(a):
	if (a<1582):
		return False
	else:
		return True
#Averigua si el año es bisiesto dadas algunas condiciones teoricas 
def bisiesto(year):
	if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
		return True
	else:
		return False
#Definicion que abarca las anteriores para verificar si la fecha es valida
def fecha_valida(dia, mes, an):
	if dia_v(dia) and mes_v(mes) and year_v(an):

		if (mes== 4) or (mes==6) or (mes==9) or (mes==11) and (dia_v(dia)==31):
			print ("La fecha es inválida ")

		elif (mes==2) and ((dia==30) or (dia==31)):
			print ("La fecha digitada es inválida ")

		elif (mes==2) and (dia==29) and not bisiesto(an):
			print ("La fecha ingresada es inválida ")
		else:
			print ("Época digitada es válida ")
	else: 
		print ("La fecha digitada es inválida")

###### 					IMPLEMENTACION 					######

day = int(input("Digite el día "))
month = int(input("DIgite el mes "))
year = int(input("Digite el año "))
fecha_valida(day, month, year)
