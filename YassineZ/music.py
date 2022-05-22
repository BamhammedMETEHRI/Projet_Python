import pygame
from time import sleep
#PK sa marche pas j'ai fais avec playaudio mais sa freez bruh 
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
    music.play(0)
    pygame.display.flip()
    return music
generique = 'music\generique.wav'
combat_pokemon= "music\combat_dresseur.wav"
combat_dresseur = "music\combat_pokemon.wav"
route00 = "music\port_pokemon.wav"
route01 = "music\\route_228.wav"
a =None
# a =mettre_music(generique,a)
# sleep(1)
# a =mettre_music(combat_dresseur,a)
# sleep(1)
# a=mettre_music(combat_pokemon,a)
# sleep(1)
# a=mettre_music(route00,a)
# sleep(1)
# a=mettre_music(route01,a)
while launched:

    stop= input("envoie rien pour stoper ou une chiffre entre 1 et 5 pour choisir ta musique : ")
    if stop == "":
        launched = False
    elif stop == "1":
        a =mettre_music(generique,a)
    elif stop == "2":
        a =mettre_music(combat_dresseur,a)
    elif stop == "3":
        a=mettre_music(combat_pokemon,a)
    elif stop == "4":
        a=mettre_music(route00,a)
    elif stop == "5":
        a=mettre_music(route01,a)
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         launched= False

            