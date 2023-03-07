print('''
*******************************************************************************
             _._                                        _._
      _.----|   |--------------------------------------|   |----._
   .-'      |.-.|      |     ||   || | | | | | | |     |.-.|      '-.
 .'        __| |__     |T|O|Y|/   \|M|A|C|H|I|N|E|    __| |__        '.
|         |o_| |_o|    |_|_|_|     |_|_|_|_|_|_|_|   |o_| |_o|         |
|         ||_ @ _||  _    _ ___ _  _  _  _  _  _  _  ||_ @ _||         |
|         |o_| |_o| |_ |/| | | |_ |_|| || ||_)| \|_  |o_| |_o|         |
 '.          | |    __||\|-| | |_ |_||_||-||\_|_/__|    | |          .'
   '-._     |'-'|                                      |'-'|     _.-'
       '----|_ _|--------------------------------------|_ _|----'
              ~                                          ~
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
while True:
  direction = input("left or right\n")
  direction = direction.lower()
  if direction == "right" or direction != "left":
    print("You fall into a hold. GAME OVER!")
    break
  elif direction == "left":
    action = input("swim or wait\n")
    action = action.lower()
    if action == "swim" or action != "wait":
      print("You were attacked by trout. GAME OVER!")
      break
    elif action == "wait":
      print("Please wait...")
  door = input("Which door: Red, Blue, Yellow?\n")
  door = door.lower()
  if door == "red":
    print("You were burned by fire. GAME OVER!")
    break
  elif door == "yellow":
    print("YOU WIN!")
  elif door == "blue":
    print("You were eaten by beasts. GAME OVER")
    break
  else:
    print("GAME OVER!")
    break
  