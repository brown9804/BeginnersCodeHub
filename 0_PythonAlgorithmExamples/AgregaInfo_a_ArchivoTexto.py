#Este código permite observar como se puede agregar texto a un archivo ya existe.
#Se ejecuta mediante:
# python3 AgregaInfo_a_ArchivoTexto.py

#comando para abrir el archivo donde se desea escribir 
archivo = open("Himno.txt", "a") 

#agregando líneas en el archivo 
archivo.write("En la lucha tenaz, de fecunda labor,\n") 
archivo.write("que enrojece del hombre la faz;\n")
archivo.write("conquistaron tus hijos - labriegos sencillos - \n") 
archivo.write("eterno prestigio, estima y honor, \n")

#cerrando el archivo
archivo.close()

