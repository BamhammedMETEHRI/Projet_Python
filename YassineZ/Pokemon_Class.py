from pickle import NONE
from tkinter import N
import colorama
from colorama import Fore
from colorama import Style
import Mouv_Class
import random
from time import sleep
import math
from os import system, name

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
# colorama.init()
# print(Fore.BLUE + Style.BRIGHT + "This is the color of the sky" + Style.RESET_ALL)
# print(Fore.GREEN + "This is the color of grass" + Style.RESET_ALL)
# print(Fore.BLUE + Style.DIM + "This is a dimmer version of the sky" + Style.RESET_ALL)
# print(Fore.YELLOW + "This is the color of the sun" + Style.RESET_ALL)
# print(len(Fore.YELLOW+Style.RESET_ALL))
# print(len(Fore.BLUE+Style.RESET_ALL))
# print(len(Fore.BLUE + Style.DIM +Style.RESET_ALL))
#La classe des pokèmon 
dessin00 ="               .-. \_/ .-.\n               \.-\/=\/.-/\n            '-./___|=|___\.-'\n           .--| \|/`\"`\|/ |--.\n          (((_)\  :____:  /(_)))\n           `\ \_`-.   .-'_/ /`_\n             '.__       __.'(_))\n                 /     \     //\n                |       |__.'/\n                \       /--'`\n            .--,-' .--. '----.\n           '----`--'  '--`----'"
asscie = []
asscie.append(dessin00)
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

def Aficher_Matrice_Des_Type():
    """
    fonction qui permet d'afficher les avantage et faiblesse de chaque type
    """
    L= ""
    for i in range(len(Matrice_Des_Type)):
        m = ""
        for j in range(len(Matrice_Des_Type[i])):
            if i == 0 and j == 0 :
                m+= "|         "#10
            else:
                if j == 0 and i!=0:
                    p ="|"+str(Fore.BLUE + Style.BRIGHT+Matrice_Des_Type[i][j]+Style.RESET_ALL)
                    while len(p) <10+len(Fore.BLUE + Style.BRIGHT+Style.RESET_ALL):#j'ai du madapter pour les couleurs
                        p +=" "
                else :
                    t = Matrice_Des_Type[i][j]
                    k=0
                    if type(t)==str :
                        p="|"+Fore.YELLOW+t+Style.RESET_ALL
                    elif t==0.5:
                        p="|"+Fore.RED+str(t)+Style.RESET_ALL
                        k= len(Fore.RED+Style.RESET_ALL)
                    elif t== 2 :
                        p="|"+Fore.GREEN+str(t)+Style.RESET_ALL
                        k= len(Fore.GREEN+Style.RESET_ALL)
                    elif t == 0:
                        p="|"+Fore.BLACK+str(t)+Style.RESET_ALL
                        k= len(Fore.BLACK+Style.RESET_ALL)
                    else:
                        p="|"+Fore.BLUE+str(t)+Style.RESET_ALL
                        k= len(Fore.BLUE+Style.RESET_ALL)
                    while len(p)<= len(Matrice_Des_Type[0][j])+k:
                        p+= " "
                m += p
        L+= m + "\n"
    print(L)

#Aficher_Matrice_Des_Type()
def Calcule_State_HP(Base,IV,EV,NIV):
        PV = ((((2*Base+IV+(EV/4)))*NIV)/100)+NIV+10
        return round(PV*1000)/1000
    
def Calcule_Sate(Base,IV,EV,NIV,CRAN=None):
        State = ((2*Base+IV+(EV/4))*NIV)+5
        if CRAN != None:
            State = State*CRAN
        return round(State*1000)/1000
#0 1 2 3 4 5 6 7 8 9 10 11 12 
Liste_de_Cran = [2/8,2/7,2/6,2/5,2/4,2/3,2/2,3/2,4/2,5/2,6/2,7/2,8/2]
Liste_de_Cran_Esquive_Precision = [3/9,3/8,3/7,3/6,3/5,3/4,3/3,4/3,5/3,6/3,7/3,8/3,9/3]

Liste_de_Pokemon = []
#definir un pokemon il est composé de quoi comme variable #Next_Evolution est un tupler un chifre et Pokemon
class Pokemon:
    def __init__(self,name,Type,competence,sauvage,State_Base_HP,State_Base_Attack,State_Base_Def,State_Base_AttackSPE,State_Base_DefSPE,State_Base_Speed,Taux_De_Capture,New_ability=None,Next_Evolution=None) :
        self.Next_Evolution = Next_Evolution
        self.name = name                #str, nom du pokemon le Joueur peut nommer son pokemon mais il ne peut pas changer ....
        self.Espece = name              #...l'espece du Pokemon fix qui est fixe 
        self.Type= Type                 #peut avoir 2 ou 1 type [str]
        self.competence= competence        #peut entre 1 et avoir max 4 Mouv et chaque Mouv à un nombre de pp et un type [ataque]
        self.Level = 1
        self.Exp=0
        self.NewAbility = New_ability
#Racine des state
        self.State_Base_HP=State_Base_HP
        self.State_Base_Attack=State_Base_Attack
        self.State_Base_AttackSPE =State_Base_AttackSPE
        self.State_Base_Def=State_Base_Def
        self.State_Base_DefSPE = State_Base_DefSPE
        self.State_Base_Speed = State_Base_Speed
##################################################################################################### EV
        self.EV = 600 #294 par state #6 a chaque niveaux il gagne 6 point d'exp
        self.EV_HP=0
        self.EV_Att=0
        self.EV_AttSPE=0
        self.EV_Def=0
        self.EV_DefSPE=0
        self.EV_Speed=0
##################################################################################################### IV
        self.IV_HP=0
        self.IV_Att=0
        self.IV_AttSPE=0
        self.IV_Def=0
        self.IV_DefSPE=0
        self.IV_Speed=0
#################################################################################################### state MAX
        self.HP_full = Calcule_State_HP(self.State_Base_HP,self.IV_HP,self.EV_HP,self.Level)          #HP_MAX -> point de vie max
        self.Attack_full = Calcule_Sate(self.State_Base_Attack,self.IV_Att,self.EV_Att,self.Level)  #Attack physique max
        self.AttackSPE_full =Calcule_Sate(self.State_Base_AttackSPE,self.IV_AttSPE,self.EV_AttSPE,self.Level)
        self.Defense_full = Calcule_Sate(self.State_Base_Def,self.IV_Def,self.EV_Def,self.Level)
        self.DefenseSPE_full =Calcule_Sate(self.State_Base_DefSPE,self.IV_DefSPE,self.EV_DefSPE,self.Level)
        self.Speed_full = Calcule_Sate(self.State_Base_Speed,self.IV_Speed,self.EV_Speed,self.Level)
########################################################################################################### Utiliser pour le combat
        self.HP=self.HP_full                 #HP actuel
        self.Attack = self.Attack_full
        self.AttackSPE =self.AttackSPE_full
        self.Defense = self.Defense_full
        self.DefenseSPE = self.DefenseSPE_full
        self.Speed = self.Speed_full
############################################################################################################################# cran pour le boust de state
        self.Cran_Attack =0
        self.Cran_AttackSPE =0
        self.Cran_Defense = 0
        self.Cran_DefenseSPE =0
        self.Cran_Speed = 0
        self.Cran_Esquive = 0
        self.Cran_Precision = 0
#fin
        self.canAttack = True
        self.statu = None
        self.PetitStatu = []
        self.Taux_De_Capture = Taux_De_Capture
        self.Esquive = 100
        self.Precision = 100
        self.dialogue = self.Espece +" "+ self.Espece +" " + self.Espece +" !!!"
        self.sauvage = sauvage  #bool True = il est sauvage , False = il est capturè
        Liste_de_Pokemon.append(self)
        self.All_Variable = {
            "name":self.name,"Espece":self.Espece,"type":self.Type,"competence":self.competence,"Level":self.Level,"Experience":self.Exp,
            "State Base HP":self.State_Base_HP,"IV HP":self.IV_HP,"EV HP":self.EV_HP,"HP full":self.HP_full,"HP":self.HP,
            "State base Attack":self.State_Base_Attack,"IV Att":self.IV_Att,"EV Att":self.EV_Att,"Attack full":self.Attack_full,"Attack":self.Attack,
            "State base AttackSPE":self.State_Base_AttackSPE,"IV AttSPE":self.IV_AttSPE,"EV AttSPE":self.EV_AttSPE,"AttackSPE full":self.AttackSPE_full,"AttackSPE":self.AttackSPE,
            "State base Def":self.State_Base_Def,"IV Def":self.IV_Def,"EV Def":self.EV_Def,"Defense full":self.Defense_full,"Defense":self.Defense,
            "State base DefSPE":self.State_Base_DefSPE,"IV DefSPE":self.IV_DefSPE,"EV DefSPE":self.EV_DefSPE,"DefenseSPE full":self.DefenseSPE_full,"DefenseSPE":self.DefenseSPE,
            "State base Speed":self.State_Base_Speed,"IV Speed":self.IV_Speed,"EV Speed":self.EV_Speed,"Speed full":self.Speed_full,"Speed":self.Speed,
            "statu":self.statu,"Taux De Capture":self.Taux_De_Capture,"Esquive":self.Esquive,"Precision":self.Precision,"dialogue":self.dialogue,"sauvage":self.sauvage
        }
    
        
    def agir(self,Competence,Cible):
        r = True
        for i in self.PetitStatu:
            if i.name=="Peur":
                r = i.update_entity(self)
        if self.statu != None:
            if self.statu.name == "paralyse":
                return self.statu.update_entity(self)
        if Competence.toucher(self,Cible) and self.canAttack and r :
            return True
        else:
            print("il a rater sont attaque")
            return False

    def Info_Pokemon(self):
        a= asscie[random.randint(1,len(asscie))-1]
        print("INFO DU POKEMON ",self.name," : ")
        print(a)
        print("Espece : ",self.Espece,end="")
        print(" | TYPE   : ",self.Type[0],end="")
        if len(self.Type)>=2:
            print(", ",self.Type[1],end="")
        print()
        print("NIV = ",self.Level,"         | PV     = ",self.HP," / ",self.HP_full)
        print("ATK = ",self.Attack,"     | ATKspe =",self.AttackSPE)
        print("DEF = ",self.Defense,"     | DEFspe =",self.DefenseSPE)
        print("SPEED = ",self.Speed)
        input("apuie sur entrée pour voir les info sur ces attaque ")
        clear()
        print("Structure des competence :\n\nNom du pokemon \" representation non contractuel du pokemon \"\n\nID. Nom de l'attaque : \n-Type\n-Sa Puissance\n-PP : Nombre de PP Actuel/ Nombre de PP Max\n-Class de l'attaque si elle utilise les states spe ou normal ou aucune\n-Sa cible\n-description\n  - Nom de l'effect \n  - description de l'effet")
        input("apuie sur entrée pour voir les info sur ces attaque ")
        clear()
        print("INFO DES COMPETENCE DE ",self.name," : ")
        print(a)
        for i in range(4):
            if i> len(self.competence)-1:
                print("ID ",i+1,". PAS DE COMPETENCE")
            else:
                print("ID ",i+1,". ",self.competence[i].name,"\n  - Type : ",self.competence[i].Type)
                print("  - Puissance : ",self.competence[i].Puissance)
                print("  -PP : ",self.competence[i].PP,' / ',self.competence[i].full_PP)
                print("  -C'est une attaque : ",self.competence[i].Class)
                print("  -Cible : ",self.competence[i].target)
                print("Description : ",self.competence[i].description)
                if self.competence[i].Effect != None:
                    print("    -Nom d'effect : ",self.competence[i].Effect.name)
                    print("    -description effect : ",self.competence[i].Effect.description)
                print()
        input()
        


    def afficher_state(self):
        debut=False
        space=[len("State base AttackSPE "),len("IV AttSPE "),len("EV AttSPE "),len("AttackSPE full "),len("AttackSPE ")]
        color=[Fore.GREEN,Fore.RED,Fore.LIGHTMAGENTA_EX,Fore.BLUE,Fore.CYAN,Fore.LIGHTWHITE_EX]
        index_color =0
        index_space=0
        for i in self.All_Variable.keys():
            if i=="State Base HP":
                debut=True
                
            if debut:
                if i[0:5]=="State":
                    print(Style.RESET_ALL)
                    print(color[index_color])
                    index_color +=1
                print(i,end="")
                for _ in range(space[index_space]-len(i)):
                    print(" ",end="")
                print(": ",self.All_Variable[i],end="")
                for _ in range(6-len(str(self.All_Variable[i]))):
                    print(" ",end="")
                print(end="| ")
                index_space+=1
                if index_space==5:
                    index_space=0
            if i == "Speed":
                print()
            if i=="statu":
                print(Style.RESET_ALL)
                return

    def afficher_element(self):#ameliorer la fonction
        self.afficher_state()
        space = 16
        pause = True
        for i in self.All_Variable.keys():  
            if i=="State Base HP":
                pause=False
            if pause:  
                print(i," :",end="")
                for _ in range(space-len(i)):
                        print(" ",end="")
                if i == "competence":
                    for j in range(len(self.All_Variable[i])):#pour les compétence
                        if j!=len(self.All_Variable[i])-1:
                            print(j,". ",self.All_Variable[i][j].Name,end=" | ")
                        else:
                            print(j,". ",self.All_Variable[i][j].Name)
                else:
                    print(self.All_Variable[i])
            if i=="Speed":
                pause = True

    def update(self):
        self.HP_full = Calcule_State_HP(self.State_Base_HP,self.IV_HP,self.EV_HP,self.Level)          #HP_MAX -> point de vie max
        self.Attack_full = Calcule_Sate(self.State_Base_Attack,self.IV_Att,self.EV_Att,self.Level)  #Attack physique max
        self.AttackSPE_full =Calcule_Sate(self.State_Base_AttackSPE,self.IV_AttSPE,self.EV_AttSPE,self.Level)
        self.Defense_full = Calcule_Sate(self.State_Base_Def,self.IV_Def,self.EV_Def,self.Level)
        self.DefenseSPE_full =Calcule_Sate(self.State_Base_DefSPE,self.IV_DefSPE,self.EV_DefSPE,self.Level)
        self.Speed_full = Calcule_Sate(self.State_Base_Speed,self.IV_Speed,self.EV_Speed,self.Level)
        #########################################################################""
        self.All_Variable["HP full"] = self.HP_full
        self.All_Variable["Attack full"] = self.Attack_full
        self.All_Variable["AttackSPE full"] = self.AttackSPE_full
        self.All_Variable["Defense full"] = self.Defense_full
        self.All_Variable["DefenseSPE full"] = self.DefenseSPE_full
        self.All_Variable["Speed full"] = self.Speed_full
########################################################################################################### Utiliser pour le combat
        self.HP=self.HP_full                 #HP actuel
        self.Attack = self.Attack_full
        self.AttackSPE =self.AttackSPE_full
        self.Defense = self.Defense_full
        self.DefenseSPE = self.DefenseSPE_full
        self.Speed = self.Speed_full
        #########################################################################""
        self.All_Variable["HP"] = self.HP
        self.All_Variable["Attack"] = self.Attack
        self.All_Variable["AttackSPE"] = self.AttackSPE
        self.All_Variable["Defense"] = self.Defense
        self.All_Variable["DefenseSPE"] = self.DefenseSPE
        self.All_Variable["Speed"] = self.Speed
            
    def gain_Exp(self,EXP_Gagner):
        if self.Level==100:
            return
        self.Exp += EXP_Gagner
        while self.Exp >= self.Level*0.07:
            a=self.Level
            print("Votre Pokemon Monte de Niveau Felicitation ces state augmente de ",a," --> ",a+1," Niveau")
            self.Level += 1
            self.EV_Make()
            self.apprendre_competence()
            self.update()
            if self.Level==100 :
                self.Level=100
                self.All_Variable["Level"] = self.Level
                self.Exp =0
                self.All_Variable["Experience"] = self.Exp
                print("Votre Pokemon qui s'apelle ",self.name," a atteint son niveaux max bravo !!!")
                return
            self.Exp -= a*0.07
            self.All_Variable["Level"] = self.Level
            self.All_Variable["Experience"] = self.Exp

    def IV_Make(self):
        self.IV_HP = random.randint(0,31)
        self.IV_Att = random.randint(0,31)
        self.IV_AttSPE = random.randint(0,31)
        self.IV_Def = random.randint(0,31)
        self.IV_DefSPE = random.randint(0,31)
        self.IV_Speed = random.randint(0,31)
        ###################################################""
        self.All_Variable["IV HP"] = self.IV_HP
        self.All_Variable["IV Att"]= self.IV_Att
        self.All_Variable["IV AttSPE"]= self.IV_AttSPE
        self.All_Variable["IV Def"]= self.IV_Def
        self.All_Variable["IV DefSPE"]=self.IV_DefSPE
        self.All_Variable["IV Speed"]=self.Speed
        self.update()

    def EV_Make(self):
        self.EV -=6
        choix_de_la_state = random.randint(1,6)
        if choix_de_la_state == 1 :
            if self.EV_HP == 294:
                self.EV += 6
                self.EV_Make()
            self.EV_HP += 6
            self.All_Variable["EV HP"]=self.EV_HP
        elif choix_de_la_state == 2 :
            if self.EV_Att == 294:
                self.EV += 6
                self.EV_Make()
            self.EV_Att += 6
            self.All_Variable["EV Att"]= self.EV_Att
        elif choix_de_la_state == 3 :
            if self.EV_AttSPE == 294:
                self.EV += 6
                self.EV_Make()
            self.EV_AttSPE += 6
            self.All_Variable["EV AttSPE"]= self.EV_AttSPE
        elif choix_de_la_state == 4 :
            if self.EV_Def == 294:
                self.EV += 6
                self.EV_Make()
            self.EV_Def += 6
            self.All_Variable["EV Def"] = self.EV_Def
        elif choix_de_la_state == 5 :
            if self.EV_DefSPE == 294:
                self.EV += 6
                self.EV_Make()
            self.EV_Def += 6
            self.All_Variable["EV DefSPE"] = self.EV_DefSPE
        elif choix_de_la_state == 6 :
            if self.EV_Speed == 294:
                self.EV += 6
                self.EV_Make()
            self.EV_Def += 6
            self.All_Variable["EV Speed"] = self.EV_Speed

    def Make_Level(self,Level):
        for _ in range(Level-self.Level):
            self.EV_Make()
        self.Level = Level
        self.apprendre_competence()
        self.All_Variable["Level"] = self.Level
        self.update()
    
    def Changement_de_Cran(self,state,changement):
        if state ==  "Attaque" :
            self.Cran_Attack +=changement
            if self.Cran_Attack >=6:
                self.Cran_Attack = 6
                print("Les States d'attaque son boosté en max")
            elif self.Cran_Attack <=-6:
                self.Cran_Attack = -6
                print("Les States d'attaque son diminuer au maximume")
        elif state == "AttaqueSPE":
            self.Cran_AttackSPE += changement
            if self.Cran_AttackSPE >=6:
                self.Cran_AttackSPE = 6
                print("Les States d'attaque spécial son boosté en max")
            elif self.Cran_AttackSPE <=-6:
                self.Cran_AttackSPE = -6
                print("Les States d'attaque spécial son diminuer au maximume")
        elif state == "Defense":
            self.Cran_Defense += changement
            if self.Cran_Defense >=6:
                self.Cran_Defense = 6
                print("Les States de défense  boosté en max")
            elif self.Cran_Defense <=-6:
                self.Cran_Defense = -6
                print("Les States de défense son diminuer au maximume")
        elif state == "DefenseSPE":
            self.Cran_DefenseSPE += changement
            if self.Cran_DefenseSPE >=6:
                self.Cran_DefenseSPE = 6
                print("Les States de défense spécial son boosté en max")
            elif self.Cran_DefenseSPE <=-6:
                self.Cran_DefenseSPE = -6
                print("Les States de défense spécial son diminuer au maximume")
        elif state == "Speed":
            self.Cran_Speed += changement
            if self.Cran_Speed >=6:
                self.Cran_Speed = 6
                print("Les States de vitesse son boosté en max")
            elif self.Cran_Speed <=-6:
                self.Cran_Speed = -6
                print("Les States de vitesse son diminuer au maximume")
        elif state == "Esquive":
            self.Cran_Esquive += changement
            if self.Cran_Esquive >=6:
                self.Cran_Esquive = 6
                print("Les States d'esquive son boosté en max")
            elif self.Cran_Esquive <=-6:
                self.Cran_Esquive = -6
                print("Les States d'esquie son diminuer au maximume")
        elif state == "Precision":
            self.Cran_Precision += changement
            if self.Cran_Precision >=6:
                self.Cran_Precision = 6
                print("Les States de précision son boosté en max")
            elif self.Cran_Precision <=-6:
                self.Cran_Precision = -6
                print("Les States de précision son diminuer au maximume")
        else:
            print("tu as selectioner une mauvaise state")
        self.Changement_de_State()
    
    def Changement_de_State(self):
        self.Attack = self.Attack_full * Liste_de_Cran[self.Cran_Attack+6]
        self.AttackSPE =self.AttackSPE_full * Liste_de_Cran[self.Cran_AttackSPE+6]
        self.Defense = self.Defense_full * Liste_de_Cran[self.Cran_Defense+6]
        self.DefenseSPE =self.DefenseSPE_full*Liste_de_Cran[self.Cran_DefenseSPE+6]
        self.Speed = self.Speed_full * Liste_de_Cran[self.Cran_Speed+6]
        self.Esquive = 100 * Liste_de_Cran_Esquive_Precision[self.Cran_Esquive+6]
        self.Precision = 100 * Liste_de_Cran_Esquive_Precision[self.Cran_Precision+6]
                #########################################################################""
        self.All_Variable["Attack"] = self.Attack
        self.All_Variable["AttackSPE"] = self.AttackSPE
        self.All_Variable["Defense"] = self.Defense
        self.All_Variable["DefenseSPE"] = self.DefenseSPE
        self.All_Variable["Speed"] = self.Speed
    
    def Fin_de_Combat(self,option=None):
        if option != None:
            if self.Cran_Attack < 0:
                self.Cran_Attack = 0
            if self.Cran_AttackSPE < 0:
                self.Cran_AttackSPE = 0
            if self.Cran_Defense < 0:
                self.Cran_Defense = 0
            if self.Cran_DefenseSPE < 0:
                self.Cran_DefenseSPE = 0
            if self.Cran_Esquive < 0:
                self.Cran_Esquive = 0   
            if self.Cran_Precision < 0:
                self.Cran_Precision = 0   
            if self.Cran_Speed < 0:
                self.Cran_Speed = 0    
        else:
            self.Cran_Attack = 0
            self.Cran_AttackSPE = 0
            self.Cran_Defense = 0
            self.Cran_DefenseSPE = 0
            self.Cran_Esquive = 0
            self.Cran_Precision = 0
            self.Cran_Speed = 0
        #####################################
        self.Attack = self.Attack_full * Liste_de_Cran[self.Cran_Attack+6]
        self.AttackSPE =self.AttackSPE_full * Liste_de_Cran[self.Cran_AttackSPE+6]
        self.Defense = self.Defense_full * Liste_de_Cran[self.Cran_Defense+6]
        self.DefenseSPE =self.DefenseSPE_full*Liste_de_Cran[self.Cran_DefenseSPE+6]
        self.Speed = self.Speed_full * Liste_de_Cran[self.Cran_Speed+6]
        self.Esquive = 100 * Liste_de_Cran_Esquive_Precision[self.Cran_Esquive+6]
        self.Precision = 100 * Liste_de_Cran_Esquive_Precision[self.Cran_Precision+6]
        self.statu = None
                #########################################################################""
        self.All_Variable["Attack"] = self.Attack
        self.All_Variable["AttackSPE"] = self.AttackSPE
        self.All_Variable["Defense"] = self.Defense
        self.All_Variable["DefenseSPE"] = self.DefenseSPE
        self.All_Variable["Speed"] = self.Speed
        self.All_Variable["statu"] = self.statu
        ###################################################"""""""""""""""""""
        if option == None:
            for i in self.competence:
                i.BonusCritique = False
#######################################################################"
    def Barre_HP(self):
        Barre = ""
        Nombre_de_barre = (self.HP * 20) / self.HP_full
        Nombre_de_barre = math.ceil(Nombre_de_barre)
        for _ in range (int(Nombre_de_barre)) :
            Barre += "-"
        for i in self.Type:
            print(i,end=" | ")
        print(Fore.LIGHTCYAN_EX+"NIV ",self.Level,Style.RESET_ALL)
        print(self.name,end=": ")
        blabla = ""
        if self.statu != None:
            blabla= self.statu.name
        if Nombre_de_barre<=0:
            return "D"
        elif Nombre_de_barre <= 5 :
            print(Fore.RED+Barre+Style.RESET_ALL+" "+blabla)
            return "L"
        elif Nombre_de_barre <= 10 :
            print(Barre+" "+blabla)
            return "MI"
        else :
            print(Fore.GREEN + Barre + Style.RESET_ALL+" "+blabla)
            return "MA"

    def All_Mouv(self):
        max = 0
        for j in self.competence:
            if len(j.name)>max:
                max = len(j.name)
        for i in range (4):
            if i<len(self.competence):
                print("ID:",i+1," . ",self.competence[i].name,end="")
                for _ in range(max-len(self.competence[i].name)):
                    print(end=" ")
                print("| PP : ",self.competence[i].PP," | ",self.competence[i].Type)
            else:
                print("ID:",i+1," .")

    def New_Pokemon_same_espece(self):
        a=Pokemon(self.name,self.Type,self.competence,self.sauvage,self.HP,self.Attack,self.Defense,self.AttackSPE,self.DefenseSPE,self.Speed,self.Taux_De_Capture)
        a.IV_Make()
        return a

    def apprendre_competence(self):
        if self.NewAbility == None:
            return
        for i in range(self.Level):
            if has_key(self.NewAbility,i):
                if len(self.competence) <4:
                    self.competence.append(self.NewAbility[i])
                    del self.NewAbility[i]
                else:
                    c= random.randint(0,4)
                    if c!=4:
                        self.competence[c] = self.NewAbility[i]
                        del self.NewAbility[i]
                    else:
                        del self.NewAbility[i]
    def Evolution(self):
        if self.Next_Evolution != None:
            if self.Level>=self.Next_Evolution[0]:
                if self.name ==self.Espece:
                    self.name = self.Next_Evolution[1].name
                self.Espece = self.Next_Evolution[1].Espece
                self.HP_full = self.Next_Evolution[1].HP_full
                self.HP = self.HP_full
                self.State_Base_Attack = self.Next_Evolution[1].State_Base_Attack
                self.State_Base_AttackSPE = self.Next_Evolution[1].State_Base_AttackSPE
                self.State_Base_Def = self.Next_Evolution[1].State_Base_Def
                self.State_Base_DefSPE = self.Next_Evolution[1].State_Base_DefSPE
                self.State_Base_Speed = self.Next_Evolution[1].State_Base_Speed
                self.Type = self.Next_Evolution[1].Type
                self.Next_Evolution = self.Next_Evolution[1].Next_Evolution
                self.update()

def has_key(Dic,key):
    for i in Dic.keys():
        if i == key:
            return True
    return False



###################CREATION POKEMON

def attaque_aleatoire():
    L=[]
    for i in range(4):
        c = Mouv_Class.AllCompetence[random.randint(0,len(Mouv_Class.AllCompetence)-1)]
        # print(c)
        # sleep(3)
        c=c[random.randint(0,len(c)-1)]
        # print(c)
        # sleep(3)
        if L ==[]:
            L.append(c.Newattaque())
        else:
            while Mouv_Class.alreadyHer(c,L):
                c = Mouv_Class.AllCompetence[random.randint(0,len(Mouv_Class.AllCompetence)-1)]
                c = c[random.randint(0,len(c)-1)]
            L.append(c.Newattaque())
    return L
###########Normal
Persian = Pokemon('Persian',["Normal"],[Mouv_Class.Griffe.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,65,70,60,65,65,115,90,{12:Mouv_Class.Morsure.Newattaque(),17:Mouv_Class.Jackpot.Newattaque(),24:Mouv_Class.CombotGriffe.Newattaque(),44:Mouv_Class.Tranche.Newattaque()},None)
Miaouss = Pokemon("Miaouss",["Normal"],[Mouv_Class.Griffe.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,40,45,35,40,40,90,255,{12:Mouv_Class.Morsure.Newattaque(),17:Mouv_Class.Jackpot.Newattaque(),24:Mouv_Class.CombotGriffe.Newattaque(),44:Mouv_Class.Tranche.Newattaque()},(15,Persian.New_Pokemon_same_espece()))
###########FEUX
Dracaufeu = Pokemon("Dracaufeu",["Feu","Vol"],[Mouv_Class.Griffe.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,78,84,78,109,85,100,45,{9:Mouv_Class.flameche.Newattaque(),15:Mouv_Class.GrozYeux.Newattaque(),30:Mouv_Class.Tranche.Newattaque(),38:Mouv_Class.LanceFlammes.Newattaque()},None)
Reptincel  = Pokemon('Reptincel',["Feu"],[Mouv_Class.Griffe.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,58,64,58,80,65,80,45,{9:Mouv_Class.flameche.Newattaque(),15:Mouv_Class.GrozYeux.Newattaque(),30:Mouv_Class.Tranche.Newattaque(),38:Mouv_Class.LanceFlammes.Newattaque()},(30,Dracaufeu.New_Pokemon_same_espece()))
Salameche = Pokemon("Salameche",["Feu"],[Mouv_Class.Griffe.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,39,52,43,60,50,65,45,{9:Mouv_Class.flameche.Newattaque(),15:Mouv_Class.GrozYeux.Newattaque(),30:Mouv_Class.Tranche.Newattaque(),38:Mouv_Class.LanceFlammes.Newattaque()},(15,Reptincel.New_Pokemon_same_espece()))
###########EAU
Tortank = Pokemon("Tortank",["Eau"],[Mouv_Class.charge.Newattaque(),Mouv_Class.MimiQueue.Newattaque()],True,79,83,100,85,105,78,45,{8:Mouv_Class.Ecume.Newattaque(),15:Mouv_Class.PistoletO.Newattaque(),22:Mouv_Class.Morsure.Newattaque(),28:Mouv_Class.Repli.Newattaque(),35:Mouv_Class.CoudKrane.Newattaque(),42:Mouv_Class.HydroCanon.Newattaque()},None)
Carabaffe = Pokemon("Carabaffe",["Eau"],[Mouv_Class.charge.Newattaque(),Mouv_Class.MimiQueue.Newattaque()],True,59,63,80,65,80,58,45,{8:Mouv_Class.Ecume.Newattaque(),15:Mouv_Class.PistoletO.Newattaque(),22:Mouv_Class.Morsure.Newattaque(),28:Mouv_Class.Repli.Newattaque(),35:Mouv_Class.CoudKrane.Newattaque(),42:Mouv_Class.HydroCanon.Newattaque()},(30,Tortank.New_Pokemon_same_espece()))
Carapuce = Pokemon("Carapuce",["Eau"],[Mouv_Class.charge.Newattaque(),Mouv_Class.MimiQueue.Newattaque()],True,44,48,65,50,64,43,44,{8:Mouv_Class.Ecume.Newattaque(),15:Mouv_Class.PistoletO.Newattaque(),22:Mouv_Class.Morsure.Newattaque(),28:Mouv_Class.Repli.Newattaque(),35:Mouv_Class.CoudKrane.Newattaque(),42:Mouv_Class.HydroCanon.Newattaque()},(15,Carabaffe))
########### Plante
Florizarre = Pokemon("Florizarre",["Plante","Poison"],[Mouv_Class.charge.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,80,82,83,100,100,80,45,{7:Mouv_Class.Vampigraine.Newattaque(),13:Mouv_Class.FouetLianes.Newattaque(),20:Mouv_Class.PoudreToxique.Newattaque(),27:Mouv_Class.TrancheHerbe.Newattaque(),41:Mouv_Class.PoudreDodo.Newattaque()},None)
Herbizarre = Pokemon("Herbizarre",["Plante","Poison"],[Mouv_Class.charge.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,60,62,63,80,80,60,45,{7:Mouv_Class.Vampigraine.Newattaque(),13:Mouv_Class.FouetLianes.Newattaque(),20:Mouv_Class.PoudreToxique.Newattaque(),27:Mouv_Class.TrancheHerbe.Newattaque(),41:Mouv_Class.PoudreDodo.Newattaque()},(30,Florizarre.New_Pokemon_same_espece()))
Bulbizarre = Pokemon("Bulbizarre",["Plante","Poison"],[Mouv_Class.charge.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,45,49,49,65,65,45,45,{7:Mouv_Class.Vampigraine.Newattaque(),13:Mouv_Class.FouetLianes.Newattaque(),20:Mouv_Class.PoudreToxique.Newattaque(),27:Mouv_Class.TrancheHerbe.Newattaque(),41:Mouv_Class.PoudreDodo.Newattaque()},(30,Herbizarre.New_Pokemon_same_espece()))
########## "Électrik"

Raichu = Pokemon("Raichu",["Électrik"],[Mouv_Class.Eclair.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,60,90,55,90,80,110,75,{9:Mouv_Class.CageEclaire.Newattaque(),16:Mouv_Class.Vive_attaque.Newattaque(),26:Mouv_Class.Meteor.Newattaque(),33:Mouv_Class.hate.Newattaque(),43:Mouv_Class.FatalFoudre.Newattaque()},None)
Pikachu = Pokemon("Pikachu",["Électrik"],[Mouv_Class.Eclair.Newattaque(),Mouv_Class.rugissement.Newattaque()],True,35,55,40,50,50,90,190,{9:Mouv_Class.CageEclaire.Newattaque(),16:Mouv_Class.Vive_attaque.Newattaque(),26:Mouv_Class.Meteor.Newattaque(),33:Mouv_Class.hate.Newattaque(),43:Mouv_Class.FatalFoudre.Newattaque()},(20,Raichu.New_Pokemon_same_espece()))# print(str(type(Pikachu))== "<class '__main__.Pokemon'>")
##########"Glace"
Lokhlass = Pokemon("Lokhlass",["Glace","Eau"],[Mouv_Class.PistoletO.Newattaque(),Mouv_Class.rugissement.Newattaque],True,130,85,80,85,95,60,45,{16:Mouv_Class.Berceuse.Newattaque(),20:Mouv_Class.Brume.Newattaque(),25:Mouv_Class.Plaquage.Newattaque(),31:Mouv_Class.OndeFolie.Newattaque(),38:Mouv_Class.LaserGlace.Newattaque(),46:Mouv_Class.HydroCanon.Newattaque()},None)
##########""Combat"
Mackogneur = Pokemon("Mackogneur",["Combat"],[Mouv_Class.PoingKarate.Newattaque(),Mouv_Class.CoupdBoule.Newattaque()],True,90,130,80,65,85,55,45,{25:Mouv_Class.GrozYeux.Newattaque(),32:Mouv_Class.Puissance.Newattaque(),39:Mouv_Class.FrappeAtlas.Newattaque(),46:Mouv_Class.Sacrifice.Newattaque()},None)
Machopeur = Pokemon("Machopeur",["Combat"],[Mouv_Class.PoingKarate.Newattaque(),Mouv_Class.CoupdBoule.Newattaque()],True,80,100,70,50,60,45,90,{25:Mouv_Class.GrozYeux.Newattaque(),32:Mouv_Class.Puissance.Newattaque(),39:Mouv_Class.FrappeAtlas.Newattaque(),46:Mouv_Class.Sacrifice.Newattaque()},(30,Mackogneur.New_Pokemon_same_espece()))
Machoc = Pokemon("Machoc",["Combat"],[Mouv_Class.PoingKarate.Newattaque(),Mouv_Class.CoupdBoule.Newattaque()],True,70,80,50,35,35,35,180,{25:Mouv_Class.GrozYeux.Newattaque(),32:Mouv_Class.Puissance.Newattaque(),39:Mouv_Class.FrappeAtlas.Newattaque(),46:Mouv_Class.Sacrifice.Newattaque()},(15,Machopeur.New_Pokemon_same_espece()))
##########""Poison"
Smogogo = Pokemon("Smogogo",["Poison"],[Mouv_Class.charge.Newattaque(),Mouv_Class.Puredpois.Newattaque()],True,65,90,120,85,70,60,60,{10:Mouv_Class.Detritus.Newattaque(),20:Mouv_Class.Jetsable.Newattaque(),30:Mouv_Class.Destruction.Newattaque,35:Mouv_Class.Brume.Newattaque(),50:Mouv_Class.Explosion.Newattaque()},None)
Smogo = Pokemon("Smogo",["Poison"],[Mouv_Class.charge.Newattaque(),Mouv_Class.Puredpois.Newattaque()],True,40,65,95,60,45,35,190,{10:Mouv_Class.Detritus.Newattaque(),20:Mouv_Class.Jetsable.Newattaque(),30:Mouv_Class.Destruction.Newattaque,35:Mouv_Class.Brume.Newattaque(),50:Mouv_Class.Explosion.Newattaque()},(20,Smogogo.New_Pokemon_same_espece()))
##########""Vol"
Roucarnage = Pokemon("Roucarnage",["Vol","Normal"],[Mouv_Class.Tornade.Newattaque()],True,83,80,75,70,70,101,45,{5:Mouv_Class.Jetsable.Newattaque(),12:Mouv_Class.Vive_attaque.Newattaque(),19:Mouv_Class.CruAile.Newattaque(),28:Mouv_Class.hate.Newattaque()},None)
Roucoups  = Pokemon("Roucoups",["Vol","Normal"],[Mouv_Class.Tornade.Newattaque()],True,63,60,55,50,50,71,120,{5:Mouv_Class.Jetsable.Newattaque(),12:Mouv_Class.Vive_attaque.Newattaque(),19:Mouv_Class.CruAile.Newattaque(),28:Mouv_Class.hate.Newattaque()},(30,Roucarnage.New_Pokemon_same_espece()))
Roucool = Pokemon("Roucool",["Vol","Normal"],[Mouv_Class.Tornade.Newattaque()],True,40,45,40,35,35,56,255,{5:Mouv_Class.Jetsable.Newattaque(),12:Mouv_Class.Vive_attaque.Newattaque(),19:Mouv_Class.CruAile.Newattaque(),28:Mouv_Class.hate.Newattaque()},(15,Roucoups.New_Pokemon_same_espece()))
##########""Psy"
Flagadoss = Pokemon("Flagadoss",["Eau","Psy"],[Mouv_Class.Chocmental.Newattaque(),Mouv_Class.charge.Newattaque()],True,95,75,110,100,80,30,75,{22:Mouv_Class.CoupdBoule.Newattaque(),27:Mouv_Class.rugissement.Newattaque(),33:Mouv_Class.PistoletO.Newattaque(),40:Mouv_Class.Amnesie.Newattaque(),48:Mouv_Class.Psyko.Newattaque()},None)
Ramoloss = Pokemon("Ramoloss",["Eau","Psy"],[Mouv_Class.Chocmental.Newattaque(),Mouv_Class.charge.Newattaque()],True,90,65,65,40,40,15,190,{22:Mouv_Class.CoupdBoule.Newattaque(),27:Mouv_Class.rugissement.Newattaque(),33:Mouv_Class.PistoletO.Newattaque(),40:Mouv_Class.Amnesie.Newattaque(),48:Mouv_Class.Psyko.Newattaque()},(15,Flagadoss.New_Pokemon_same_espece()))
##########""Insect"
Papilusion= Pokemon("Papilusion ",["Insecte","Vol"],[Mouv_Class.Secretation.Newattaque(),Mouv_Class.charge.Newattaque(),Mouv_Class.Repli.Newattaque()],True,60,45,50,90,80,70,45,{31:Mouv_Class.Chocmental.Newattaque(),32:Mouv_Class.PoudreToxique.Newattaque(),33:Mouv_Class.CageEclaire},None)
Chrysacier = Pokemon("Chrysacier",["Insecte"],[Mouv_Class.Secretation.Newattaque(),Mouv_Class.charge.Newattaque(),Mouv_Class.Repli.Newattaque()],True,50,20,55,25,25,30,120,{31:Mouv_Class.Chocmental.Newattaque(),32:Mouv_Class.PoudreToxique.Newattaque(),33:Mouv_Class.CageEclaire},(30,Papilusion.New_Pokemon_same_espece()))
Chenipan = Pokemon("Chenipan",["Insect"],[Mouv_Class.Secretation.Newattaque(),Mouv_Class.charge.Newattaque(),Mouv_Class.Repli.Newattaque()],True,45,30,35,20,20,45,255,{31:Mouv_Class.Chocmental.Newattaque(),32:Mouv_Class.PoudreToxique.Newattaque(),33:Mouv_Class.CageEclaire},(15,Chrysacier.New_Pokemon_same_espece()))
##########""Roche"

Grolem = Pokemon("Grolem",["Sol","Roche"],[Mouv_Class.charge.Newattaque(),Mouv_Class.Repli.Newattaque()],True,80,120,130,55,65,45,45,{16:Mouv_Class.JetPierre.Newattaque(),21:Mouv_Class.Destruction.Newattaque(),31:Mouv_Class.Seisme.Newattaque(),36:Mouv_Class.Explosion.Newattaque()},None)
Gravalanch = Pokemon("Gravalanch",["Sol","Roche"],[Mouv_Class.charge.Newattaque(),Mouv_Class.Repli.Newattaque()],True,55,95,115,45,45,35,120,{16:Mouv_Class.JetPierre.Newattaque(),21:Mouv_Class.Destruction.Newattaque(),31:Mouv_Class.Seisme.Newattaque(),36:Mouv_Class.Explosion.Newattaque()},(30,Grolem.New_Pokemon_same_espece()))
Racaillou = Pokemon("Racaillou",["Roche","Sol"],[Mouv_Class.charge.Newattaque(),Mouv_Class.Repli.Newattaque()],True,40,80,100,30,30,20,255,{16:Mouv_Class.JetPierre.Newattaque(),21:Mouv_Class.Destruction.Newattaque(),31:Mouv_Class.Seisme.Newattaque(),36:Mouv_Class.Explosion.Newattaque()},(15,Gravalanch.New_Pokemon_same_espece()))
##########""Spectre"
Ectoplasma =Pokemon("Ectoplasma",["Spectre","Poison"],[Mouv_Class.Lechouille.Newattaque(),Mouv_Class.Psyko.Newattaque(),Mouv_Class.Hypnose.Newattaque(),Mouv_Class.Detritus.Newattaque()],True,60,65,60,130,75,110,45,None,None)
Spectrum= Pokemon("Spectrum",["Spectre","Poison"],[Mouv_Class.Lechouille.Newattaque(),Mouv_Class.Psyko.Newattaque(),Mouv_Class.Hypnose.Newattaque(),Mouv_Class.Detritus.Newattaque()],True,45,50,45,115,55,95,90,None,(30,Ectoplasma.New_Pokemon_same_espece()))
Fantominus=Pokemon("Fantominus",["Spectre","Poison"],[Mouv_Class.Lechouille.Newattaque(),Mouv_Class.Psyko.Newattaque(),Mouv_Class.Hypnose.Newattaque(),Mouv_Class.Detritus.Newattaque()],True,30,35,30,100,35,80,190,None,(15,Spectrum.New_Pokemon_same_espece()))
######################" TEST IV "
# Pikachu.afficher_state()
# Pikachu.IV_Make()
# print("____________________________________\napres : ")
# Pikachu.afficher_state()

###########################################################################################"TEST Niveau et EV"
# print("Niveau : ",Pikachu.Level,"  | EXP : ",Pikachu.Exp)
# Pikachu.afficher_state()
# Pikachu.gain_Exp(100)#faire une fonction qui fait la monter des Niveau
# print("Niveau : ",Pikachu.Level,"  | EXP : ",Pikachu.Exp)
# Pikachu.afficher_state()

################################################################################### Changement des cran
# Pikachu.afficher_state()
# Pikachu.Changement_de_Cran("Attaque",1)
# Pikachu.afficher_state()

######################################################################################## VERIFICATION DES STATE AJOUT
# Pikachu.afficher_state()
# Mouv_Class.Brule1sur10.update_entity(Pikachu)
# Pikachu.afficher_state()
############################################################################# VERIFICATION DES EFFET DES STATES
# Pikachu.statu = Mouv_Class.Brule1sur10
# Pikachu.afficher_state()
# Pikachu.statu.update_entity(Pikachu)
# Pikachu.afficher_state()
##################################################################"VERIFICATION D4APRENTISSAGE DES NOUVELLE COMPETENCE"
# print(Pikachu.Level)
# for i in Pikachu.competence:
#     print(" : ",i.name)
# print("\n")
# Pikachu.gain_Exp(100)#faire une fonction qui fait la monter des Niveau

# Pikachu.Make_Level(6)
# print(Pikachu.Level)
# for i in Pikachu.competence:
#     print(" : ",i.name)
##################################"" Afficher all pokemon
#crée une liste avec plein plein de pokémon#
def afficher_Liste_Pokemon():
    for i in range (len(Liste_de_Pokemon)):
        print(i," : ",Liste_de_Pokemon[i].name)
#afficher_Liste_Pokemon()
# print()
# Aficher_Matrice_Des_Type()

