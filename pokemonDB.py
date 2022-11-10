import movesDB

class Pokemon:
  def __init__(self, species, type, name, level, gender, move1, move2, move3, hp, attack, defense): #TODO Add Special and Speed
    self.species = species
    self.type = type
    self.name = name
    self.level = level
    self.gender = gender
    self.move1 = move1
    self.move2 = move2
    self.move3 = move3
    self.hp = hp
    self.attack = attack
    self.defense = defense


    

charmander = Pokemon("CHARMANDER", "Fire", "CHARMANDER", 5, "M", movesDB.growl, movesDB.scratch, movesDB.ember, 39, 52, 43)
squirtle = Pokemon("SQUIRTLE", "Water", "SQUIRTLE", 5, "M", movesDB.tailWhip, movesDB.tackle, movesDB.waterGun, 44, 48, 65)
bulbasaur = Pokemon("BULBASAUR", "Grass", "BULBASAUR", 5, "M", movesDB.growl, movesDB.tackle, movesDB.leechSeed, 45, 49, 49)
rattata = Pokemon("RATTATA", "Normal", "RATTATA", 5, "M", movesDB.tackle, movesDB.tailWhip, "Quick Attack", 0, 0, 0)
pidgey = Pokemon("PIDGEY", "Normal", "PIDGEY", 5, "M", "Gust", "Sand-Attack", "Quick Attack", 0, 0, 0)
caterpie = Pokemon("CATERPIE", "Bug", "CATERPIE", 5, "M", movesDB.tackle, "String Shot", "", 0, 0, 0)
weedle = Pokemon("WEEDLE", "Bug", "WEEDLE", 5, "M", "Poison Sting", "String Shot", "", 0, 0, 0)
nidoranM = Pokemon("NIDORAN", "Poison", "NIDORAN", 5, "M", "Leer", movesDB.tackle, "Horn Attack", 0, 0, 0)
nidoranF = Pokemon("NIDORAN", "Poison", "NIDORAN", 5, "F", movesDB.growl, movesDB.tackle, movesDB.scratch, 0, 0, 0)