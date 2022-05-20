#La class Mouv permet de donner des mouv    au pokèmon#



class Mouv:
    def __init__(self,name,Type,Class,Precision,PP,Puissance=None,Effect=None,description=None,target=None):
        self.PP = PP                #Nombre de fois que l'on peut utiliser cette attaque
        self.Name = name            #nom de l'attaque 
        self.Type= Type             #Type de l'attaque unique
        self.Puissance =  Puissance #Puissance de l'attaque
        if Class==0:
            self.Class = "Physique"  #Physique = 0 ou Special = 1 et autre = 2
        elif Class==1:
            self.Class = "Special"
        else:
            self.Class = "Autre"
        self.Precision = Precision  #Taux de chance de toucher une cible
        self.Effect = Effect        #classe Effect qui est juste en dessous
        self.description = description
        if target==None:
            target="Adversaire"
        else:
            target="self"

    def afficher_element(self):
        if self.Effect ==None:
            All_Variable = {"name":self.Name,"Type":self.Type,"Classe":self.Class,"Precision":str(self.Precision)+"%","Puissance":self.Puissance,"Effect":self.Effect.Name+" : \n "+self.Effect.description}
        else:
            All_Variable = {"name":self.Name,"Type":self.Type,"Classe":self.Class,"Precision":str(self.Precision)+"%","Puissance":self.Puissance,"Effect":"None"}
        space = len("Puissance")+1
        for i in All_Variable.keys():
            print(i," :",end="")
            for _ in range(space-len(i)):
                print(" ",end="")
            print(All_Variable[i])
class Effect:
    def __init__(self,Name,description,list_fonction) :
        self.Name = Name                #Nom de l'effect
        self.description = description  #Description de l'effect
        self.Allfunction= list_fonction #Liste de toutes les fonctions que je dois appliquer par tour au statut
    
    def update_entity(self,target):
        if self.Name == "Baisse de la defense cran 1":
            target.Changement_de_Cran("Attaque",1)

#Class = 0:Physique ,1:Speacial ,2:Autre
#Precision = valeur entre 1 et 100 (pourcentage)
#Nome Type Class Precision Puissance Effect
charge = Mouv("charge","Normal",0,100,35,50,None,"Le lanceur charge l'ennemi et le percute de tout son poids.")
# charge.afficher_element()