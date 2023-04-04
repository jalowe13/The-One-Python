import os
import random


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
        enemy_path = 'game/data/enemies'
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
            os.system("cls||clear")
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
