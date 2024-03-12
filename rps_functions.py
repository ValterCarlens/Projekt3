import os
from colors import bcolors
os.system("cls")


#ikoner
    
def hand_icon(hand):
    if hand == "Sten": 
        print("""
   _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/
""")
        
    elif hand == "Sax":
        print("""
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/
""")

    elif hand =="Påse":
        print("""
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/
"""  )

# startup program
        
def startup():
    print( bcolors.YELLOW + 
    """
                ====;'{Welcome TO}';===
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~ ________           ________         ________      ~
    ~|\   __  \         |\   __  \       |\   ____\     ~
    ~\ \  \|\  \        \ \  \|\  \      \ \  \___|_    ~
    ~ \ \   _  _\        \ \   ____\      \ \_____  \   ~
    ~  \ \  \\  \|  ___   \ \  \___| ___   \|____|\  \  ~
    ~   \ \__\\ _\ |\__\   \ \__\   |\__\    ____\_\  \ ~
    ~    \|__|\|__|\|__|    \|__|   \|__|   |\_________\~
    ~                                       \|_________|~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                V1.0 By Valter Carlens
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        (R)ock, (P)aper, (S)cissors, (Q)uit (N)ew_game
    """+ bcolors.DEFAULT ) 


def hand(choice):
    if choice == "R" or choice=="1" or choice==1:
        return "Sten"
    
    elif choice =="S" or choice=="2" or choice==2:
        return "Sax"
    
    elif choice == "P" or choice=="3" or choice==3:
        return "Påse"
    
    elif choice =="Q" or choice=="":
        return "Quit"
    
    elif choice=="N":
        return "New_game"
    

def menu():
    print(bcolors.YELLOW + """
---------------------------------------------
(R)ock, (P)aper, (S)cissors (Q)uit (N)ew_game
""" + bcolors.DEFAULT)