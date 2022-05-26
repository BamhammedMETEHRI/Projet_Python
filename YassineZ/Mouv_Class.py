import math
import random
from time import sleep

#La class Mouv permet de donner des mouv    au pokèmon#
Liste_Type = ["Normal","Feu","Eau","Plante","Électrik","Glace","Combat","Poison","Sol","Vol","Psy","Insecte","Roche","Spectre"]

Efficace = 2

Pas_Efficace = 1/2

Aucun_Effet = 0
#[Type,"Normal","Feu","Eau","Plante","Électrik","Glace","Combat","Poison","Sol","Vol","Psy","Insecte","Roche","Spectre"]
#[Type,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre]
Neutre = 1
#La Matrice est les avantage et fatigue de chaque type
Matrice_Des_Type =[
    ["En attaque\\En défense","Normal","Feu","Eau","Plante","Électrik","Glace","Combat","Poison","Sol","Vol","Psy","Insecte","Roche","Spectre"],
    ["Normal",Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Pas_Efficace,Aucun_Effet],
    ["Feu",Neutre,Pas_Efficace,Pas_Efficace,Efficace,Neutre,Efficace,Neutre,Neutre,Neutre,Neutre,Neutre,Efficace,Pas_Efficace,Neutre],
    ["Eau",Neutre,Efficace,Pas_Efficace,Pas_Efficace,Neutre,Neutre,Neutre,Neutre,Efficace,Neutre,Neutre,Neutre,Efficace,Neutre],
    ["Plante",Neutre,Pas_Efficace,Efficace,Pas_Efficace,Neutre,Neutre,Neutre,Pas_Efficace,Efficace,Pas_Efficace,Neutre,Pas_Efficace,Efficace,Neutre],
    ["Électrik",Neutre,Neutre,Efficace,Pas_Efficace,Pas_Efficace,Neutre,Neutre,Neutre,Aucun_Effet,Efficace,Neutre,Neutre,Neutre,Neutre],
    ["Glace",Neutre,Neutre,Pas_Efficace,Efficace,Neutre,Pas_Efficace,Neutre,Neutre,Efficace,Efficace,Neutre,Neutre,Neutre,Neutre],
    ["Combat",Efficace,Neutre,Neutre,Neutre,Neutre,Efficace,Neutre,Pas_Efficace,Neutre,Pas_Efficace,Pas_Efficace,Pas_Efficace,Efficace,Aucun_Effet],
    ["Poison",Neutre,Neutre,Neutre,Efficace,Neutre,Neutre,Neutre,Pas_Efficace,Pas_Efficace,Neutre,Neutre,Efficace,Pas_Efficace,Pas_Efficace],
    ["Sol",Neutre,Efficace,Neutre,Pas_Efficace,Efficace,Neutre,Neutre,Efficace,Neutre,Aucun_Effet,Neutre,Pas_Efficace,Efficace,Neutre],
    ["Vol",Neutre,Neutre,Neutre,Efficace,Pas_Efficace,Neutre,Efficace,Neutre,Neutre,Neutre,Neutre,Efficace,Pas_Efficace,Neutre],
    ["Psy",Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Efficace,Efficace,Neutre,Neutre,Pas_Efficace,Neutre,Neutre,Neutre],
    ["Insect",Neutre,Pas_Efficace,Neutre,Efficace,Neutre,Neutre,Pas_Efficace,Efficace,Neutre,Pas_Efficace,Efficace,Neutre,Neutre,Pas_Efficace],
    ["Roche",Neutre,Efficace,Neutre,Neutre,Neutre,Efficace,Pas_Efficace,Neutre,Pas_Efficace,Efficace,Neutre,Efficace,Neutre,Neutre],
    ["Spectre",Aucun_Effet,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Neutre,Aucun_Effet,Neutre,Neutre,Efficace]
]
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
        self.full_PP = PP
        self.PP = self.full_PP                #Nombre de fois que l'on peut utiliser cette attaque
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
            self.target="Adversaire"
        else:
            self.target="self"
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

    def Coup_critique(self,equipier):

        vitesse = round(equipier.Speed)
        if not(vitesse%2 == 0):
            vitesse -=1
        if random.randint(0,255) <= vitesse /2:
            print("1. COUP CRITIQUE !!!!")
            sleep(2)
            return (2*equipier.Level+5)/(equipier.Level+5)
        else:
            return 1

    def Staber(self,equipier):
        for i in equipier.Type:
            if i == self.Type:
                print("2. L'attaque est staber")
                sleep(2)
                return 1.5
        return 1 

    def BonusType(self,adversaire):
        print("3.Cette attaque est : ")
        multiplicateur = 1
        for t in range(len(Liste_Type)):
            if Liste_Type[t]==self.Type:
                Type_Attaque = t+1
        for i in adversaire.Type:
            for j in range(len(Liste_Type)):
                Type_Defense = j+1
                if Liste_Type[j] == i :
                    if Matrice_Des_Type[Type_Attaque][Type_Defense] == 2:
                        print( "     /!\\ SUPER EFFICACE !!! /!\\")
                    elif Matrice_Des_Type[Type_Attaque][Type_Defense] == 1/2:
                        print("     V PAS tres efficace V ")
                    elif Matrice_Des_Type[Type_Attaque][Type_Defense] == 0:
                        print("     0 cette Attaque n'as aucun effet 0 ")
                    else:
                        print("     - Efficace ")
                    multiplicateur *= Matrice_Des_Type[Type_Attaque][Type_Defense]
        if multiplicateur == 4:
            print("     $$$$ CETTE ATTAQUE EST SUPER SUPER EFFICACE OMG $$$$")
        return multiplicateur
    
    def Calcule_CM(self,equipier,adversaire):
        CM = 1
        CM *= (random.randint(85,100)/100) 
        CM *= self.Coup_critique(equipier)
        CM *= self.Staber(equipier)
        CM *= self.BonusType(adversaire)
        sleep(2)
        return CM

    def Calcule_Degat(self,equipier,adversaire):
        print(equipier.name," utilise, ",self.name," sur ",adversaire.name," : \n")
        if self.Class == "Statut" or self.Class == "Autre":
            print("cette ataque ne fais pas de degat elle a un effet \n") 
            if self.target == "self":
                self.Other_Attack(equipier)
            else :
                self.Other_Attack(adversaire)
            return 0
        CM = self.Calcule_CM(equipier,adversaire)

        if self.Class == "Physique":
            print("c'est une Attack physique \n")
            Attaque= equipier.Attack
            Defense = adversaire.Defense
        elif self.Class == "Special" :
            print("c'est une Attack special \n")
            Attaque= equipier.AttackSPE
            Defense = adversaire.DefenseSPE
        sleep(2)

        Degat = ((equipier.Level*0.4+2)*Attaque*self.Puissance)
        Degat = Degat / (Defense*50)
        Degat = (Degat +2) * CM
        print(adversaire.name," perd environs",round(Degat)," PV")
        sleep(1)
        if self.Effect != None and adversaire.statu == None:
            self.Effect.update_entity(adversaire)
        return Degat

    def Other_Attack(self,target):
        self.Effect.update_entity(target)
    
    def toucher(self,equipier,adversaire):
        PrecisionAttaquant = equipier.Precision
        PrecisionAttaque = self.Precision
        EsquiveDeffenseur =adversaire.Esquive
        Probabiliter_reussite = PrecisionAttaque * (PrecisionAttaquant/EsquiveDeffenseur)
        Aleatoire = random.randint(0,100)
        if Aleatoire <= Probabiliter_reussite :
            # print(equipier.name," reussi son attaque ",self.name," sur ",adversaire.name,".")
            return True
        else :
            print(equipier.name," rate son attaque .")
            return False

class Effect:
    def __init__(self,name,description,fonction_aplication=None,nbrDeTour=None) :#effect = permanant pendant tout un combat
        self.nbrTour = nbrDeTour
        self.name = name                #Nom de l'effect
        self.description = description  #Description de l'effect
        self.Fonction_aplication = fonction_aplication
    
    def update_entity(self,target):
        if self.name == "l'attaque baisse":

            print("L'attaque de ",target.name," baisse ")
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
                    self.nbrTour -=1
                    print("Aïe Aïe ",target.name," subit des degat a cause de bruler")                                 
                    target.HP = target.HP - (target.HP_full*(1/16))
                    print("il perds ",math.ceil(target.HP_full*(1/16))," PV")
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
Brule1sur10 = Effect("bruler","le Joueur ayant ce statu perds 1 / 16 de ces pv complet",pourcent1sur10,random.randint(5,7)) 

#attaque
rugissement = Mouv("rugissement","Normal",2,100,40,None,attaque_baisse,"Le lanceur pousse un cri tout mimi pour tromper la vigilance de l'ennemi et baisser son Attaque.")
charge = Mouv("charge","Normal",0,100,35,50,None,"Le lanceur charge l'ennemi et le percute de tout son poids.")
flameche = Mouv("Flammèche","Feu",1,100,25,40,Brule1sur10,"L'ennemi est attaqué par une faible flamme. Peut aussi le brûler. (proba : 1 sur 10 l'attaque dur entre 5 et 7 tour)",None)
Griffe = Mouv("Griffe","Normal",0,100,35,40,None,"Lacère l'ennemi avec des griffes acérées pour lui infliger des dégâts.")
# charge.afficher_element()