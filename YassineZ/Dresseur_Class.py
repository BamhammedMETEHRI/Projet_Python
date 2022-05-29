#crée la class des dresseurs, toute les entités ( se sont des dresseur de pokèmon) et non des pokèmons #
#ici où je teste mes class
# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep, time
from colorama import Fore
from colorama import Style
import random

import Item_Class 

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
    La class Dresseur sera le parent de tout les 
    Personnage (sauf les Pokèmons) 
    """
    def __init__(self,name,team,physique):
        """
        chaque personnage aura
        un inventaire (potion et pokeball ...)
        name le nom
        chaque personnage aura une équipe de pokèmon
        et chaque personnage aura de l'argent avec laquel on poura acheter des objets
        """
        self.avant = ""
        self.AxeX = None
        self.AxeY = None
        self.name=name      #nom du dresseur 
        self.money=0        #l'argent que possède le dresseur
        self.inventaire=[]  #les objets que possède le dresseur 
        self.team= team     #l'equipe du dresseur qui sera une liste de 6
        self.dialogue= ""   #chaque dresseur aura une boite de dialogue
        self.physique = physique  #a quoi ressemblera le personnage sur la carte.town
    
    def recherche_Map(self,map):
        for i in range (len(map.town)):
            for j in range(len(map.town[0])):
                if map.town[i][j]==self:
                    return i,j
        print("on as rien trouver")
    
    def affichage_Item(self):
        
        max=[]
        for i in range(len(Item_Class.all_Object)):
            nbr = 0
            for j in self.inventaire :
                if Item_Class.all_Object[i] == j :
                    nbr += 1
            if nbr>0:
                max.append(i+1)
                print(Fore.LIGHTRED_EX+"Id "+str(i+1)+Style.RESET_ALL+"\nNom : ",Item_Class.all_Object[i].name,"\nNBR d'exemplaire : ",nbr,"\nDescription : ",Item_Class.all_Object[i].description,"\n")
        return max
    
    def selection_Item(self):
        while True:
            try:
                max =self.affichage_Item()
                choix = int(input("----------------------------------------------------\n\nselectionai l'"+Fore.LIGHTRED_EX+"ID"+Style.RESET_ALL+" de l'objet que vous voulez choisir OU 0 pour retourner en arriere\nChoix = "+Fore.LIGHTRED_EX+""))
                print(""+Style.RESET_ALL+"")
                if choix==0 :
                    return choix
                elif choix in max:
                    for i in range(len(self.inventaire)) :
                        if self.inventaire[i].name == Item_Class.all_Object[choix-1].name:
                            obj = self.inventaire.pop(i)

                            return obj

                else:
                    clear()
            except ValueError:
                clear()



    def Perdu(self):
        for i in self.team:
            if i.HP > 0:
                return True
        print(self.name," a Perdu !")
        return False


######### celui qui va jouer ########################################################################################################
class Joueur(Dresseur):
    """
    ce si est la class du joueur qui jouera
    """

    def __init__(self, name, team):
        self.PC_DU_JOUEUR = []  # la ou iront tout le surplus de pokèmon qui ne poura pas etre dans son équipe
        self.avant = "" #Pour le deplacement
        super().__init__(name, team,Fore.WHITE+'H'+Style.RESET_ALL)# il sera en H pour Hero

    def affichage_Team(self):
        for i in range(6):
            if len(self.team) >i :
                print("ID.",i+1," ",self.team[i].name,end=" - ")
                if self.team[i].HP<=0:
                    print(Fore.LIGHTRED_EX+"K.O"+Style.RESET_ALL)
                else:
                    print(Fore.GREEN+str(round(self.team[i].HP*100/self.team[i].HP_full))+"%"+Style.RESET_ALL)
            else:
                print("ID.",i," RIEN")

    def Selector_Info_Pokemon(self):
        while True:
            clear()
            try:
                self.affichage_Team()
                choix_Pokemon = int(input("Quel Pokemon slectioner (0 pour retourner en arriere): "))
                if choix_Pokemon == 0:
                    return 0,None
                elif choix_Pokemon >0 and choix_Pokemon<= len(self.team):
                    print("\nTu as choisi ",self.team[choix_Pokemon-1].name,"\n")
                    choix = input("Appuie sur \'S\' pour choisir ce pokemon ou nimporte quoi dautre pour avoire des info sur ce pokemon : ")
                    if choix=="S":
                        return choix_Pokemon,self.team[choix_Pokemon-1]
                    else:
                        self.team[choix_Pokemon-1].Info_Pokemon()
                
            except ValueError:
                clear()
    #------------------------------------------------------------------
    def afficher_PC(self):
        """
        affichage de tout les pokèmons que le joueur à attraper et 
        qui ne sont pas dans son équipe
        """
        for i in range(len(self.PC_DU_JOUEUR)):
            print("id ",i,", nom ",self.Boite[i].name)
    #------------------------------------------------------------------
    def ajouter_membre(self,membre):
        """
        La fonction qui permet de rajouter 
        les pokèmon dans l'équipe du joueur 
        """
        membre.sauvage = False
        Nom= input("Veut tu donner un nom a ce pokemon ?? ")
        if Nom != "":
            membre.name = Nom
            print(membre.Espece," s'apelle a present ",membre.name)
            sleep(2)
        if len(self.team)<6:
            self.team.append(membre)
        else:
            print("Votre équipe est complète votre pokèmon sera stocker dans le PC")
            self.PC_DU_JOUEUR.append(membre)
            sleep(2)
    #------------------------------------------------------------------
    def Deplacement_dans_la_Map(self,carte):
        clear()
        carte.show()
        ###Début de la boucle while tant qu'on ne tombe pas sur Fin
        stop = True
        while stop:
            #Pour PNJ_Adverse
            if carte.List_of_Adversaire != []:
                print("il y a ",len(carte.List_of_Adversaire)," Adversaire attention")
                print("Voila leur Nom : ")
                for z in carte.List_of_Adversaire:
                    print(" -",z.name)
                    z.changement_de_position(1)
                    z.vision(carte)
            #FIN
    #######################################################################################
            deplacer=input(
            "  "+Fore.LIGHTBLUE_EX+"Z"+Style.RESET_ALL+"  \n"+Fore.LIGHTGREEN_EX+"Q"+Style.RESET_ALL+" "+Fore.LIGHTMAGENTA_EX+"S"+Style.RESET_ALL+" "+Fore.LIGHTYELLOW_EX+"D"+Style.RESET_ALL+"\n"+Fore.LIGHTBLUE_EX+"Z haut"+Style.RESET_ALL+", "+Fore.LIGHTGREEN_EX+"Q a gauche"+Style.RESET_ALL+", "+Fore.LIGHTMAGENTA_EX+"S en bas "+Style.RESET_ALL+"et "+Fore.LIGHTYELLOW_EX+"D a droite "+Style.RESET_ALL+": ")
            clear()
            if deplacer == "Z":
                self.AxeY -= 1
                if str(type(carte.town[self.AxeY][self.AxeX]))=="<class 'map_Class.biome'>":
                    if carte.town[self.AxeY][self.AxeX].effect =="Stop":
                        print("Aie !! un Mur tu ne peux pas aller plus loin faite demi-tour")
                        self.AxeY +=1
                    else :
                        carte.town[self.AxeY+1][self.AxeX] = self.avant
                        self.avant = carte.town[self.AxeY][self.AxeX] 
                else :
                    carte.town[self.AxeY+1][self.AxeX] = self.avant
                    self.avant = carte.town[self.AxeY][self.AxeX] 
            elif deplacer == "Q":
                self.AxeX -= 1
                if str(type(carte.town[self.AxeY][self.AxeX]))=="<class 'map_Class.biome'>":
                    if carte.town[self.AxeY][self.AxeX].effect =="Stop":
                        print("Aie !!! un Mur tu ne peux pas aller plus loin faite demi-tour")
                        self.AxeX +=1
                    else :
                        carte.town[self.AxeY][self.AxeX+1] = self.avant
                        self.avant = carte.town[self.AxeY][self.AxeX] 
                else :
                    carte.town[self.AxeY][self.AxeX+1] = self.avant
                    self.avant = carte.town[self.AxeY][self.AxeX] 
                    
            elif deplacer == "S":
                self.AxeY += 1
                if str(type(carte.town[self.AxeY][self.AxeX]))=="<class 'map_Class.biome'>":
                    if carte.town[self.AxeY][self.AxeX].effect =="Stop":
                        print("Aie !!! un Mur tu ne peux pas aller plus loin faite demi-tour")
                        self.AxeY -=1
                    else :
                        carte.town[self.AxeY-1][self.AxeX] = self.avant
                        self.avant = carte.town[self.AxeY][self.AxeX]
                else :
                    carte.town[self.AxeY-1][self.AxeX] = self.avant
                    self.avant = carte.town[self.AxeY][self.AxeX] 
                    
            elif deplacer == "D":
                self.AxeX += 1
                if str(type(carte.town[self.AxeY][self.AxeX]))=="<class 'map_Class.biome'>":
                    if carte.town[self.AxeY][self.AxeX].effect =="Stop":
                        print("Aie !!! un Mur tu ne peux pas aller plus loin faite demi-tour")
                        self.AxeX -=1
                    else :
                        carte.town[self.AxeY][self.AxeX-1] = self.avant
                        self.avant = carte.town[self.AxeY][self.AxeX]   
                else :
                    carte.town[self.AxeY][self.AxeX-1] = self.avant
                    self.avant = carte.town[self.AxeY][self.AxeX]    
    #####################################################################################       
            carte.town[self.AxeY][self.AxeX]=self
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
            elif type(self.avant)==PNJ_Soigneur_Marchand or type(self.avant)==PNJ_Adverse:
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
    
    def action(self,target):
        print(self.dialogue)
        print("Un combat commence entre ",self.name," et ",target.name)
        sleep(2.5)
        clear()

    def changement_de_position(self,bouge):
        self.posture += bouge
        if self.posture == -1:
            self.posture = len(self.position)-1
        elif self.posture>=len(self.position):
            self.posture = 0
        self.physique = self.position[self.posture]

    def vision(self,map):
        for y in range (len(map.town)):
            for x in range (len(map.town[0])):
                if type(map.town[y][x])==Joueur:   
                    if  x<self.AxeX and y==self.AxeY and self.physique == self.position[1]:
                        print("Je te Vois HAHAHA tu es a gauche")
                        self.Aller_a_gauche(map,self.AxeX-x)
                        break
                    elif y<self.AxeY and x==self.AxeX and self.physique == self.position[2]:
                        print("Je te Vois HAHAHA tu es en Haut")
                        self.Aller_en_haut(map,self.AxeY-y)
                        break
                    elif x>self.AxeX and y==self.AxeY and self.physique == self.position[3]:
                        print("Je te Vois HAHAHA tu es a Droite")
                        self.Aller_a_droite(map,self.AxeX-x)
                        break
                    elif y>self.AxeY and x==self.AxeX and self.physique == self.position[0]:
                        print("Je te Vois HAHAHA tu es en Bas !!")
                        self.Aller_en_bas(map,self.AxeY-y)
                        break
    def Aller_a_gauche(self,map,nbr):
        self.posture -=1
        self.physique = self.position[self.posture]
        for _ in range(nbr):
            map.town[self.AxeY][self.AxeX]=self.avant
            self.AxeX -= 1
            self.avant=map.town[self.AxeY][self.AxeX]
            map.town[self.AxeY][self.AxeX] = self
            if str(type(self.avant)) == "<class 'map_Class.biome'>" and self.avant.effect == "Stop":
                map.town[self.AxeY][self.AxeX]=self.avant
                self.AxeX +=1
                self.avant = map.town[self.AxeY][self.AxeX]
                map.town[self.AxeY][self.AxeX]=self
                print(self.name," c'est cogné contre un mur")
                return
            elif type(self.avant)==Joueur:
                A = self.avant.avant
                self.avant.avant = self
                self.avant = A
            sleep(0.75)
            clear()
            map.show()
            
        sleep(1)

    def Aller_a_droite(self,map,nbr):
        self.posture -=1
        self.physique = self.position[self.posture]
        for _ in range(nbr*-1):
            map.town[self.AxeY][self.AxeX]=self.avant
            self.AxeX += 1
            self.avant=map.town[self.AxeY][self.AxeX]
            map.town[self.AxeY][self.AxeX] = self
            if str(type(self.avant)) == "<class 'map_Class.biome'>" and self.avant.effect == "Stop":
                map.town[self.AxeY][self.AxeX]=self.avant
                self.AxeX -=1
                self.avant = map.town[self.AxeY][self.AxeX]
                map.town[self.AxeY][self.AxeX]=self
                print(self.name," c'est cogné contre un mur")
                return
            elif type(self.avant)==Joueur:
                A = self.avant.avant
                self.avant.avant = self
                self.avant = A
            sleep(0.75)
            clear()
            map.show()
        sleep(1)
    
    def Aller_en_haut(self,map,nbr):
        self.posture -=1
        self.physique = self.position[self.posture]
        for _ in range(nbr):
            map.town[self.AxeY][self.AxeX]=self.avant
            self.AxeY -= 1
            self.avant=map.town[self.AxeY][self.AxeX]
            map.town[self.AxeY][self.AxeX] = self
            if str(type(self.avant)) == "<class 'map_Class.biome'>" and self.avant.effect == "Stop":
                map.town[self.AxeY][self.AxeX]=self.avant
                self.AxeY +=1
                self.avant = map.town[self.AxeY][self.AxeX]
                map.town[self.AxeY][self.AxeX]=self
                print(self.name," c'est cogné contre un mur")
                return
            elif type(self.avant)==Joueur:
                A = self.avant.avant
                self.avant.avant = self
                self.avant = A
            sleep(0.75)
            clear()
            map.show()
            
        sleep(1)
    
    def Aller_en_bas(self,map,nbr):
        self.posture -=1
        self.physique = self.position[self.posture]
        for _ in range(nbr*-1):
            map.town[self.AxeY][self.AxeX]=self.avant
            self.AxeY += 1
            self.avant=map.town[self.AxeY][self.AxeX]
            map.town[self.AxeY][self.AxeX] = self
            if str(type(self.avant)) == "<class 'map_Class.biome'>" and self.avant.effect == "Stop":
                map.town[self.AxeY][self.AxeX]=self.avant
                self.AxeY -=1
                self.avant = map.town[self.AxeY][self.AxeX]
                map.town[self.AxeY][self.AxeX]=self
                print(self.name," c'est cogné contre un mur")
                return
            elif type(self.avant)==Joueur:
                A = self.avant.avant
                self.avant.avant = self
                self.avant = A
            sleep(0.75)
            clear()
            map.show()
            
        sleep(1)
    

######## soigneur et vendeur #########################################################################################################
class PNJ_Soigneur_Marchand(Dresseur):
    """
    Se sont des Pnj qui permet de soigné les pokémons du joueur et de vendre
    des pokèballs et des potions
    """
    def __init__(self, name, team):
        super().__init__(name, team,Fore.BLUE+"♡"+Style.RESET_ALL)
        self.inventaire= Item_Class.all_Object
    
    def action(self,target):
        print("Bonjour je suis ",self.name," je peux soignier tout t'es pokèmon où vendre des objets qui peuvent t'aider")
        choix = input("1- Soigner \n2-Comercer \n3-Quiter\n")
        while choix != "3":
            clear()
            if choix == "2":
                self.comercer(target)
            elif choix =="1":
                self.health(target)
            choix = input("1- Soignier \n2-Commercer \n3-Quitter\n")
            clear()
    
    #------------------------------------------------------------------
    def health(self,target):
        """
        fonction qui permet de soigner les pokèmons de target
        """
        if len(target.team)>0 and str(type(target.team[0]))=="<class '__main__.Pokemon'>":
                for i in target.team:
                    i.HP=i.HP_full                 #HP actuel
                    i.Attack = i.Attack_full
                    i.AttackSPE =i.AttackSPE_full
                    i.Defense = i.Defense_full
                    i.DefenseSPE = i.DefenseSPE_full
                    i.Speed = i.Speed_full
                    for j in i.competence:
                        j.PP = j.full_PP
                    print(i.name," Est soignier :)")
                    sleep(1)
        else:
            print("Mais !!? tu n'as pas de pokemon >:(")
            sleep(2)
    #------------------------------------------------------------------

    def comercer(self,target):
        """
        fonction qui permet de faire du commerce avec target
        """
        Choix0 = input("1.Acheter 2.Vendre 3.Quitter\n")
        if Choix0 == "1" :
            clear()
            print("Voila ce que je vend")
            for i in range(len(self.inventaire)):
                print("id ",i,"| nom ",self.inventaire[i].name," , prix : ",self.inventaire[i].prix)
            print("\ntu as ",self.money,"€\n")
            Choix = int(input("que souhaite tu acheter ? : "))
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
                Choix = int(input("que souhaite tu vendre? : "))
                target.money += target.inventaire[Choix].prix
                target.inventaire.pop(Choix)
        elif Choix0 == "3" :
            print("Au revoir :) ")
            clear()
            return
        else : 
            clear()
        sleep(1.5)
        clear()
    #------------------------------------------------------------------
