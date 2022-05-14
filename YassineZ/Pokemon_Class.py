import colorama
from colorama import Fore
from colorama import Style
import Mouv_Class

colorama.init()
print(Fore.BLUE + Style.BRIGHT + "This is the color of the sky" + Style.RESET_ALL)
print(Fore.GREEN + "This is the color of grass" + Style.RESET_ALL)
print(Fore.BLUE + Style.DIM + "This is a dimmer version of the sky" + Style.RESET_ALL)
print(Fore.YELLOW + "This is the color of the sun" + Style.RESET_ALL)
print(len(Fore.YELLOW+Style.RESET_ALL))
print(len(Fore.BLUE+Style.RESET_ALL))
print(len(Fore.BLUE + Style.DIM +Style.RESET_ALL))
#La classe des pokèmon 
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
        return PV
    
def Calcule_Sate(Base,IV,EV,NIV):
        State = ((2*Base+IV+(EV/4))*NIV)+5
        return State


#definir un pokemon il est composé de quoi comme variable 
class Pokemon:
    def __init__(self,name,Type,competence,sauvage,State_Base_HP,State_Base_Attack,State_Base_Def,State_Base_AttackSPE,State_Base_DefSPE,State_Base_Speed,Taux_De_Capture) :
        self.name = name                #str, nom du pokemon le Joueur peut nommer son pokemon mais il ne peut paschanger ....
        self.Espece = name              #...l'espece du Pokemon fix qui est fixe 
        self.type= Type                 #peut avoir 2 ou 1 type [str]
        self.competence= competence        #peut entre 1 et avoir max 4 Mouv et chaque Mouv à un nombre de pp et un type [ataque]
        self.Level = 1
        self.Exp=0
#Racine des state
        self.State_Base_HP=State_Base_HP
        self.State_Base_Attack=State_Base_Attack
        self.State_Base_AttackSPE =State_Base_AttackSPE
        self.State_Base_Def=State_Base_Def
        self.State_Base_DefSPE = State_Base_DefSPE
        self.State_Base_Speed = State_Base_Speed
##################################################################################################### EV
        self.reste_EV = 510 #252 par state
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
#fin
        self.statu = []
        self.Taux_De_Capture = Taux_De_Capture
        self.Esquive = 100
        self.Precision = 100
        self.dialogue = self.Espece +" "+ self.Espece +" " + self.Espece +" !!!"
        self.sauvage = sauvage  #bool True = il est sauvage , False = il est capturè

    def afficher_element(self):
        All_Variable = {
            "name":self.name,"Espece":self.Espece,"type":self.type,"competence":self.competence,"Niveau":self.Level,
            "State Base HP":self.State_Base_HP,"IV HP":self.IV_HP,"EV HP":self.EV_HP,"HP full":self.HP_full,"HP":self.HP,
            "State base Attack":self.State_Base_Attack,"IV Att":self.IV_Att,"EV Att":self.EV_Att,"Attack full":self.Attack_full,"Attack":self.Attack,
            "State base AttackSPE":self.State_Base_AttackSPE,"IV AttSPE":self.IV_AttSPE,"EV AttSPE":self.EV_AttSPE,"AttackSPE full":self.AttackSPE_full,"AttackSPE":self.AttackSPE,
            "State base Def":self.State_Base_Def,"IV Def":self.IV_Def,"EV Def":self.EV_Def,"Defense full":self.Defense_full,"Defense":self.Defense,
            "State base DefSPE":self.State_Base_DefSPE,"IV DefSPE":self.IV_DefSPE,"EV DefSPE":self.EV_DefSPE,"DefenseSPE full":self.DefenseSPE_full,"DefenseSPE":self.DefenseSPE,
            "State base Speed":self.State_Base_Speed,"IV Speed":self.IV_Speed,"EV Speed":self.EV_Speed,"Speed full":self.Speed_full,"Speed":self.Speed,
            "statu":self.statu,"Taux De Capture":self.Taux_De_Capture,"Esquive":self.Esquive,"Precision":self.Precision,"dialogue":self.dialogue,"sauvage":self.sauvage
        }
        space = 16
        tour=-1
        debut=True
        for i in All_Variable.keys():
            if i == "State Base HP" or tour>=0:
                if tour==-1:
                    tour=6*5
                
                if tour%5==0:
                    if not(debut):
                        # if tour==30:
                        #     print(Fore.BLUE,end="")
                        # else:
                        #     print(Fore.RED)
                        print("")
                        print("  EH dffgpb,prgbpojernj georbtepirzfnboeguOH")
                        debut=False
                    else:
                        if tour!=0:
                            print("")
                            print("  |",i," : ",All_Variable[i],end="")
                        else:
                            print(" ")
                        # print(Style.RESET_ALL)
                        debut=True
                        
                else:
                    print(" | ",i," : ",All_Variable[i],end=" ")
                        
                tour=tour-1
            else:
                print(i," :",end="")
                for _ in range(space-len(i)):
                    print(" ",end="")
                if i == "competence":
                    for j in range(len(All_Variable[i])):
                        if j!=len(All_Variable[i])-1:
                            print(j,". ",All_Variable[i][j].Name,end=" | ")
                        else:
                            print(j,". ",All_Variable[i][j].Name)
                else:
                    print(All_Variable[i])

#crée une liste avec plein plein de pokémon#
Pikachu = Pokemon("Pikachu",["Électrik"],[Mouv_Class.charge],False,35,55,40,50,50,90,255)#A remplir
Pikachu.afficher_element()
