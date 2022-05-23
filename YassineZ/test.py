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
import random
# import sleep to show output for some time period
from time import sleep
from colorama import Fore
from colorama import Style
import Dresseur_Class, Pokemon_Class,map_Class,Mouv_Class,Item_Class


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
    lifeP1 = P1.Barre_HP()
    if lifeP1 == "D":
        print(Fore.RED+"0"+Style.RESET_ALL)
    print("__________________________________________________",end="\n\n")
    
def interface_du_Joueur(P1,P2):
    action =0
    while True:
        try :
            print("1. ATTAQUE | 2. EQUIPE \n3. SAC     | 4. FUITE !!!!!")
            action = int(input("QUOI FAIRE !!! : "))
            if action >=1 and action<=4:
                clear()
                return action
        except ValueError:
            clear()
            Affichage_du_Duel(P1,P2)



def Joueur_choix(Joueur,Adverser,P1,P2=None):
    if P2 == None:
        Affichage_du_Duel(P1,Adverser)
        c = interface_du_Joueur(P1,Adverser)
        if c == 1:
            Affichage_du_Duel(P1,Adverser)
            attaque=0
            while True:
                try :
                    P1.All_Mouv()
                    print("0 pour retourner en arrier ")
                    attaque = int(input("QUOI FAIRE !!! : "))
                    if attaque >=0 and attaque<= len(P1.competence):
                        break
                    else: 
                        clear()
                        Affichage_du_Duel(P1,Adverser)
                except ValueError:
                    clear()
                    Affichage_du_Duel(P1,Adverser)
            if attaque == 0:
                clear()

                return Joueur_choix(Joueur,Adverser,P1)
            else:
                P1.competence[attaque-1].PP -=1 
                return P1.competence[attaque-1]
        if c == 2:
            print("Tout t'es pokemon tu peux voire leur attaque et ces point de vie et tu peux changer avec le pokemon qui est sur le terrain")
            sleep(20)
        if c == 3:
            print("tu peux utiliser des objet")
            sleep(20)
        if c == 4:
            print("tu peux fuir un combat ")
            sleep(20)

def IA_Pokemon_Sauvage(Pokemon):
    choix = random.randint(0,len(Pokemon.competence)-1)
    return Pokemon.competence[choix]

def Duel(J1,P1,P2,Choix1,Choix2):
    if P1.Speed >= P2.Speed :
        first = P1
        ChoixFirst = Choix1
        second = P2
        ChoixSecond=Choix2
        print(first.name," commence ")
    else:
        first = P2
        ChoixFirst = Choix2
        second = P1
        ChoixSecond=Choix1
        print(first.name," commence ")
    if type(Choix1) == int:
        print("Tu as voulue Fuire")
    elif type(Choix1) == Item_Class.Item:
        print("Tu as choisi un objet ",Choix1.name)
    else:
        if type(Choix1)== Pokemon_Class.Pokemon:
            print("tu as choisi un pokemon ",Choix1.name)
        clear()
        Affichage_du_Duel(P1,P2)
        if ChoixFirst.toucher(first,second):
            d = ChoixFirst.Calcule_Degat(first,second)
            second.HP -= d
            if second.HP < 0:
                second.HP = 0
                return P1
        sleep(3)
        clear()
        Affichage_du_Duel(P1,P2)
        if ChoixSecond.toucher(second,first):
            d = ChoixSecond.Calcule_Degat(second,first)
            first.HP -= d
            if first.HP < 0:
                first.HP = 0
                return P1
        sleep(3)
        clear()
        Affichage_du_Duel(P1,P2)
        if P1.statu != None:
            P1.statu.update_entity(P1)
            sleep(3)
            clear()
            Affichage_du_Duel(P1,P2)
        if P2.statu != None:
            P2.statu.update_entity(P2)
            sleep(3)
            clear()
            Affichage_du_Duel(P1,P2)
        return P1

def COMBAT(map,Joueur,Adverser):
    P1 = Joueur.team[0]
    print(map,Joueur,Adverser)
    # cligniotement(map)
    if str(type(Adverser)) == "<class 'Pokemon_Class.Pokemon'>" :
        print("Un Pokemon Sauvage !!!!")
        while Joueur.Perdu() and Adverser.HP > 0 and Adverser.sauvage :
                ActionJ1 = Joueur_choix(Joueur,Adverser,P1)
                ActionJ2 = IA_Pokemon_Sauvage(Adverser)
                P1 = Duel(Joueur,P1,Adverser,ActionJ1,ActionJ2)
        clear()
        Affichage_du_Duel(P1,Adverser)
        if not(Joueur.Perdu()):
            print("Dommage Gamme OVER :(")
        else :
            P1.gain_Exp(Adverser.Level)
            print("FIN DU COMBAT")
            for i in Joueur.team:
                i.Fin_de_Combat()
            sleep(4)
            clear()

    else :
        print("Un Dresseur !! ")
Pikachu.statu = Mouv_Class.Brule1sur10
COMBAT(carte,moi,Pikachu)


#Faire les degat 
#aplication d'effet
# le fais de pouvoir utilisé des potion changer de pokemon
#pouvoir utilisé un objet
# et Pouvoir fuire 