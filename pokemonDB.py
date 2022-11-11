import movesDB

class Pokemon:
  def __init__(self, species, type, name, level, move1, move2, move3, move4, hp, attack, defense, special, speed): #TODO Add Special and Speed
    self.species = species
    self.type = type
    self.name = name
    self.level = level
    self.move1 = move1
    self.move2 = move2
    self.move3 = move3
    self.move4 = move4
    self.hp = hp
    self.attack = attack
    self.defense = defense

    self.special = special
    self.speed = speed


    
charmander = Pokemon("CHARMANDER", "Fire", "CHARMANDER", 5, movesDB.scratch, movesDB.growl, movesDB.ember, "Smokescreen", 19, 11, 10, 11, 12)
squirtle = Pokemon("SQUIRTLE", "Water", "SQUIRTLE", 5, movesDB.tackle, movesDB.tail_whip, movesDB.water_gun, "bubble", 20, 10, 12, 11, 10)
bulbasaur = Pokemon("BULBASAUR", "Grass", "BULBASAUR", 5, movesDB.tackle, movesDB.growl, movesDB.leech_seed, movesDB.vine_whip, 20, 10, 10, 13, 10)
rattata = Pokemon("RATTATA", "Normal", "RATTATA", 5, movesDB.tackle, movesDB.tail_whip, "Quick Attack", "bite", 0, 0, 0, 0, 0)
pidgey = Pokemon("PIDGEY", "Normal", "PIDGEY", 5, "Gust", "Sand-Attack", "Quick Attack", "Agility", 0, 0, 0, 0, 0)
caterpie = Pokemon("CATERPIE", "Bug", "CATERPIE", 5, movesDB.tackle, "String Shot", "", "", 0, 0, 0, 0, 0)
weedle = Pokemon("WEEDLE", "Bug", "WEEDLE", 5, "Poison Sting", "String Shot", "", "", 0, 0, 0, 0, 0)
pikachu = Pokemon("PIKACHU", "Elecric", "PIKACHU", 5, "Thundershock", "growl", "", "", 0, 0, 0, 0, 0)
nidoranM = Pokemon("NIDORAN", "Poison", "NIDORAN", 5, "Leer", movesDB.tackle, "Horn Attack", "", 0, 0, 0, 0, 0)
nidoranF = Pokemon("NIDORAN", "Poison", "NIDORAN", 5, movesDB.growl, movesDB.tackle, movesDB.scratch, "", 0, 0, 0, 0, 0)
