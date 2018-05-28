print ("Bienvenido a la máquina de Atwood, consiste en dos masas m1 y m2, conectadas por una cuerda inelástica de masa despreciable con una polea ideal de masa despreciable")
m1 = input("Digite la masa del objeto 1 en kilogramos, considere que este objeto es el más pesado: ") #contiene masa del objeto meas pesado
m2 = input ("Digite la masa objeto 2 en kilogramos: ") #va a contener el valor de la masa del objeto menos pasado
g = 9.81 #constante de gravedad
aceleraci = (g * (float(m1) - float(m2)) / (float(m1) + float(m2))) #fórmula para calcular la aceleración
print ("Recuerde que la gravedad es 9.81 m/s2") #recordatorio del valor de la gravedad
print ("Considerando los datos anteriores, la aceleración es equivalente a: " + str(aceleraci) + "m/s2") #resultado de la aceleración
tension =  (g * 2*(float(m1) * float(m2)) / (float(m1) + float(m2))) #fórmula de la tensión
print ("La tensión de la cuerda en Newtons es: " +  str(tension) + "metros * kg / seg2") #imprime el resultado de la tensión en N
tensiondi = (g*0.01 * 2*(float(m1) * float(m2))*0.001 / (float(m1) + float(m2))*0.001) #se multiplicó por 0.001 para pasar los kg a gramos y por 0.01 la gravedad debido a los cm
print("La tensión en dinas es: " + str(tensiondi) + "cm * gr /seg2") #resultado lo da en dinas


