from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drinks = Menu()
resource = CoffeeMaker()
payment = MoneyMachine()
while True:
    Choice = input(f"What would you want to order from {Menu.get_items(drinks)}: ")
    if Choice == "report":
        resource.report()
        payment.report()
    elif Choice == "off":
        break
    else:
        order_name = drinks.find_drink(Choice)
        if resource.is_resource_sufficient(order_name) and payment.make_payment(order_name.cost):
            resource.make_coffee(order_name)

            
