import os
import random

from game.mechanics.weapon import Weapon


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
                os.system("cls||clear")
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
        print(self.get_name() + " has equipped the " + str(self.stats["equipped_weapon"]))

    def store_backpack(self, item):
        backpack = self.stats["backpack"]
        backpack.append()

    def add_gold(self, amount):  # Passes in amount of new gold
        os.system("cls||clear")
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