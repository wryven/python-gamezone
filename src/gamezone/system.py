import json
from player import Player

class System:
  # CONSTRUCTORS 

  def __init__(self, player_list=[]):
    self.player_list = player_list
    self.load_sys_data()

  # METHODS

    ## Player List

  def register_player(self, player : Player):
    if self.__unique_id(player.id):
      self.player_list.append(player)
      return True
    else:
      return False
    
  def unregister_player(self, id : int):
    for player in self.player_list:
      if player.id == id:
        self.player_list.remove(player)
        return True
    return False
    
  def __unique_id(self, id):
    for player in self.player_list:
      if player.id == id:
        return False
    return True
  
  ## File W/R
  def save_sys_data(self):
    data : json = {}
    for player in self.player_list:
      data[f'{player.id}'] = {
        'name': player.name,
        'age': player.age
      }


    out_file = open('player_list.json', 'w')
    json.dump(data, out_file, indent=4)
    out_file.close()

    return True

  def load_sys_data(self):
    with open('player_list.json', 'r') as file:
      data = json.load(file)
      for id in data:
        player = data[id]
        self.register_player(player['name'], player['age'])

      return False

