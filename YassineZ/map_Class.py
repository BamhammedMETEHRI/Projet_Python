#Class des map et Biome
from colorama import Fore
from colorama import Style

class biome:
    def __init__(self,physique,effect=None):
        self.image =physique
        self.effect =effect
mur= biome(Fore.BLACK+"#"+Style.RESET_ALL,"Stop")
Herbe_All = biome(Fore.GREEN+"~"+Style.RESET_ALL,"Taux d'appiration de tout les pokèmon egaux")
rien = biome(" ")
class Map:
    def __init__(self,Longuer,Largeur):
        self.town =[]
        for i in range(Largeur+2):
            l=[]
            for j in range(Longuer+2):
                if i ==0 or j==0 or i==Largeur+1 or j == Longuer+1:
                    l.append(mur)
                else:
                    l.append(rien)
            self.town.append(l)
    def append_biome(self,element,Point_de_depart_X,Point_de_depart_Y,Longuer_Y,Largeur_X):
        if Point_de_depart_X+Largeur_X > (len(self.town[0])-2) or Point_de_depart_Y+Longuer_Y >(len(self.town)-2):
            print("Dimmension pas correcte error Out-of-Range")
            return
        else:
            for i in range(Longuer_Y):
                for j in range(Largeur_X):
                    self.town[Point_de_depart_Y+i+1][Point_de_depart_X+j+1] = element
        
    def show(self):
        for i in self.town:
            for j in i:
                print(j.image,end="")
            print()
test = Map(10,10)
test.show()
test.append_biome(Herbe_All,0,0,1,1)
test.show()
