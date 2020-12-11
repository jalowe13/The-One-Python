import os
import random

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
        self.stats["heal_gold"]  = int(self.stats["heal_gold"])
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

     #Getters for Stats
    def getName(self): 
        username = str(self.stats.get("username"))
        return username

    def getLevel(self):
        return int(self.stats["level"])

    def getHP(self):
        return int(self.stats["hp"])

    def getWeapon(self):
        return str(self.stats["equipped_weapon"])

    def getWeaponDmg(self):
        return int(self.stats["dmg_base"])

    def attack(self): # Amount to calculate for damage
     damage_mod = random.randint(1,20) # Random Damage Modifier
     return int(int(self.stats["dmg_base"]) + damage_mod)

    def attacked(self,amount): # Passes in amount of damage taken
        newHealth = int(self.stats["hp"] - amount)
        self.stats["hp"] = newHealth
        print(self.getName() + " was hit for " + str(amount) + "HP")
        os.system("pause")

    def heal(self):  # Healing condition to self heal when called when the right amount of heal gold is met
        if self.stats["gold"] >= self.stats["heal_gold"]:
            hp_dif = self.stats["max_hp"] - self.stats["hp"]
            self.stats["gold"] = self.stats["gold"] - self.stats["heal_gold"]
            self.stats["hp"] = self.stats["max_hp"]
            print(self.stats["username"] + " has healed " + str(hp_dif) + " HP")
            os.system("pause")
            os.system('cls')
        else:
            print(self.stats["username"] + " does not have enough gold")
            print("Gold[" + str(self.stats["gold"]) + "] Gold Needed[" + str(self.stats["heal_gold"] - self.stats["gold"]) + "]")
            os.system("pause")
    def equip(self):
        print(os.listdir("data\weapons"))
        print("Please enter the name of the item you would like to equip")
        weapon_name = input("Selection: ")
        equiped = Weapon(weapon_name)
        self.stats["equipped_weapon"] = equiped.load_name()
        self.stats["dmg_base"] = equiped.load_dmg()
        print(self.getName() + "has equipped the " + str(self.stats["equipped_weapon"]))
    def store_backpack(item):
        backpack = self.stats["backpack"]
        backpack.append()

    def addGold(self,amount): # Passes in amount of new gold
        newGold = int(self.stats["gold"] + amount)
        self.stats["gold"] = newGold
        print(self.getName() + " gained " + str(amount) + "GP")
        os.system("pause")
    # Generalized Enemy Class
class Enemy:
    stats = {
        "name":"",
        "level_base": 0,
        "gold_base": 0,
        "exp_base": 0,
        "hp_base": 0,
        "dmg_base": 0
    }

    def __init__(self):
        # Select Random Enemy File
        enemy_path = 'data\enemies'
        random_enemy = random.choice(os.listdir(enemy_path))
        # Parsing Data
        try:
            with open(enemy_path + '/' + random_enemy, "r") as enemy_values:
                for line in enemy_values:
                       newline = line.split('=')
                       name = newline[0].rstrip()  # Removing newline characters
                       enemy_value = newline[1].rstrip()
                       self.stats[name] = enemy_value

        except IOError as e: #Error for not finding save file
            os.system('cls')
            print("Enemy Instantiation Save File Error")
    # Local stats variables
        self.stats["level_base"] = int(self.stats["level_base"])
        self.stats["gold_base"] = int(self.stats["gold_base"])
        self.stats["exp_base"] = int(self.stats["exp_base"])
        self.stats["hp_base"] = int(self.stats["hp_base"])
        self.stats["dmg_base"] = int(self.stats["dmg_base"])
    # Random stats modifier ex attack
        stats_mod = random.randint(1,3)
        self.stats["level_base"]  *= stats_mod
        self.stats["gold_base"] *= stats_mod
        self.stats["exp_base"] *= stats_mod
        self.stats["hp_base"] *= stats_mod
        self.stats["dmg_base"] *= stats_mod

    #Getters for Stats
    def getName(self): 
        return str(self.stats["name"])

    def getLevel(self):
        return int(self.stats["level_base"])

    def getHP(self):
        return int(self.stats["hp_base"])

    def getGold(self):
        return int(self.stats["gold_base"])

    def attack(self): # Amount to calculate for damage
     damage_mod = random.randint(1,20) # Random Damage Modifier
     return int(int(self.stats["dmg_base"]) + damage_mod)
     
    def attacked(self,amount): # Passes in amount of damage taken
        newHealth = int(self.stats["hp_base"] - amount)
        self.stats["hp_base"] = newHealth
        print(self.getName() + " was hit for " + str(amount) + "HP")
        os.system("pause")
    # Generalized Weapon Class
class Weapon:
    stats = {
        "name":"Default_Weapon",
        "dmg": 1
    }
    def __init__(self,weapon):
        # Select Weapon File
        weapon_path = 'data\weapons'
        # Parsing Data
        try:
            with open(weapon_path + '/' + weapon + ".txt", "r") as weapon_values:
                for line in weapon_values:
                       newline = line.split('=')
                       name = newline[0].rstrip()  # Removing newline characters
                       weapon_value = newline[1].rstrip()
                       self.stats[name] = weapon_value
        except IOError as e: #Error for not finding save file
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
        with open(username + ".txt", "r") as values:
            for line in values:
                if correct:
                    newline = line.split('=')
                    name = newline[0].rstrip()  # Removing newline characters
                    value = newline[1].rstrip()
                    # Int converstion check
                    if name  == "username" or name == "password" or name == "equipped_weapon":
                        player.stats[name] = value
                    else:
                        player.stats[name] = int(player.stats[name])
                        player.stats[name] = int(value)

                    if name == "password" and value != password:
                        correct = 0
                        os.system('cls')
                        print("Password incorrect")
                        player.stats["password"] = "DENIED"
                        main()
    except IOError as e:
        os.system('cls')
        print("*******Save file for " + username + " not found*******")
        main()
    return player
def create_account():
    username = input('What would you like your username to be?: ')
    password = input('What would you like your password to be?: ')

    #   Save File Contents
    save = open(username + ".txt", "w")
    save.write("username=" + username + "\n")
    save.write("password=" + password + "\n")
    player = Character(username, password)
    with open("data/" + "default_values.txt") as values:
        for line in values:
            save.write(line)
    return player
    # Saving file in town
def save_file(player):
    #   Save File Contents Of All Stats
    new_save = open(player.stats["username"] + ".txt", "w")
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
    new_save.write("equipped_weapon=" + str(player.stats["equipped_weapon"]) + "\n")
    new_save.write("dmg_base=" + str(player.stats["dmg_base"]) + "\n")
    print("Saved")
    return player
def main():
    version = "version 0.6.1 (2020-12-05) [Jacob Lowe]"
    os.system("title The One [" + version + "]")
    print("This game is best in fullscreen...")
    print("[Project Notice][This is not a completed Version of the Game]")
    print("The following program only has the following parts implemented for the ECE 2524 Project to correctly show the UNIX System Administration work involved, such as file management")
    print("--------------------")
    print("Features Implemented")
    print("--------------------")
    print("- File Creation, Updating, and Reference")
    print("- Main Town")
    print("- Heal at Town")
    print("- Save at Town")
    print("- Basic Combat")
    print("- Equip in Combat")
    os.system("pause")
    os.system('cls')
    title_file = open("art/" + "titleart.txt", 'r')  # Opening the file in a different directory
    print(title_file.read())
    print('Python Edition ')
    print(version)
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
    main()
    # Area One
def town(player):
    os.system('cls')
    print(" ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»")
    print(" º What would you like to do?  º")
    print(".ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹")
   # print(" º 1) Travel to the next town  º")
   # print(".º                             º")
   # print(" º 2) Elvendale Weapon Shop    º")
   # print(".º                             º")
   # print(" º 3) Elvendale Armor Shop     º")
   # print(".º                             º")
   # print(" º 4) Elvendale Trading Post   º")
   # print(".º                             º")
    print(" º 5) Local Elven-dale Cave    º")
   # print(".º                             º")
   # print(" º 6) Skill Chart              º")
   # print(".º                             º")
    #print(" º 7) World Bank               º")
   # print(".º                             º")
   # print(" º 8) Quest's                  º")
   # print(".º                             º")
    print(" º 9) Save                     º")
   # print(" º                             º")
    print(" º 10) Heal                    º")
   # print(" º                             º")
   # print(" º 98) " + player.stats["username"] + "'s Inventory º")
    print(" ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")
    print(".")
    print(".")
    print(".")
    print(".          [" + player.stats["username"] + "]")
    print(".               _")
    print(".              ( )")
    print(".               I")
    print(".              YIY")
    print(".               I")
    print(".              I I")
    print(".")
    print(".    ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»")
    print(".    º HP[" + str(player.stats["hp"]) + "] ºGold[" + str(player.stats["gold"]) + "] º")
    print(".    ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")
    print("     [Currently Equipped][" + player.getWeapon() + "] [Base Damage] [" + str(player.getWeaponDmg()) + "]")
    print(".    ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(" ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»")
    print("   Currently logged in as " + player.stats["username"])
    print(".ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹")
    print(" º 99) Log out                           º")
    print(" ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")
    print(".")
    town_selection = input("Selection: ")

    #   Selection statements
    if town_selection == '10':
        player.heal()
        town(player)
    if town_selection == '5':
        elv_cave_enter(player)
    if town_selection == '9':
        player = save_file(player)
        town(player)
    if town_selection == '99':
        exit(0)
    else:
        print("Command not found")
        os.system("pause")
        town(player)
def elv_cave_enter(player):
    os.system('cls')
    print("You step into the cave")
    current_enemy = Enemy()
    # print(current_enemy.stats) #debugging stats
    os.system("pause")
    combat_start(player,current_enemy)
    # Combat Start Tasks and Randomization
def combat_start(player,enemy):
    os.system('cls')
    print("[" + player.getName() + "] [Level " + str(player.getLevel()) + "] [" + str(player.getHP()) + "HP]  [" + enemy.getName() + "][Level" + str(enemy.getLevel()) + "] [" + str(enemy.getHP()) + "HP]")
    print("[Currently Equipped][" + player.getWeapon() + "] [Base Damage] [" + str(player.getWeaponDmg()) + "]")
    print("")
    print( "What would you like to do?")
    print("")
    print("")
    print(" 1)Attack")
    print(" 2)Equip")
    print(" 3)Run")
    combat_selection = input("Selection: ")
    if combat_selection == '1': # Attack
        combat_player_attack(player,enemy)
    if combat_selection == '2': # Equip
        player.equip()
        combat_start(player,enemy)
    if combat_selection == '3': # Run
        if (player.getHP() > enemy.getHP()):
            print(player.getName() + " runs away from " + enemy.getName())
            os.system("pause")
            elv_cave_exit(player)
        else:
            print("The " + enemy.getName() + " strikes fear into your heart. You cannot escape")
            os.system("pause")
            combat_start(player,enemy)
    combat_start(player,enemy)
        # Player and Enemy Attacks
    # Player attack portion of the cave
def combat_player_attack(player,enemy):
    os.system("cls")
    damage = player.attack()
    print(player.getName() + " attacked " + enemy.getName())
    enemy.attacked(damage)
    enemyHP = int(enemy.getHP())
    if enemyHP <= 0:
       gold = enemy.getGold()
       player.addGold(gold)
       elv_cave_post_battle(player)
    else:
        combat_enemy_attack(player,enemy)
    # Enemy attack portion of the cave
def combat_enemy_attack(player,enemy):
    os.system("cls")
    damage = enemy.attack()
    print(enemy.getName() + " attacked " + player.getName())
    player.attacked(damage)
    enemyHP = int(enemy.getHP())
    playerHP = int(player.getHP())
    if playerHP <=0:
        elv_cave_faint(player)
    if enemyHP <= 0:
        gold = enemy.getGold()
        player.addGold(gold)
        elv_cave_post_battle(player)
    combat_start(player,enemy)
    # Cave Exit Method
def elv_cave_exit(player):
    os.system("cls")
    print("You step out of the cave")
    os.system("pause")
    town(player)
    # Cave Exit Post Battle
def elv_cave_post_battle(player):
    os.system("cls")
    print("What would you like to do?")
    print(" 1) Decend deeper into the cave 2) Exit the cave")
    select = input("Selection: ")
    if select == '1':
        new_enemy = Enemy()
        combat_start(player,new_enemy)
    if select == '2':
        town(player)
    elv_cave_post_battle(player)
    # Cave Death
def elv_cave_faint(player): # Player fainting under 0 HP
    print(player.getName() + " has faded into existance, only the winds whisper " + player.getName() + "'s name now.")
    print(" ")
    print("[Game Over]")
    os.system("pause")
    exit(0)
if __name__ == "__main__":
    main()
