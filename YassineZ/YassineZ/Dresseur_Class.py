import random
#crée une classe dresseur qui aura
#nom,à entre  1 et 6 pokémon(sauf pour le joueur qui aura 0 ), à de l'argent

class PC:
    def __init__(self):
        self.Boite= []
    def afficher(self):
        for i in range(len(self.Boite)):
            print("id ",i,", nom ",self.Boite[i].name)


class Dresseur:
    def __init__(self,name):
        self.inventaire=[]
        self.name=name
        self.team= []
        self.money=0

    def ajouter_membre(self,membre):
        if len(self.team)<6:
            self.team(membre)
        else:
            print("Votre equipe est complète votre pokèmon sera dans le PC")

class Protagoniste(Dresseur):
    def __init__(self, name):
        super().__init__(name)

class ORDI(Dresseur):

    def __init__(self, name):
        super().__init__(name)
        self.money = random.randint(10,20)

class Soigneuse_Marchand(Dresseur):

    def __init__(self, name):
        self.inventaire
        super().__init__(name)

    def health(self,target):
        for i in target.team:
            i.HP = i.fullHP
    
    def comercer(self,target):
        
        for i in range(self.inventaire):
            print("id ",i," nom ",self.inventaire[i].name," prix",self.inventaire[i].prix)
        Choix = int(input("que shouaite tu acheter? : "))
        if self.inventaire[Choix].prix <= target.money:
            target.inventaire.append(self.inventaire[Choix])
        else :
            print("Trop cher!!")
            