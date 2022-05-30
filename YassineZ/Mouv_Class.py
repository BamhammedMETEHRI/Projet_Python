import math
import random
from statistics import NormalDist
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

def alreadyHer(Attck,L):
    for i in range(len(L)):
        if L[i].name == Attck.name:
            return True
    return False
class Mouv:
    def __init__(self,name,Type,Class,Precision,PP,Puissance=None,Effect=None,description=None,target=None,CoeficienCritique=None):
        self.CoeficienCritique = 0
        if CoeficienCritique != None:
            self.CoeficienCritique += CoeficienCritique
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
            if i==0  :
                Liste_attaque_Normal.append(self)
            elif i ==1  :
                Liste_attaque_Feu.append(self)
            elif i==2 :
                Liste_attaque_Eau.append(self)
            elif i == 3 :
                Liste_attaque_Plante.append(self)
            elif i==4 :
                Liste_attaque_Électrik.append(self)
            elif i==5 :
                Liste_attaque_Glace.append(self)
            elif i==6 :
                Liste_attaque_Combat.append(self)
            elif i==7 :
                Liste_attaque_Poison.append(self)
            elif i == 8 :
                Liste_attaque_Sol.append(self)
            elif i==9 :
                Liste_attaque_Vol.append(self)
            elif i==10 :
                Liste_attaque_Psy.append(self)
            elif i==10:
                Liste_attaque_Insecte.append(self)
            elif i==11 :
                Liste_attaque_Roche.append(self)
            elif i==12 :
                Liste_attaque_Spectre.append(self)

    def Newattaque(self):
        if self.Class == "Physique":
            C=0
        elif self.Class == "Special":
            C=1
        else:
            C=2
        if self.Effect==None:
            Effet = None
        elif type(self.Effect)==str:
            Effet =self.Effect 
        else:
            Effet = self.Effect.NewEffect()
        t =Mouv(self.name,self.Type,C,self.Precision,self.full_PP,self.Puissance,Effet,self.description,self.target)
        for i in AllCompetence:
            if len(i) > 1 and i[len(i)-1]==self:
                i.pop(len(i)-1)
        return t

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
        T = (vitesse /2)
        b = 8
        if self.CoeficienCritique == 0:
            b = 1
        else:
            b*= self.CoeficienCritique
        if random.randint(0,255) <= T*b :
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
        if self.name =="Frappe Atlas":
            Attaque = equipier.Level
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
        print(adversaire.name," perd environs",(Degat*100)//adversaire.HP_full,"% PV")
        sleep(1)
        if self.Effect != None and self.Effect.target == "self":
            self.Effect.update_entity(equipier)
        if self.Effect != None and adversaire.statu == None:
            self.Effect.update_entity(adversaire)
        elif self.Effect != None and self.Effect.name=="Infecter":
            self.Effect.update_entity(adversaire,equipier)
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
            if self.name == "Météores":
                return True
            print(equipier.name," rate son attaque .")
            return False

class Effect:
    def __init__(self,name,description,fonction_aplication=None,nbrDeTour=None,target=None) :#effect = permanant pendant tout un combat
        self.name = name                #Nom de l'effect
        self.nbrTour = nbrDeTour
        self.description = description  #Description de l'effect
        self.Fonction_aplication = fonction_aplication
        if target == None:
            self.target = "other"
        else:
            self.target = "self"
    def NewEffect(self):
        return Effect(self.name,self.description,self.Fonction_aplication,self.nbrTour,self.target)

    def update_entity(self,target,Lanceur=None):
        if self.name == "l'attaque baisse":

            print("L'attaque de ",target.name," baisse ")
            target.Changement_de_Cran("Attaque",-1)

        elif self.name[0:17] == "la Precision baisse":
            print("La Precision du Joueur ",target.name," baisse. ")
            target.Changement_de_Cran("Precision",-1-len(self.name[17:]))

        elif self.name[0:17] == "la vitesse baisse":
            print("La vitesse du Joueur ",target.name," baisse. ")
            target.Changement_de_Cran("Speed",-1-len(self.name[17:]))

        elif self.name[0:18] == "la vitesse augment":
            print("La vitesse du Joueur ",target.name," augmente. ")
            target.Changement_de_Cran("Speed",+1+len(self.name[18:]))
        
        elif self.name[0:17] == "la defense baisse":
            print("La defense du Joueur ",target.name," baisse. ")
            target.Changement_de_Cran("Defense",-1-len(self.name[17:]))

        elif self.name[0:18] == "la defense augment":
            print("La defense du Joueur ",target.name," augmente. ")
            target.Changement_de_Cran("Defense",+1+len(self.name[18:]))

        elif self.name[0:21] == "la defensespe augment":
            print("La defense du Joueur ",target.name," augmente. ")
            target.Changement_de_Cran("DefenseSPE",+1+len(self.name[21:]))
        
        elif self.name[0:20] == "la defensespe baisse" and self.Fonction_aplication():
            print("La defense du Joueur ",target.name," baisse. ")
            target.Changement_de_Cran("DefenseSPE",-1-len(self.name[20:]))

        elif self.name == "Peur":
            if self.Fonction_aplication() and self.nbrTour > 0:
                target.PetitStatu.append(self)
            elif self.nbrTour <=0 :
                print(target.name," n'a plus peur")
                for i in range(len(target.PetitStatu)):
                    if target.PetitStatu[i]==self:
                        target.PetitStatu.pop(i)
            else:
                self.nbrTour -=1
                print("Il a Peur Il ne peut pas attaquer")
                sleep(3)
                return False
            
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
        
        elif self.name == "Empoisoner":

            if self.Fonction_aplication() and target.statu==None and self.nbrTour > 0:
                target.statu=self
                print("Mince Maintenant ",target.name," est empoisoner !")
            elif self.nbrTour <=0 :
                print(target.name," n'est plus empoisoner")
                target.statu = None
            elif type(target.statu)== Effect: 
                if target.statu.name == "Empoisoner":
                    self.nbrTour -=1
                    print("Aïe Aïe ",target.name," subit des degat a cause du poison")                                 
                    target.HP = target.HP - (target.HP_full*(1/16))
                    print("il perds ",math.ceil(target.HP_full*(1/16))," PV")
                    target.All_Variable["HP"] = target.HP


        elif self.name == "Infecter":

            if not(self in target.PetitStatu):
                target.PetitStatu.append(self)
                print("Mince Maintenant ",target.name," est Infecter !")
            else: 
                print("Aïe Aïe ",target.name," subit des degat a cause de l'infection")                                 
                target.HP = target.HP - (target.HP_full*(1/8))
                print("il perds ",math.ceil(target.HP_full*(1/8)*100)//target.HP_full," PV")
                Lanceur.HP += Lanceur.HP_full*0.3
                if Lanceur.HP > Lanceur.HP_full:
                    Lanceur.HP = Lanceur.HP_full
                print("Et ",Lanceur.name," gagne 30% \de ces PV")

        elif self.name == "Confusion":

            if not(self in target.PetitStatu):
                target.PetitStatu.append(self)
                print("Mince Maintenant, ",target.name ,"est confus !")
            elif self.nbrTour <=0 :
                print(target.name," n'est plus confus")
                target.canAttack = True
                for i in range(len(target.PetitStatu)):
                    if self.name == target.PetitStatu[i]:
                        target.PetitStatu.pop(i)
            else: 
                if random.randint(1,2) == 1:
                    target.canAttack = False
                    print(target.name," se frappe lui meme")
                    Degat = ((target.Level*0.4+2)*target.Attack*40)
                    Degat = Degat / (target.Defense*50)
                    Degat = (Degat +2)
                    target.HP -= Degat
                    print("il perd ",(Degat*100)//target.HP_full,"%\ de ces PV")
                else:
                    target.canAttack = True


        elif self.name == "Neutre":

            if not(self in target.PetitStatu):
                target.PetitStatu.append(self)
                print("Maintenant ton equipe ne pas baisser leur state !")
            elif self.nbrTour <=0 :
                print("Vous nete plus proteger par les changement de state")
            else: 
                self.nbrTour -=1
                target.Fin_de_Combat("o")
        elif self.name == "Someil":

            if self.Fonction_aplication() and target.statu==None and self.nbrTour > 0:
                target.statu=self
                target.All_Variable["statu"] = self.name
                print("Mince Maintenant ",target.name," est ENDORMIE !")
            elif self.nbrTour <=0 :
                print(target.name," n'est plus endormie et il est reveiler")
                target.canAttack = True
                target.statu = None
            elif type(target.statu)== Effect: 
                if target.statu.name == "Someil":
                    self.nbrTour -=1
                    print(target.name," dors paisiblement")                                 
                    target.canAttack = False

        elif self.name == "Gel":

            if self.Fonction_aplication() and target.statu==None and self.nbrTour > 0:
                target.statu=self
                target.All_Variable["statu"] = self.name
                print("Mince Maintenant ",target.name," est GELER !")
            elif self.nbrTour <=0 :
                print(target.name," n'est plus geler")
                target.canAttack = True
                target.statu = None
            elif type(target.statu)== Effect: 
                if target.statu.name == "Gel":
                    self.nbrTour -=1
                    print(target.name," est comme un galçons")                                 
                    target.canAttack = False

        elif self.name == "paralyse":

            if self.Fonction_aplication() and target.statu==None and self.nbrTour > 0:
                target.statu=self
                target.speed /=2
                print("Mince Maintenant ",target.name," est Paralyse !")
            elif self.nbrTour <=0 :
                print(target.name," n'est plus paralyse")
                target.speed = target.speed_full
                target.statu = None
            elif type(target.statu)== Effect: 
                if target.statu.name == "paralyse":
                    self.nbrTour -=1
                    if random.randint(1,4) == 1 :
                        print(target.name," Ne peut pas jouer il est Paralyse")
                        return False
        elif self.name == "Contre coup":
            print("Contre coup le jouer qui lancer l'attaque ce blesse il perd 5% de ces pV")
            target.HP -= target.HP_full * 0.5 
        elif self.name == "AUTO KO":
            print(target.name," se suicide")
            target.HP=0
        return True
            

def pourcent1sur10():
    if random.randint(0,100)<=10:
        return True
    return False
def pourcent1sur4():
    if random.randint(1,4)== 1:
        return True
    return False
def pourcent1sur3():
    if random.randint(0,2)== 0:
        return True
    return False
def sure():
    return True
# print(pource
# nt1sur10())

#Class = 0:Physique ,1:Speacial ,2:Autre
#Precision = valeur entre 1 et 100 (pourcentage)
#Nome Type Class Precision Puissance Effect

#CREATION effet
attaque_baisse1 = Effect("l'attaque baisse","L'attaque du Joueur adverse baisse d'un Cran")
defense_baisse1 = Effect("la defense baisse","Baisse la Défense des cibles d'un Cran")
defense_baisse2 = Effect("la defense baisse+","Baisse la Défense des cibles de 2 Cran")
vitesse_baisse1 = Effect("la vitesse baisse","Baisse la vitesse du joueur d'un cran")
vitesse_augment2 = Effect("la vitesse augment+","Augmente la vitesse du joueur de 2 cran",None,"self")
defense_augment1 = Effect("la defense augment","Augment la Défense des cibles d'un Cran",None,"self")
defensespe_augment2 = Effect("la defensespe augment+","Augment la Défense des cibles de 2 Cran",sure,"self")
defensespe_baisse1_1sur10 = Effect("la defensespe baisse","Baisse la DéfenseSPE des cibles d'un Cran",pourcent1sur10)


Brule1sur10 = Effect("bruler","le Joueur ayant ce statu perds 1 / 16 de ces pv complet",pourcent1sur3,random.randint(5,7)) 
parylyse1sur10=Effect("paralyse","Des coup jus qui paralyse Le joueur",pourcent1sur10,random.randint(5,7))
parylyse1sur3=Effect("paralyse","Des coup jus qui paralyse Le joueur",pourcent1sur10,random.randint(5,7))
PrisonFeux = Effect("bruler","Il piegier dans dans des flammes",sure,5)
Priority = Effect("First","à la priorité donc comence en premier")
Peur1sur3 = Effect("Peur","30%¨de chance que l\'adversaire ne fasse rien",pourcent1sur3)
# Gain = Effect("Argent","L'argent gagné suit la formule : 5 * Niveau du lanceur * Nombre de Jackpot utilisés",None,None,"self") USELESS
repeat = Effect("Repeat","Le joueur re utilise son attaque",None,random.randint(2,5))
Infecter = Effect("Infecter","1/8 des PV max de la cible sont drainés pour le lanceur à la fin de chaque tour jusqu'à que la cible soit retirée du terrain. N'affecte pas les Pokémon Plante. La Grosse Racine augmente les PV restaurés de 30%.",)
Dodo = Effect("Someil","Le joueur est endormie il ne peut pas joueur",None,random.randint(1,7))
Poison = Effect("Empoisoner","le Joueur est empoisonne il perd 1 16iem de ces pv",sure,None,random.randint(6,8))
Gel1sur10 = Effect("Gel","Le joueur est geler il ne peut pas joueur",pourcent1sur10,random.randint(1,7))
parylyse = Effect("paralyse","Un faible choc électrique frappe l'ennemi. Si l'attaque le touche, celui-ci est paralysé.",sure,random.randint(5,7))
NeutreState = Effect("Neutre","Une brume blanche enveloppe l'équipe du lanceur et empêche la réduction des stats par les autres Pokémon durant 5 tours.",None,5,"self")
Confus1sur10 =  Effect("Confusion","Un rayon sinistre qui plonge l'ennemi dans un état de confusion.",sure,5)
Confus =  Effect("Confusion","Un rayon sinistre qui plonge l'ennemi dans un état de confusion.",pourcent1sur10,5)
Contrecoup = Effect("Contre coup","Le joueur se blesse en fesant cette attaque","self")
Poison1sur4 = Effect("Empoisoner","le Joueur est empoisonne il perd 1 16iem de ces pv",pourcent1sur4,random.randint(6,8))
Poison1sur3 = Effect("Empoisoner","le Joueur est empoisonne il perd 1 16iem de ces pv",pourcent1sur3,random.randint(6,8))
AutoDestrucion= Effect("AUTO KO","Le pokemon se tue lui meme",None,None,"self")
precision_baisse1 = Effect("la Precision baisse","baisse la precision du joueur d'un' cran",None,"self")
#######################################################CREATION attaque
charge = Mouv("charge","Normal",0,100,35,50,None,"Le lanceur charge l'ennemi et le percute de tout son poids.")
Vive_attaque=Mouv("Vive-attaque","Normal",0,100,30,40,Priority,"Le lanceur fonce sur l'ennemi si rapidement qu'on parvient à peine à le discerner. Frappe en priorité.")
Griffe = Mouv("Griffe","Normal",0,100,35,40,None,"Lacère l'ennemi avec des griffes acérées pour lui infliger des dégâts.")
rugissement = Mouv("rugissement","Normal",2,100,40,None,attaque_baisse1,"Le lanceur pousse un cri tout mimi pour tromper la vigilance de l'ennemi et baisser son Attaque.")

flameche = Mouv("Flammèche","Feu",1,100,25,40,Brule1sur10,"L'ennemi est attaqué par une faible flamme. Peut aussi le brûler. (proba : 1 sur 10 l'attaque dur entre 5 et 7 tour)",None)
GrozYeux = Mouv("Groz'Yeux","Normal",2,100,30,None,defense_baisse1,"Le lanceur fait les gros yeux à l'ennemi pour l'intimider et baisser sa Défense.")
MimiQueue = Mouv("Mimi-Queue","Normal",2,100,30,None,defense_baisse1,"Le lanceur remue son adorable queue pour tromper la vigilance de l'ennemi et baisser sa Défense.")
Tranche = Mouv("Tranche","Normal",0,100,20,70,None,"Un coup de griffe ou autre tranche l'ennemi. Taux de critiques élevé.",None,1)

LanceFlammes = Mouv("Lance-Flammes","Feu",1,100,15,90,Brule1sur10,"L'ennemi reçoit un torrent de flammes. Peut aussi le brûler.")
CombotGriffe = Mouv("Combo-Griffe","Normal",0,80,15,18,repeat,"L'ennemi est lacéré par des faux ou des griffes de deux à cinq fois d'affilée.")
Jackpot  = Mouv("Jackpot","Normal",0,100,20,40,None,"Des pièces sont lancées sur l'ennemi. Permet d'obtenir de l'argent à la fin du combat.")
Vampigraine = Mouv("Vampigraine","Plante",2,90,10,None,Infecter,"Une graine est semée sur l'ennemi. À chaque tour, elle lui dérobe des PV que le lanceur récupère.")

TrancheHerbe = Mouv("Tranch'Herbe","Plante",0,95,25,55,None,"Des feuilles aiguisées comme des rasoirs entaillent l'ennemi. Taux de critiques élevé.",None,1)
PoudreDodo = Mouv("Poudre Dodo","Plante",2,75,15,None,Dodo,"Le lanceur répand une poudre soporifique qui endort la cible.")
PoudreToxique = Mouv("Poudre Toxik","Poison",2,75,35,None,Poison,"Une poudre toxique empoisonne l'ennemi.")
Eclair = Mouv("Éclair","Électrik",1,100,30,40,parylyse1sur10,"Une décharge électrique tombe sur l'ennemi. Peut aussi le paralyser.")
CageEclaire = Mouv("Cage Éclair","Électrik",2,90,20,None)
Meteor = Mouv("Météores","Normal",1,100,20,60,None,"Le lanceur envoie des rayons d'étoiles. Touche toujours l'ennemi.")
hate = Mouv("Hâte","Psy",2,1000,30,None,vitesse_augment2,"Le lanceur se relaxe et allège son corps pour beaucoup augmenter sa Vitesse.","self")
FatalFoudre=Mouv("Fatal-Foudre","Électrik",1,70,10,110,parylyse1sur3,"La foudre tombe sur l'ennemi pour lui infliger des dégâts. Peut aussi le paralyser.")
Ecume = Mouv("Écume","Eau",1,100,30,40,vitesse_baisse1,"Une attaque de bulles pouvant baisser la Vitesse.")
PistoletO = Mouv("Pistolet à O","Eau",1,100,25,40,None,"De l'eau est projetée avec force sur l'ennemi.")
Morsure = Mouv("Morsure","Normal",0,100,25,60,Peur1sur3,"L'ennemi est mordu par de tranchantes canines. Peut l'apeurer.")
Repli = Mouv("Repli","Eau",2,1000,40,None,defense_augment1,"Le lanceur se recroqueville dans sa carapace, ce qui augmente sa Défense.","self")
CoudKrane = Mouv("Coud'Krâne","Normal",0,100,10,130,defense_augment1,"Le lanceur baisse la tête pour augmenter sa Défense au premier tour et percuter l'ennemi au second.")
HydroCanon = Mouv("Hydrocanon ","Eau",1,80,5,110,None,"Un puissant jet d'eau est dirigé sur l'ennemi.")
Berceuse = Mouv("Berceuse","Normal",2,55,15,None,Dodo,"Une berceuse plonge l'ennemi dans un profond sommeil.")
Brume = Mouv('Brume',"Glace",2,1000000,30,None,NeutreState,"Une brume blanche enveloppe l'équipe du lanceur et empêche la réduction des stats par les autres Pokémon durant 5 tours.","self")
Plaquage = Mouv("Plaquage","Normal",0,100,15,85,parylyse1sur3,"Le lanceur se laisse tomber sur l'ennemi de tout son poids. Peut aussi le paralyser.")
OndeFolie = Mouv("Onde Folie","Spectre",2,100,10,None,Confus,"Un rayon sinistre qui plonge l'ennemi dans un état de confusion.")
LaserGlace= Mouv("Laser Glace","Glace",1,100,10,90,Gel1sur10,"Un rayon de glace frappe l'ennemi. Peut aussi le geler.")
PoingKarate = Mouv('Poing Karaté',"Combat",0,100,25,50,None,"Une attaque tranchante à taux de critiques élevé.",None,1)
FrappeAtlas=Mouv("Frappe Atlas","Combat",0,100,20,1,None,"L\'ennemi est projeté grâce au pouvoir de la gravité. Inflige des dégâts équivalents au niveau du lanceur.")
Puissance = Mouv("Puissance","Normal",2,10000,30,None,None,"Le lanceur prend une profonde inspiration et se concentre pour augmenter son taux de critiques.","self",2)
Sacrifice = Mouv("Sacrifice","Combat",0,80,20,80,Contrecoup,"Le lanceur agrippe l'ennemi et l'écrase au sol. Blesse aussi légèrement le lanceur.")
Puredpois = Mouv("Purédpois","Poison",1,70,20,30,"Le lanceur attaque à l'aide d'une éruption de gaz répugnants. Peut aussi empoisonner l'ennemi.")
Detritus = Mouv("Détritus","Poison",1,100,20,65,Poison1sur3,"Des détritus toxiques sont projetés sur l'ennemi. Peut aussi l'empoisonner.")
Destruction = Mouv("Destruction","Normal",0,100,5,200,AutoDestrucion,"Le lanceur explose en blessant tous les Pokémon autour de lui. Le lanceur tombe K.O.")
Explosion = Mouv("Explosion","Normal",0,100,5,250,AutoDestrucion,"Le lanceur explose en blessant tous les Pokémon autour de lui. Le lanceur tombe K.O.")
Jetsable = Mouv("Jet de Sable","Sol",2,100,15,None,precision_baisse1,"Lance du sable au visage de l'ennemi pour baisser sa Précision.")
Seisme = Mouv("Séisme","Sol",0,100,10,100,None,"Le lanceur provoque un tremblement de terre touchant tous les Pokémon autour de lui.")
Tornade = Mouv("Tornade","Vol",1,100,35,40,None,"Peut toucher un Pokémon utilisant Rebond, Vol ou Chute Libre et double de puissance.")
CruAile = Mouv("Cru-Ailes","Vol",0,100,35,60,None,"L'ennemi est frappé par de larges ailes déployées pour infliger des dégâts.")
Chocmental = Mouv("Choc Mental","Psy",1,100,25,50,Confus1sur10,"Une faible vague télékinétique frappe l'ennemi. Peut aussi le plonger dans la confusion.")
CoupdBoule = Mouv("Coup d'Boule","Normal",0,100,15,70,Peur1sur3,"zidane")
Amnesie = Mouv("Amnésie","Psy",2,100000,20,None,defensespe_augment2,"Le lanceur fait le vide dans son esprit pour oublier ses soucis. Augmente beaucoup sa Défense Spéciale.")
Psyko = Mouv("Psyko","Psy",1,100,10,90,defensespe_baisse1_1sur10,"Une puissante force télékinétique frappe l'ennemi. Peut aussi faire baisser sa Défense Spéciale.")
Secretation = Mouv("Sécrétion","Insect",2,95,40,None,vitesse_baisse1,"Le lanceur crache de la soie pour ligoter l'ennemi et beaucoup baisser sa Vitesse.")
JetPierre = Mouv("Jet-Pierres","Roche",0,90,15,50,None,"Le lanceur lâche une pierre sur l'ennemi.")
FouetLianes = Mouv("Fouet Lianes","Plante",0,100,25,45,None,"Fouette l'ennemi avec de fines lianes pour infliger des dégâts.")
Lechouille = Mouv("Léchouille","Spectre",0,100,30,30,parylyse1sur3,"Un grand coup de langue qui inflige des dégâts à l'ennemi. Peut aussi le paralyser.")
Hypnose = Mouv("Hypnose","Psy",2,60,20,None,Dodo,"Le lanceur hypnotise l'ennemi pour le plonger dans un profond sommeil.")
# charge.afficher_element()
AllCompetence = [
    Liste_attaque_Normal,
    Liste_attaque_Feu,
    Liste_attaque_Eau,Liste_attaque_Plante,
    Liste_attaque_Électrik,
    Liste_attaque_Glace,
    Liste_attaque_Combat,
    Liste_attaque_Poison,
    Liste_attaque_Sol,
    Liste_attaque_Vol,
    Liste_attaque_Psy,
    Liste_attaque_Insecte,
    Liste_attaque_Roche,
    Liste_attaque_Spectre]