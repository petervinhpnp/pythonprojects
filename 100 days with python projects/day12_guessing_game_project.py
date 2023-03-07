import random
logo = """
 _   _                 _                 _____                     _             
| \ | |               | |               |  __ \                   (_)            
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` |
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| |
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, |
                                                                            __/ |
                                                                           |___/ """
congratulations_logo = """
         ________  ________  ________   ________  ________  ________  _________  ___  ___  ___       ________  _________  ___  ________  ________   ________      
|\   ____\|\   __  \|\   ___  \|\   ____\|\   __  \|\   __  \|\___   ___\\  \|\  \|\  \     |\   __  \|\___   ___\\  \|\   __  \|\   ___  \|\   ____\     
\ \  \___|\ \  \|\  \ \  \\ \  \ \  \___|\ \  \|\  \ \  \|\  \|___ \  \_\ \  \\\  \ \  \    \ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \ \  \___|_    
 \ \  \    \ \  \\\  \ \  \\ \  \ \  \  __\ \   _  _\ \   __  \   \ \  \ \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \ \_____  \   
  \ \  \____\ \  \\\  \ \  \\ \  \ \  \|\  \ \  \\  \\ \  \ \  \   \ \  \ \ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \|____|\  \  
   \ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\\ \__\ \__\   \ \__\ \ \_______\ \_______\ \__\ \__\   \ \__\ \ \__\ \_______\ \__\\ \__\____\_\  \ 
    \|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|\|__|\|__|    \|__|  \|_______|\|_______|\|__|\|__|    \|__|  \|__|\|_______|\|__| \|__|\_________\
                                                                                                                                              \|_________|"""
print(logo)
print("WELCOME TO THE GUESSING NUMBER GAME!")
print("The number you need to guess will be between 1 and 100")
level = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
if level == 'easy':
    guess_turn = 10
else:
    guess_turn = 5
print(f"You have {guess_turn} attempts left to guess the number")
random_number = random.randint(1,100)
while True:
    guess_number = int(input("Guess a number: "))
    if guess_number > random_number:
        print("Too high.")
        print("Try again.")
    elif guess_number < random_number:
        print("Too low.")
        print("Try again.")
    else:
        print("You've guess it correctly. YOU WIN!")
        break
    if guess_number != random_number:
        guess_turn -= 1
    print(f"Incorrect, you have {guess_turn} left to guess!\n")
    if guess_number == 0:
        print("You lost!")
        break


