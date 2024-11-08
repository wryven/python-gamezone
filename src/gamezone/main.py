from system import System
from player import Player

def run():
  print('Welcome to G A M E Z O N E\n')

  # Tutorial
  user_input = ask_input("Do you need a tutorial? y/N", [ "", "y", "n"])

  if user_input == 'y':
    print("Tutorial")

  main_menu()

def main_menu():
  options = [
    '0',
    '1',
    '2',
    '3'
  ]

  prompt = '''
          MAIN MENU:\n
              [1] - Game Menu\n
              [2] - Players Menu\n
              [3] - Settings\n
              [0] - Exit
          '''
  
  while(user_input != '0'):
    user_input = ask_input(prompt, options)
    
    match user_input:
      case '1':
        print("Game Menu")
      case '2':
        print("Players Menu")
      case '3':
        print('Settings')
      case '0':
        ask_input("Are you sure you want to exit? y/N", ['', 'y', 'n'])
        if user_input == 'n':
          user_input = '-'

def game_menu():
  pass

def players_menu():
  pass

def settings_menu():
  pass

def ask_input(promt : str, options : list):
  user_input = input(promt).lower()

  while(user_input not in options):
    user_input = input('ERROR: Invalid input! Try again: ').lower()

  return user_input

def test():
  sys = System()
  print('Players: [', end='')
  for player in sys.player_list:
    print(f'{player}, ')
  print(']')

if __name__ == '__main__':
  test()