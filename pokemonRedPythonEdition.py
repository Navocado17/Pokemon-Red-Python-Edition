#IMPORTS
from pygame import mixer
import os
import pokemonDB
import mechanics

#INIT VARIABLES
isDeciding = True
player=[]
money=0
rival=[]
party=[]
player_pokedex = []
rival_pokedex = []

#LEVEL STRUCTURES
def tutorialStagePalletTown():
    isDeciding = True
    while isDeciding == True:
               print("\nWhere will you go now?")
               print(rname+"'s house")
               print("OAK POKéMON RESEARCH LAB")
               print("Tall grass")
               pt=input("Choose where you will go? ▼")
               pt=pt.lower()
               if pt==(rname.lower()+"'s house") or pt==(rname.lower()+"s house"):
                    print("You decide to go to", rname+"'s house. As you walk in, you are greeted by his sister", end = "")
                    input("")
                    print("Hi", name+"!", rname, "is out at Grandpa's lab.", end = "")
                    input("")
                    print("You decide to go back out", end = "")
                    input("")
                    continue
               if pt=="oak pokémon research lab" or pt=="oak pokemon research lab" or pt=="research lab" or pt=="lab":
                    print("You decide to head straight over to PROF.OAK's lab, just like your mother insisted. As you enter, you see a lot of scientists", end = "")
                    input("")
                    print("You then walk deeper into the room, just to see",rname, end = "")
                    input("")
                    print(rname+": Yo", name+"!", "Gramps isn't around!", end = "")
                    input("")
                    print("Without wasting more time, you head out of the lab in search of him", end = "")
                    input("")
                    continue
               if pt=="tall grass":
                    isDeciding = False
                    print("Wandering around in search of professor Oak, you stumble a patch of tall grass", end = "")
                    input("")
                    print("It interests you, so you decide to step in the grass", end = "")

def palletTown():
    mixer.music.load("SOUND/04 Pallet Town's Theme.mp3")
    mixer.music.play()
    isDeciding = True
    while isDeciding == True:
                    mixer.music.load("SOUND/04 Pallet Town's Theme.mp3")
                    mixer.music.play()
                    print("\nNow in Pallet Town!")
                    print("Where will you go now?")
                    print("Your house")
                    print(rname+"'s house")
                    print("OAK POKéMON RESEARCH LAB")
                    print("ROUTE 1")
                    pt=input("Choose where you will go? ▼")
                    pt=pt.lower()
                    if pt==(rname.lower()+"'s house") or pt==(rname.lower()+"s house"):
                         print("You decide to go to", rname+"'s house. As you walk in, you are greeted by his sister", end = "")
                         input("")
                         print("Hi", name+"!", rname, "is out at Grandpa's lab.", end = "")
                         input("")
                         print("You decide to go back out", end = "")
                         input("")
                         continue
                    if pt=="oak pokémon research lab" or pt=="oak pokemon research lab" or pt=="research lab" or pt=="lab":
                         print("You decide to head straight over to PROF.OAK's lab, just like your mother insisted. As you enter, you see a lot of scientists", end = "")
                         input("")
                         print("You then walk deeper into the room, just to see",rname, end = "")
                         input("")
                         print(rname+": Yo", name+"!", "Gramps isn't around!", end = "")
                         input("")
                         print("Without wasting more time, you head out of the lab in search of him", end = "")
                         input("")
                         continue
                    if pt=="route 1":
                         isDeciding = False
                         route1()
                         
def route1():
    isDeciding = True
    print("\nNow in ROUTE 1!")
    while isDeciding == True:
        mixer.music.load("SOUND/18 The Road to Viridian City ~ from Pallet.mp3")
        mixer.music.play()
        print("Where will you go now?")
        print("Pallet Town")
        print("Viridian City")
        print("Tall Grass")
        pt=input("Choose where you will go ▼")
        pt=pt.lower()
        if pt == "pallet town":
            palletTown()
        if pt == "viridian city":
            print("After walking a bit you step into 'The Eternally Green Paradise', Viridian city!")
            viridianCity()
        if pt == "tall grass":
            isWon = mechanics.battle(party[0], pokemonDB.rattata, 3, 1)

def viridianCity():
    mixer.music.load("SOUND/07 Pewter City's Theme.mp3")
    mixer.music.play()
    print("\nNow in Viridian City!")
    parcelQuest=True
    print("Where will you go now? ▼")
    print("POKéMON Center")
    print("POKéMON Mart")
    print("Route 2")
    print("Route 22")
    print("POKéMON Gym")
    print("Route 1") 
    vc=input("Choose where you will go ▼")
    if vc.lower() == "pokemon center":
        mixer.music.load("SOUND/05 Pokemon Center.mp3")
        mixer.music.play()
        print("You enter the POKéMON center")
        input()
        print("Heal pokemon")
        print("Use PC")
        pokecenter=input("What would you like to do in the POKéMON center?")
        if pokecenter.lower()=="heal" or pokecenter.lower()=="heal pokemon":
            print("You walk over and talk to nurse joy",end="")
            input()
            print("Joy: Welcome to our POKéMON CENTER! We heal your POKéMON back to perfect health!",end="")
            input()
            heal=input("Shall we heal your POKéMON? [Heal/cancel]")
            if heal.lower()=="heal" or heal.lower()=="yes":
                print("OK. We'll need your POKéMON.",end="")
                input()
                print("*pokemon heals* (under dev)",end="")
                input()
                print("Thank you! Your POKéMON are fighting fit! We hope to see you again!",end="")
                input()
                viridianCity()
        if pokecenter.lower()=="pc" or pokecenter.lower()=="use pc":
            print("You booted up the PC. It died. (under development",end="")
            input()
            print("You walk out of the POKéMON center",end="")
            viridianCity()
    if vc.lower()=="pokemon mart" or vc.lower=="mart":
        mixer.music.load("SOUND/05 Pokemon Center.mp3")
        mixer.music.play()
        while parcelQuest==True:
            print("As you step in the POKéMON mart, you grab the attention of the mart clerk",end="")
            input()
            print("Clerk: Hey! You came from PALLET TOWN?",end="")
            input()
            print("you walk over to the clerk",end="")
            input()
            print("You know PROF. OAK, right? His order came in. Will you take it to him?",end="")
            input()
            print(name,"got OAK's PARCEL!",end="")
            input()
            print("Clerk: Okay! Say hi to PROF. OAK for me!",end="")
            input()
            print("You step out of the POKéMON mart and make your way to deliver the parcel to professor oak",end="")
            viridianCity()

    if vc.lower()=="route 2":
        while parcelQuest==True:
            print("You try to make your way over to route 2, but it appears there is an old man lying on the road, blocking the path",end="")
            input()
            print("Old man: You can't go through here! This is private property!",end="")
            input()
            print("Grand Daughter: Oh Grandpa! Don't be so mean! He hasn't had his coffee yet.",end="")

    if vc.lower()=="route 1":
        print("You decide to head back to route 1")
        route1()
            
            
            
    
    
    
#GAME START
mixer.init()
mixer.music.load("SOUND/01 Opening (part 1).mp3")
mixer.music.play()
print("11-A\n\n")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.")
print("\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |")
print(" \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |")
print("   \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     |")
print("     \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |")
print("      \\    \\ \\      /       `-.`.___,-' |  |\\  /| \\      /  | |   |")
print("       \\    \\ `.__,'|  |`-._    `|      |__| \\/ |  `.__,'|  | |   |")
print("        \\_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("                          Red Python Edition\n\n                                          ")
print("                            ⠀⠀⠀⣀⠔⠒⠒⠂⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("                            ⠀⠀⢰⢅⠀⠀⢀⣤⢄⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("                            ⠀⠀⣾⡆⠀⠀⠀⢸⠼⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("                            ⠀⢀⢗⠂⠀⠀⡀⠈⢉⠅⠇⠀⠀⠀⠀⠀⠀⢠⣄⠀")
print("                            ⠀⠈⠢⣓⠔⣲⠖⡫⠊⡘⠀⠀⠀⠀⠀⠀⠲⡟⠙⡆")
print("                            ⠀⢀⢀⠠⠘⣇⠖⢄⠀⠉⠐⠠⢄⣀⡀⠀⠜⠀⠀⣁")
print("                            ⠘⣏⣀⣀⣀⠃⠀⠀⠑⣀⣀⣀⣰⠼⠇⠈⠄⠀⠈⡻")
print("                            ⠀⠁⠀⠀⢰⠀⠀⠀⠀⠠⠀⠡⡀⠀⠀⠀⠈⡖⠚⠀")
print("                            ⠀⠀⠀⡠⠘⠀⠀⠀⠀⢀⠆⠀⠐⡀⠀⡠⠊⣠⠀⠀")
print("                            ⠀⠀⢐⠀⠀⠁⡀⠀⠀⢀⠀⠀⠀⢨⠀⡠⡴⠂⠀⠀")
print("                            ⠀⢀⣨⣤⠀⠀⠐⠃⠐⠚⠢⠀⠀⠈⠑⠊⠀⠀⠀")
print("                            ⠀⠘⠓⠋⠉⠁⠀⠀⠀⠀⠀⠓⢶⡾⠗⠀⠀⠀⠀")

input("\n                        (Press Enter To Continue)")

mixer.music.load("SOUND/02 Opening (part 2).mp3")
mixer.music.play()
while isDeciding == True:
     print("\n\nPOKéMON Red: Python edition!")
     print(">NEW GAME")
     print(">OPTION")
 
     option=input("Enter your option ▼")
     option = option.lower()
     if option=="new game" or option=="newgame" or option=="ng" or option=="new" or option=="n":
          mixer.init()
          mixer.music.load("SOUND/03 To Bill's Origin ~ From Cerulean.mp3 ")
          mixer.music.play()
          print("Hello there! Welcome to the world of POKéMON!", end = "")
          input("")
          print("My name is OAK! People call me the POKéMON PROF!", end = "")
          input("")
          print("This world is inhabited by creatures called POKéMON!", end = "")
          input("")
          print("For some people, POKéMON are pets. Others use them for fights.", end = "")
          input("")
          print("Myself... I study POKéMON as a profession.", end = "")
          input("")
          name=input("First, what is your name? ▼")
          if name==(""):
               name=("RED")
          else:
               pass
          player.append(name)
          print("Right! So your name is", name+"!", end = "")
          input("")
          print("This is my grand-son. He's been your rival since you were a baby.", end = "")
          input("")
          rname=input("...Erm, what is his name again?_")
          if rname==(""):
               rname=("BLUE")
          else:
               pass
          rival.append(rname)
          print("That's right! I remember now! His name is", rname+"!", end = "")
          input("")
          print(name+"!", end = "")
          input("")
          print("Your very own POKéMON legend is about to unfold!", end = "")
          input("")
          print("A world of dreams and aventures with POKéMON awaits! Let's go!", end = "")
          input("")
          mixer.music.load("SOUND/50 Pokedex Fanfare 1.mp3")
          mixer.music.play()
          print("..........", end = "")
          input("")
          print("You wake up in your room, you're a boy who just turned 10, which means you're able to get your first POKéMON!", end = "")
          input("")
          print("You've wanted a POKéMON forever! And today's finally the day!", end = "")
          mixer.music.load("SOUND/04 Pallet Town's Theme.mp3")
          mixer.music.play()
          input("")
          print("You walk down the stairs, and you're greeted by your mom", end = "")
          input("")
          print("MOM: Right. All boys leave home some day. It said so on TV. ", end = "")
          input("")
          print("PROF.OAK, next door, is looking for you.", end = "")
          input("")
          print("You step outside your house, as the blinding lights of the outdoors hit, you look around", end = "")
          input("")
          tutorialStagePalletTown()
          input("")
          print("But before you can take a step further in-", end = "")
          input("")
          mixer.music.load("SOUND/14 Professor Oak.mp3")
          mixer.music.play()
          print("OAK: Hey! Wait! Don't go out!", end = "")
          input("")
          print("It's unsafe! Wild POKéMON live in tall grass!", end = "")
          input("")
          print("You need your own POKéMON for your protection.", end = "")
          input("")
          print("I know! Here, come with me!", end = "")
          input("")
          print("Professor Oak takes you to his lab", end = "")
          input("")
          mixer.music.load("SOUND/31 Oak Research Lab.mp3")
          mixer.music.play()
          print("You see",rname,"impatiently waiting")
          print(rname+": Gramps! I'm fed up with waiting!", end = "")
          input("")
          print("OAK:",rname+"? Let me think...", end = "")
          input("")
          print("Oh, that's right, I told you to come! Just wait!", end = "")
          input("")
          print("Here,",name+"!", end = "")
          input("")
          print("There are 3 POKéMON here!", end = "")
          input("")
          print("Haha! They are inside the POKé BALLs.", end = "")
          input("")
          print("When I was young, I was a serious POKéMON trainer! In my old age, I have only 3 left, but you can have one! Choose!", end = "")
          input("")
          print(rname+": Hey! Gramps! What about me?", end = "")
          input("")
          print("OAK: Be patient!", rname+", you can have one too!", end = "")
          input("")
          print("On the table to your right, you see 3 POKéBALLs, each containing a strong unique POKéMON", end = "")
          input("")
          print("The first ball contains CHARMANDER, the FIRE lizard POKéMON", end = "")
          input("")
          print("The second ball contains SQUIRTLE, the WATER tinyturtle POKéMON", end = "")
          input("")
          print("The third ball contains BULBASAUR, the GRASS seed POKéMON", end = "")
          input("")
          print("You can choose between any of the 3 POKéMON on the table", end = "")
          input("")
          print("\nWhich one do you want?")
          print("CHARMANDER, the FIRE lizard POKéMON")
          print("SQUIRTLE, the WATER tinyturtle POKéMON")
          print("BULBASAUR, the GRASS seed POKéMON")
          isDeciding = True
          while isDeciding == True:
               starter=input("\nChoose your starter POKéMON ▼")
               if starter.lower()=="charmander":
                    confirm=input("So! You want the fire POKéMON, CHARMANDER? [>YES/>NO]")
                    if confirm.lower()=="yes" or confirm.lower()=="y":
                         player_pokedex.append(pokemonDB.charmander)
                         rival_pokedex.append(pokemonDB.squirtle)
                         isDeciding = False
                    else:
                         continue
               if starter.lower()=="squirtle":
                    confirm=input("So! You want the water POKéMON, SQUIRTLE? [>YES/>NO]")
                    if confirm.lower()=="yes" or confirm.lower()=="y":
                         player_pokedex.append(pokemonDB.squirtle)
                         rival_pokedex.append(pokemonDB.bulbasaur)
                         isDeciding = False
                    else:
                         continue
               if starter.lower()=="bulbasaur":
                    confirm=input("So! You want the plant POKéMON, BULBASAUR? [>YES/>NO]")
                    if confirm.lower()=="yes" or confirm.lower()=="y":
                         player_pokedex.append(pokemonDB.bulbasaur)
                         rival_pokedex.append(pokemonDB.charmander)
                         isDeciding = False
                    else:
                         continue

          party.append(player_pokedex[0])
          print("This POKéMON is really energetic!", end = "")
          input("")
          mixer.music.load("SOUND/51 Pokedex Fanfare 2.mp3")
          mixer.music.play()
          print(name,"received a",player_pokedex[0].species+"!", end = "")
          input("")
          mixer.music.load("SOUND/31 Oak Research Lab.mp3")
          mixer.music.play()
          nick = input("Do you want to give a nickname to " + player_pokedex[0].species +"? (>YES/>NO)")
          if nick.lower() == "yes" or nick.lower()=="y":
               player_pokedex[0].name = input("Enter Nickname for " + player_pokedex[0].species + ": ")      
          print(rname+": I'll take this one then!", end = "")
          input("")
          mixer.music.load("SOUND/51 Pokedex Fanfare 2.mp3")
          mixer.music.play()
          print(rname,"received a",rival_pokedex[0].species+"!", end = "")
          input("")
          mixer.music.load("SOUND/31 Oak Research Lab.mp3")
          mixer.music.play()
          print("As you're about to walk out of the lab, extremely excited,",rname,"stops you", end = "")
          input("")
          mixer.music.load("SOUND/15 Rival Appears.mp3")
          mixer.music.play()
          print(rname+": Wait",name+"!", end = "")
          input("")
          print("Let's check out our POKéMON!", end = "")
          input("")
          print("Come on, I'll take you on!", end = "")
          input("")
          print(rname,"approaches you, and you engage in your first POKéMON BATTLE!", end = "")
          input("")
          mixer.music.load("SOUND/23 Battle (VS Trainer).mp3")
          mixer.music.play()
          print(rname,"wants to fight!", end = "")
          input("")
          print(rname,"sent out",rival_pokedex[0].species+"!", end = "")
          input("")
          print("Go!",player_pokedex[0].name+"!")
          IsWon=mechanics.battle(party[0], rival_pokedex[0], 5, 2)
          if IsWon == True:
               print(rname+": WHAT? Unbelievable!", end = "")
               input("")
               print("I picked the wrong POKéMON!",end = "")
               input("")
               print(name,"got 175₽ for winning!", end = "")
               input("")
               print(rname+": Okay! I'll make my POKéMON fight to toughen it up!", end = "")
               input("")
               print(name+"! Gramps! Smell you later!", end = "")
               mixer.music.load("SOUND/15 Rival Appears.mp3")
               mixer.music.play()
               input("")
               print(rname,"marches out of the Lab, frustrated but determined.", end = "")
          if IsWon == False:
               print(rname+": Yeah! Am I great or what?", end = "")
               input("")
               print(rname+": Okay! I'll make my POKéMON fight to toughen it up!", end = "")
               input("")
               print(name+"! Gramps! Smell you later!", end = "")
               mixer.music.load("SOUND/15 Rival Appears.mp3")
               mixer.music.play()
               input("")
               print(rname,"marches out of the Lab, cocky and fullfiled", end = "")
               input("")
          mixer.music.load("SOUND/31 Oak Research Lab.mp3")
          mixer.music.play()
          print("You walk over to Professor OAK after the fight")
          input("")
          print("OAK:",name+", raise your young POKéMON by making it fight!", end = "")
          input("")
          print("So, you walk out of the lab, and set out on your Pokémon journey")
          palletTown()
          
          













