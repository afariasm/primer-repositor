from Classbanco import Bank

def main():
    #pedir al usuario
    print("Bienvenido al registro de su cuenta: ")
    id = int(input("Ingrese su rut completo sin punto y sin guión (si su digito identificador es (K) remplácelo por un cero ): "))
    name = input("Ingrese su(s) nombre(s) completo(s): ")
    surname = input("Ingrese su(s) apellido(s): ")
    
    #seleccionbanco
    print("-------------------------------------------------------")
    print ("Seleccione el tipo de banco que quiere pertenecer : ")
    print("1.-Match")
    print("2.-Banco Estado")
    print("3.-Tenpo")
    bank = 0
    while ((bank < 1) or (3 < bank) ):
        bank = int(input("ingrese la opción que usted quiere : "))
        if (bank == 1):
            bank = "Match"
            break
        elif(bank == 2):
            bank = "Banco Estado"
            break
        elif(bank == 3):
            bank = "Tenpo"
            break
        else:
            print("La opción ingresada no es valida, intente denuevo.")
    #pedir clave ausuario
    key = ""
    key = input("ingrese la clave que quiere tener para su cuenta :")
    full_money = 0
    
    #ingresar los datos a la class
    user = Bank(id,name,surname,bank,key,full_money)
    
    #llamar al metodo para mostrar los datos en pantalla
    user.print_user()
    
    #realizar deposito 
    print("¿Quiere realizar un depósito a su cuenta ?")
    print("1.-Si")
    print("2.-No")
    opcion = 0
    while ((opcion != 1) and (opcion != 2)):
        opcion = int(input("ingrese la opcion a realizar: "))
        if(opcion == 1):
            user.deposit()
            break
        elif(opcion == 2):
            print("Perfecto, Bienvenido")
            break
        else:
            print("la opción ingresada no es valida")

    #llamar al metodo para mostrar los datos en pantalla
    user.print_user()
if(__name__) == "__main__":
    main()
