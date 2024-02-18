from Animal import setUpAnimalCards, get_animals_list
from Planet import setUpPlanetCards, get_planets_list

from random import choice
from time import sleep
from os import system

gameOptions = ["animals", "planets"]
print(gameOptions)
deckAnswer = input("What type of deck would you prefer?")

# while answer is invalid, ask for new input
while deckAnswer not in gameOptions:
  deckAnswer = input("type valid option:")
  
# setting up game
gameList = []
if deckAnswer == "animals":
  setUpAnimalCards()
  gameList = get_animals_list()
elif deckAnswer == "planets":
  setUpPlanetCards()
  gameList = get_planets_list()

  
print("welcome to card battles")
print("")
print("CARDS:")
for oneCard in gameList:
  print(oneCard.name)
  
playAgainOptions = ["y", "yes", "yup", "sure", "ye", "yea"]
playAgain = "y"
userScore = 0
botScore = 0


# game loop
while playAgain in playAgainOptions:
  
  userChoice = choice(gameList)
  print("")
  print("\nYour card is...", userChoice.name)
  userChoice.print_stats()
  
  gameList.remove(userChoice)
  botChoice = choice(gameList)
  print("\nComputer's card is...???")
  
  print("\nChoose a stat:")
  print(userChoice.options)
  
  answer = input()
  while answer not in userChoice.options:
    answer = input("type valid option:")
    
  user_stat = userChoice.get_value(answer)
  bot_stat = botChoice.get_value(answer)
  
  print("comparing " + answer + "...")
  sleep(1)
  print(userChoice.name + " " + str(user_stat))
  print(botChoice.name + " " + str(bot_stat))
  
  # check which is bigger
  if user_stat > bot_stat:
    print("You Win!")
    userScore += 1
  elif user_stat == bot_stat:
    print("Tied!")
  else:
    print("Bot Wins!")
    botScore += 1
    
  print("Current user score: " + str(userScore))
  print("Current bot score: " + str(botScore))
  
  sleep(2)
  playAgain = input("Would you like to play again?")
  playAgain.lower().strip()
  
  # clears screen
  system("clear")
  
print("Game Over!")
print("Final user score: " + str(userScore))
print("Final bot score: " + str(botScore))
print("")

if userScore > botScore:
  print("you beat the machine!")
elif userScore == botScore:
  print("you both tied!")
else:
  print("the machine is victorious")
