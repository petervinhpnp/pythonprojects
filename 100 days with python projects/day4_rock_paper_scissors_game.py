import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_input = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ')
player_result = str("")
choice_list = [rock, paper, scissors]
computer_choice = random.choice(choice_list)
if player_input == '0':
    player_result = rock
elif player_input == '1':
    player_result = paper 
else:
    player_result = scissors
print(player_result)
print('Computer chose: ')
print(computer_choice)

#checking the result between player and computer choices
if player_result == computer_choice:
    print('You draw')
if player_result == rock and computer_choice == paper:
    print('You lose')
elif player_result == rock and computer_choice == scissors:
    print('You win')
elif player_result == paper and computer_choice == scissors:
    print('You lose')
elif player_result == paper and computer_choice == rock:
    print('You win')
elif player_result == scissors and computer_choice == paper:
    print('You win')
elif player_result == scissors and computer_choice == rock:
    print('You lose')

