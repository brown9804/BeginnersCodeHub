print (" Este programa sirve para verificar si es una terna pitagórica")
c1 = input ("Ingrese el valor de un valor ")
c2 = input ("Por favor, digite el segundo dato: ")
h = input("Digite e tercer dato: ")
if (int(h)**2 == int(c1)**2 + int(c2)**2): #compara primeros dos datos con el tercero
	print ("Los números " + c1, c2, h +" sí son una terna") #imprime solo si sí se cumple
elif  (int(c1)**2 == int(h)**2 +  int(c2)**2): # compara primer dato con los otros dos 
	print ("Sí es una terna " + c1, c2, h) #si se cumple la comparación entonces lo imprime
elif (int(c2)**2 == int(h)**2 + int(c1)**2): # compara segundo dato con el primero y el tercero
	print ("Estos números: " + c1, c2, h + " generan una terna")
else: #sino se cumple ninguna de las compraciones anteriores
	print ("Lamentablemente no son una terna")

