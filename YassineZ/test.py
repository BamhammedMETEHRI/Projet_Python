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
mur= Fore.BLACK+"#"+Style.RESET_ALL
Herbe_All = Fore.GREEN+"~"+Style.RESET_ALL
rien = " "

Pokemon_Class.Aficher_Matrice_Des_Type()
map_Deux =[
    [mur*12],                       #1
    [mur,Herbe_All*5,rien*5,mur],   #2
    [mur,Herbe_All*5,rien*5,mur],   #3
    [mur,Herbe_All*5,rien*5,mur],   #4
    [mur,Herbe_All*5,rien*5,mur],   #5
    [mur,Herbe_All*5,rien*5,mur],   #6
    [mur,Herbe_All*5,rien*5,mur],   #7
    [mur,Herbe_All*5,rien*5,mur],   #8
    [mur,Herbe_All*5,rien*5,mur],   #9
    [mur,Herbe_All*5,rien*5,mur],   #10
    [mur,Herbe_All*5,rien*5,mur],   #11
    [mur*12]                        #12
    ]

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
def afficher_map(world):
    for i in world:
        for j in i:
            print(j,end="")
        print()
afficher_map(map_Deux)

def test(Joueur):#10 1 
    print(Joueur.physique)
    avant = map[10][1]
    print(avant)
    map[10][1] = Fore.GREEN+Joueur.physique
    afficher_map(map)
    map[10][1] = avant
    avant = map[10][2]
    map[10][2] = Joueur.physique
    afficher_map(map)
#test(bob)
def Bouger_anciene_map(Joueur):
    x = 1
    y = 10
    avant =map[y][x]
    if x == 1:
        map[y][x] =Fore.GREEN+Joueur.physique
    elif x == 5:
        map[y][x] =Joueur.physique+Style.RESET_ALL
    else:
        map[y][x]=Joueur.physique
    afficher_map(map)
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
        afficher_map(map)

# def bouger(Joueur):

#Bouger_anciene_map(bob)
print("salut")
print(type(bob)== Dresseur_Class.Joueur)

#                    _M___M_
#                   /       \
#                  /  \   /  \
#     _M____M_    /  °     °  \
#    /²²¨¨¨¨²²\  /      V      \
#   /²²¨¨¨¨¨¨²²\/     WWWWW     \
#  /²²¨¨¨¨¨¨¨¨²²\
# /²²¨¨¨¨¨¨¨¨¨¨²²\
#                    _M___M_
#                   /       \
#                  /  _     _\
#     _M____M_    /  °     °  \
#    /²²¨¨¨¨²²\  /      U      \
#   /²²¨¨¨¨¨¨²²\/     -----     \
#  /²²¨¨¨¨¨¨¨¨²²\
# /²²¨¨¨¨¨¨¨¨¨¨²²\
#                    _M___M_
#                   /       \
#                  / /     \ \
#     _M____M_    /  O    O   \
#    /²²¨¨¨¨²²\  /      -      \
#   /²²¨¨¨¨¨¨²²\/     ~~~~~~    \
#  /²²¨¨¨¨¨¨¨¨²²\
# /²²¨¨¨¨¨¨¨¨¨¨²²\
clear()
s = [Fore.BLUE+"<"+Style.RESET_ALL,">"+Style.RESET_ALL,"V","^"+Style.RESET_ALL]
print(s[1])
clear()
# print("N\{&#x25A0}")
# print("■")
inters=[' ','╴','╷', '┐','╶','─','┌','┬','╵','┘','│','┤','└','┴','├','┼']
print(inters[6],inters[3])
print(inters[12],inters[9])
print()
print(inters[6],inters[5],inters[3])
print(inters[10],inters[0],inters[10])
print(inters[12],inters[5],inters[9])
print()
print(inters[6],inters[7],inters[3])
print(inters[14],inters[15],inters[11])
print(inters[12],inters[13],inters[9])
clear()