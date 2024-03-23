from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
import check_input
import random

'''Dragon Tamer
   3/6/2024
   A dragon fighting game based on one of the opening scenes of How to Train Your Dragon.
'''

def main():
  '''The main method of the project'''

  print("What is your name, challenger?")
  name = input()
  print(f"Welcome to dragon training, {name}. \nYou must defeat 3 dragons.")

  
  #Construct hero and dragons
  player = Hero(name,50)
  d1 = Dragon("Deadly Nadder",10)
  d2 = FireDragon("Gronckle",15,3)
  d3 = FlyingDragon("Timberjack",20,5)
  d_list = [d1,d2,d3]
  

  #Loop until all dragons are defeated
  while len(d_list) > 0 and player.hp > 0:
    print(player)
    for i, dragon in enumerate(d_list, start=1):
      remaining = ""
      if isinstance(dragon, FireDragon):
        remaining = f"Fire Shots remaining: {dragon.f_shots}"
      elif isinstance(dragon, FlyingDragon):
        remaining = f"Swoop attacks remaining: {dragon.swoops}"
      print(f"{i}. Attack {dragon.name}: {dragon.hp}/{dragon.max_hp}")
      if remaining:
        print(remaining)
      

    
    dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(d_list))
    selected_dragon = d_list[dragon_choice-1]

    print("\nAttack with:")
    print("1. Arrow (1 D12)")
    print("2. Sword (2 D6)")
    attack_choice = check_input.get_int_range("Enter weapon: ", 1, 2)
    
    if attack_choice == 1:
      print(player.arrow_attack(selected_dragon))
    else:
      print(player.sword_attack(selected_dragon))
    
    #If dragon is defeated, remove it
    if selected_dragon.hp <= 0:
      print(f'You defeated the {selected_dragon.name}!')
      d_list.remove(selected_dragon)

    if len(d_list) > 0:
      dragon_attacked = random.choice(d_list)
      attack_method = random.choice([dragon_attacked.basic_attack, dragon_attacked.special_attack])
      print(attack_method(player))


  
  if player.hp <=0:
    print("You have been defeated. Game over.")
  else:
    print("\nCongratulations! You defeated all 3 dragons. You have passed the trials.")

main()