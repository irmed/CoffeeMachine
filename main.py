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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print report on coffee machine resources.
def print_report(resources):
    print("--------------------\nAvailable Resources\n--------------------")
    for resource,value in resources.items():
        print(f"{resource.title()}: {value}")
    print(f"Money: ${money:.2f}")

# TODO: 2. Add money to resources
money = 0

# TODO: 3. Check Available Resources
def check_resource(drink):
    val = 0
    if drink in MENU.keys():
        commonKeys = MENU[drink]["ingredients"].keys() & resources.keys()
        flag = 0
        for key in commonKeys:
            res = resources[key] - MENU[drink]["ingredients"][key]
            if res < 0:
                print(f"Sorry, there is not enough {key}.")
                val = 0
            else:
                flag += 1
        if flag == len(commonKeys):
            print(f"Resource for {drink} is available.")
            val = 1
    else:
        val = 0
    return val

# TODO: 4. Compute the cost

def compute_costs(drink, quarters, dimes, nickles, pennies):
    quarters_total = quarters/4
    dimes_total = dimes/10
    nickles_total = nickles/20
    pennies_total = pennies/100
    sum_total = quarters_total + dimes_total + nickles_total + pennies_total
    return sum_total

# TODO: 5. Compute leftover resources

def compute_leftover(drink):
    global resources
    commonKeys = MENU[drink]["ingredients"].keys() & resources.keys()
    for key in commonKeys:
        res = resources[key] - MENU[drink]["ingredients"][key]
        resources[key] = res


# TODO: Write body

coffee_machine = True
while coffee_machine:
    action = input("What would you like? (espresso/latte/cappuccino) Type 'off' if you want to turn off the machine").lower()
    if action == "report":
       print_report(resources)
    elif action == "off":
        print("Thank you for using this app")
        coffee_machine = False
    elif action in MENU.keys():
        val = check_resource(action)
        if val == 1:
            change = 0
            print(f"The price is {MENU[action]['cost']:.2f}")
            if money < MENU[action]["cost"]:
                print(f"Please insert coins.")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickles = int(input("How many nickles? "))
                pennies = int(input("How many pennies? "))
                sum_total = compute_costs(action, quarters, dimes, nickles, pennies)
                change = sum_total - MENU[action]["cost"]
                money += change
            else:
                change = money - MENU[action]["cost"]
                money = money - MENU[action]["cost"]

            if change > 0:
                print(f"Your change is ${change:.2f}")
                print(f"Here is your {action}! Enjoy!")
                compute_leftover(action)
                print_report(resources)
            elif change == 0 :
                print(f"There is no change.")
            else:
                print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Invalid input. Please try again.")