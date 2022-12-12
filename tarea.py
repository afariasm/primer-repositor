#fuerza,magia,curacion
#iq,vida,ataque,defensa
#todos parten con 100 de vida
#20 % mas por eleccion de clase magias= iq curacion = defensa ataque = fuerza 
#biblioteca rand() de py para #2, dependiendo de la clase tuiene q ser +50 + el 20% 
#ara ejecutar el codigo tiene que crearse 2 pj y pelearse

class Pesonaje():
    def __init__(self,nick,typee,life = 100):
        self._nick = nick
        self._typee = typee
        self._life = 100

    def typee_pj(self):
      
otro archivo
def main():
    #pedir a usuario
    print("\tBienvenido")
    nick = input("Ingrese el apodo de su personaje")
    opcion = 1
    while (0 < opcion < 4 ):
        print("\t Seleccione su clase principal")
        print("1.-Fuerza")
        print("2.-Magia")
        print("3.-Curacion")
        opcion = ("Ingrese la opcion que eligio")
        if (opcion == 1):
            typee = "Fuerza"
            break
        elif (opcion == 2):
            typee = "Magia"
            break
        elif (opcion == 3):
            typee = "Curacion"
            break
        else:
            ("ingrese una opcion valida")
