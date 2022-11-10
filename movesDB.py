class Move:
  def __init__(self, moveName, movePWR, moveType, movePP): #TODO Add Move Accuracy and Priority and Attribute Moves and Special Moves
    self.moveName = moveName
    self.movesPWR = movePWR
    self.moveType = moveType
    self.moveCharge = movePP

growl = Move("Growl", 0, "Normal", 40)
scratch = Move("Scratch", 40, "Normal", 35)
ember = Move("Ember", 40, "Fire", 25)
tailWhip = Move("Tail Whip", 0, "Normal", 30)
tackle = Move("Tackle", 35, "Normal", 35)
waterGun = Move("Water Gun", 40, "Water", 25)
leechSeed = Move("Leech Seed", 0, "Grass", 10)

#TODO The other pokemon moves in pokemonDB