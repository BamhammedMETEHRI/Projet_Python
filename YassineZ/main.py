from os import system, name
from re import A
import random
from click import style
import pygame

# import sleep to show output for some time period
from time import sleep
from colorama import Fore
from colorama import Style
import Pokemon_Class
import Dresseur_Class
import map_Class
import Combat
"""
<sound>.play(loop = 0 , time = 0, fadein = 0)
    .stop()
    .fadeout(ms)
    .set_volume(0.0 -> 1.0)
    .get_volume()
    .get_lenght(s)
"""
window_resolution = (640,480)
launched = True
pygame.init()
pygame.display.set_caption("Python - jouer du son")
window_surface = pygame.display.set_mode(window_resolution)

def mettre_music(chemin,music=None):
    if music!=None:
        music.stop()
    music = pygame.mixer.Sound(chemin)#mp3 sa marche pas
    music.play(10000)
    pygame.display.flip()
    return music
generique = 'music\generique.wav'
combat_pokemon= "music\combat_dresseur.wav"
combat_dresseur = "music\combat_pokemon.wav"
route00 = "music\port_pokemon.wav"
route01 = "music\\route_228.wav"
Prof = "music\\Professor.wav"
son=None

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def printFPS(str,time=None):
    if time==None:
        time=1/25
    for i in range(len(str)):
        clear()
        print(str[0:i],end="")
        sleep(time)
ecran ="                        888                                           \n                        888                                           \n                        888                                           \n        88888b.  .d88b. 888  888 .d88b. 88888b.d88b.  .d88b. 88888b.  \n        888 \"88bd88\"\"88b888 .88Pd8P  Y8b888 \"888 \"88bd88\"\"88b888 \"88b \n        888  888888  888888888K 88888888888  888  888888  888888  888 \n        888 d88PY88..88P888 \"88bY8b.    888  888  888Y88..88P888  888 \n        88888P\"  \"Y88P\" 888  888 \"Y8888 888  888  888 \"Y88P\" 888  888 \n        888                                                           \n        888                                                           \n        8888"
Proffesseur="      ////^\\\\\n      | ^   ^ |\n     @ (o) (o) @\n      |   <   |\n      | |___| |\n       \_____/\n     ____|  |____\n    /    \__/    \\\n   /              \n  /\_/|        |\_/\n / /  |        |  \ \n( <   |        |   > )\n \ \  |        |  / /\n  \ \ |________| / /\n   \ \|"

def changement_Map(Joueur,AncieneMap,son=None):
    if son!=None:
        if random.randint(1,2)==1:
            son=mettre_music(route01,son)
        else:
            son=mettre_music(route00,son)
    AncieneMap.del_Dresseur(Joueur)
    AncieneMap.NextMap.Placement_Dresseur(Joueur,0,9)
    clear()
    AncieneMap.NextMap.show()
    Joueur.Deplacement_dans_la_Map(AncieneMap.NextMap)


def Aparition_Pokemon_sauvage (Joueur,map):
    if random.randint(1,4)==1:
        print("Attention Un Pokemon Sauvage!!")
        pk = Pokemon_Class.Selection_Random_PK()
        if Joueur.team[0].Level <=5:
            pk.Make_Level(random.randint(Joueur.team[0].Level,Joueur.team[0].Level+5))
        else:
            pk.Make_Level(Joueur.team[0].Level-2,Joueur.team[0].Level+5)
        Combat.COMBAT(map,Joueur,pk)
Porte1to2 = map_Class.biome("P",changement_Map)
Porte2to3 = map_Class.biome("P",changement_Map)
Porte3to4 = map_Class.biome("P",changement_Map)
Porte4to5 = map_Class.biome("P",changement_Map)
FIN = map_Class.biome("F","FIN du Jeux Merci D'avoir Jouer :) ")

Herbe_All = map_Class.biome(Fore.GREEN+"~"+Style.RESET_ALL,Aparition_Pokemon_sauvage)


def creatMultiPokemon(PK,NVX):
    L=[]
    for p in PK:
        pk = p.New_Pokemon_same_espece()
        pk.Make_Level(NVX)
        L.append(pk)
    return L

Boss0= Dresseur_Class.PNJ_Adverse("JO",creatMultiPokemon([Pokemon_Class.Reptincel,Pokemon_Class.Racaillou],10))
boss1=Dresseur_Class.PNJ_Adverse("Zelephe",creatMultiPokemon([Pokemon_Class.Tortank,Pokemon_Class.Ramoloss],30))
boss2=Dresseur_Class.PNJ_Adverse("Mourenio",creatMultiPokemon([Pokemon_Class.Lokhlass,Pokemon_Class.Ectoplasma,Pokemon_Class.Pikachu],50))
boss3=Dresseur_Class.PNJ_Adverse("Brando",creatMultiPokemon([Pokemon_Class.Raichu,Pokemon_Class.Roucarnage,Pokemon_Class.Papilusion],50))
boss4=Dresseur_Class.PNJ_Adverse("JO",creatMultiPokemon([Pokemon_Class.Florizarre,Pokemon_Class.Dracaufeu,Pokemon_Class.Tortank,Pokemon_Class.Mackogneur],100))
allBoss=[Boss0,boss1,boss2,boss3,boss4]
Infirmier = Dresseur_Class.PNJ_Soigneur_Marchand("JOEL",[Pokemon_Class.Pikachu.New_Pokemon_same_espece()])


map5 = map_Class.Map(10,10)
map4 = map_Class.Map(10,10,map5)
map3 = map_Class.Map(10,10,map4)
map2 = map_Class.Map(10,10,map3)
map1 = map_Class.Map(10,10,map2)
allMap=[map1,map2,map3,map4,map5]
map1.append_biome(Porte1to2,len(map1.town)-3,len(map1.town[0])-3,1,1)
map2.append_biome(Porte2to3,len(map2.town)-3,len(map2.town[0])-3,1,1)
map3.append_biome(Porte3to4,len(map3.town)-3,len(map3.town[0])-3,1,1)
map4.append_biome(Porte4to5,len(map4.town)-3,len(map4.town[0])-3,1,1)
for i in range(len(allMap)):
    allMap[i].Placement_Dresseur(Infirmier,0,0)
    allMap[i].Placement_Dresseur(allBoss[i],9,0)
    allMap[i].append_biome(Herbe_All,2,2,5,5)
map5.append_biome(FIN,len(map1.town)-3,len(map1.town[0])-3,1,1)





window_resolution = (640,480)
def ecranAcueil():
    print(Fore.LIGHTMAGENTA_EX+"")
    printFPS(ecran,1/5000)
    print(""+Style.RESET_ALL)
    print(Fore.RED+"                   1. JOUER"+Style.RESET_ALL)
    print(Fore.BLUE+"                   2. CREDIT"+Style.RESET_ALL)
    print(Fore.YELLOW+"                   3. Bute du jeux ?"+Style.RESET_ALL)
    while True:
        try:
            choix=int(input("\n                   Votre choix : "))
            if choix >= 1 and choix<=3:
                clear()
                return choix
            else:
                clear()
        except ValueError:
            clear()
        print(Fore.LIGHTMAGENTA_EX+"")
        print(ecran)
        print(""+Style.RESET_ALL)
        print(Fore.RED+"                   1. JOUER"+Style.RESET_ALL)
        print(Fore.BLUE+"                   2. CREDIT"+Style.RESET_ALL)
        print(Fore.YELLOW+"                   3. Bute du jeux ?"+Style.RESET_ALL)
def debutJeux():
    clear()
    printFPS("HEin!!! Mais...\ncomment est tu arriver la cela doit etre un acte d'arceus et tu viens surement d'une autre dimension")
    print(". . . .",1)
    print("AH j'en Oublie Les bonne Maniere !!")
    input()
    clear()
    print("                Salut Je suis le Prof Raoult bienvenu dans le monde\nDES POKEMON!!\n.... tu es Nouveaus de ce que je vois")
    print(Proffesseur)
    input()
    clear()
    print("                Bah! si tu es nouveau comment tapelle tu ??\n")
    print(Proffesseur)
    Nom = input("                - Je m'apelle ")
    clear()
    print("                Jolie Prenom ",Nom," .Bon je te fais un petit debreff.\n Dans notre monde nous vivons en harmonie avec des creature Puissante efrayente Grande petit Mignion etc..\n On appelle c'est creature des pokemon.")
    print(Proffesseur)
    input()
    print(Fore.RED+"                Si tu Shouaite rejoindre ton monde tu devra etre acompagner de pokemon pour vaincre c'est malfrat qui agrece dans les route !!!\nSi tu peut te debarasser d'eux se SERAIS SUPER!! Si tu veux je te passe un pokemon et 10£ "+Style.RESET_ALL)
    print(Proffesseur)
    input()
    print("                queler Pokemon Veut TU\n1.Salameche\n2.Carapuce\n3.Bulbizare\nQui choisi TU ?")
    print(Proffesseur)
    while True:
        try:
            choix=int(input("1.Salameche\n2.Carapuce\n3.Bulbizard"))
            if choix>=1 and choix<=3:
                if choix==1:
                    pk = Pokemon_Class.Salameche.New_Pokemon_same_espece()
                elif choix==2:
                    pk = Pokemon_Class.Carapuce.New_Pokemon_same_espece()
                else:
                    pk = Pokemon_Class.Bulbizarre.New_Pokemon_same_espece()
                j = Dresseur_Class.Joueur(Nom,[])
                j.ajouter_membre(pk)
                j.money +=10
                return j
            clear()
        except ValueError:
            clear()

def Credit():
    print("Travaile de groupe pour le projet Python paris Ynov Campus fais part\n")
    print("   -Meliha Urlu -> ces ocuper des musics des la classe Item")
    print("   -Bamh Metheri -> ces ocuper de la classe Dresseur deplacement dans la map")
    print("   -Yassine Frikiche  -> ces ocuper de la creation de map avec les events")
    print("   -Yassine Zaoui -> ces ocuper des classe pokemon et Mouv")
    input()
    clear()
def Explication():
    clear()
    print("ce si est un jeux qui essaye de ressembler au jeux pokemon\n qui est un rpg vous commencer l'aventure en choisissant un starter\n puis vous spawnerer sur une map (il y a 5Map) a chaque map un boss le but et de passer tout les boss")
    input()
    clear()



def Jeux():
    son=mettre_music(generique)
    c = ecranAcueil()
    while c != 1:
        if c==2:
            Credit()
        if c==3:
            Explication()
        c = ecranAcueil()
    son=mettre_music(Prof,son)
    Joueur= debutJeux()
    map1.Placement_Dresseur(Joueur,0,9)
    map1.show()
    Joueur.Deplacement_dans_la_Map(map1)

# Jeux()
# Joueur = Dresseur_Class.Joueur("jose",[Pokemon_Class.Papilusion])
# map1.Placement_Dresseur(Joueur,0,9)
# map1.show()1
# Joueur.Deplacement_dans_la_Map(map1)
Jeux()