class Entity:
  '''
  A class containing basic attributes of a fighter.\n
  (str) name: The name of the fighter\n
  (int) max_hp: The maximum health of the fighter\n
  (int) _hp: The fighter's current HP\n
  take_damage(damage): Updates _hp\n
  '''

  def __init__(self, name, max_hp):
    '''Constructs a fighter'''
    self._name = name
    self.max_hp = max_hp
    self._hp = self.max_hp

  def take_damage(self, dmg):
    '''Subtracts dmg from hp'''
    self._hp -= dmg
    if(self._hp < 0):
      self._hp = 0

  def __str__(self):
    '''Represents an entity as a string'''
    return(f"\n{self._name}: {self._hp}/{self.max_hp}")
  
  @property
  def name(self):
    '''Accesses the name property'''
    return self._name
  
  @property
  def hp(self):
    '''Accesses the hp property'''
    return self._hp