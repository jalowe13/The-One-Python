import os
import random
# import pyautogui
from . import mechanics

print("Importing Main Game")


# Classes
# Generalized Character Class for Player
class Character:
    stats = {
        "username": "",
        "password": "",
        "hp": 0,
        "max_hp": 0,
        "gold": 0,
        "bank_gold": 0,
        "heal_gold": 0,
        "flee_gold": 0,
        "town": 1,
        "level": 1,
        "max_cave_level": 1,
        "equipped_weapon": "Fists",
        "dmg_base": 1,
        "backpack": []
    }

    def __init__(self, username, password):
        self.stats["username"] = username
        self.stats["password"] = password
        # Convert to int
        self.stats["hp"] = int(self.stats["hp"])
        self.stats["max_hp"] = int(self.stats["max_hp"])
        self.stats["gold"] = int(self.stats["gold"])
        self.stats["bank_gold"] = int(self.stats["bank_gold"])
        self.stats["heal_gold"] = int(self.stats["heal_gold"])
        self.stats["flee_gold"] = int(self.stats["flee_gold"])
        self.stats["town"] = int(self.stats["town"])
        self.stats["level"] = int(self.stats["level"])
        # Weapon
        self.stats["equipped_weapon"] = str(self.stats["equipped_weapon"])
        self.stats["dmg_base"] = int(self.stats["dmg_base"])
        # Initial Load values
        self.stats["hp"] = 100
        self.stats["max_hp"] = 100
        self.stats["gold"] = 25
        self.stats["bank_gold"] = 0
        self.stats["heal_gold"] = 20
        self.stats["flee_gold"] = 50
        self.stats["town"] = 1
        self.stats["level"] = 1

    # print("Default Values for new Character " + username + "Loaded!") # For Loading Default Value Debug

    def print_stats(self):  # Prints out stats of the character
        print("Printing Stats for User[" + self.stats["username"] + "]")
        print(self.stats)

    # Getters for Stats
    def get_name(self):
        username = str(self.stats.get("username"))
        return username

    def get_level(self):
        return int(self.stats["level"])

    def get_hp(self):
        return int(self.stats["hp"])

    def get_weapon(self):
        return str(self.stats["equipped_weapon"])

    def get_weapon_dmg(self):
        return int(self.stats["dmg_base"])

    def get_gold(self):
        return int(self.stats["gold"])

    def get_bank_gold(self):
        return int(self.stats["bank_gold"])

    def get_max_cave_level(self):
        return int(self.stats["max_cave_level"])

    def inc_cave_level(self):
        new_level = int(self.stats["max_cave_level"])
        self.stats["max_cave_level"] = new_level + 1

    def set_cave_level(self, new_level):
        self.stats["max_cave_level"] = new_level

    def attack(self):  # Amount to calculate for damage
        damage_mod = random.randint(1, 20)  # Random Damage Modifier
        return int(int(self.stats["dmg_base"]) + damage_mod)

    def attacked(self, amount):  # Passes in amount of damage taken
        new_health = int(self.stats["hp"] - amount)
        self.stats["hp"] = new_health
        print(self.get_name() + " was hit for " + str(amount) + "HP")
        os.system("pause")

    def heal(self, condition):  # Healing condition to self heal when called when the right amount of heal gold is met
        if condition == 0:  # Gold required
            if self.stats["gold"] >= self.stats["heal_gold"]:
                hp_dif = self.stats["max_hp"] - self.stats["hp"]
                self.stats["gold"] = self.stats["gold"] - self.stats["heal_gold"]
                self.stats["hp"] = self.stats["max_hp"]
                print(self.stats["username"] + " has healed " + str(hp_dif) + " HP")
                os.system("pause")
                os.system('cls')
            else:
                print(self.stats["username"] + " does not have enough gold")
                print("Gold[" + str(self.stats["gold"]) + "] Gold Needed[" + str(
                    self.stats["heal_gold"] - self.stats["gold"]) + "]")
                os.system("pause")
        if condition == 1:  # Bypass gold
            self.stats["hp"] = self.stats["max_hp"]

    def equip(self):
        print(os.listdir("game\data\weapons"))
        print("Please enter the name of the item you would like to equip")
        weapon_name = input("Selection: ")
        equipped = Weapon(weapon_name)
        self.stats["equipped_weapon"] = equipped.load_name()
        self.stats["dmg_base"] = equipped.load_dmg()
        print(self.get_name() + "has equipped the " + str(self.stats["equipped_weapon"]))

    def store_backpack(self, item):
        backpack = self.stats["backpack"]
        backpack.append()

    def add_gold(self, amount):  # Passes in amount of new gold
        os.system("cls")
        new_gold = int(self.stats["gold"] + amount)
        self.stats["gold"] = new_gold
        print(self.get_name() + " gained " + str(amount) + "GP")
        os.system("pause")

    def set_gold(self, amount):
        new_gold = int(amount)
        self.stats["gold"] = new_gold

    def set_bank_gold(self, amount):
        new_gold = int(amount)
        self.stats["bank_gold"] = new_gold
    # Generalized Enemy Class


class Enemy:
    stats = {
        "name": "",
        "level_base": 0,
        "gold_base": 0,
        "exp_base": 0,
        "hp_base": 0,
        "dmg_base": 0
    }

    def __init__(self):
        # Select Random Enemy File
        enemy_path = 'game\data\enemies'
        random_enemy = random.choice(os.listdir(enemy_path))
        # Parsing Data
        try:
            with open(enemy_path + '/' + random_enemy, "r") as enemy_values:
                for line in enemy_values:
                    newline = line.split('=')
                    name = newline[0].rstrip()  # Removing newline characters
                    enemy_value = newline[1].rstrip()
                    self.stats[name] = enemy_value

        except IOError as e:  # Error for not finding save file
            os.system('cls')
            print("Enemy Instantiation Save File Error")
        # Local stats variables
        self.stats["level_base"] = int(self.stats["level_base"])
        self.stats["gold_base"] = int(self.stats["gold_base"])
        self.stats["exp_base"] = int(self.stats["exp_base"])
        self.stats["hp_base"] = int(self.stats["hp_base"])
        self.stats["dmg_base"] = int(self.stats["dmg_base"])
        # Random stats modifier ex attack
        stats_mod = random.randint(1, 3)
        self.stats["level_base"] *= stats_mod
        self.stats["gold_base"] *= stats_mod
        self.stats["exp_base"] *= stats_mod
        self.stats["hp_base"] *= stats_mod
        self.stats["dmg_base"] *= stats_mod

    # Getters for Stats
    def get_name(self):
        return str(self.stats["name"])

    def get_level(self):
        return int(self.stats["level_base"])

    def get_hp(self):
        return int(self.stats["hp_base"])

    def get_gold(self):
        return int(self.stats["gold_base"])

    def attack(self):  # Amount to calculate for damage
        damage_mod = random.randint(1, 20)  # Random Damage Modifier
        return int(int(self.stats["dmg_base"]) + damage_mod)

    def attacked(self, amount):  # Passes in amount of damage taken
        new_health = int(self.stats["hp_base"] - amount)
        self.stats["hp_base"] = new_health
        print(self.get_name() + " was hit for " + str(amount) + "HP")
        os.system("pause")
    # Generalized Weapon Class


class Weapon:
    stats = {
        "name": "Default_Weapon",
        "dmg": 1
    }

    def __init__(self, weapon):
        # Select Weapon File
        weapon_path = 'game\data\weapons'
        # Parsing Data
        try:
            with open(weapon_path + '/' + weapon, "r") as weapon_values:
                for line in weapon_values:
                    newline = line.split('=')
                    name = newline[0].rstrip()  # Removing newline characters
                    weapon_value = newline[1].rstrip()
                    self.stats[name] = weapon_value
        except IOError as e:  # Error for not finding save file
            os.system('cls')
            print("Enemy Instantiation Save File Error")

    def load_name(self):
        return str(self.stats["name"])

    def load_dmg(self):
        return int(self.stats["dmg"])


# Methods
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
                        os.system('cls')
                        print("*******Password for " + username + " was not correct*******")
                        player.stats["password"] = "DENIED"
                        os.system("pause")
                        os.system("cls")
                        launch()
    except IOError as e:
        os.system('cls')
        print("*******Save file for " + username + " not found*******")
        os.system("pause")
        os.system("cls")
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
    # os.system("pause") # Uncomment for debugging module loading
    os.system("cls")
    version = "version 0.7.2 (2020-12-21) [Jacob Lowe]"
    os.system("title The One [" + version + "]")
    mechanics.basic_media.printimage("titleart.txt")
    print('Python Edition ')
    print(version)
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
        os.system('cls')
        town(p)
    if title_selection == '1':
        loaded_player = login()
        os.system('cls')
        town(loaded_player)
    os.system("cls")
    launch()
    # Area One


def town(player):
    os.system('cls')
    mechanics.basic_media.printimage("pico.txt")
    print(" ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»      [" + player.stats["username"] + "]")
    print(" º What would you like to do?")
    print(".ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ")
    print(" º 1) Local Elven-dale Cave    º")
    print(" º 2) Equip                    º")
    print(" º 3) Save                     º")
    print(" º 4) Heal                     º")
    print(" º 5) Bank                     º")
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
            mechanics.basic_media.savesound()
            town(player)
        if town_selection == 4:
            player.heal(0)
            town(player)
        if town_selection == 5:
            mechanics.bank.enter(player)
        if town_selection == 9:
            launch()
    except ValueError:
        print("Command not found")
        os.system("pause")
        town(player)


def elv_cave_enter(player):
    os.system('cls')
    print("You step into the cave")
    current_enemy = Enemy()
    mechanics.basic_media.printimage("cave.txt")
    os.system("pause")
    os.system('cls')
    print("Cave Level [" + str(player.get_max_cave_level()) + "]")
    mechanics.basic_combat.start(player, current_enemy)
    elv_cave_post_battle(player)
    # Combat Start Tasks and Randomization

    # Player and Enemy Attacks
    # Player attack portion of the cave


def elv_cave_exit(player):
    os.system("cls")
    print("You step out of the cave")
    os.system("pause")
    town(player)
    # Cave Exit Post Battle


def elv_cave_post_battle(player):
    player.inc_cave_level()
    os.system("cls")
    print("[" + player.get_name() + "] [Level " + str(player.get_level()) + "] [" + str(player.get_hp()) + "HP]")
    print("What would you like to do?")
    print(" 1) Decend deeper into the cave 2) Exit the cave")
    try:
        select = int(input("Selection: "))
    except ValueError:
        elv_cave_post_battle(player)
    if select == 1:
        new_enemy = Enemy()
        os.system("cls")
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
