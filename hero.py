from entity import Entity
#Can't import dragon due to circular import
import random

class Hero(Entity):
  '''
  The hero fighter\n
  sword_attack(self, dragon) -> str: Deals 2D6 damage to dragon. Returns a string describing the attack.\n
  arrow_attack(self, dragon) -> str: Deals 1D12 damage to dragon. Returns a string describing the attack.
  '''

  #Uses the constructor from Entity
  
  def sword_attack(self, dragon) -> str:
    '''Attacks dragon for 2D6 damage'''
    #Two dice rolls
    dmg = random.randint(1,6)
    dmg += random.randint(1,6)
    dragon.take_damage(dmg)
    return f"\nYou slash the {dragon.name} with your sword for {dmg} damage!"

  def arrow_attack(self, dragon) -> str:
    '''Attacks dragon for 1D12 damage'''
    dmg = random.randint(1,12)
    dragon.take_damage(dmg)
    return f"\nYou hit the {dragon.name} with an arrow for {dmg} damage!"