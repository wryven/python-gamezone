import itertools

class Player:

  id = itertools.count()

  def __init__(self, name : str, age : int):
    self.id = next(self.id)
    self.name = name
    self.age = age

  def __str__(self):
    return f"[{self.id}] - {self.name} ({self.age})"

  def change_name(self, new_name):
    self.name = new_name



