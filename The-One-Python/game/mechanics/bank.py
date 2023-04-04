# Bank module
import os
from . import basic_media
from .. import title

print("Importing Bank...")


#   Enter into bank
def enter(player):
    os.system("cls")
    basic_media.printimage("bank_greeting_art.txt")
    print("Current Gold: " + str(player.get_gold()) + "     Bank Gold: " + str(player.get_bank_gold()))
    print("1) Deposit       2) Withdraw         3) Exit")
    try:  # Deposit or withdraw
        selection = int(input("Selection: "))
        if selection == 1:
            deposit(player)
        if selection == 2:
            withdraw(player)
        if selection == 3:
            title.town(player)
    except ValueError:
        enter(player)


#   Deposit amount
def deposit(player):
    os.system("cls")
    basic_media.printimage("bank_withdraw_art.txt")
    current_bank_gold = player.get_bank_gold()
    current_gold = player.get_gold()
    try:  # Try to deposit amount
        amount = int(input("Amount: "))
        if current_gold >= amount and current_gold > 0:
            player.set_bank_gold(current_bank_gold + amount)
            player.set_gold(current_gold - amount)
            os.system("cls")
            print(str(amount) + " gold deposited")
            os.system("pause")
            enter(player)
        else:
            os.system("cls")
            print("You don't have enough gold!")
            os.system("pause")
            enter(player)
    except ValueError:  # Could not transfer to Int
        enter(player)


#   Withdraw amount
def withdraw(player):
    os.system("cls")
    basic_media.printimage("bank_withdraw_art.txt")
    current_bank_gold = player.get_bank_gold()
    current_gold = player.get_gold()
    try:  # Try to deposit amount
        amount = int(input("Amount: "))
        if current_bank_gold >= amount and current_bank_gold > 0:
            player.set_gold(current_gold + amount)
            player.set_bank_gold(current_bank_gold - amount)
            os.system("cls")
            print(str(amount) + " gold withdrawn")
            os.system("pause")
            enter(player)
        else:
            os.system("cls")
            print("You don't have enough gold in the bank!")
            os.system("pause")
            enter(player)
    except ValueError:  # Could not transfer to Int
        enter(player)


print("Bank Imported!")
