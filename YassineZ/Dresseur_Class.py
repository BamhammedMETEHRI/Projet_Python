#crée la classe des dresseur toute les entité ( se sont des dresseur de pokèmon) non pokèmon #
import colorama
from colorama import Fore
from colorama import Style
import random

from Item_Class import Item

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
        self.physique = physique  #a quoi ressemblera le personnage sur la map
        
######### celui qui va jouer ########################################################################################################
class Joueur(Dresseur):
    """
    ce si est la classe du joueur qui jouera
    """

    def __init__(self, name, team):
        self.PC_DU_JOUEUR = []  # la ou iront tout le surplus de pokèmon qui ne poura pas etre dans son equipe
        super().__init__(name, team,Fore.BLACK+'H'+Style.RESET_ALL)# il sera en H pour Hero
        
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
        super().__init__(name, team)
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
