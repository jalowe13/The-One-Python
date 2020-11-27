import ctypes

ctypes.windll.kernel32.SetConsoleTitleA('The One')  # Setting the command prompt window opened to a specific title


def login():
    pass


def create_account():
    print('What would you like your username to be?')
    username = input()
    print('What would you like your password to be?')
    password = input()

#   Save File Contents
    save = open(username + ".py", "w")
    save.write("username = '" + username + "'\n")
    save.write("password = '" + password + "'\n")
    with open("data_values/" + "default_values.py") as default_values:
        for line in default_values:
            save.write(line)


def title():
    title = open("art/" + "titleart.txt", 'r')  # Opening the file in a different directory
    print(title.read())
    print('Current Version: v0.3_80 [Jacob Lowe]')
    print('1) Login')
    print('2) Create Account')
    print('3) Exit')
    title_selection = input()

    if title_selection == '2':
        create_account()


title()
