class Student:
    #atributos
    id = 0
    run = 0
    dv = ""
    alternative_identification = 0
    names = ""
    first_name= ""
    last_name = ""    
    #constructor 
    def __init__(self,id,run,dv,alternative_identifcation,names,first_name,last_name):
        self.id=id
        self.run=run 
        self.dv=dv
        self.alternative_identification = alternative_identification
        self.names = names 
        self.first_name = first_name
        self.last_name = last_name




#inicializar variables
run = 0
dv = ""
alternative_identification = 0
names = ""
first_name= ""
last_name = ""
response = ""
#pedir a usuario
response = input("¿Usted pose rut ?  si si posee ponga (si) si no pose ponga (no) =")
if (response == "si"):
    run = int(input("ingrese su rut sin puntos y sin guion: "))
    dv = input("ingrese su digito identificador: ")
    print ("Su rut es :",run,"-",dv)
elif (response == "no"):
    alternative_identification = int(input("ingrese su identificacion alternativa: "))
    print("su identificador es: ",alternative_identification)
else:
    print("La opcion ingresada no es valida")
    exit()  
names = input("Ingrese sus dos nombres: ")
first_name = input("Ingrese su primer apellido: ")
last_name = input ("ingrese su segundo apellido: ")
print("Su nombre es : ",names,first_name,last_name)
