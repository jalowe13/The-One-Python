import os
import random
from . import mechanics
from .mechanics.character import Character
from .mechanics.enemy import Enemy
from .mechanics.weapon import Weapon

print("Importing Main Game")

#   VERSION UPDATE CONTROL
#   Change these values for each version update
version_number = "0.7.4"  # version number for each commit
version_date = "2021-01-09"  # the date for each commit version
#   VERSION UPDATE CONTROL


def login():
    username = input("Username: ")
    password = input("Password: ")
    correct = 1
    player = Character(username, password)
    # Parsing Save File
    try:
        with open("game/data/saves/" + username, "r") as values:
            for line in values:
                if correct:
                    newline = line.split('=')
                    name = newline[0].rstrip()  # Removing newline characters
                    value = newline[1].rstrip()
                    # Int conversion check
                    if name == "username" or name == "password" or name == "equipped_weapon":
                        player.stats[name] = value
                    else:
                        player.stats[name] = int(player.stats[name])
                        player.stats[name] = int(value)

                    if name == "password" and value != password:
                        correct = 0
                        os.system("cls||clear")
                        print("*******Password for " + username + " was not correct*******")
                        player.stats["password"] = "DENIED"
                        os.system("pause")
                        os.system("cls||clear")
                        launch()
    except IOError as e:
        os.system("cls||clear")
        print("*******Save file for " + username + " not found*******")
        os.system("pause")
        os.system("cls||clear")
        launch()
    return player


def create_account():
    username = input('What would you like your username to be?: ')
    password = input('What would you like your password to be?: ')

    #   Save File Contents
    save = open("game/data/saves/" + username, "w")
    save.write("username=" + username + "\n")
    save.write("password=" + password + "\n")
    player = Character(username, password)
    with open("game/data/" + "default_values.txt") as values:
        for line in values:
            save.write(line)
    return player
    # Saving file in town


def save_file(player):
    #   Save File Contents Of All Stats
    new_save = open("game/data/saves/" + player.stats["username"], "w")
    new_save.write("username=" + player.stats["username"] + "\n")
    new_save.write("password=" + player.stats["password"] + "\n")
    new_save.write("hp=" + str(player.stats["hp"]) + "\n")
    new_save.write("max_hp=" + str(player.stats["max_hp"]) + "\n")
    new_save.write("gold=" + str(player.stats["gold"]) + "\n")
    new_save.write("bank_gold=" + str(player.stats["bank_gold"]) + "\n")
    new_save.write("heal_gold=" + str(player.stats["heal_gold"]) + "\n")
    new_save.write("flee_gold=" + str(player.stats["flee_gold"]) + "\n")
    new_save.write("town=" + str(player.stats["town"]) + "\n")
    new_save.write("level=" + str(player.stats["level"]) + "\n")
    new_save.write("max_cave_level=" + str(player.stats["max_cave_level"]) + "\n")
    new_save.write("equipped_weapon=" + str(player.stats["equipped_weapon"]) + "\n")
    new_save.write("dmg_base=" + str(player.stats["dmg_base"]) + "\n")
    print("Saved")
    return player


def launch():
    print("Launched")
    # os.system("pause")  # Uncomment for debugging module loading
    os.system("cls||clear")
    os.system("title The One [" + version_number + "]")
    mechanics.basic_media.printimage("titleart.txt")
    print('Python Edition ')
    print("version " + version_number + " (" + version_date + ") [Jacob Lowe]")
    mechanics.basic_media.printimage("title_valley.txt")
    print('1) Login')
    print('2) Create Account')
    print('3) Exit')
    title_selection = input("Selection: ")
    # Title Selection
    if title_selection == '3':
        exit(0)
    if title_selection == '2':
        p = create_account()
        os.system("cls||clear")
        town(p)
    if title_selection == '1':
        loaded_player = login()
        os.system("cls||clear")
        town(loaded_player)
    os.system("cls||clear")
    launch()
    # Area One


def town(player):
    os.system("cls||clear")
    mechanics.basic_media.printimage("pico.txt")
    print(" ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»      [" + player.stats["username"] + "]")
    print(" º What would you like to do?")
    print(".ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ")
    print(" º 1) Local Elven-dale Cave    º")
    print(" º 2) Equip                    º")
    print(" º 3) Save                     º")
    print(" º 4) Heal                     º")
    print(" º 5) Bank                     º")
    print(" º 6) Shop                     º")
    print(" º 9) Log Out                  º")
    print(" ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")
    print(".    º HP[" + str(player.stats["hp"]) + "] ºGold[" + str(player.stats["gold"]) + "] º")
    print(".    ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")
    print("     [Currently Equipped][" + player.get_weapon() + "] [Base Damage] [" + str(player.get_weapon_dmg()) + "]")

    try:
        town_selection = int(input("Selection: "))

        #   Selection statements
        if town_selection == 1:
            elv_cave_enter(player)
        if town_selection == 2:
            player.equip()
            town(player)
        if town_selection == 3:
            player = save_file(player)
            # Removed for linux # mechanics.basic_media.savesound()
            town(player)
        if town_selection == 4:
            player.heal(0)
            town(player)
        if town_selection == 5:
            mechanics.bank.enter(player)
        if town_selection == 6:
            os.system("cls||clear")
            print(player.get_name() + " has entered the shop")
            os.system("pause")
            mechanics.shop.enter(player)
        if town_selection == 9:
            launch()
    except ValueError:
        print("Command not found")
        os.system("pause")
        town(player)


def elv_cave_enter(player):
    os.system("cls||clear")
    print("You step into the cave")
    current_enemy = Enemy()
    mechanics.basic_media.printimage("cave.txt")
    os.system("pause")
    os.system("cls||clear")
    print("Cave Level [" + str(player.get_max_cave_level()) + "]")
    mechanics.basic_combat.start(player, current_enemy)
    elv_cave_post_battle(player)
    # Combat Start Tasks and Randomization

    # Player and Enemy Attacks
    # Player attack portion of the cave


def elv_cave_exit(player):
    os.system("cls||clear")
    print("You step out of the cave")
    os.system("pause")
    town(player)
    # Cave Exit Post Battle


def elv_cave_post_battle(player):
    player.inc_cave_level()
    os.system("cls||clear")
    print("[" + player.get_name() + "] [Level " + str(player.get_level()) + "] [" + str(player.get_hp()) + "HP]")
    print("What would you like to do?")
    print(" 1) Decend deeper into the cave 2) Exit the cave")
    try:
        select = int(input("Selection: "))
    except ValueError:
        elv_cave_post_battle(player)
    if select == 1:
        new_enemy = Enemy()
        os.system("cls||clear")
        print("Cave Level [" + str(player.get_max_cave_level()) + "]")
        won = mechanics.basic_combat.start(player, new_enemy)
        if won:
            elv_cave_post_battle(player)
        else:
            print("Error in Win Condition")
    if select == 2:
        town(player)
    else:
        elv_cave_post_battle(player)
    # Cave Death


print("Main Game imported!")
