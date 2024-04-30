import random, time, os

#subroutine 1: character name and type

def character_name_and_type():
  character_name = input("Name your Legend: ")
  character_type = input("Character Type (Human, Elf, Wizard, Orc): ")
  return character_name, character_type

#subroutine 2: health stats

def health_stats():
  health_stats = (random.randint(1,6) * random.randint(1,12))/2 + 10
  return health_stats

#subroutine 3: strength stats

def strength_stats():
  strength_stats = (random.randint(1,6) * random.randint(1,12))/2 + 12
  return strength_stats

#subroutine 4: random sided dice

def dice_roll():
  dice_roll = random.randint(1,6)
  return dice_roll

#Main Menu
def main_menu():
  while True:
    print("⚔️ Character Builder ⚔️")
    print()
    time.sleep(1)
    character_name, character_type = character_name_and_type()
    print()
    time.sleep(1)
    print(character_name)
    time.sleep(1)
    print("HEALTH:", health_stats())
    time.sleep(1)
    print("STRENGTH:", strength_stats())
    print()
    print("May your name go down in Legend...")
    print()
    new_round = input("Would you like to create a new character? ")
    if new_round == "yes" or new_round == "Yes" or new_round == "Y":
      os.system("clear")
      continue
    elif new_round == "no" or new_round == "No" or new_round == "N":
      print("Thank you for playing! See you next time!")
      break
    else: 
      print("Invalid input. Please try again.")
      print(new_round)
      continue
  
main_menu()
