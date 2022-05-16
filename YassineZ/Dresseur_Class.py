#crée la classe des dresseur toute les entité ( se sont des dresseur de pokèmon) non pokèmon #
#ici ou je teste mes class
# import only system from os
from os import system, name
from re import A
# import sleep to show output for some time period
from time import sleep
from colorama import Fore
from colorama import Style
import random

from Item_Class import Item
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
####### le parent de tout les pnj et joueur ##########################################################################################################
class Dresseur:
    """
    La classe Dresseur sera le parent de tout les 
    Personage (sauf les Pokèmons) 
    """
    def __init__(self,name,team,physique):
        """
        chaque personage aura
        un inventaire (potion et pokeball et autre peut etre)
        name le nom
        chaque personage aura une equipe de pokèmon
        et chaque personage aura de l'argent avec la quel on poura acheter des objet
        """
        self.name=name      #nom du dresseur 
        self.money=0        #l'argent que possède le dresseur
        self.inventaire=[]  #les objet que possède le dresseur 
        self.team= team     #l'equipe du dresseur qui sera une liste de 6
        self.dialogue= ""   #chaque dresseur aura une boite de dialogue
        self.physique = physique  #a quoi ressemblera le personnage sur la carte.town
        
######### celui qui va jouer ########################################################################################################
class Joueur(Dresseur):
    """
    ce si est la classe du joueur qui jouera
    """

    def __init__(self, name, team):
        self.PC_DU_JOUEUR = []  # la ou iront tout le surplus de pokèmon qui ne poura pas etre dans son equipe
        self.avant = "" #Pour le deplacement
        super().__init__(name, team,Fore.WHITE+'H'+Style.RESET_ALL)# il sera en H pour Hero
        
    #------------------------------------------------------------------
    def afficher(self):
        """
        affiche tout les pokèmon que le joueur à attraper et 
        qui ne sont pas dans son equipe
        """
        for i in range(len(self.PC_DU_JOUEUR)):
            print("id ",i,", nom ",self.Boite[i].name)
    #------------------------------------------------------------------
    def ajouter_membre(self,membre):
        """
        La fonction qui permet de rajouter 
        les pokèmon dans l'equipe du joueur
        """
        membre.sauvage = False
        if len(self.team)<6:
            self.team(membre)
        else:
            print("Votre equipe est complète votre pokèmon sera dans le PC")
            self.Ordi.append(membre)
    #------------------------------------------------------------------
    def Deplacement_dans_la_Map(self,carte):
        y=0
        x=0
        for i in range(len(carte.town)):
            for j in range(i):
                if type(carte.town[i][j])==Joueur:
                    y=i
                    x=j
                    break
            if x !=0 and y != 0:
                break
        clear()
        carte.show()
        stop = True
        while stop:
            deplacer=input(
            "  "+Fore.LIGHTBLUE_EX+"Z"+Style.RESET_ALL+"  \n"+Fore.LIGHTGREEN_EX+"Q"+Style.RESET_ALL+" "+Fore.LIGHTMAGENTA_EX+"S"+Style.RESET_ALL+" "+Fore.LIGHTYELLOW_EX+"D"+Style.RESET_ALL+"\n"+Fore.LIGHTBLUE_EX+"Z haut"+Style.RESET_ALL+", "+Fore.LIGHTGREEN_EX+"Q a gauche"+Style.RESET_ALL+", "+Fore.LIGHTMAGENTA_EX+"S en bas "+Style.RESET_ALL+"et "+Fore.LIGHTYELLOW_EX+"D a droite "+Style.RESET_ALL+": ")
            clear()
            if deplacer == "Z":
                y -= 1
                if str(type(carte.town[y][x]))=="<class 'map_Class.biome'>":
                    if carte.town[y][x].effect =="Stop":
                        print("Aie un Mur tu ne peux pas aller par la dcp tu ne bouge pas")
                        y +=1
                    else :
                        carte.town[y+1][x] = self.avant
                        self.avant = carte.town[y][x] 
                else :
                    carte.town[y+1][x] = self.avant
                    self.avant = carte.town[y][x] 
            elif deplacer == "Q":
                x -= 1
                if str(type(carte.town[y][x]))=="<class 'map_Class.biome'>":
                    if carte.town[y][x].effect =="Stop":
                        print("Aie un Mur tu ne peux pas aller par la dcp tu ne bouge pas")
                        x +=1
                    else :
                        carte.town[y][x+1] = self.avant
                        self.avant = carte.town[y][x] 
                else :
                    carte.town[y][x+1] = self.avant
                    self.avant = carte.town[y][x] 
                    
            elif deplacer == "S":
                y += 1
                if str(type(carte.town[y][x]))=="<class 'map_Class.biome'>":
                    if carte.town[y][x].effect =="Stop":
                        print("Aie un Mur tu ne peux pas aller par la dcp tu ne bouge pas")
                        y -=1
                    else :
                        carte.town[y-1][x] = self.avant
                        self.avant = carte.town[y][x]
                else :
                    carte.town[y-1][x] = self.avant
                    self.avant = carte.town[y][x] 
                    
            elif deplacer == "D":
                x += 1
                if str(type(carte.town[y][x]))=="<class 'map_Class.biome'>":
                    if carte.town[y][x].effect =="Stop":
                        print("Aie un Mur tu ne peux pas aller par la dcp tu ne bouge pas")
                        x -=1
                    else :
                        carte.town[y][x-1] = self.avant
                        self.avant = carte.town[y][x]   
                else :
                    carte.town[y][x-1] = self.avant
                    self.avant = carte.town[y][x]           
            carte.town[y][x]=self
            carte.show()
            if str(type(self.avant))=="<class 'map_Class.biome'>":
                if (self.avant.image == "F"):
                    stop=False
                    clear()
                    print(self.avant.effect)
                    sleep(2)
                    clear()
                    print("Fais par \n Yassine Zaoui \n Bahm Metheri \n Yassine Frikiche \n Meliha")
                    sleep(2)
                    clear()
            


######## les joueur adverse##############################################################################################
class PNJ_Adverse(Dresseur):
    """
    Se sont les ordi qui provoque des duel au Joueur
    """
    def __init__(self, name, team):
        super().__init__(name, team)
        self.money = random.randint(10,20)

######## soigneur et vendeur #########################################################################################################
class PNJ_Soigneur_Marchand(Dresseur):
    """
    Se sont des Pnj qui permet de soigné les pokémon du joueur et de vendre
    des pokèball et des potion
    """
    def __init__(self, name, team):
        super().__init__(name, team,Fore.BLUE+"♡"+Style.RESET_ALL)
        self.inventaire=[Item("Potion",""),Item("Poké ball","pokeball")]
    
    #------------------------------------------------------------------
    def health(self,target):
        """
        fonction qui permet de soigner les pokemon de target
        """
        for i in target.team:
            i.HP = i.fullHP
    #------------------------------------------------------------------

    def comercer(self,target):
        """
        fonction qui permet de faire du comerce avec target
        """
        Choix0 = int(input("1.Acheter 2.Vendre 3.Quiter"))
        if Choix0 == 1 :
            for i in range(self.inventaire):
                print("id ",i," nom ",self.inventaire[i].name," prix",self.inventaire[i].prix)
            Choix = int(input("que shouaite tu acheter? : "))
            if self.inventaire[Choix].prix <= target.money:
                target.inventaire.append(self.inventaire[Choix])
            else :
                print("Trop cher!!")
        elif Choix0 == 2:
            if target.iventaire == []:
                print("tu n'as rien n'a vendre :\\")
            else:
                for i in (target.inventaire):
                    print("id ",i," nom ",self.inventaire[i].name," prix",self.inventaire[i].prix)
                Choix = int(input("que shouaite tu vendre? : "))
                target.money += target.inventaire[Choix].prix
                target.inventaire.pop(Choix)
        else :
            print("Au revoir :)")
            return
    #------------------------------------------------------------------
