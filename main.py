"""
Terminal python project on operating a coffee machine

To do:
-include wrong input debugging
"""


# ask function
def ask(resources):
    usrinput = input("What would you like? (espresso/latte/cappuccino):")

    if usrinput == "espresso":
        espresso(resources)
    elif usrinput == "latte":
        latte(resources)
    elif usrinput == "cappuccino":
        cappuccino(resources)
    elif usrinput == "report":
        printReport(resources)
    elif usrinput == "off":
        print("Shutting down")
    elif usrinput == "add":
        addResources(resources)


# function for printing report
def printReport(resources):
    print("Water: ", resources["water"], "ml")
    print("Milk: ", resources["milk"], "ml")
    print("Coffee: ", resources["coffee"], "g")
    print("Money: $", resources["money"])

    ask(resources)


# function for checking resources
def sufficientResources(choice, resources):
    if choice == "espresso":
        # 50ml water, 18g coffee
        if resources["water"] - 50 >= 0 and resources["coffee"] - 18 >= 0:
            return True
        else:
            print("Insufficient resources\n\n")
            return False
    elif choice == "latte":
        # 200ml water, 24g coffee, 150ml milk
        if resources["water"] - 200 >= 0 and resources["coffee"] - 24 >= 0 and resources["milk"] - 150 >= 0:
            return True
        else:
            print("Insufficient resources\n\n")
            return False
    elif choice == "cappuccino":
        if resources["water"] - 250 >= 0 and resources["coffee"] - 24 >= 0 and resources["milk"] - 100 >= 0:
            return True
        else:
            print("Insufficient resources\n\n")
            return False



# function for coins
def sufficientCoins(choice, resources):
    totalInputtedCoins = inputMoney(resources)

    if choice == "espresso":
        #costs 1.50
        if totalInputtedCoins >= 1.50:
            return True, totalInputtedCoins
        else:
            print("Unable to complete order. Insufficient money. Refunding...\n\n")
            return False, totalInputtedCoins
    elif choice == "latte":
        #costs 2.50
        if totalInputtedCoins >= 2.50:
            return True, totalInputtedCoins
        else:
            print("Unable to complete order. Insufficient money. Refunding...\n\n")
            return False, totalInputtedCoins
    elif choice == "cappuccino":
        #costs 3.50
        if totalInputtedCoins >= 3.00:
            return True, totalInputtedCoins
        else:
            print("Unable to complete order. Insufficient money. Refunding...\n\n")
            return False, totalInputtedCoins

def inputMoney(resources):
    q=0.25
    d=0.10
    n=0.05
    p=0.01
    inpQuarters = input("How many quarters?")
    inpDimes = input("How many dimes?")
    inpNickels = input("How many nickels?")
    inpPennies = input("How many pennies?")

    totalInputtedCoins = float(inpQuarters)*q + float(inpDimes)*d + float(inpNickels)*n + float(inpPennies)*p
    return totalInputtedCoins


# espresso
def espresso(resources):
    # 50ml water, 18g coffee
    suffResources = sufficientResources("espresso", resources)
    if suffResources:
        suffCoins, inpMoney = sufficientCoins("espresso", resources)
    if suffResources and suffCoins:
        resources["water"] -= 50
        resources["coffee"] -= 18
        #moneycalcs
        if inpMoney > 1.50:
            change = inpMoney - 1.50
            print("returning change: $", "{:.2f}".format(change))
        else:
            resources["money"] += 1.50
        print("Enjoy your espresso\n\n")
    ask(resources)

# latte
def latte(resources):
    # 200ml water
    # 24g coffee
    # 150ml milk
    # $2.50
    suffResources = sufficientResources("latte", resources)
    if suffResources:
        suffCoins, inpMoney = sufficientCoins("latte", resources)
    if suffResources and suffCoins:
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
        #moneycalcs
        if inpMoney > 2.50:
            change = inpMoney - 2.50
            print("returning change: $", "{:.2f}".format(change))
        else:
            resources["money"] += 2.50
        print("Enjoy your latte\n\n")
    ask(resources)

# cappuccino
def cappuccino(resources):
    # 250ml water
    # 24g coffee
    # 100ml milk
    # $3.00
    suffResources = sufficientResources("cappuccino", resources)
    if suffResources:
        suffCoins, inpMoney = sufficientCoins("cappuccino", resources)
    if suffResources and suffCoins:
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100
        #moneycalcs
        if inpMoney > 3.00:
            change = inpMoney - 3.00
            print("returning change: $", "{:.2f}".format(change))
        else:
            resources["money"] += 3.00
        print("Enjoy your cappuccino\n\n")
    ask(resources)


def addResources(resources):
    resources["water"] += float(input("How much water are you adding?"))
    resources["milk"] += float(input("How much milk are you adding?"))
    resources["coffee"] += float(input("How much coffee are you adding?"))
    print("\n\n")
    ask(resources)

# -----------------------------------------------------------------------
# Starting resource values
water = 100
milk = 50
coffee = 76
money = 2.5

resources = {
    "water": water,
    "milk": milk,
    "coffee": coffee,
    "money": money
}

ask(resources)
