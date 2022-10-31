from pygame import mixer
mixer.init()
mixer.music.load("SOUND/02 Opening (part 2).mp3")
mixer.music.play()
print("POKéMON Red Python edition!")
print("1.CONTINUE")
print("2.NEW GAME")
print("3.OPTION")

option=int(input("Enter your option:"))
if option==2:
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
     name=input("First, What is your name? _")
     if name==(""):
          name=("RED")
     else:
          pass
     player.append(name)
     print("Right! So your name is",name+"!", end = "")
     input("")
     print("This is my grand-son. He's been your rival since you were a baby.", end = "")
     input("")
     rname=input("...Erm, what is his name again?")
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
     print("A world of dreams and aventures with POKéMON awaits! Let's go!")
     print(player)
     
     
     
     
     
