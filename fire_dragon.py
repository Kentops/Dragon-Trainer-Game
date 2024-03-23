from entity import Entity
from hero import Hero
import random
from dragon import Dragon 

class FireDragon(Dragon):
  '''
  The fire dragon fighter
  '''

  def __init__(self,name, max_hp, f_shots):
    '''Constructs a Fire Dragon'''
    super().__init__(name, max_hp)
    self._f_shots = f_shots

  def special_attack(self, hero: Hero) -> str:
    '''A special attack exclusive to Fire Dragons'''
    if self._f_shots>0:
      dmg = random.randint(5,9)
      hero.take_damage(dmg)
      self._f_shots -= 1
      return f"{self.name} breaths fire, dealing {dmg} damage to you!"
    else:
      return f" {self.name} tries to breathe fire, but has no more shots remaining!"
  
  def __str__(self):
    return super().__str__() + f"\nFire Shots remaining: {self._f_shots}"

  @property
  def f_shots(self):
    '''Accesses the f_shots property'''
    return self._f_shots