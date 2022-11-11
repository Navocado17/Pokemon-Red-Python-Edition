from pygame import mixer
mixer.init()

def battle(playerPokemon, enemyPokemon):
     while playerPokemon.hp > 0 and enemyPokemon.hp > 0:
          print("\n"+playerPokemon.name + " - HP: " + str(playerPokemon.hp))
          print(enemyPokemon.name + " - HP: " + str(enemyPokemon.hp))
          print(">FIGHT  >PkMn \n>ITEM  >RUN")
          input("")
          #Players Turn
          isChoosing = True
          while isChoosing == True:
               print("Moves:", playerPokemon.move1.moveName +",", playerPokemon.move2.moveName+",", playerPokemon.move3.moveName)
               selectedMove = input("Select A Move: ")
               if selectedMove.lower() == playerPokemon.move1.moveName.lower():
                    currentMovePower = playerPokemon.move1.movePWR
                    type = playerPokemon.move1.moveType
                    playerPokemon.move1.movePP = playerPokemon.move1.movePP - 1
                    isChoosing = False
               elif selectedMove.lower() == playerPokemon.move2.moveName.lower():
                    currentMovePower = playerPokemon.move2.movePWR
                    type = playerPokemon.move2.moveType
                    playerPokemon.move2.movePP = playerPokemon.move2.movePP - 1
                    isChoosing = False
               elif selectedMove.lower() == playerPokemon.move3.moveName.lower():
                    currentMovePower = playerPokemon.move3.movePWR
                    type = playerPokemon.move3.moveType
                    playerPokemon.move3.movePP = playerPokemon.move3.movePP - 1
                    isChoosing = False
          
          #Damage Calculation and application
          if type == playerPokemon.type:
               STAB = 1.5
          else: 
               STAB = 1
          critical = 1
          type1 = 1
          type2 = 1
          random = 217/255 # TODO actually make random
          damage = ((((2 * playerPokemon.level * critical)/5 + 2) * currentMovePower * playerPokemon.attack/enemyPokemon.defense)/50 + 2) * STAB * type1 * type2 * random 
          damage = round(damage)
          print("\n"+playerPokemon.name,"used", selectedMove)
          print("You did " + str(damage) +" DMG")
          input("")
          enemyPokemon.hp -= damage
          if enemyPokemon.hp <= 0:
               print(enemyPokemon.name, "has fainted!")
               print("You Won!")
               mixer.music.load("SOUND/26 Victory (VS Trainer).mp3")
               mixer.music.play()
               input("")
               return True 

          #Enemys Turn (No rng rn uses only second move)
          selectedMove = enemyPokemon.move2.moveName
          currentMovePower = enemyPokemon.move2.movePWR
          type = enemyPokemon.move2.moveType
          enemyPokemon.move2.movePP = enemyPokemon.move1.movePP - 1

          if type == enemyPokemon.type:
               STAB = 1.5
          else: 
               STAB = 1
          critical = 1
          type1 = 1
          type2 = 1
          random = 217/255 # TODO actually make random
          damage = ((((2 * enemyPokemon.level * critical)/5 + 2) * currentMovePower * enemyPokemon.attack/playerPokemon.defense)/50 + 2) * STAB * type1 * type2 * random 
          damage = round(damage)
          print("Enemy",enemyPokemon.name + " used " + selectedMove)
          print(enemyPokemon.name + " did " + str(damage) + " DMG")
          input("")
          
          playerPokemon.hp -= damage
          if playerPokemon.hp <= 0:
               print(playerPokemon.name, "fainted!")
               input("")
               return False
