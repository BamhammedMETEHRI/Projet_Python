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

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def printFPS(str,time=None):
    if time==None:
        time=1/25
    for i in range(len(str)):
        clear()
        print(str[0:i],end="")
        sleep(time)
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
CAPTURE_FAIL="                   _W___W_\n                  /       \\\n                 /  \\   /  \\\n    _M____M_    /( 0 )-( 0 )\\\n   /²²¨¨¨¨²²\  /   _______   \\\n  /²²¨¨¨¨¨¨²²\/   |V     V|   \\\n /²²¨¨¨¨¨¨¨¨²²\\   \\_^___^_/    \\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
CAPTURE_SUCCES="\n                \n            \n    _M____M_       * *\n   /²²¨¨¨¨²²\      (❍)\n  /²²¨¨¨¨¨¨²²\\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"

######################################################################################################################

# ☐ ■
Salameche = Pokemon_Class.Pokemon("Salameche",["Feu"],[Mouv_Class.flameche,Mouv_Class.Griffe,Mouv_Class.rugissement],True,39,52,43,60,50,65,45)
Pikachu = Pokemon_Class.Pokemon("Pikachu",["Électrik"],[Mouv_Class.charge],True,35,55,40,50,50,90,190)
PKSauvage = Pokemon_Class.Liste_de_Pokemon[random.randint(0,len(Pokemon_Class.Liste_de_Pokemon)-1)].New_Pokemon_same_espece()
Salameche_du_Joueur = Salameche.New_Pokemon_same_espece()
Salameche_du_Joueur.sauvage = False
moi = Dresseur_Class.Joueur("Yassine",[Salameche_du_Joueur])
moi.inventaire.append(Item_Class.potion_normal) 
moi.inventaire.append(Item_Class.pokeball) 
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

def Animation_Capture(nbr):
    for _ in range(nbr+1):
        clear()
        print(CAPTURE_ON)
        sleep(1)
        for _ in range(10):
            clear()
            print(CAPTURE_OFF)
            sleep(1/100)
            clear()
            print(CAPTURE_ON)
            sleep(1/100)
        clear()
        print(CAPTURE_OFF)
        sleep(1/10)

    if nbr<4:
        clear()
        printFPS(CAPTURE_FAIL)
        clear()
        print(CAPTURE_FAIL)
        print("La Capture a Echouer le Pokemon est enerver")
        sleep(3)
        return 0
    else:
        clear()
        printFPS(CAPTURE_SUCCES)
        clear()
        print(CAPTURE_SUCCES)
        print("La Capture est une reussite")
        sleep(3)
        return 1

# Animation_Capture(4)

def Affichage_du_Duel(P1,P2):
    """
    affiche 2 pokemon qui sont entrain de se battre
    """
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
    """
    Menu du joueur avec 4 option 
    1 = affiche les attaque du pokemon
    2= affiche les pokemon et peut changer de place
    3= Le sac et peut utilise des objet pendant le combat
    4= Tu peux Fuire si tu joue contre un pokemon sauvage
    """
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

#####################################################################

def Joueur_choix(Joueur,Adverser,P1,P2=None):
    """
    C'est ici ou le joueur choisi
    j'ai separement pour que le joueur puisse retourne en arriere
    """
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
            clear()
            while True:
                try:
                    for i in range(6):
                        if len(Joueur.team) >i :
                            print("ID.",i+1," ",Joueur.team[i].name)
                        else:
                            print("ID.",i," RIEN")
                    choix_Pokemon = int(input("Quel Pokemon remplacer"))
                    if choix_Pokemon == 0 or Joueur.team[choix_Pokemon-1] ==P1:
                        if Joueur.team[choix_Pokemon-1] ==P1:
                            clear()
                            print("Ce pokemon est deja Sur le terrain")
                            sleep(5)
                        return Joueur_choix(Joueur,Adverser,P1)
                    else :
                        return Joueur.team[choix_Pokemon-1]
                except ValueError:
                    clear()

        if c == 3:
            clear()
            obj = Joueur.selection_Item()
            if obj==0:
                clear()
                return Joueur_choix(Joueur,Adverser,P1)
            else:
                return obj
        if c == 4:
            print("tu peux fuir un combat ")
            return 100


def IA_Pokemon_Sauvage(Pokemon):
    choix = random.randint(0,len(Pokemon.competence)-1)
    return Pokemon.competence[choix]

def Duel(J1,P1,P2,Choix1,Choix2):
############################################ Le plus rapide commence
    Affichage_du_Duel(P1,P2)
    if P1.Speed >= P2.Speed :
        print("TON POKEMON COMMENCE !!")
        first = P1
        ChoixFirst = Choix1
        second = P2
        ChoixSecond=Choix2
    else:
        print("ton pokemon NE COMMENCE PAS !!")
        first = P2
        ChoixFirst = Choix2
        second = P1
        ChoixSecond=Choix1
    sleep(3)
#######################################################""
    if str(type(Choix1))== "<class 'Pokemon_Class.Pokemon'>":
        print("tu as choisi un pokemon ",Choix1.name)
#######################################################
    if str(type(ChoixFirst)) == "<class 'Item_Class.Item'>":
        print("Tu as choisi un objet ",ChoixFirst.name)
        if ChoixFirst.name == "pokeball" :
            r=ChoixFirst.apllicaion_object(second)
            if r >= 0 :
                r = Animation_Capture(r)
                if r == 1 :
                    J1.ajouter_membre(second)
                    clear()
                    P2.Info_Pokemon()
                    return P2
        else:
            ChoixFirst.apllicaion_object(first)
    if str(type(ChoixSecond)) == "<class 'Item_Class.Item'>":
        print("Tu as choisi un objet ",ChoixSecond.name)
        if ChoixSecond.name == "pokeball" :
            r = ChoixSecond.apllicaion_object(first)  
            if r >= 0 :
                r = Animation_Capture(r)
                if r == 1:
                    J1.ajouter_membre(first)
                    clear()
                    P2.Info_Pokemon()
                    return P2
        else:
            ChoixSecond.apllicaion_object(second) 
#######################################################################Aplication des attaque
    clear()
    Affichage_du_Duel(P1,P2)
    print(first.name," commence ")
    if str(type(ChoixFirst)) == "<class 'Mouv_Class.Mouv'>":
        if ChoixFirst.toucher(first,second) :
            d = ChoixFirst.Calcule_Degat(first,second)
            second.HP -= d
            if second.HP < 0:
                second.HP = 0
                return P1
    sleep(3)
    clear()
    Affichage_du_Duel(P1,P2)
    if str(type(ChoixSecond)) == "<class 'Mouv_Class.Mouv'>":
        if ChoixSecond.toucher(second,first):
            d = ChoixSecond.Calcule_Degat(second,first)
            first.HP -= d
            if first.HP < 0:
                first.HP = 0
                return P1
##############################################################################Aplication des Statu
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
#########################################################################################


def COMBAT(map,Joueur,Adverser):
    """
    fonction combat qui peut interpreter un pokemon sauvage ou un dresseur adverse
    """
    P1 = Joueur.team[0]
    print(map,Joueur,Adverser)
    # cligniotement(map)
    if str(type(Adverser)) == "<class 'Pokemon_Class.Pokemon'>" :
        print("Un Pokemon Sauvage !!!!")
        while Joueur.Perdu() and Adverser.HP > 0 and Adverser.sauvage :
                ActionJ1 = Joueur_choix(Joueur,Adverser,P1)
                if ActionJ1 == 100 :
                    clear()
                    Affichage_du_Duel(P1,Adverser)
                    print("Tu as Fuis !!!")
                    for i in Joueur.team:
                        i.Fin_de_Combat()
                    sleep(3)
                    clear()
                    return "Fuite"
                ActionJ2 = IA_Pokemon_Sauvage(Adverser)
                P1 = Duel(Joueur,P1,Adverser,ActionJ1,ActionJ2)
        if not(Joueur.Perdu()):
            print("Dommage Gamme OVER :(")
            sleep(3)
            return "Defaite"
        elif Adverser.HP ==0 :
            P1.gain_Exp(Adverser.Level)
            print("FIN DU COMBAT")
            for i in Joueur.team:
                i.Fin_de_Combat()
            sleep(4)
            clear()
            return "Victoire"
        else:
            clear()
            print("FIN un pokemon capturer")
            """fonction qui montre les state du pokemon"""

    else :
        print("Un Dresseur !! ")
# Pikachu.statu = Mouv_Class.Brule1sur10
NVX_PK = Pikachu.New_Pokemon_same_espece()
NVX_PK.name= "JOSE"
moi.team.append(NVX_PK)
COMBAT(carte,moi,PKSauvage)
#Salameche_du_Joueur.Info_Pokemon()
#Faire les degat  FAIT
#aplication d'effet FAIT
# le fais de pouvoir utilisé des potion FAIT
#créé la fonction generate pokemon FAIT 
# changer de pokemon EN COURS /!\
# et Pouvoir fuire FAIT