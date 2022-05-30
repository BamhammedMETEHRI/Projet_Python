# import Dresseur_Class, map_Class,Pokemon_Class
# import random
# import Combat
# from colorama import Fore
# from colorama import Style

# ###################### creation de biome
# def Aparition_Pokemon_sauvage (Joueur):
#     if random.randint(1,4)==1:
#         print("Attention Un Pokemon Sauvage!!")
#         pk = Pokemon_Class.afficher_Liste_Pokemon[random.randint(0,len(Pokemon_Class.afficher_Liste_Pokemon)-1)]
#         while len(pk)<0:
#             pk = Pokemon_Class.afficher_Liste_Pokemon[random.randint(0,len(Pokemon_Class.afficher_Liste_Pokemon)-1)]
#         pk=pk[random.randint(0,len(pk)-1)]
#         if Joueur.team[0].Level <=5:
#             pk.Make_Level(random.randint(Joueur.team[0].Level,Joueur.team[0].Level+5))
#         else:
#             pk.Make_Level(Joueur.team[0].Level-2,Joueur.team[0].Level+5)
#         Combat.COMBAT(map,Joueur,)

# Herbe_All = map_Class.biome(Fore.GREEN+"~"+Style.RESET_ALL,"Taux d'apparition de tout les pokèmons égaux")
# Joel = Dresseur_Class.PNJ_Soigneur_Marchand("Joel",[])
# Adversaire = Dresseur_Class.PNJ_Adverse("Loupio",[])
# Adversaire2 = Dresseur_Class.PNJ_Adverse("Trodor",[])
# Adversaire.dialogue = "Je Vais te Battre !! "
# Adversaire2.dialogue = "Je vais prendre ton argent !!!"
# # print(Joel.physique)
# # print(type(Joel)== Dresseur_Class.PNJ_Soigneur_Marchand)

# test = map_Class.Map(10,10)
# test.append_biome(Herbe_All,0,0,10,5)
# test.append_biome(FIN,0,0,1,1)
# # test.append_biome(map_Class.mur,4,5,1,1)
# # test.append_biome(map_Class.mur,6,5,1,1)
# # test.append_biome(map_Class.mur,5,4,1,1)
# # test.append_biome(map_Class.mur,5,6,1,1)
# test.Placement_Dresseur(Adversaire2,4,4)
# test.Placement_Dresseur(Adversaire,5,5)
# test.Placement_Dresseur(Joel,9,1)
# Gamer = Dresseur_Class.Joueur("Yassine",[])
# test.Placement_Dresseur(Gamer,0,9)
# test.show()
# Gamer.Deplacement_dans_la_Map(test)
# # print(str(type(FIN))=="<class 'map_Class.biome'>")

# #FINIR IV ET EV fini  FIN
# #PUIS finir les interaction avec la map FIN 4/5
# #(jai fais la moitier du chemin ) refaire la fonction de deplacement FIN  puis rendre optionel certaine fonction du Joueur adverse
# #PUIS la fonction de Combat
# #apres jaurais fini

