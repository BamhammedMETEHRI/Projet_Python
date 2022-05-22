import random
#La class Mouv permet de donner des mouv    au pokèmon#
Liste_Type = ["Normal","Feu","Eau","Plante","Électrik","Glace","Combat","Poison","Sol","Vol","Psy","Insecte","Roche","Spectre"]

Liste_attaque_Normal=[]
Liste_attaque_Feu=[]
Liste_attaque_Eau=[]
Liste_attaque_Plante=[]
Liste_attaque_Électrik=[]
Liste_attaque_Glace=[]
Liste_attaque_Combat=[]
Liste_attaque_Poison = []
Liste_attaque_Sol = []
Liste_attaque_Vol = []
Liste_attaque_Psy = []
Liste_attaque_Insecte = []
Liste_attaque_Roche = []
Liste_attaque_Spectre = []

class Mouv:
    def __init__(self,name,Type,Class,Precision,PP,Puissance=None,Effect=None,description=None,target=None):
        self.PP = PP                #Nombre de fois que l'on peut utiliser cette attaque
        self.name = name            #nom de l'attaque 
        self.Type= Type             #Type de l'attaque unique
                
        self.Puissance =  Puissance #Puissance de l'attaque
        if Class==0:
            self.Class = "Physique"  #Physique = 0 ou Special = 1 et autre = 2
        elif Class==1:
            self.Class = "Special"
        elif Class==2:
            self.Class = "Statut"
        else:
            self.Class = "Autre"
        self.Precision = Precision  #Taux de chance de toucher une cible
        self.Effect = Effect        #classe Effect qui est juste en dessous
        self.description = description
        if target==None:
            target="Adversaire"
        else:
            target="self"
        for i in range(len(Liste_Type)):
            if i==0:
                Liste_attaque_Normal.append(self)
            elif i ==1:
                Liste_attaque_Feu.append(self)
            elif i==2:
                Liste_attaque_Eau.append(self)
            elif i == 3:
                Liste_attaque_Plante.append(self)
            elif i==4:
                Liste_attaque_Électrik.append(self)
            elif i==5:
                Liste_attaque_Glace.append(self)
            elif i==6:
                Liste_attaque_Combat.append(self)
            elif i==7:
                Liste_attaque_Poison.append(self)

    def afficher_element(self):
        if self.Effect ==None:
            All_Variable = {"name":self.name,"Type":self.Type,"Classe":self.Class,"Precision":str(self.Precision)+"%","Puissance":self.Puissance,"Effect":self.Effect.name+" : \n "+self.Effect.description}
        else:
            All_Variable = {"name":self.name,"Type":self.Type,"Classe":self.Class,"Precision":str(self.Precision)+"%","Puissance":self.Puissance,"Effect":"None"}
        space = len("Puissance")+1
        for i in All_Variable.keys():
            print(i," :",end="")
            for _ in range(space-len(i)):
                print(" ",end="")
            print(All_Variable[i])
class Effect:
    def __init__(self,name,description,fonction_aplication=None,nbrDeTour=None) :#effect = permanant pendant tout un combat
        self.nbrTour = nbrDeTour
        self.name = name                #Nom de l'effect
        self.description = description  #Description de l'effect
        self.Fonction_aplication = fonction_aplication
    
    def update_entity(self,target):
        if self.name == "l'attaque baisse":
            print("L'attaque de ",target," baisse ")
            target.Changement_de_Cran("Attaque",-1)
        elif self.name == "bruler":
            if self.Fonction_aplication() and target.statu==None and self.nbrTour > 0:
                target.statu=self
                target.All_Variable["statu"] = self.name
                print("Mince Maintenant ",target.name," a brulure !")
            elif self.nbrTour <=0 :
                print(target.name," n'est plus bruler")
                target.statu = None
            elif type(target.statu)== Effect: 
                if target.statu.name == "bruler":
                    print("Aïe Aïe ",target.name," subit des degat a cause de bruler")
                    target.HP = target.HP - round((target.HP_full*(1/16)))
                    target.All_Variable["HP"] = target.HP
            

def pourcent1sur10():
    if random.randint(0,100)<=10:
        return True
    return False
# print(pourcent1sur10())

#Class = 0:Physique ,1:Speacial ,2:Autre
#Precision = valeur entre 1 et 100 (pourcentage)
#Nome Type Class Precision Puissance Effect
#effet
attaque_baisse = Effect("l'attaque baisse","L'attaque du Joueur adverse baisse d'un Cran")
Brule1sur10 = Effect("bruler","10%\ de bruler",pourcent1sur10,random.randint(3,4)) 

#attaque
rugissement = Mouv("rugissement","Normal",2,100,40,None,attaque_baisse,"Le lanceur pousse un cri tout mimi pour tromper la vigilance de l'ennemi et baisser son Attaque.")
charge = Mouv("charge","Normal",0,100,35,50,None,"Le lanceur charge l'ennemi et le percute de tout son poids.")
flameche = Mouv("Flammèche","Feu",1,100,25,40,Brule1sur10,"L'ennemi est attaqué par une faible flamme. Peut aussi le brûler.",None)
Griffe = Mouv("Griffe","Normal",0,100,35,40,None,"Lacère l'ennemi avec des griffes acérées pour lui infliger des dégâts.")
# charge.afficher_element()