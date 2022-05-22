# 
# 
#                This fichier is not important anymore
# 
# 
# 
#ici ou je teste mes class
# import only system from os
from os import system, name
from re import A
# import sleep to show output for some time period
from time import sleep
from colorama import Fore
from colorama import Style
import Dresseur_Class, Pokemon_Class,map_Class,Mouv_Class


#######################################################################################################################################
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
###############################################################################################################################################################
MAX_LIFE="                   _M___M_\n                  /       \\\n                 /  \   /  \\\n    _M____M_    /  °     °  \\\n   /²²¨¨¨¨²²\  /      V      \\\n  /²²¨¨¨¨¨¨²²\/     WWWWW     \\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
MID_LIFE="                   _M___M_\n                  /       \\\n                 /  _     _\\\n    _M____M_    /  °     °  \\\n   /²²¨¨¨¨²²\  /      U      \\\n  /²²¨¨¨¨¨¨²²\/     -----     \\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
LOW_LIFE = "                   _M___M_\n                  /       \\\n                 / /     \ \\\n    _M____M_    /  O    O   \\\n   /²²¨¨¨¨²²\  /      -      \\\n  /²²¨¨¨¨¨¨²²\/     ~~~~~~    \\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
DEAD="                   _M___M_\n                  /       \\\n                 /         \\\n    _M____M_    /  X    X   \\\n   /²²¨¨¨¨²²\  /             \\\n  /²²¨¨¨¨¨¨²²\/     ::::      \\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
CAPTURE_ON="\n                \n            \n    _M____M_    \n   /²²¨¨¨¨²²\        ●\n  /²²¨¨¨¨¨¨²²\\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
CAPTURE_OFF="\n                \n            \n    _M____M_    \n   /²²¨¨¨¨²²\        ❍\n  /²²¨¨¨¨¨¨²²\\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
######################################################################################################################

# ☐ ■
Salameche = Pokemon_Class.Pokemon("Salameche",["Feu"],[Mouv_Class.flameche,Mouv_Class.Griffe,Mouv_Class.rugissement],True,39,52,43,60,50,65,45)
Pikachu = Pokemon_Class.Pokemon("Pikachu",["Électrik"],[Mouv_Class.charge],True,35,55,40,50,50,90,190)
Salameche_du_Joueur = Salameche
Salameche_du_Joueur.IV_Make()
Salameche_du_Joueur.sauvage = False
moi = Dresseur_Class.Dresseur("Yassine",[Salameche_du_Joueur],None)
carte = map_Class.Map(10,10)
############################################################################################################################################################
def cligniotement(map):
    clear()
    max = len(map.town)
    if max < len(map.town[0]):
        max = len(map.town[0])
    jour = " "
    nuit = " "
    for i in range(len(map.town)):
        for j in range(len(map.town[0])):
            if i == j or i+j == max-1:
                jour += "■ "
                nuit += "☐ "
            else :
                jour += "☐ "
                nuit += "■ "
        jour += "\n "
        nuit += "\n "
    for _ in range(4):
        print(nuit)
        sleep(0.5)
        clear()
        print(jour)
        sleep(0.5)
        clear()

def Affichage_du_Duel(P1,P2):
    clear()
    lifeP2 = P2.Barre_HP()
    if lifeP2 == "MA":
        print(MAX_LIFE,end="\n\n")
    elif lifeP2 == "MI":
        print(MID_LIFE,end="\n\n")
    elif lifeP2 == "L":
        print(LOW_LIFE,end="\n\n")
    elif lifeP2 == "D":
        print(Fore.RED+"0"+Style.RESET_ALL)
        print(DEAD,end="\n\n")
    P1.Barre_HP()
    print("__________________________________________________",end="\n\n")
    
def interface_du_Joueur(Joueur,P1):
    print("1. ATTAQUE | 2. EQUIPE \n3. SAC     | 4. FUITE !!!!!")
    action =""
    while action != "1" and action!="2"  and action!="3" and action != "4":
        action = input("QUOI FAIRE !!! : ")
    clear()
    return action

def COMBAT(map,Joueur,Adverser):
    P1 = Joueur.team[0]
    print(map,Joueur,Adverser)
    cligniotement(map)
    if str(type(Adverser)) == "<class 'Pokemon_Class.Pokemon'>" :
        print("Un Pokemon Sauvage !!!!")
        Affichage_du_Duel(P1,Adverser)
        c = interface_du_Joueur(Joueur,P1)
        if c == "1":
            Affichage_du_Duel(P1,Adverser)
            P1.All_Mouv()
            attaque = input("Tu choisi quel attaque ? : ")
    else :
        print("Un Dresseur !! ")
COMBAT(carte,moi,Pikachu)


#Faire les degat 
#aplication d'effet
# le fais de pouvoir utilisé des potion changer de pokemon
#pouvoir utilisé un objet
# et Pouvoir fuire 