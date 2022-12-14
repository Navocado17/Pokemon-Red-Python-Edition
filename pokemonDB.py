import movesDB

class Pokemon:
  def __init__(self, species, type, name, level, move1, move2, move3, move4, baseHP, baseATK, baseDEF, baseSPC, baseSPD, expYield): #TODO Add Special and Speed
    self.species = species
    self.type = type
    self.name = name
    self.level = level
    self.move1 = move1
    self.move2 = move2
    self.move3 = move3
    self.move4 = move4

    self.IVconstant = 15
    self.EVconstant = 0 #this is supposed to be square root of EV divided by 4 but EV doesnt exist yet so this value should work for now
    self.baseHP = baseHP
    self.baseATK = baseATK
    self.baseDEF = baseDEF
    self.baseSPC = baseSPC
    self.baseSPD = baseSPD
    self.hp = round((((baseHP + self.IVconstant) * 2 + self.EVconstant) * level)/100 + level + 10)
    self.attack = round((((baseATK + self.IVconstant) * 2 + self.EVconstant) * level)/100 + 5)
    self.defense = round((((baseDEF + self.IVconstant) * 2 + self.EVconstant) * level)/100 + 5)
    self.special = round((((baseSPC + self.IVconstant) * 2 + self.EVconstant) * level)/100 + 5)
    self.speed = round((((baseSPD + self.IVconstant) * 2 + self.EVconstant) * level)/100 + 5)
    self.expYield = expYield
    self.exp = ((6/5) * (level ** 3)) - (15 * (level ** 2)) + (100 * level) - 140

bulbasaur = Pokemon("BULBASAUR", "Grass", "BULBASAUR", 5, movesDB.tackle, movesDB.growl, movesDB.leech_seed, "", 45, 49, 49, 65, 45, 64)
ivysaur = None
venusaur = None
charmander = Pokemon("CHARMANDER", "Fire", "CHARMANDER", 5, movesDB.scratch, movesDB.growl, movesDB.ember, "", 39, 52, 43, 50, 65, 62)
charmeleon = None
charizard = None
squirtle = Pokemon("SQUIRTLE", "Water", "SQUIRTLE", 5, movesDB.tackle, movesDB.tail_whip, movesDB.water_gun, "", 44, 48, 65, 50, 43, 63)
wartortle = None
blastoise = None
caterpie = Pokemon("CATERPIE", "Bug", "CATERPIE", 5, movesDB.tackle, "String Shot", "", "", 0, 0, 0, 0, 0, 0)
metapod = None
butterfree = None
weedle = Pokemon("WEEDLE", "Bug", "WEEDLE", 5, "Poison Sting", "String Shot", "", "", 0, 0, 0, 0, 0, 0)
kakuna = None
beedrill = None
pidgey = Pokemon("PIDGEY", "Normal", "PIDGEY", 5, "Gust", "Sand-Attack", "Quick Attack", "Agility", 0, 0, 0, 0, 0, 0)
pidgeotto = None
pidgeot = None
rattata = Pokemon("RATTATA", "Normal", "RATTATA", 3, movesDB.tackle, movesDB.tail_whip, "", "", 30, 56, 35, 25, 72, 57)
raticate = None
spearow = None
fearow = None
ekans = None
arbok = None
pikachu = Pokemon("PIKACHU", "Elecric", "PIKACHU", 5, "Thundershock", "growl", "", "", 0, 0, 0, 0, 0, 0)
raichu = None
sandshrew = None
sandslash = None
nidoran_f = Pokemon("NIDORAN", "Poison", "NIDORAN", 5, movesDB.growl, movesDB.tackle, movesDB.scratch, "", 0, 0, 0, 0, 0, 0)
nidoran_n = Pokemon("NIDORAN", "Poison", "NIDORAN", 5, "Leer", movesDB.tackle, "Horn Attack", "", 0, 0, 0, 0, 0, 0)
