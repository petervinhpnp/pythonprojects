import os
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import random
from day14_gamedata import data

current_score = 0
compare_a = random.choice(data) #it's a dictionary/ attribute : name , follower_count , description ,  country
compare_b = random.choice(data)
a_follower_count = compare_a['follower_count'] #it's int
b_follower_count = compare_b['follower_count'] 
user_guess = 0
computer_guess = 0
object_continue = {}

#start game
#first time guess/question (function) 
print(logo)
print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.") 
print(vs)
print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")

def first_time():
    global answer
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    global current_score
    if answer == 'a':
        user_guess = a_follower_count
        computer_guess = b_follower_count
        if user_guess >= computer_guess: #in case the user win
            current_score += 1
            print(logo)
            print(f"You're right! Current score: {current_score}.")
            return current_score, a_follower_count, compare_a
        else: # if it ends here then it ends here
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}.")
            quit()
    else:
        user_guess = b_follower_count
        computer_guess = a_follower_count
        if user_guess >= computer_guess:
            current_score += 1
            print(logo)
            print(f"You're right! Current score: {current_score}.")
            return current_score, b_follower_count, compare_b
        else: # if it ends here then it ends here
            print(logo)
            print(f"Sorry, that's wrong. Final score: {current_score}.")
            quit()
      
current_score , new_user_guess, user_compare = first_time()
   
# function that keeps playing later 
def game_continue(score, user_next_guess, user_current_compare):
    new_compare_a = user_current_compare # use this for A dictionary
    user_next_guess # follower count of A
    game_should_continue = True
    while game_should_continue:
        # it's a dictionary/ attribute : name , follower_count , description ,  country
        compare_b = random.choice(data)
        new_computer_answer = compare_b['follower_count']        
        print(logo)
        print(f"Compare A: {new_compare_a['name']}, a {new_compare_a['description']}, from {new_compare_a['country']}.") 
        print(vs)
        print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_answer == 'a': # if choose as a then we still keep the number count:
            if user_next_guess >= new_computer_answer:
                score += 1
                print(logo)
                print(f"You're right! Current score {score}")
                new_compare_a = compare_b
                user_next_guess = compare_b['follower_count']

            else:
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}.")
                break
        else:
            new_computer_answer = user_next_guess
            user_next_guess = compare_b['follower_count']
            if user_next_guess >= new_computer_answer:
                score += 1
                print(logo)
                print(f"You're right! Current score {score}")
                new_compare_a = compare_b
            else:
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}.")
                break

game_continue(score= current_score, user_next_guess= new_user_guess, user_current_compare= user_compare)



































