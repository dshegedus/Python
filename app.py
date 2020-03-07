### Transport 11, Meal 5

transport_fee = 11
transport_day = 1
meal_fee = 5
meal_day = 0.46
menu_decision = 0
import csv


while int(menu_decision) not in [1, 2, 3, 4]:
    try:
         menu_decision = int(input("Select an option from the menu by typing in its number. \n 1. See Current Savings. \n 2. Add Weekly Cycles and Meals. \n 3. See Wishes. \n 4. Add a Wish. \n...   "))
    except ValueError:
         print("Oops! Please give a valid number from the menu. \n")


if menu_decision == 1:

    with open("savings.csv") as csvfile:
        readCSV = csv.reader(csvfile)

        dates = []
        cycles = []
        meals = []

        for row in readCSV:
            date = row[0]
            cycle = int(row[1])
            meal = int(row[2])

            dates.append(date)
            cycles.append(cycle)
            meals.append(meal)

        
    sum_cycles = sum(cycles)
    sum_meals = sum(meals)
    total_savings = (sum_cycles * transport_fee) + (sum_meals * meal_fee)

    print (" So far you have saved a total of £{}\n by cycling to work {} times\n and bringing {} meals to work.".format(total_savings, sum_cycles, sum_meals))

    
elif menu_decision == 2:
    print("this2")


elif menu_decision == 3:
    with open("wish_list.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print("Item: {} £{}".format(row["item"], row["price"]))

elif menu_decision == 4:
    with open("wish_list.csv", "a") as wl:
        writer = csv.writer(wl)

        new_item = input("New wish name: \n")
        new_price = input("New wish price: \n")

        cycle_days = int(new_price) / transport_fee
        cycle_meal_days = int(new_price) / (transport_fee + meal_fee)

        writer.writerow([new_item, new_price])

    print("{} with £{} has been added to your wish list. \n It will take an additional {:.2f} days of cycling \n OR {:.2f} days if you bring your own meal as well.".format(new_item.title(), new_price, cycle_days, cycle_meal_days))
