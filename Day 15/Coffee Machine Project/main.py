
MENU:dict[str,dict] = {
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
    "money": 0.0

}

penny=0.01
nickel=0.05
dime=0.10
quarter=0.25


def check_resources(coffee):
    """Checks to make sure that the coffee machine has enough resources to make the requested drink."""
    for key in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][key]>resources[key]:
            print(f"Sorry, there is not enough {key}.")
            return False
    return True


def check_and_return_value(coin):
    """Verifies if the number of coins inputted is the correct value and returns accepted results."""
    number=-1
    while number<0:
        try:
            number=int(input(f"How many {coin}?\n"))
        except ValueError:
            print("You've typed an invalid value. Try typing a number such as '10'.")
            continue
        if number<0:
            print("You can't insert a negative number of coins.")
    return number


def check_money(coffee):
    """Ask for coins and return True if they cover the drink's cost, printing any change; otherwise return False."""
    print("Please insert coins")
    user_quarters = check_and_return_value("quarters")
    user_dimes = check_and_return_value("dimes")
    user_nickels=check_and_return_value("nickels")
    user_pennies=check_and_return_value("pennies")
    user_total=round((user_quarters*quarter)+(user_dimes*dime)+(user_nickels*nickel)+(user_pennies*penny),2)
    if user_total<MENU[coffee]["cost"]:
        print("Sorry, that is not enough money. Money refunded.")
        return False
    elif user_total>MENU[coffee]["cost"]:
        change=user_total-MENU[coffee]["cost"]
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        return True


def make_coffee(coffee):
    """Accepts and stores the cost of the drink and takes the materials of the drink from the machine's resources to make drink. """
    resources["money"] += MENU[coffee]["cost"]
    resources["water"]=resources["water"]-MENU[coffee]["ingredients"]["water"]
    resources["coffee"]=resources["coffee"]-MENU[coffee]["ingredients"]["coffee"]
    if coffee=="cappuccino" or coffee=="latte":
        resources["milk"]=resources["milk"]-MENU[coffee]["ingredients"]["milk"]


def coffee_machine():
    """Run the coffee machine loop, handling orders, reports and switching off."""
    machine_on=True
    while machine_on:
        opening=input("What would you like? (espresso/latte/cappuccino)\n").lower()
        if opening=="report":
            print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml"
            f"\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]:.2f}")

        elif opening=="off":
            machine_on=False
        elif opening in MENU:
            enough_resources=check_resources(opening)
            if enough_resources:
                enough_money=check_money(opening)
                if enough_money:
                    make_coffee(opening)
                    print(f"Here is your {opening}. Enjoy!")
        else:
            print("Sorry, that was not an option. Please try again.")


coffee_machine()