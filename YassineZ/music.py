import pygame

window_resolution = (640,480)
launched = True
#PK sa marche pas j'ai fais avec playaudio mais sa freez bruh 
pygame.init()
pygame.display.set_caption("Python - jouer du son")
window_surface = pygame.display.set_mode(window_resolution)
music = pygame.mixer.Sound('music.wav')#mp3 sa marche pas
"""
<sound>.play(loop = 0 , time = 0, fadein = 0)
    .stop()
    .fadeout(ms)
    .set_volume(0.0 -> 1.0)
    .get_volume()
    .get_lenght(s)
"""
music.play(0,50000)
print("salut")
pygame.display.flip()

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched= False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                music.stop()
            