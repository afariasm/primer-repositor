class Bank:
    #constructor
    def __init__(self,id,name,surname,bank,key,full_money = 0):
        self._id = id
        self._name = name
        self._surname = surname
        self._bank = bank
        self._key = key
        self._full_money = 0
    
    #metodo mostrar en pantalla
    def print_user(self):
        print("--------------------------")
        print("---DATOS DEL USUARIO---")
        print("nombre : ",self._name)
        print ("su RUT es : ",self._id)
        print("Su banco es:",self._bank)
        print("Su dinero actual es:",self._full_money)
        
    #metodo de deposito
    def deposit(self):
        id = 0
        while(self._id != id): #while en caso de que el rut no sea el mismo 
            id = int(input("ingrese su RUT : ")) 
            if(self._id == id):
                break
            elif(self._id != id):
                print("el RUT ingresado no es valido, intente nuevamente")
        key = ""
        while (self._key != key): #while en caso de que la clave sea incorrecta 
            key = input("Ingrese su clave :")
            if(self._key == key):
                break
            elif(self._key != key):
                print("La clave ingresada es incorrecta, intente nuevamente")
        deposit_amount = 0
        while(deposit_amount <= 0  ): #
            deposit_amount = int(input("Ingrese la cantidad a depositar (Tiene que ser mayor que cero): "))
            if (0 <deposit_amount ):
                print("la cantidad a depostiar es : ",deposit_amount)
                break
        self._full_money = self._full_money + deposit_amount 
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_bank(self):
        return self._bank

    def get_key(self):
        return self._key

    def get_full_money(self):
        return self._full_money

    
    
