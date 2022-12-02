from pygame import mixer
import random
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
               playerselectedMove = input("Select A Move: ")
               if playerselectedMove.lower() == playerPokemon.move1.moveName.lower():
                    playercurrentMovePower = playerPokemon.move1.movePWR
                    type = playerPokemon.move1.moveType
                    playerPokemon.move1.movePP = playerPokemon.move1.movePP - 1
                    isChoosing = False
               elif playerselectedMove.lower() == playerPokemon.move2.moveName.lower():
                    playercurrentMovePower = playerPokemon.move2.movePWR
                    type = playerPokemon.move2.moveType
                    playerPokemon.move2.movePP = playerPokemon.move2.movePP - 1
                    isChoosing = False
               elif playerselectedMove.lower() == playerPokemon.move3.moveName.lower():
                    playercurrentMovePower = playerPokemon.move3.movePWR
                    type = playerPokemon.move3.moveType
                    playerPokemon.move3.movePP = playerPokemon.move3.movePP - 1
                    isChoosing = False
          if playerPokemon.speed >enemyPokemon.speed:  
               #Damage Calculation and application
               if type == playerPokemon.type:
                    STAB = 1.5
               else: 
                    STAB = 1
               critthreshold = playerPokemon.speed/2
               if critthreshold > random.randint(0,255):
                    critical = 2
                    print("Critical Hit!")
               else:
                    critical = 1
               type1 = 1
               type2 = 1
               randomValue = random.randint(217,255)/255 # TODO actually make randomValue
               damage = ((((2 * playerPokemon.level * critical)/5 + 2) * playercurrentMovePower * playerPokemon.attack/enemyPokemon.defense)/50 + 2) * STAB * type1 * type2 * randomValue 
               damage = round(damage)
               print("\n"+playerPokemon.name,"used", playerselectedMove)
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
               moveRNG = random.randint(1,4)
               print(moveRNG)
               if moveRNG == 4 and enemyPokemon.move4 != "":
                    selectedMove = enemyPokemon.move4
               elif moveRNG == 3 and enemyPokemon.move3 != "":
                    selectedMove = enemyPokemon.move3
               elif moveRNG == 2 and enemyPokemon.move2 != "":
                    selectedMove = enemyPokemon.move2
               else:
                    selectedMove = enemyPokemon.move1
               currentMovePower = selectedMove.movePWR
               type = selectedMove.moveType
               selectedMove.movePP = selectedMove.movePP - 1

               if type == enemyPokemon.type:
                    STAB = 1.5
               else: 
                    STAB = 1

               critthreshold = enemyPokemon.speed/2
               if critthreshold > random.randint(0,255):
                    critical = 2
                    print("Critical Hit!")
               else:
                    critical = 1     
               type1 = 1
               type2 = 1
               randomValue = random.randint(217,255)/255 
               damage = ((((2 * enemyPokemon.level * critical)/5 + 2) * currentMovePower * enemyPokemon.attack/playerPokemon.defense)/50 + 2) * STAB * type1 * type2 * randomValue 
               damage = round(damage)
               print("Enemy",enemyPokemon.name + " used " + selectedMove.moveName)
               print(enemyPokemon.name + " did " + str(damage) + " DMG")
               input("")
               
               playerPokemon.hp -= damage
               if playerPokemon.hp <= 0:
                    print(playerPokemon.name, "fainted!")
                    input("")
                    return False
          else:
               #Enemys Turn (No rng rn uses only second move)
               moveRNG = random.randint(1,4)
               print(moveRNG)
               if moveRNG == 4 and enemyPokemon.move4 != "":
                    selectedMove = enemyPokemon.move4
               elif moveRNG == 3 and enemyPokemon.move3!= "":
                    selectedMove = enemyPokemon.move3
               elif moveRNG == 2 and enemyPokemon.move2 != "":
                    selectedMove = enemyPokemon.move2
               else:
                    selectedMove = enemyPokemon.move1
               currentMovePower = selectedMove.movePWR
               type = selectedMove.moveType
               selectedMove.movePP = selectedMove.movePP - 1

               if type == enemyPokemon.type:
                    STAB = 1.5
               else: 
                    STAB = 1

               critthreshold = enemyPokemon.speed/2
               if critthreshold > random.randint(0,255):
                    critical = 2
                    print("Critical Hit!")
               else:
                    critical = 1     
               type1 = 1
               type2 = 1
               randomValue = random.randint(217,255)/255 
               damage = ((((2 * enemyPokemon.level * critical)/5 + 2) * currentMovePower * enemyPokemon.attack/playerPokemon.defense)/50 + 2) * STAB * type1 * type2 * randomValue 
               damage = round(damage)
               print("Enemy",enemyPokemon.name + " used " + selectedMove.moveName)
               print(enemyPokemon.name + " did " + str(damage) + " DMG")
               input("")
               
               playerPokemon.hp -= damage
               if playerPokemon.hp <= 0:
                    print(playerPokemon.name, "fainted!")
                    input("")
                    return False



               
               #Damage Calculation and application
               if type == playerPokemon.type:
                    STAB = 1.5
               else: 
                    STAB = 1
               critthreshold = playerPokemon.speed/2
               if critthreshold > random.randint(0,255):
                    critical = 2
                    print("Critical Hit!")
               else:
                    critical = 1
               type1 = 1
               type2 = 1
               randomValue = random.randint(217,255)/255 # TODO actually make randomValue
               damage = ((((2 * playerPokemon.level * critical)/5 + 2) * playercurrentMovePower * playerPokemon.attack/enemyPokemon.defense)/50 + 2) * STAB * type1 * type2 * randomValue 
               damage = round(damage)
               print("\n"+playerPokemon.name,"used", playerselectedMove)
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

               



