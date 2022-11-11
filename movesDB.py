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
"""
growth =
guillotine =
gust =
harden =
haze =
headbutt =
hi jump kick =
horn attack =
horn drill =
hydro pump =
hyper beam =
hyper fang =
hypnosis =
ice beam =
ice punch =
jump kick =
karate chop =
kinesis =
leech life =
"""
leechSeed = Move("Leech Seed", 0, "Grass", 10)
"""
leer =
lick =
light screen =
lovely kiss =
low kick =
meditate =
mega drain =
mega kick =
mega punch =
metronome =
mimic =
minimize =
mirror move =
mist =
night shade =
pay day =
peck =
petal dance =
pin missile =
poison gas =
poison sting =
poisonpowder =
pound =
psybeam =
psychic =
psywave =
quick attack =
rage =
razor leaf =
razor wind =
recover =
reflect =
rest =
roar =
rock slide =
rock throw =
rolling kick =
sand-attack =
"""
scratch = Move("Scratch", 40, "Normal", 35)
"""
screech =
seismic toss =
selfdestruct =
sharpen =
sing =
skull bash =
sky attack =
slam =
slash =
sleep powder =
sludge =
smog =
smokescreen =
softboiled =
solarbeam =
sonicboom =
spike cannon =
splash =
spore =
stomp =
strength =
string shot =
struggle =
stun spore =
submission =
substitute =
super fang =
supersonic =
surf =
swift =
swords dance =
"""
tackle = Move("Tackle", 35, "Normal", 35)
tailWhip = Move("Tail Whip", 0, "Normal", 30)
"""
take down =
teleport =
thrash =
thunder =
thunder wave =
thunderbolt =
thunderpunch =
thundershock =
toxic =
transform =
tri attack =
twineedle =
vicegrip =
vine whip =
"""
waterGun = Move("Water Gun", 40, "Water", 25)
"""
waterfall =
whirlwind =
wing attack =
withdraw =
wrap =
"""

#TODO The other pokemon moves in pokemonDB
