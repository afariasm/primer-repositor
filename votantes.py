class Candidate:
    candidate = ""
    political_party = ""
    votes = 0

    #constructor 
    def __init__(self,candidate,political_party):
        self.candidate = candidate
        self.political_party = political_party
        
    #metodos
    def add_vote(self):
        self.votes =self.votes+1
        
#vriables
candidate_1 = ""
candidate_2 = ""
political_party_1 = ""
political_party_2 = ""
votes = 0
candidate = 0
option = 0
#pedir a user
candidate_1 = input("Ingrese el nombre del candidato numero 1 :")
candidate_2= input("Ingrese el nombre del candidato numero 2 :")
political_party_1 =  input("Ingrese el partido politico del candidato 1 :")
political_party_2 =  input("Ingrese el partido politico del candidato 2 :")

#menu
while ( option != 3):
    print("1.-",candidate_1)
    print("2.-",candidate_2)
    print("3.- Finalizar conteo")
    option = int(input("Ingrese la opcion elejida"))

    if (option == 1 ):
        candidate = Candidate(votes,candidate_1)
        candidate.add_vote
    elif (option ==2 ):
        candidate = Candidate(votes,candidate_2)
        candidate.add_vote
