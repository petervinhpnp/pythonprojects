MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
ICON = {"espresso": "🍶", "latte": "☕", "cappuccino": "🍵" }

#money counting
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

#Resource
water = 600 #ml
milk = 400 #ml
coffee = 120 #gam
change = 0

#order making function
def espresso_order():
    global water
    global coffee
    global change
    water = water - 50
    coffee = coffee - 18
    return water, coffee
def latte_order():
    global water
    global milk
    global coffee
    global change    
    water = water - 200
    milk = milk - 150
    coffee = coffee - 24
    
    return water, milk, coffee
def cappuccino_order():
    global water
    global milk
    global coffee
    global change
    water = water - 250
    milk = milk - 100
    coffee = coffee - 24
    return water, milk, coffee

continue_selling = True
while continue_selling:
    #Customer's input
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    save_order = order
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total_money_given = (quarter * QUARTERS) + (dime * DIMES) + (nickle * NICKLES) + (penny * PENNIES)

    #check if the resource still enough for making the orders
    if (order == "espresso") and (water >= 50) and (coffee >= 18):
        pass
    elif (order == "latte") and (water >= 200) and (milk >= 150) and (coffee >= 24):
        pass
    elif (order == "cappuccino") and (water >= 250) and (milk >= 100) and (coffee >= 24):
        pass
    else:
        print("The machine has ran out of the ingredients. We're so sorry about this, please come back later. Thank you!")
        break
        
    #Compare the resource and order, calculate the change
    if (order == "espresso") and (total_money_given > MENU["espresso"]["cost"]):
        espresso_order()
        change = total_money_given - MENU["espresso"]["cost"]
    elif (order == "latte") and (total_money_given > MENU["latte"]["cost"]):
        latte_order()
        change = total_money_given - MENU["latte"]["cost"]
    elif (order == "cappuccino") and (total_money_given > MENU["cappuccino"]["cost"]):
        cappuccino_order()
        change = total_money_given - MENU["cappuccino"]["cost"]
    else:
        print("You don't have enough money. Money refunded")
        total_money_given = 0 #reset the money because it has been refunded
        continue
    change = round(change,1)
    print(f"Here is ${change} in change.")
    print(f"Here is your {save_order} {ICON[save_order]}. Enjoy!")

    # print out reports
    if order == 'report':
        if save_order == "espresso":
            print("Water:" + str(MENU["espresso"]["ingredients"]["water"])+"ml")
            print("Coffee:" + str(MENU["espresso"]["ingredients"]["coffee"])+"g")
            print("Money: " + "$"+str(MENU["espresso"]["cost"]))
        elif save_order == "latte":
            print("Water:" + str(MENU["latte"]["ingredients"]["water"])+"ml")
            print("Milk:" + str(MENU["latte"]["ingredients"]["water"])+"ml")
            print("Coffee:" + str(MENU["latte"]["ingredients"]["coffee"])+"g")
            print("Money: " + "$"+str(MENU["latte"]["cost"]))
            
        else:
            print("Water:" + str(MENU["cappuccino"]["ingredients"]["water"])+"ml")
            print("Milk:" + str(MENU["cappuccino"]["ingredients"]["water"])+"ml")
            print("Coffee:" + str(MENU["cappuccino"]["ingredients"]["coffee"])+"g")
            print("Money: " + "$"+str(MENU["cappuccino"]["cost"]))






