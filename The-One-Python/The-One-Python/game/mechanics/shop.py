import os
from .. import title
print("Importing Shop...")


def enter(player):
    os.system("cls||clear")
    print("Welcome to the Town Shop!")
    print("What would you like to do?")
    print("1) Buy       2) Sell         3) Exit")
    try:
        selection = int(input("Selection:   "))
        if selection == 1:
            buy(player)
        if selection == 2:
            sell(player)
        if selection == 3:
            exit_shop(player)
    except ValueError:
        enter(player)


def buy(player):
    print("-----Shop Selection-----")
    print(os.listdir("game\data\weapons"))
    print("------------------------")
    enter(player)


def sell(player):
    enter(player)


def exit_shop(player):
    os.system("cls||clear")
    print(player.get_name() + " has exited the shop")
    os.system("pause")
    title.town(player)
    # Returns back to where the shop was called


print("Shop Imported!")
