class Move:
  def __init__(self, moveName, movePWR, moveType, movePP): #TODO Add Move Accuracy and Priority and Attribute Moves and Special Moves
    self.moveName = moveName
    self.movePWR = movePWR
    self.moveType = moveType
    self.movePP = movePP

"""
absorb =
acid =
acid armor =
agility =
amnesia =
aurora beam =
barrage =
barrier =
bide =
bind =
bite =
blizzard =
body slam =
bone club =
bonemerang =
bubble =
bubblebeam =
clamp =
comet punch =
confuse ray =
confusion =
constrict =
conversion =
counter =
crabhammer =
cut =
defense curl =
dig =
disable =
dizzy punch =
double kick =
double team =
double-edge =
doubleslap =
dragon rage =
dream eater =
drill peck =
earthquake =
egg bomb =
"""
ember = Move("Ember", 40, "Fire", 25)
"""
explosion =
fire blast =
fire punch =
fire spin =
fissure =
flamethrower =
flash =
fly =
focus energy =
fury attack =
fury swipes =
glare =
"""
growl = Move("Growl", 0, "Normal", 40)

scratch = Move("Scratch", 40, "Normal", 35)
tailWhip = Move("Tail Whip", 0, "Normal", 30)
tackle = Move("Tackle", 35, "Normal", 35)
waterGun = Move("Water Gun", 40, "Water", 25)
leechSeed = Move("Leech Seed", 0, "Grass", 10)

#TODO The other pokemon moves in pokemonDB
