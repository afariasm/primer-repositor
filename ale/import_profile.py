from Claseprofile import Profile
import random 
from datetime import date
def main():
    #pedir a usuario
    nickname = input("Ingrese su nombre de usuario: ")
    numeros = [0,1,2,3,4,5,6,7,8,9]
    id = random.sample (numeros,4)
    created_at = date.today()
    mail = input("Ingrese su mail: ")
    avatar = input("ingrese su foto formato (.PNG) : ")
   
    is_premium = input ("Quiere ser parte de discord nitro? (SI) o (NO)  ")
    status = input("Usted quiere que su estado sea (DESCONECTADO-CONECTADO-AUSENTE)")
    print("------------------------------------------------------------------------")
    #ingresar datos a la clase
    profile = Profile(nickname,id,mail,avatar,created_at,is_premium,status)

    #llamar al metodo para mostrar en pantalla 
    profile.print()

main()
