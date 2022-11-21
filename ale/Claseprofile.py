class Profile:
    #Constructor
    def __init__ (self,nickname,id,mail,avatar,created_at,is_premium = False,status = "online"): 
        self.nickname = nickname
        self.id = id
        self.avatar = avatar
        self.created_at = created_at
        self.mail = mail
        self.status = status 
        self.is_premium = is_premium

    #mostrar en pantalla
    def print(self):
        print("Su nick name es : ",self.nickname,"#",self.id)
        print("Su mail es : ",self.mail) 
        print("su avatar es : ",self.avatar) 
        print("su fecha de creacion es :",self.created_at)
        print("Usted ",self.is_premium," es premium")
        print("Usted esta",self.status)
    
