#La classe des itème son la class des objet#
from time import sleep
import random

all_Object = []
class Item:
    def __init__(self,name) :
        self.name=name
        if name == "pokeball" :
            self.value = None
            self.prix = 5
            self.description= "Un objet qui permet d'attraper un pokemon"
            all_Object.append(self)
        elif name[0:6]=="potion":
            self.value = 20
            for i in name:
                if i == "+":
                    self.value += 20
            self.prix = 10
            self.description = "Un objet qui permet de sognier "+str(self.value)+" PV"
            all_Object.append(self)
        else:
            print("OBJET INCONUE ????????????")
    #------------------------------------------------------------------
    def capture(self,pokemon):
        bonus =1
        if pokemon.statu != None:
            bonus = 2.5
        a = (1-(2/3)*(pokemon.HP/pokemon.HP_full))*pokemon.Taux_De_Capture*2*bonus
        if a >= 255 :
            return 4
        else:
            nbr = 0
            b = 65535*(((((a/255)**0.5)**0.5)**0.5)**0.5)**0.5
            for _ in range(4):
                if random.randint(0,65535) <=b:
                    nbr +=1
            return nbr
    
    def apllicaion_object(self,pokemon):
        if self.name == "pokeball":
            print("\nVous lanecer une pokeball !!")
            if pokemon.sauvage:
                return self.capture(pokemon)
            else:
                print(pokemon.name," n'est pas sauvage ... tu es un Voleur??? ")
                sleep(4)
                return -1
        elif self.name[0:6]== "potion":
            print("vous utiliser une potion sur ",pokemon.name," il gagne ",self.value," PV")
            pokemon.HP += self.value
            if pokemon.HP>pokemon.HP_full:
                pokemon.HP=pokemon.HP_full
        sleep(3)

potion_normal = Item("potion ")

pokeball = Item("pokeball")
