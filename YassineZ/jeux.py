import Dresseur_Class, map_Class
from colorama import Fore
from colorama import Style

###################### creation de biome
Herbe_All = map_Class.biome(Fore.GREEN+"~"+Style.RESET_ALL,"Taux d'appiration de tout les pokèmon egaux")
FIN = map_Class.biome("F","FIN du Jeux Merci D'avoir Jouer :)")
Joel = Dresseur_Class.PNJ_Soigneur_Marchand("Joel",[])
Adversaire = Dresseur_Class.PNJ_Adverse("Loupio",[])
# print(Joel.physique)
# print(type(Joel)== Dresseur_Class.PNJ_Soigneur_Marchand)

test = map_Class.Map(10,10)
test.append_biome(Herbe_All,0,0,10,5)
test.append_biome(FIN,0,0,1,1)
test.Placement_Dresseur(Adversaire,5,5)
test.Placement_Dresseur(Joel,9,1)
Gamer = Dresseur_Class.Joueur("Yassine",[])
test.Placement_Dresseur(Gamer,0,9)
test.show()
Gamer.Deplacement_dans_la_Map(test)
# print(str(type(FIN))=="<class 'map_Class.biome'>")

#FINIR IV ET EV fini  FIN
#PUIS finir les interaction avec la map (jai fais la moitier du chemin ) refaire la fonction de deplacement
#PUIS la fonction de Combat
#apres jaurais fini