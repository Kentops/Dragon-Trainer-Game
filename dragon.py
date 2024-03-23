from entity import Entity
from hero import Hero
import random

class Dragon(Entity):
  '''
  The dragon fighter
  basic_attack(self, hero) -> str: The dragon attacks hero for 3-7 damage\n
  special_attack(self, hero) -> str: The dragon attacks hero for 4-8 damage\n
  '''

  #Uses the constructor from Entity

  def basic_attack(self, hero:Hero) -> str:
    '''Deals 3-7 damage to hero'''
    dmg = random.randint(3,7)
    hero.take_damage(dmg)
    return f"{self.name} smashes you with its tail for {dmg} damage!"

  def special_attack(self, hero:Hero) -> str:
    '''Deals 4-8 damage to hero'''
    dmg = random.randint(4,8)
    hero.take_damage(dmg)
    return f"{self.name} slashes you with its claws for {dmg} damage!"