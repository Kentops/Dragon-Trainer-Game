from entity import Entity
from hero import Hero
import random
from dragon import Dragon 

class FlyingDragon(Dragon):
  '''The Flying Dragon fighter'''
  def __init__(self, name, max_hp, swoops):
    '''Constructs a Flying Dragon'''
    super().__init__(name,max_hp)
    self._swoops = swoops

  
  def special_attack(self, hero) -> str:
    '''A special attack exclusive to Flying Dragons'''
    if self._swoops > 0:
      dmg = random.randint(5,8)
      hero.take_damage(dmg)
      self._swoops -= 1
      return f"{self.name} swoops down, dealing {dmg} damage to you!"
    else:
      return f"{self.name} tries to swoop down, but has no more swoops remaining!"


  
  def __str__(self):
    return super().__str__() + f"\nSwoop attacks remaining: {self._swoops}"

  @property
  def swoops(self):
    '''Accesses the swoops property'''
    return self._swoops