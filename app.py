### Transport 11, Meal 5

transport_fee = 11
meal_fee = 5
menu_decision = 0

while int(menu_decision) != 1 or int(menu_decision) != 2 or int(menu_decision) != 3:
    try:
        menu_decision = int(input("Select an option from the menu by typing in its number. \n 1. See Current Savings. \n 2. Add Savings. \n 3. Add a Wish. \n...   "))
    except ValueError:
        print("Oops! Please give a valid number from the menu.")
        continue
    break
        
if int(menu_decision) == 1:
    print("this")
elif int(menu_decision) == 2:
        print("this2")
elif int(menu_decision) == 3:
        print("this3")
