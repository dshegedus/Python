#### Transport 11, Meal 5

transport_fee = 11
transport_day = 1
meal_fee = 5
meal_day = 0.46
menu_decision = 1
import csv

def get_choice():
    choice = 0
    while choice not in range(1, 5):
        try:
            choice = int(input("Select an option from the menu. \n 1. See Current Savings. \n 2. Add Weekly Cycles and Meals. \n 3. See Wishes. \n 4. Add a Wish. \n 5. Exit \n... \n"))
        except ValueError:
            print("Oops! Please give a valid number from the menu. \n")
    return choice


while menu_decision in range(1, 4):
    menu_decision = get_choice()


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

        print (" So far you have saved a total of £{}\n by cycling to work {} times\n and bringing {} meals to work.\n \n \n".format(total_savings, sum_cycles, sum_meals))

        
    elif menu_decision == 2:
        ### Part 1, getting info from user (date to update, cycle, and meal yes no 1 0)
        
        date_update = input("What day would you like to make changes to (dd/mm/yy)? \n")
        cycle_update = input("Did you cycle in? \n")
        meal_update = input("Did you bring your lunch? \n")

    ### Loading savings.csv in read mode and putting all categories from the csv into a list.
        
            

        with open("savings.csv", "r") as savr:        
                
            dates_savings = []
            cycle_savings = []
            meal_savings = []
            
            for line in savr:
                data = line.strip().split(',')
                dates_savings.append(data[0])
                cycle_savings.append(data[1])
                meal_savings.append(data[2])

            date_update_index = dates_savings.index(date_update)

            cycle_savings[date_update_index] = cycle_update
            meal_savings[date_update_index] = meal_update

            updated_info = [[dates_savings[i], cycle_savings[i], meal_savings[i]] for i in range(len(dates_savings))]

        Y_N = input("Do you want to continue with these changes (Y/N): \n Date:{} \n Cycle:{} \n Meal:{} \n ".format(date_update, cycle_update, meal_update))
        if Y_N.lower() == "y" or "yes":
            
            with open("savings.csv", "w") as savup:
                writer = csv.writer(savup, delimiter = ",")
                writer.writerows(updated_info)

    elif menu_decision == 3:
        with open("wish_list.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("Item: {} £{} \n".format(row["item"], row["price"]))

    elif menu_decision == 4:
        with open("wish_list.csv", "a") as wl:
            writer = csv.writer(wl)

            new_item = input("New wish name: \n")
            new_price = input("New wish price: \n")

            cycle_days = int(new_price) / transport_fee
            cycle_meal_days = int(new_price) / (transport_fee + meal_fee)

            writer.writerow([new_item, new_price])

        print("\n {} with £{} has been added to your wish list. \n It will take an additional {:.2f} days of cycling \n OR {:.2f} days if you bring your own meal as well.\n \n \n".format(new_item.title(), new_price, cycle_days, cycle_meal_days))

    elif menu_decision == 5:
        print("Well Done! Keep Fit!")


