print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
number_people = float(input("How many people to split the bill? "))
tip = float(input("How much percentage tip would you like to give? 10, 12, or 15? "))

each_person = round((bill + (bill * tip / 100)) / number_people,1)
print(f"Each person should pay: ${each_person}")
