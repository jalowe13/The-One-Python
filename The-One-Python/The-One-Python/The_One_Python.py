import ctypes

ctypes.windll.kernel32.SetConsoleTitleA('The One')  # Setting the command prompt window opened to a specific title


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
        print("Default Values for new Character " + username + "Loaded!")

    def print_stats(self):
        print("Printing Stats for User[" + self.stats["username"] + "]")
        print(self.stats)


def login(player):
    print("Username: ")
    username = input()
    print("Password: ")
    password = input()
    with open(username + ".txt", "r") as values:
        for line in values:
            newline = line.split('=')
            name = newline[0].rstrip()  # Removing newline characters
            value = newline[1].rstrip()
            player.stats[name] = value


def create_account():
    print('What would you like your username to be?')
    username = input()
    print('What would you like your password to be?')
    password = input()

    #   Save File Contents
    save = open(username + ".txt", "w")
    save.write("username=" + username + "\n")
    save.write("password=" + password + "\n")
    player = Character(username, password)
    with open("data/" + "default_values.txt") as values:
        for line in values:
            save.write(line)
    return player


def title():
    p = Character("UNKNOWN", "UNKNOWN")
    title_file = open("art/" + "titleart.txt", 'r')  # Opening the file in a different directory
    print(title_file.read())
    print('Current Version: v0.3_80 [Jacob Lowe]')
    print('1) Login')
    print('2) Create Account')
    print('3) Exit')
    title_selection = input()
    if title_selection == '2':
        p = create_account()
        p.print_stats()
    if title_selection == '1':
        login(p)
        p.print_stats()


title()
