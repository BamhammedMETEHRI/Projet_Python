#ici ou je teste mes class
# import only system from os
from os import system, name
from re import A
# import sleep to show output for some time period
from time import sleep
from colorama import Fore
from colorama import Style
import Dresseur_Class, Pokemon_Class

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  

bob = Dresseur_Class.Joueur("Yassine",[])

Pokemon_Class.Aficher_Matrice_Des_Type()
map = [
    [Fore.BLACK+"#","#","#","#","#","#","#","#","#","#","#","#"+Style.RESET_ALL],#1
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#2
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," ",Fore.BLUE+"<"+Style.RESET_ALL,Fore.BLACK+"#"+Style.RESET_ALL],#3
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#4
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#5
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#6
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#7
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#8
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#9
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#10
    [Fore.BLACK+"#"+Style.RESET_ALL,Fore.GREEN+"~","~","~","~","~"+Style.RESET_ALL," "," "," "," "," ",Fore.BLACK+"#"+Style.RESET_ALL],#11
    [Fore.BLACK+"#","#","#","#","#","#","#","#","#","#","#","#"+Style.RESET_ALL] #12
    ]
print()
def afficher_map():
    for i in map:
        for j in i:
            print(j,end="")
        print()
afficher_map()

def test(Joueur):#10 1 
    print(Joueur.physique)
    avant = map[10][1]
    print(avant)
    map[10][1] = Fore.GREEN+Joueur.physique
    afficher_map()
    map[10][1] = avant
    avant = map[10][2]
    map[10][2] = Joueur.physique
    afficher_map()
#test(bob)
def Bouger(Joueur):
    x = 1
    y = 10
    avant =map[y][x]
    if x == 1:
        map[y][x] =Fore.GREEN+Joueur.physique
    elif x == 5:
        map[y][x] =Joueur.physique+Style.RESET_ALL
    else:
        map[y][x]=Joueur.physique
    afficher_map()
    while (avant!=(Fore.BLUE+"<"+Style.RESET_ALL)):
        deplacer=input(
            "  "+Fore.LIGHTBLUE_EX+"Z"+Style.RESET_ALL+"  \n"+Fore.LIGHTGREEN_EX+"Q"+Style.RESET_ALL+" "+Fore.LIGHTMAGENTA_EX+"S"+Style.RESET_ALL+" "+Fore.LIGHTYELLOW_EX+"D"+Style.RESET_ALL+"\n"+Fore.LIGHTBLUE_EX+"Z haut"+Style.RESET_ALL+", "+Fore.LIGHTGREEN_EX+"Q a gauche"+Style.RESET_ALL+", "+Fore.LIGHTMAGENTA_EX+"S en bas "+Style.RESET_ALL+"et "+Fore.LIGHTYELLOW_EX+"D a droite "+Style.RESET_ALL+": ")
        clear()
#        sleep(2)
        if deplacer == "Z":
            y -= 1
            if map[y][x] ==(Fore.BLACK+"#"+Style.RESET_ALL) or map[y][x] ==(Fore.BLACK+"#") or map[y][x] ==("#"+Style.RESET_ALL) or map[y][x] ==("#"):
                print("Aie un Mur tu ne peux pas aller par la dcp tu ne bouge pas")
                y +=1
            else :
                map[y+1][x] = avant
                avant = map[y][x] 
        elif deplacer == "Q":
            x -= 1
            if map[y][x] ==(Fore.BLACK+"#"+Style.RESET_ALL) or map[y][x] ==(Fore.BLACK+"#") or map[y][x] ==("#"+Style.RESET_ALL) or map[y][x] ==("#"):
                print("Aie un Mur tu ne peux pas aller par la dcp tu ne bouge pas")
                x +=1
            else :
                map[y][x+1] = avant
                avant = map[y][x] 
                
        elif deplacer == "S":
            y += 1
            if map[y][x] ==(Fore.BLACK+"#"+Style.RESET_ALL) or map[y][x] ==(Fore.BLACK+"#") or map[y][x] ==("#"+Style.RESET_ALL) or map[y][x] ==("#"):
                print("Aie un Mur tu ne peux pas aller par la dcp tu ne bouge pas")
                y -=1
            else :
                map[y-1][x] = avant
                avant = map[y][x] 
                
        elif deplacer == "D":
            x += 1
            if map[y][x] ==(Fore.BLACK+"#"+Style.RESET_ALL) or map[y][x] ==(Fore.BLACK+"#") or map[y][x] ==("#"+Style.RESET_ALL) or map[y][x] ==("#"):
                print("Aie un Mur tu ne peux pas aller par la dcp tu ne bouge pas")
                x -=1
            else :
                map[y][x-1] = avant
                avant = map[y][x]           
        if x == 1:
            map[y][x] =Fore.GREEN+Joueur.physique
        elif x == 5:
            map[y][x] =Joueur.physique+Style.RESET_ALL
        elif avant == (Fore.BLUE+"<"+Style.RESET_ALL):
            map[y][x]=Fore.BLUE+Joueur.physique+Style.RESET_ALL
        else:
            map[y][x]=Joueur.physique
        afficher_map()


        

        
Bouger(bob)
