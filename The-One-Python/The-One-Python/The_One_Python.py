import os


class Character:
    stats = {
        "username": "",
        "password": "",
        "hp": 0,
        "max_hp": 0,
        "gold": 0,
        "bank_gold": 0,
        "flee_gold": 0,
        "town": 1,
        "level": 1
    }

    def __init__(self, username, password):
        self.stats["username"] = username
        self.stats["password"] = password
        self.stats["hp"] = 100
        self.stats["max_hp"] = 100
        self.stats["gold"] = 25
        self.stats["bank_gold"] = 0
        self.stats["flee_gold"] = 50
        self.stats["town"] = 1
        self.stats["level"] = 1
        # print("Default Values for new Character " + username + "Loaded!") # For Loading Default Value Debug

    def print_stats(self):
        print("Printing Stats for User[" + self.stats["username"] + "]")
        print(self.stats)


def login(player):
    username = input("Username: ")
    password = input("Password: ")
    correct = 1

    try:
        with open(username + ".txt", "r") as values:
            for line in values:
                if correct:
                    newline = line.split('=')
                    name = newline[0].rstrip()  # Removing newline characters
                    value = newline[1].rstrip()
                    player.stats[name] = value
                    if name == "password" and value != password:
                        correct = 0
                        print("Password incorrect")
                        player.stats["password"] = "DENIED"
    except IOError as e:
        os.system('cls')
        print("*******Save file for " + username + " not found*******")
        main()
    return player


def create_account():
    username = input('What would you like your username to be?')
    password = input('What would you like your password to be?')

    #   Save File Contents
    save = open(username + ".txt", "w")
    save.write("username=" + username + "\n")
    save.write("password=" + password + "\n")
    player = Character(username, password)
    with open("data/" + "default_values.txt") as values:
        for line in values:
            save.write(line)
    return player


def main():
    version = "version 0.4 (2020-11-28) [Jacob Lowe]"
    os.system("title The One [" + version + "]")
    print("This game is best in fullscreen...")
    os.system("pause")
    os.system("cls")
    p = Character("UNKNOWN", "UNKNOWN")
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
        p = login(p)
        os.system('cls')
        town(p)


# Area One
def town(player):
    print(" ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»")
    print(" º What would you like to do?  º")
    print(".ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹")
    print(" º 1) Travel to the next town  º")
    print(".º                             º")
    print(" º 2) Elvendale Weapon Shop    º")
    print(".º                             º")
    print(" º 3) Elvendale Armor Shop     º")
    print(".º                             º")
    print(" º 4) Elvendale Trading Post   º")
    print(".º                             º")
    print(" º 5) Local Elven-dale Cave    º")
    print(".º                             º")
    print(" º 6) Skill Chart              º")
    print(".º                             º")
    print(" º 7) World Bank               º")
    print(".º                             º")
    print(" º 8) Quest's                  º")
    print(".º                             º")
    print(" º 9) Save                     º")
    print(" º                             º")
    print(" º 10) Heal                    º")
    print(" º                             º")
    print(" º 98) " + player.stats["username"] + "'s Inventory º")
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
    print(".    º HP=%HP% ºGold=%gold%  º")
    print(".    ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼")
    print(".")
    print(".")
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

if __name__ == "__main__":
    main()
