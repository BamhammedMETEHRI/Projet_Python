import colorama
from colorama import Fore
from colorama import Style

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

class Pokemon:
    def __init__(self,name,Type,ability,sauvage,HP_full,Attack_full,Def_full,AttackSPE_full,DefenseSPE_full,Speed_full,Taux_De_Capture) :
        self.name = name                #str, nom du pokemon le Joueur peut nommer son pokemon mais il ne peut paschanger ....
        self.Espece = name              #...l'espece du Pokemon fix qui est fixe 
        self.type= Type                 #peut avoir 2 ou 1 type [str]
        self.compétence= ability             #peut entre 1 et avoir max 4 attack et chaque attack à un nombre de pp et un type [ataque]
#state
        self.HP_full = HP_full          #HP_MAX -> point de vie max
        self.Attack_full = Attack_full  #Attack physique max
        self.AttackSPE_full =AttackSPE_full
        self.Defense_full = Def_full
        self.DefenseSPE_full =DefenseSPE_full
        self.Speed_full = Speed_full
        self.HP=HP_full                 #HP actuel
        self.Attack = Attack_full
        self.Defense = Def_full
        self.AttackSPE =AttackSPE_full
        self.DefenseSPE = DefenseSPE_full
        self.Speed = Speed_full
#fin
        self.Taux_De_Capture = Taux_De_Capture
        self.Esquive = 1000
        self.Precision = 1000
        self.Level = 0
        self.Exp=0
        self.dialogue = self.Espece + self.Espece + self.Espece +" !!!"
        self.sauvage = sauvage  #bool True = il est sauvage , False = il est capturè

#crée une liste avec plein plein de pokémon#