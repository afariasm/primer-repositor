class Fraction():
    #atributos
    numerator = 0
    denominator = 1
     
    #constructor
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        
     #metodos  
    def addition(self,other): #operacion de suma
        if (other.denominator == self.denominator):
            numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator ) 
            denominator = self.denominator
            print ("El resultado de la suma es  = ",numerator ,"/",denominator)   
        else:
            numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator )  
            denominator = (self.denominator * other.denominator)
            print ("El resultado de la suma es  = ",numerator ,"/",denominator)         
    def subtraction(self,other): #operacion de resta
        if(self.denominator == other.denominator):
            numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator ) 
            denominator = self.denominator
            print("el resultado de la resta es = ", numerator,"/",denominator)
        else:
            numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator )  
            denominator = (self.denominator * other.denominator)         
            print ("El resultado de la resta es  = ",numerator ,"/",denominator)
            
    def multiplication(self,other): #operacion de multiplicación
        numerator = (self.numerator * other.numerator)
        denominator = (self.denominator * other.denominator)
        print ("El resultado de la multiplicacion es  = ",numerator ,"/",denominator)
    def division(self,other): #operacion de división
        numerator = (self.numerator * other.denominator)
        denominator = (self.denominator * other.numerator)
        print ("El resultado de la division es  = ",numerator ,"/",denominator)         
#inicialización variables 
numerator_a = 0
denominator_a = 1
numerator_b = 0
denominator_b = 1 
fraction1 = 0
fraction2 = 0

#pedir a usuario la primera fraccion
numerator_a = int(input("Ingrese el numerador de la fraccion A :"))
denominator_a = int(input("Ingrese el denominador de la fraccion A :"))
#mostrar a usuario la fraccion A
print(numerator_a ,"/", denominator_a)
#pedir a usuario la segunda fraccion
numerator_b = int(input("Ingrese el numerador de la fraccion B :"))
denominator_b = int(input("Ingrese el denominador de la fraccion B :"))
#mostrar a usuario la fraccion B
print(numerator_b ,"/", denominator_b)

#agrupar los valores en una sola variable
fraction1 = Fraction(numerator_a, denominator_a)
fraction2 = Fraction(numerator_b, denominator_b)

#pedir al usario la  operacion a realizar
operation = input ("ingrese la operacion que quiere realizar, puede ser: Suma (+), resta (-), multiplicación (x) o division (:) = ")
#Menu de operaciones
if (operation == "+"):
    fraction1.addition(fraction2)    
elif (operation == "-"):
    fraction1.subtraction(fraction2)
elif (operation == "x"):
    fraction1.multiplication(fraction2)     
elif (operation == ":"):
    fraction1.division(fraction2)
else:
    print ("La operacion ingresada no es valida, intente denuevo con : Suma (+), resta (-), multiplicación (x) o division (:) ")
