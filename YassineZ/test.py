# 
# 
#                This fichier is not important anymore
# 
# 
# 
#ici ou je teste mes class
# import only system from os
from os import system, name
from re import A
# import sleep to show output for some time period
from time import sleep
from colorama import Fore
from colorama import Style
import Dresseur_Class, Pokemon_Class,map_Class,Mouv_Class


######################################################################################################################
MAX_LIFE="                   _M___M_\n                  /       \\\n                 /  \   /  \\\n    _M____M_    /  °     °  \\\n   /²²¨¨¨¨²²\  /      V      \\\n  /²²¨¨¨¨¨¨²²\/     WWWWW     \\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
MID_LIFE="                   _M___M_\n                  /       \\\n                 /  _     _\\\n    _M____M_    /  °     °  \\\n   /²²¨¨¨¨²²\  /      U      \\\n  /²²¨¨¨¨¨¨²²\/     -----     \\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
LOW_LIFE = "                   _M___M_\n                  /       \\\n                 / /     \ \\\n    _M____M_    /  O    O   \\\n   /²²¨¨¨¨²²\  /      -      \\\n  /²²¨¨¨¨¨¨²²\/     ~~~~~~    \\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
DEAD="                   _M___M_\n                  /       \\\n                 /         \\\n    _M____M_    /  X    X   \\\n   /²²¨¨¨¨²²\  /             \\\n  /²²¨¨¨¨¨¨²²\/     ::::      \\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
CAPTURE_ON="\n                \n            \n    _M____M_    \n   /²²¨¨¨¨²²\        ●\n  /²²¨¨¨¨¨¨²²\\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
CAPTURE_OFF="\n                \n            \n    _M____M_    \n   /²²¨¨¨¨²²\        ❍\n  /²²¨¨¨¨¨¨²²\\\n /²²¨¨¨¨¨¨¨¨²²\\\n/²²¨¨¨¨¨¨¨¨¨¨²²\\"
#######################################################################################################################################
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
###############################################################################################################################################################
Griffe = Mouv_Class.Mouv("Griffe","Normal",0,100,35,40,None,"Lacère l'ennemi avec des griffes acérées pour lui infliger des dégâts.")


Salameche = Pokemon_Class.Pokemon("Salameche",["Feu"],)

############################################################################################################################################################
def COMBAT(map,Joueur,Adverser=None,Sauvage=None):
    print(map,Joueur,Adverser,Sauvage)
# clear()
# s = [Fore.RED+"<"+Style.RESET_ALL,Fore.RED+"^"+Style.RESET_ALL,Fore.RED+">"+Style.RESET_ALL,Fore.RED+"V"+Style.RESET_ALL]
# print(s[0]+s[1]+s[2]+s[3])

# # print("N\{&#x25A0}")
# # print("■")
# inters=[' ','╴','╷', '┐','╶','─','┌','┬','╵','┘','│','┤','└','┴','├','┼']
# print(inters[6],inters[3])
# print(inters[12],inters[9])
# print()
# print(inters[6],inters[5],inters[3])
# print(inters[10],inters[0],inters[10])
# print(inters[12],inters[5],inters[9])
# print()
# print(inters[6],inters[7],inters[3])
# print(inters[14],inters[15],inters[11])
# print(inters[12],inters[13],inters[9])
