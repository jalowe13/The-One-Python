import ctypes

ctypes.windll.kernel32.SetConsoleTitleA('The One')  # Setting the command prompt window opened to a specific title


class Character:
    name = ''
    password = ''
    hp = 0
    max_hp = 0
    gold = 0
    bank_gold = 0
    flee_gold = 0
    town = 1
    level = 1

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.hp = 100
        self.max_hp = 100
        self.gold = 25
        self.bank_gold = 0
        self.flee_gold = 50
        self.town = 1
        self.level = 1
        print("Default Values Loaded!")

    def print_values(self):
        print("Values for " + self.name + "lvl " + str(self.level))
        print("HP[" + str(self.hp) + "/" + str(self.max_hp) + "]")
        print("Gold[" + str(self.gold) + "]")
        print("Bank Gold[" + str(self.bank_gold) + "]")
        print("Flee Gold Cost[" + str(self.flee_gold) + "]")
        print("Current Town[" + str(self.town) + "]")


def login():
    pass


def create_account():
    print('What would you like your username to be?')
    username = input()
    print('What would you like your password to be?')
    password = input()

    #   Save File Contents
    save = open(username + ".txt", "w")
    save.write("username = '" + username + "'\n")
    save.write("password = '" + password + "'\n")
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
        p.print_values()



title()


