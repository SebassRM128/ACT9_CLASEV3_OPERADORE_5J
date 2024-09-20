print("Act 9 clases v2")
print("Sebastian Rojas Mat: 22308051281303")
# zona de class

class Operadores1303:
    #Zona de funciones
    def suma1303(self,S,R):
        s1303=S+R           
        print(f"La suma de {S} + {R} = {s1303}")
    def resta1303(self,S,R):
        r1303=S-R            
        print(f"La resta de {S} - {R} = {r1303}")
    def mult1303(self,S,R):
        m1303=S*R            
        print(f"La multiplicacion de {S} * {R} = {m1303}")
    def div1303(self,S,R):
        s1303=S/R            
        print(f"La division de {S} / {R} = {s1303}")
    def mod1303(self,S,R):
        s1303=S%R            
        print(f"La modulo de {S} % {R} = {s1303}")
    def exp1303(self,S,R):
        s1303=S**R            
        print(f"La exponente de {S} ** {R} = {s1303}")
    def coc1303(self,S,R):
        s1303=S//R            
        print(f"La cociente de {S} // {R} = {s1303}")
    


# Zona de creacion del objeto
operasebas=Operadores1303()

#Zona de uso de objetos
print(" Funcion suma")
operasebas.suma1303(5,5)
print(" Funcion resta")
operasebas.resta1303(5,5)
print(" Funcion mult")
operasebas.mult1303(5,5)
print(" Funcion divison")
operasebas.div1303(5,5)
print(" Funcion modulo")
operasebas.mod1303(5,5)
print(" Funcion exponente")
operasebas.exp1303(5,5)
print(" Funcion cociente")
operasebas.coc1303(5,5)
