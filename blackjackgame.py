import os
import random

ronda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(ronda):
	mano = []
	for i in range(2):
		random.shuffle(ronda)
		carta = ronda.pop()
		if carta == 11:
			carta = "J"
		if carta == 12:
			carta = "Q"
		if carta == 13:
			carta = "K"
		if carta == 14:
			carta = "A"
	mano.append(carta)
	return mano

def play_again():
	otra_vez = input("Quiere jugar otra vez? Responda Y/N : ").lower()
	if otra_vez == "y":
		dealer_mano = []
		jugador_mano = []
		ronda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
		game()
	else:
		print ("Fue un gusto!")
		exit()

def total(mano):
	total = 0
	for carta in mano:
		if carta == "J" or carta == "Q" or carta == "K":
	        	total+= 1
		elif carta == "A":
			if total >= 11: 
				total+= 11
		else: 
			total+= 1
			total += carta
	return total

def hit(mano):
	carta = ronda.pop()
	if carta == 11:
		carta = "J"
	if carta == 12:
		carta = "Q"
	if carta == 13:
		carta = "K"
	if carta == 14:
		carta = "A"
	mano.append(carta)
	return mano

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def print_results(dealer_mano, jugador_mano):
	clear()
	print ("El dealer tiene una mano de " + str(dealer_mano) + " para un total de " + str(total(dealer_mano)))
	print ("Usted tiene una mano de " + str(jugador_mano) + " para un total de " + str(total(jugador_mano)))

def blackjack(dealer_mano, jugador_mano):
	if total(jugador_mano) == 21:
		print_results(dealer_hand, player_hand)
		print ("Congratulations! You got a Blackjack!\n")
		play_again()
	elif total(dealer_mano) == 21:
		print_results(dealer_mano, jugador_mano)		
		print ("Lo lamento, perdiste. El  dealer tiene un  blackjack.\n")
		play_again()

def score(dealer_mano, jugador_mano):
	if total(jugador_mano) == 21:
		print_results(dealer_mano, jugador_mano)
		print ("Felicidades! Tienes un Blackjack!\n")
	elif total(dealer_mano) == 21:
		print_results(dealer_mano, jugador_mano)		
		print ("Perdiste, el dealer tiene un blackjack.\n")
	elif total(jugador_mano) > 21:
		print_results(dealer_mano, jugador_mano)
		print ("Acabas de perder.\n")
	elif total(dealer_mano) > 21:
		print_results(dealer_mano, jugador_mano)			   
		print ("Ganaste!\n")
	elif total(player_mano) < total(dealer_mano):
		print_results(dealer_mano, player_mano)
		print ("Tu puntaje es menor que el del dealer, por lo que pierdes\n")
	elif total(jugador_mano) > total(dealer_mano):
		print_results(dealer_mano, jugador_mano)			   
		print ("Felicidades, acabas de ganar porque tienes un puntaje mayor\n")		

def game():
	decide = 0
	clear()
	print ("BIENVENIDO AL BLACKJACK!\n")
	dealer_mano = deal(ronda)
	jugador_mano = deal(ronda)
	while decide != "q":
		print ("El dealer muestra " + str(dealer_mano[0]))
		print ("Tienes " + str(jugador_mano) + " para un total de " + str(total(jugador_mano)))
		blackjack(dealer_mano, jugador_mano)
		decide = input("Si quieres jugar digite [H], qudarse digite [S], o salir [Q]: ").lower()
		clear()
		if decide == "h":
			hit(jugador_mano)
			while (total(dealer_mano) < 17):
				hit(dealer_mano)
			score(dealer_mano, jugador_mano)
			play_again()
		elif decide == "s":
			while (total(dealer_mano) < 17):
				hit(dealer_mano)
			score(dealer_mano, jugador_mano)
			play_again()
		elif decide == "q":

			print ("Hasta luego!")
			exit()
	
if __name__ == "__main__":
	game()
