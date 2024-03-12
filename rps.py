import os
os.system("cls")
import time
from colors import bcolors
from rps_functions import *
from msvcrt import getwch
import random
from rps_functions import hand

wins = 0
losses = 0
ties = 0
turns = 0

keys=["R", "P", "S","Q", "N", "1", "2", "3"]

def newgame():
    ties,wins,turns,losses

#en funktion som printar ut välkommsmenyn
startup()

#funktion som printar ut det olika alternatiyven man har 
menu()

#huvudloop  
while True:
    while True:
        human_choice = getwch().upper()

        if human_choice in keys:
            break

    os.system("cls")

    ai_choice = random.randint(1, 3)

    #ai är vad hand returnerar av ai choice
    ai = hand(ai_choice)


    human=hand(human_choice)

    #printar menyn som visar vilka alternativ man har när programmet är igång
    menu()

    #hand_icon är en funktion som printar sten,sax eller påse beroende på vad ai är
    hand_icon(ai)
    
    print(f"AI valde:" + ai)


    hand_icon(human)

    print(f"Du valde:" + human)

    if human == ai:
      
        ties +=1
        print(bcolors.YELLOW + "Det blev lika"  + bcolors.DEFAULT)

    elif human=="Sten":
        if ai =="Sax":
            wins +=1
            print(bcolors.BLUE + "Du vann!" + bcolors.DEFAULT)
        elif ai=="Påse":
            print(bcolors.RED + "Du förlorade!" + bcolors.DEFAULT)
            losses +=1

    elif human=="Sax":
        if ai=="Sten":
            losses+=1
            print(bcolors.RED + "Du förlorade!" + bcolors.DEFAULT)
        elif ai=="Påse":
            wins+=1
            print(bcolors.BLUE + "Du vann!" + bcolors.DEFAULT)

    elif human=="Påse":
        if ai=="Sten":
            wins+=1
            print(bcolors.BLUE + "Du vann!" + bcolors.DEFAULT)
        elif ai =="Sax":
            print(bcolors.RED + "Du förlorade" + bcolors.DEFAULT) 
            losses +=1

    elif human=="Quit":
        os.system("cls")
        print(f"{bcolors.YELLOW}Slutligt Resultat:\nties={ties}\nwins={wins}\nturns={turns}\nlosses={losses}\n" + bcolors.DEFAULT)
        exit()
    
    elif human=="New_game":  
        time.sleep(0.5)
        wins=0
        losses=0 
        ties=0 
        turns=-1

    turns+=1

    #printar slutresultat om human=="New_game"
    print(f"\n{bcolors.GREEN}ties={ties} wins={wins} turns={turns} losses={losses}"  + bcolors.DEFAULT)