import mechanics
import pokemonDB
from pokemonRedPythonEdition import name, rname, money, party

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
               if pt=="oak pokémon research lab" or pt=="oak pokemon research lab":
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
    isDeciding = True
    while isDeciding == True:
                    print("\nWhere will you go now?")
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
                    if pt=="oak pokémon research lab" or pt=="oak pokemon research lab":
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
    print("Now in ROUTE 1!")
    while isDeciding == True:
        print("\nWhere will you go now?")
        print("Pallet Town")
        print("Viridian City")
        print("Tall Grass")
        pt=input("Choose where you will go? ▼")
        pt=pt.lower()
        if pt == "Pallet Town":
            palletTown()
        if pt == "Viridian City":
            print("Under Development!")
        if pt == "Tall Grass":
            mechanics.battle(party[0], pokemonDB.rattata)

               