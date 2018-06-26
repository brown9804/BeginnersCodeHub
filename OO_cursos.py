class Curso():
    def __init__(self, nombre, año, semestre):
        self.nombre = nombre
        self.año = año
        self.semestre = semestre
        self.alumnos = []
        self.mejores = []
        self.ampliacion = []
        self.perdieron = []

    def __str__(self):
        return ("Curso: " + self.nombre)

    def imprimir_notas_curso(self):
        print("Notas del curso", self.nombre)
        self.imprimir_notas(self.alumnos)

    def imprimir_notas(self, lista):
        if lista == []:
            print(" ___ ")
        else:
            print("Carnet    Nota")
            for j in lista:
                print(j[0], "   ", j[1])

    def promedio_notas(self):
        contador = 0
        for j in self.alumnos:
            contador = contador + j[1]
        return contador / len(self.alumnos)

    def imprimir_promedio(self):
        print ("El promedio es: ", self.promedio_notas())

    def agregar_alumno(self, carnet, nota):
        self.alumnos.append([carnet, nota])

    def calcula_mejores_promedios(self):
        self.mejores = []
        mejor_nota = 0
        for k in self.alumnos:
            if k[1] > mejor_nota:
                mejor_nota = k[1]
        for l in self.alumnos:
            if l[1] == mejor_nota:
                self.mejores.append(l)
                
    def imprimir_mejores_promedios(self):
        print("Mejores promedios:")
        self.imprimir_notas(self.mejores)

    def calcula_ampliacion(self):  
        self.ampliacion = []
        for n in self.alumnos:
            if n[1] >= 60 and n[1] < 70:
                self.ampliacion.append(n)
                
    def imprimir_ampliacion(self):
        print("Van a ampliación:")
        self.imprimir_notas(self.ampliacion)
        
    def calcula_perdieron_curso(self):  
        self.perdieron = []
        for d in self.alumnos:
            if d[1] < 60:
                self.perdieron.append(d)

    def imprimir_perdieron(self):
        print("Perdieron el curso:")
        self.imprimir_notas(self.perdieron)
        


####Debido a la manera en la que se programó pegue los giguientes datos en un documento con extensión ".txt" sin el "#" ya que es para comentar.
#CI0202, B601234, 85
#CI0202, B607777, 50
#CI0101, B602222, 90
#CI0101, B602345, 80
#CI0202, B502340, 95
#CI0101, B502346, 80
#CI0202, B622222, 60
#CI0202, B566222, 60
#CI0101, B555555, 65
#CI0202, B677222, 75
#CI0202, B602332, 95
#CI0202, B604432, 85
#CI0202, B604433, 85
#CI0202, B684432, 99
#CI0101, B666555, 85

CI0202 = Curso("Principos de Informática", 2018, 1)
CI0101 = Curso("Introduccion a Microcomputadores", 2018, 1)
    
archivo = open("notas2cursos.txt", "r")
for línea in archivo:
    curso, carnet, nota = línea.split(",")
    if curso == "CI0202":
        CI0202.agregar_alumno(carnet, int(nota))
    elif curso == "CI0101":
        CI0101.agregar_alumno(carnet, int(nota))
archivo.close()

CI0101.imprimir_notas_curso()
CI0101.imprimir_promedio()
CI0101.calcula_mejores_promedios()
CI0101.imprimir_mejores_promedios()
CI0101.calcula_ampliacion()
CI0101.imprimir_ampliacion()
CI0101.calcula_perdieron_curso()
CI0101.imprimir_perdieron()
print()
CI0202.imprimir_notas_curso()
CI0202.imprimir_promedio()
CI0202.calcula_mejores_promedios()
CI0202.imprimir_mejores_promedios()
CI0202.calcula_ampliacion()
CI0202.imprimir_ampliacion()
CI0202.calcula_perdieron_curso()
CI0202.imprimir_perdieron()
print()
