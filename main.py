from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# object creation:
money_machine = MoneyMachine()
coffeeMachine = CoffeeMaker()
menu = Menu()

# variables:
items_available = menu.get_items()
make_drink = True



while make_drink:
    choice = input(f"What would you like? {items_available}): ")
    if choice == "report":
        coffeeMachine.report()
        money_machine.report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        requested = menu.find_drink(choice)
        go = coffeeMachine.is_resource_sufficient(requested)
        if go:
            inserted_money = 0.00
            money_ok = money_machine.make_payment(inserted_money)
            if money_ok:
                coffeeMachine.make_coffee(requested)
            else:
                "Not enough money."
        else:
            print(f"Not enough resources for {choice}, sorry")
    elif choice == "off":
        make_drink = False
    else:
        print("Incorrect selection, please try again.")

print("Good Bye!")