class Bank:
    #constructor
    def __init__(self,id,name,surname,bank,key,full_money = 0):
        self.id = id
        self.name = name
        self.surname = surname
        self.bank = bank
        self.key = key
        self.full_money = 0
    
    #metodo mostrar en pantalla
    def print_user(self):
        print("--------------------------")
        print("---DATOS DEL USUARIO---")
        print("nombre : ",self.name)
        print ("su RUT es : ",self.id)
        print("Su banco es:",self.bank)
        print("Su dinero actual es:",self.full_money)
        
    #metodo de deposito
    def deposit(self):
        id = 0
        while(self.id != id): #while en caso de que el rut no sea el mismo 
            id = int(input("ingrese su RUT : ")) 
            if(self.id == id):
                break
            elif(self.id != id):
                print("el RUT ingresado no es valido, intente nuevamente")
        key = ""
        while (self.key != key): #while en caso de que la clave sea incorrecta 
            key = input("Ingrese su clave :")
            if(self.key == key):
                break
            elif(self.key != key):
                print("La clave ingresada es incorrecta, intente nuevamente")
        deposit_amount = 0
        while(deposit_amount <= 0  ): #
            deposit_amount = int(input("Ingrese la cantidad a depositar (Tiene que ser mayor que cero): "))
            if (0 <deposit_amount ):
                print("la cantidad a depostiar es : ",deposit_amount)
                break
        self.full_money = self.full_money + deposit_amount 
