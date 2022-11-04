class Pokemon:
  def __init__(self, species, type, name, age, gender, move1, move2, move3):
    self.species = species
    self.type = type
    self.name = name
    self.age = age
    self.gender = gender
    self.move1 = move1
    self.move2 = move2
    self.move3 = move3

charmander = Pokemon("CHARMANDER", "Fire", "CHARMANDER", 1, "M", "Growl", "Scratch", "Ember")
squirtle = Pokemon("SQUIRTLE", "Water", "SQUIRTLE", 1, "M", "Tail Whip", "Tackle", "Water Gun")
bulbasaur = Pokemon("BULBASAUR", "Grass", "BULBASAUR", 1, "M", "Growl", "Tackle", "Leech Seed")
rattata = Pokemon("RATTATA", "Normal", "RATTATA", 1, "M", "Tackle", "Tail Whip", "Quick Attack")
pidgey = Pokemon("PIDGEY", "Normal", "PIDGEY", 1, "M", "Gust", "Sand-Attack", "Quick Attack")
caterpie = Pokemon("CATERPIE", "Bug", "CATERPIE", 1, "M", "Tackle", "String Shot", "")
weedle = Pokemon("WEEDLE", "Bug", "WEEDLE", 1, "M", "Poison Sting", "String Shot", "")
nidoranM = Pokemon("NIDORAN", "Poison", "NIDORAN", 1, "M", "Leer", "Tackle", "Horn Attack")
nidoranF = Pokemon("NIDORAN", "Poison", "NIDORAN", 1, "F", "Growl", "Tackle", "Scratch")