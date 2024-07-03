#Python3

#Algoritmo que permite modelar el comporamiento de la máquina de Atwood.

print ("Bienvenido a la máquina de Atwood, consiste en dos masas m1 y m2, conectadas por una cuerda inelástica de masa despreciable con una polea ideal de masa despreciable")
#Masa 1, contiene masa del objeto meas pesado
m1 = input("Digite la masa del objeto 1 en kilogramos, considere que este objeto es el más pesado: ") 
#Masa 2, va a contener el valor de la masa del objeto menos pasado
m2 = input ("Digite la masa objeto 2 en kilogramos: ")
#constante de gravedad
g = 9.81
#fórmula para calcular la aceleración
aceleraci = (g * (float(m1) - float(m2)) / (float(m1) + float(m2))) 
#recordatorio del valor de la gravedad
print ("Recuerde que la gravedad es 9.81 m/s2")
#resultado de la aceleración
print ("Considerando los datos anteriores, la aceleración es equivalente a: " + str(aceleraci) + "m/s2")
#fórmula de la tensión (Fuerza)
tension =  (g * 2*(float(m1) * float(m2)) / (float(m1) + float(m2)))
#imprime el resultado de la tensión en N
print ("La tensión de la cuerda en Newtons es: " +  str(tension) + "metros * kg / seg2") 
#se multiplicó por 0.001 para pasar los kg a gramos y por 0.01 la gravedad debido a los cm
tensiondi = (g*0.01 * 2*(float(m1) * float(m2))*0.001 / (float(m1) + float(m2))*0.001) 
#resultado lo da en dinas
print("La tensión en dinas es: " + str(tensiondi) + "cm * gr /seg2") 


