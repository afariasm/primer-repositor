class Person():
    #constructor
    def __init__(self,name,last_name,birthday,sex):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.birthday = birthday
        self.sex = sex
    #mostrar info de la persona
    def print_info(self):
        print ("Su(s) nombre(s) es(son) : ",self.name)
        print ("Su(s) apaellido(s) es(son) : ",self.last_name)
        print ("Su fecha de nacimiento es : ",self.birthday)
        print ("Su sexo es ",self.sex)
        
        
SEGUNDO ARCHIVO

from ClassPerson import Person

class SuperHero(Person):
    def __init__(self,name,last_name,birthday,nick,power):
        super.__init__(name,last_name,birthday)
        self.nick = nick
        self.power = power

    def print_superhero (self):
        print ("Su(s) nombre(s) es(son) : ",self.name)
        print ("Su(s) apaellido(s) es(son) : ",self.las_name)
        print ("Su fecha de nacimiento es : ",self.birtday)
        print ("Su sexo es ",self.sex)
        print ("Su nombre de super heroe",self.nick)
        print ("Su suoper poder es : ".self.power)
    
main()

from ClassPerson import SuperHero
from ClassPerson import Person

def main():
    #pedir a usuario 
name = input("Ingrese su(s) nombre(s) : ")
last_name = input("Ingrese su(s) apellido(s) : ")
birthday = input("Ingrese su fecha de nacimiento : ")
#Menu opciones de genero
opcion = 1
while (0 < opcion < 4 ):
    print("\t Seleccione su sexo")
    print("1.-Masculino")
    print("2.-Femenino")
    print("3.-Sin especificar")
    opcion = ("Ingrese la opcion que eligio")
    if (opcion == 1):
        sex = "masculino"
        break
    elif (opcion == 2):
        sex = "femenino"
        break
    elif (opcion == 3):
        sex = "Sin especificar"
        break
    else:
        ("ingrese una opcion valida")

superhero = input("¿ Es un super-heroe ? ingrese (1) para SI y (2) para NO") 
while (0 < superhero < 3):
