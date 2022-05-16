import Dresseur_Class, map_Class
from colorama import Fore
from colorama import Style

###################### creation de biome
Herbe_All = map_Class.biome(Fore.GREEN+"~"+Style.RESET_ALL,"Taux d'appiration de tout les pokèmon egaux")
FIN = map_Class.biome("F","FIN du Jeux Merci D'avoir Jouer :)")
a = Dresseur_Class.PNJ_Soigneur_Marchand("Joel",[])
# print(a.physique)
# print(type(a)== Dresseur_Class.PNJ_Soigneur_Marchand)

test = map_Class.Map(10,10)
test.append_biome(Herbe_All,0,0,10,5)
test.append_biome(FIN,0,0,1,1)
test.Placement_Dresseur(a,9,1)
bob = Dresseur_Class.Joueur("Yassine",[])
test.Placement_Dresseur(bob,0,9)
test.show()
bob.Deplacement_dans_la_Map(test)
# print(str(type(FIN))=="<class 'map_Class.biome'>")

#FINIR IV ET EV fini  FIN
#PUIS finir les interaction avec la map (jai fais la moitier du chemin )
#PUIS la fonction de Combat
#apres jaurais fini