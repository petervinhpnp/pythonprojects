import random
import os

#logo for the game
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print("WELCOME TO THE GAME")
print(logo)
#stages of hangman go backward
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list  = ['game', 'weather', 'animal', 'storm', 'song', 'complexion', 'multiple', 'addition', 'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack']
chosen_word = random.choice(word_list)
lives = 6
answer_string = ''
# Create a list of answer's characters and reveal the correct letter into the string from user's input
answer_list = list(chosen_word)
for i in range(len(answer_list)):
    answer_list[i] = '_'
# print defualt stage of hangman
print(stages[6])
# Show the number of letters in that word to the user
for i in range(len(chosen_word)):
  print('_', end = ' ')
print('\n')

# Take user's input and start checking the result 
while lives > 0: 
    guess_letter = input("Guess a letter in the word: ").lower()
    os.system('cls')  #clear the obvious stages for everytime guess (for aesthetic looking purpose)
    if guess_letter in answer_list:
      print(f"You've guessed {guess_letter} already")

    for position in range(len(chosen_word)):
      if chosen_word[position] == guess_letter:
          answer_list[position] = guess_letter
          answer_string = ' '.join(answer_list)
      else:
        continue
    print(answer_string) 
    if (guess_letter in answer_list):
      print(stages[lives])
    elif (guess_letter not in answer_list):
      lives = lives -1
      print(stages[lives])
    if '_' not in answer_list:
      print("You've won")
      break
else:
  print('You lose')
  print(f'The answer is {chosen_word}')
    




