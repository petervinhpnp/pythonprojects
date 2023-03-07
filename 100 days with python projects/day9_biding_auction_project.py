import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
money_store = []
name_store = []
# os.system('cls')
continue_bid = True
name = str(input("What's your name? "))
money = int(input("What is your bid? $"))
bid_store_dict = {name : money}
while continue_bid:
    updated_dict = {**bid_store_dict, name : money}
    other_bidder = str(input("Is there another player next to you? Type 'Yes' to continue or 'No' to stop the auction ")).lower()
    if other_bidder == 'no':
        continue_bid = False
    else:
        os.system('cls')
        name = str(input("What's your name? "))
        money = int(input("What is your bid? $"))
for name in updated_dict:
    money_store.append(updated_dict[name])
highest_bid = max(money_store)
for name in updated_dict:    
    if updated_dict[name] == highest_bid:
        print(f"The winner is {name} with a bid of ${highest_bid}")




