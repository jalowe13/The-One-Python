import os


class Weapon:
    stats = {
        "name": "Default_Weapon",
        "dmg": 1
    }

    def __init__(self, weapon):
        # Select Weapon File
        weapon_path = "game\data\weapons"
        # Parsing Data
        try:
            with open(weapon_path + '/' + weapon, "r") as weapon_values:
                for line in weapon_values:
                    newline = line.split('=')
                    name = newline[0].rstrip()  # Removing newline characters
                    weapon_value = newline[1].rstrip()
                    self.stats[name] = weapon_value
        except IOError as e:  # Error for not finding save file
            os.system("cls||clear")
            print("Enemy Instantiation Save File Error")

    def load_name(self):
        return str(self.stats["name"])

    def load_dmg(self):
        return int(self.stats["dmg"])
