from pygame import mixer
isExploring = True
isChoosing = True
player_pokedex = []
rival_pokedex = []
mixer.init()
mixer.music.load("SOUND/02 Opening (part 2).mp3")
mixer.music.play()
print("POKéMON Red: Python edition!")
print(">NEW GAME")
print(">OPTION")

option=input("Enter your option_")
if option.upper()=="NEW GAME":
     mixer.init()
     mixer.music.load("SOUND/03 To Bill's Origin ~ From Cerulean.mp3 ")
     mixer.music.play()
     player=[]
     rival=[]
     print("Hello there! Welcome to the world of POKéMON!", end = "")
     input("")
     print("My name is OAK! People call me the POKéMON PROF!", end = "")
     input("")
     print("This world is inhabited by creatures called POKéMON!", end = "")
     input("")
     print("For some people, POKéMON are pets. Others use them for fights", end = "")
     input("")
     print("Myself... I study POKéMON as a profession", end = "")
     input("")
     name=input("First, What is your name?_")
     if name==(""):
          name=("RED")
     else:
          pass
     player.append(name)
     print("Right! So your name is",name+"!", end = "")
     input("")
     print("This is my grand-son. He's been your rival since you were a baby.", end = "")
     input("")
     rname=input("...Erm, what is his name again?_")
     if rname==(""):
          rname=("BLUE")
     else:
          pass
     rival.append(rname)
     print("That's right! I remember now! His name is",rname+"!", end = "")
     input("")
     print(name+"!" , end = "")
     input("")
     print("Your very own POKéMON legend is about to unfold!", end = "")
     input("")
     print("A world of dreams and aventures with POKéMON awaits! Let's go!", end = "")
     input("")
     mixer.music.load("SOUND/50 Pokedex Fanfare 1.mp3")
     mixer.music.play()
     print("...........", end = "")
     input("")
     print("You wake up in your room, you're a boy who just turned 10, which means you're able to get your first POKéMON!", end = "")
     input("")
     print("You've wanted a POKéMON forever! And today's finally the day!", end = "")
     mixer.init()
     mixer.music.load("SOUND/04 Pallet Town's Theme.mp3")
     mixer.music.play()
     input("")
     print("You walk down the stairs, and you're greeted by your mom", end = "")
     input("")
     print("MOM: Right. All boys leave home some day. It said so on TV. ", end = "")
     input("")
     print("PROF.OAK,  next door, is looking for you.", end = "")
     input("")
     print("You step outside your house, as the blinding lights of the outdoors hit, you look around", end = "")
     input("")
     while isExploring == True:
          print("\nWhere will you go now?", end = "")
          input("")
          print(rname+"'s house")
          print("OAK POKéMON RESEARCH LAB")
          print("Wild grass")
          pt=input("Choose where you will go _")
          if pt.lower()==(rname.lower()+"'s house"):
               print("You decide to go to",rname,"'s house. As you walk in, you are greeted by his sister", end = "")
               input("")
               print("Hi",name+"!",rname,"is out at Grandpa's lab.", end = "")
               continue
          if pt.upper()=="OAK POKEMON RESEARCH LAB":
               print("You decide to head straight over to PROF.OAK's lab, just like your mother insisted. As you enter, you see a lot of scientists", end = "")
               input("")
               print("You then walk deeper into the room, just to see",rname)
               input("")
               print(rname+": Yo",name,"Gramps isn't around!", end = "")
               print("Without wasting more time, you head out of the lab in search of him", end = "")
               continue
          if pt.lower()=="wild grass":
               isExploring = False
               print("You notice a patch of tall grass", end = "")
               input("")
               print("It interests you, so you decide to step in the grass", end = "")
     input("")
     print(rname+"'s house (Under dev)")
     print("OAK POKéMON RESEARCH LAB (Not finished)")
     print("Wild grass")
     pt=input("Choose where you will go _")
     if pt.lower()==rname+"'s house":
          print("You decide to go to",rname,"'s house. As you walk in, you are greeted by his sister", end = "")
          input("")
          print("Hi",name+"!",rname,"is out at Grandpa's lab.", end = "")
     if pt.upper()=="OAK POKEMON RESEARCH LAB":
          print("You decide to head straight over to PROF.OAK's lab, just like your mother insisted. As you enter, you see a lot of scientists", end = "")
          input("")
          print("You then walk deeper into the room, just to see",rname, end = "")
          input("")
          print(rname+": Yo",name,"Gramps isn't around!", end = "")
          input("") 
          print("Without wasting more time, you head out of the lab in search of him", end = "")
     if pt.lower()=="wild grass":
          print("You notice a patch of tall grass", end = "")
          input("")
          print("It interests you, so you decide to step in the grass", end = "")
          input("")
          print("But before you can take a step further in-", end = "")
          input("")
          mixer.music.load("SOUND/14 Professor Oak.mp3")
          mixer.music.play()
          print("OAK: Hey! Wait! Don't go out!", end = "")
          input("")
          print("It's unsafe! Wild POKéMON live in tall grass!", end = "")
          input("")
          print("You need your own POKéMON for your protection", end = "")
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
          print("They are inside the POKé BALLs.", end = "")
          input("")
          print("When I was young, I was a serious POKéMON trainer! In my old age, I have only 3 left, but you can have one! Choose!", end = "")
          input("")
          print(rname+": Hey! Gramps! What about me?", end = "")
          input("")
          print("OAK: Be patient!",rname+", you can have one too!", end = "")
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
          print("Which one do you want?", end = "")
          input("")
          print("CHARMANDER, the FIRE lizard POKéMON")
          print("SQUIRTLE, the WATER tinyturtle POKéMON")
          print("BULBASAUR, the GRASS seed POKéMON")
          starter=input("Choose your starter POKéMON_(for now only charmander works)")
     print("But before you can take a step further in-", end = "")
     input("")
     mixer.music.load("SOUND/14 Professor Oak.mp3")
     mixer.music.play()
     print("OAK: Hey! Wait! Don't go out!", end = "")
     input("")
     print("It's unsafe! Wild POKéMON live in tall grass!", end = "")
     input("")
     print("You need your own POKéMON for your proctection", end = "")
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
     print("They are inside the POKé BALLs.", end = "")
     input("")
     print("When I was young, I was a serious POKéMON trainer! In my old age, I have only 3 left, but you can have one! Choose!", end = "")
     input("")
     print(rname+": Hey! Gramps! What about me?", end = "")
     input("")
     print("OAK: Be patient!",rname+", you can have one too!", end = "")
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
     print("Which one do you want?", end = "")
     input("")
     print("CHARMANDER, the FIRE lizard POKéMON")
     print("SQUIRTLE, the WATER tinyturtle POKéMON")
     print("BULBASAUR, the GRASS seed POKéMON")
     while isChoosing == True:
          starter=input("\nChoose your starter POKéMON_")   
          if starter.lower()=="charmander":
               confirm=input("So! You want the fire POKéMON, " + name  + "? [Y/n]")
               if confirm.lower()=="y":
                    player_pokedex.append("CHARMANDER")
                    rival_pokedex.append("SQUIRTLE")
                    isChoosing = False
               else:
                    continue
          if starter.lower()=="squirtle":
               confirm=input("So! You want the water POKéMON, " + name  + "? [Y/n]")
               if confirm.lower()=="y":
                    player_pokedex.append("SQUIRTLE")
                    rival_pokedex.append("BULBASAUR")
                    isChoosing = False
               else:
                    continue
          if starter.lower()=="bulbasaur":
               confirm=input("So! You want the plant POKéMON, " + name  + "? [Y/n]")
               if confirm.lower()=="y":
                    player_pokedex.append("BULBASAUR")
                    rival_pokedex.append("CHARMANDER")
                    isChoosing = False
               else:
                    continue

     print("This POKéMON is really energetic!", end = "")
     input("")
     mixer.music.load("SOUND/51 Pokedex Fanfare 2.mp3")
     mixer.music.play()
     print(name,"received a",player_pokedex[0],"!", end = "")
     input("")
     mixer.music.load("SOUND/31 Oak Research Lab.mp3")
     mixer.music.play()
     print(rname+": I'll take this one then!", end = "")
     input("")
     mixer.music.load("SOUND/51 Pokedex Fanfare 2.mp3")
     mixer.music.play()
     print(rname,"received a",rival_pokedex[0],"!", end = "")
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
     print(rname,"wants to fight!") 
                    
                    
                    
                    
                    
     
          
     
     
     
     
     
     
     
     
