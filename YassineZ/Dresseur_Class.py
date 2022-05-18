#crée la classe des dresseur toute les entité ( se sont des dresseur de pokèmon) non pokèmon #
#ici ou je teste mes class
# import only system from os
from os import system, name
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
    def afficher_PC(self):
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
            self.PC_DU_JOUEUR.append(membre)
    #------------------------------------------------------------------
    def Deplacement_dans_la_Map(self,carte):
        ListeOfAdversaire= []    
        y=0
        x=0
        ### Pour trouver la position du Joueur

        for i in range(len(carte.town)):
            for j in range(len(carte.town[0])):
                if str(type(carte.town[i][j])) == "<class 'Dresseur_Class.PNJ_Adverse'>":
                    print("Y a QUELQUN !!")
                    sleep(1)
                    ListeOfAdversaire.append(carte.town[i][j])
                elif type(carte.town[i][j])==Joueur:
                    print("On as trouver la position du Joueur")
                    sleep(1)
                    y=i
                    x=j
        ### FIN
        clear()
        carte.show()
        ###Debut de la boucle while tant qu'on ne tombe pas sur Fin
        stop = True
        while stop:
            #Pour PNJ_Adverse
            if ListeOfAdversaire != []:
                print("il y a ",len(ListeOfAdversaire)," Adversaire attention")
                print("Voila leur Nom : ")
                for z in ListeOfAdversaire:
                    print(" -",z.name)
                    z.changement_de_position(1)
            #FIN
    #######################################################################################
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
    #####################################################################################       
            clear()
            carte.town[y][x]=self
            carte.show()
            ######################################################################
            if str(type(self.avant))=="<class 'map_Class.biome'>":
                if (self.avant.image == "F"):
                    stop=False
                    clear()
                    print(self.avant.effect)
                    sleep(2)
                    clear()
                    print("Fais par \n Yassine Zaoui \n Bamhammed Metehri \n Yassine Frikich \n Meliha Urlu")
                    sleep(2)
                    clear()
            elif type(self.avant)==PNJ_Soigneur_Marchand:
                self.avant.action(self)
                carte.show()
            


######## les joueur adverse##############################################################################################
class PNJ_Adverse(Dresseur):
    """
    Se sont les ordi qui provoque des duel au Joueur
    """
    def __init__(self, name, team):
        self.position = [Fore.RED+"<"+Style.RESET_ALL,Fore.RED+"^"+Style.RESET_ALL,Fore.RED+">"+Style.RESET_ALL,Fore.RED+"V"+Style.RESET_ALL]
        self.posture = 0 
        super().__init__(name, team,self.position[self.posture])
        self.money = random.randint(10,20)
        self.deplacement = [] 
    
    def changement_de_position(self,bouge):
        self.posture += bouge
        if self.posture == -1:
            self.posture = len(self.position)-1
        elif self.posture>=len(self.position):
            self.posture = 0
        self.physique = self.position[self.posture]
    
    def vision(self):
        pass

    

######## soigneur et vendeur #########################################################################################################
class PNJ_Soigneur_Marchand(Dresseur):
    """
    Se sont des Pnj qui permet de soigné les pokémon du joueur et de vendre
    des pokèball et des potion
    """
    def __init__(self, name, team):
        super().__init__(name, team,Fore.BLUE+"♡"+Style.RESET_ALL)
        self.inventaire=[Item("Potion",""),Item("Poké ball","pokeball")]
    
    def action(self,target):
        print("Bonjour je suis ",self.name," je peux soignier tout t'es pokemon ou vendre des objet qui peuvent t'aider")
        choix = input("1- Soigner \n2-Comercer \n3-Quiter\n")
        while choix != "3":
            clear()
            if choix == "2":
                self.comercer(target)
            elif choix =="1":
                self.health(target)
            choix = input("1- Soignier \n2-Comercer \n3-Quite\n")
            clear()
    
    #------------------------------------------------------------------
    def health(self,target):
        """
        fonction qui permet de soigner les pokemon de target
        """
        if len(target.team)>0 and str(type(target.team[0]))=="<class '__main__.Pokemon'>":
                for i in target.team:
                    i.HP=i.HP_full                 #HP actuel
                    i.Attack = i.Attack_full
                    i.AttackSPE =i.AttackSPE_full
                    i.Defense = i.Defense_full
                    i.DefenseSPE = i.DefenseSPE_full
                    i.Speed = i.Speed_full
                    print(i.name," Est soignier :)")
                    sleep(1)
        else:
            print("Mais !!? tu n'as pas de pokemon >:(")
            sleep(2)
    #------------------------------------------------------------------

    def comercer(self,target):
        """
        fonction qui permet de faire du comerce avec target
        """
        Choix0 = input("1.Acheter 2.Vendre 3.Quiter\n")
        if Choix0 == "1" :
            clear()
            print("Voila ce que je vend")
            for i in range(len(self.inventaire)):
                print("id ",i,"| nom ",self.inventaire[i].name," , prix : ",self.inventaire[i].prix)
            print("\ntu as ",self.money,"€\n")
            Choix = int(input("que shouaite tu acheter? : "))
            if self.inventaire[Choix].prix <= target.money:
                target.money -= self.inventaire[Choix].prix
                target.inventaire.append(self.inventaire[Choix])
            else :
                print("Trop cher!!")
        elif Choix0 == "2":
            if target.inventaire == []:
                print("tu n'as rien n'a vendre :\\")
                sleep(2)
            else:
                for i in (target.inventaire):
                    print("id ",i," nom ",self.inventaire[i].name," prix",self.inventaire[i].prix)
                Choix = int(input("que shouaite tu vendre? : "))
                target.money += target.inventaire[Choix].prix
                target.inventaire.pop(Choix)
        elif Choix0 == "3" :
            print("Au revoir :)")
            clear()
            return
        else : 
            clear()
        sleep(1.5)
        clear()
    #------------------------------------------------------------------
