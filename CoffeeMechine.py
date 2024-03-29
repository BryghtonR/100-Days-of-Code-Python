# 100 days of coding day 15: Coffee Mechine

    # Could use input error checking and a way to cancel or reset order

import os
os.system('cls')

#Dictionary for all possible drink choices
drinks = {
    "Expresso": {"water": 50, "coffee_grounds": 18, "milk": 0, "cost": 1.50},
    "Latte": {"water": 200, "coffee_grounds": 24, "milk": 150, "cost": 2.50},
    "Cappuccino": {"water": 250, "coffee_grounds": 24, "milk": 100, "cost": 3.00},
}

# Starting values for resources
coffee_grounds = 100
water = 300
milk = 200

# Starting values for money and coin values
coin_values = {
    "penny": .01,
    "nickel": .05,
    "dime": .10,
    "quarter": .25,
    }
penny_stack = 10
nickel_stack = 10
dime_stack = 10
quarter_stack = 10

# Function: print out total value of all coin stacks
def total_money():
    total_money = (penny_stack*coin_values["penny"])+(nickel_stack*coin_values["nickel"])+(dime_stack*coin_values["dime"])+(quarter_stack*coin_values["quarter"])
    print(total_money)

# Function: print out of current money/coins
def display_financial():
    print(f"Pennies: {penny_stack}")
    print(f"Nickels: {nickel_stack}")
    print(f"Dime: {dime_stack}")
    print(f"Quaters: {quarter_stack}")

# Function: print out of current resources
def display_resources():
    print(f"Coffee Grounds: {coffee_grounds}")
    print(f"Water: {water}")
    print(f"Milk: {milk}")

# Main Loop
play_again = "y"
while play_again == "y":
    #Main decision branching
    init_selection = input("Would you like to buy a drink?: y/n/r/f ")
    if init_selection == "y":
        drink_choice = input("What drink would you like to purchase? Expresso/Latte/Cappuccino ")

        # Check for available resources
        sufficient_resource = True
        if coffee_grounds < drinks[drink_choice]["coffee_grounds"]:
            print("Insufficient Coffee Grounds")
            sufficient_resource = False
        if water < drinks[drink_choice]["water"]:
            print("Insufficient Water")
            sufficient_resource = False
        if milk < drinks[drink_choice]["milk"]:
            print("Insufficient Milk")
            sufficient_resource = False
        if sufficient_resource == True:

            # Function: convert all deposited coins into int value
            def tally_coin_deposites():
                current_coin_value = 0 
                for coin in range(0,len(coin_deposites)):
                    current_coin_value += coin_values[coin_deposites[coin]]
                return round(current_coin_value, 2)

            # Accept money
            cost = drinks[drink_choice]["cost"]
            coin_deposites = []
            while cost> tally_coin_deposites():
                new_coin_deposite = input(f"{drink_choice}: ${tally_coin_deposites()} / ${cost} \nPlease incert coins now: penny/nickel/dime/quarter: ")
                coin_deposites.append(new_coin_deposite)
                total_deposite = tally_coin_deposites()

            # Deposite new money to coin stacks
            penny_stack += coin_deposites.count("penny")
            nickel_stack += coin_deposites.count("nickel")
            dime_stack += coin_deposites.count("dime")
            quarter_stack += coin_deposites.count("quarter")

            #wrap up transaction
            print("********** DESPENSE DRINK************")
            change = tally_coin_deposites() - cost
            print(f"Your change is ${change}")
            while change > 0:
                if change >= .25 and quarter_stack > 0:
                    print("Change: Quarter")
                    change -= .25
                    quarter_stack -= 1
                elif change >= .1 and dime_stack > 0:
                    print("Change: Dime")
                    change -= .1
                    dime_stack -= 1
                elif change >= .05 and nickel_stack > 0:
                    print("Change: Nickel")
                    change -= .05
                    nickel_stack -= 1
                elif change >= .01  and penny_stack > 0:
                    print("Change: Penny")
                    change -= .01
                    penny_stack -= 1
                elif change >0:
                    print("Out of change")
                    break;

            # Deduct resources
            coffee_grounds = coffee_grounds - drinks[drink_choice]["coffee_grounds"]
            water = water - drinks[drink_choice]["water"]
            mink = milk - drinks[drink_choice]["milk"]

    elif init_selection =="r":
        display_resources()
    elif init_selection =="f":
        display_financial()
        total_money()
    else:
        print("Thankyou and have a nice day!")

    play_again = input("Would you like to make another transaction: y/n ")
print("Program end")


