import ctypes
ctypes.windll.kernel32.SetConsoleTitleA('The One') #Setting the command prompt window opened to a certian title

def login():
    pass

def createAccount():
    print('create')

def title():
    file = open("art/" + "titleart.txt" , 'r') # Opening the file in a different directory
    print(file.read())
    print ('Current Version: v0.3_80 [Jacob Lowe]')
    print ('1) Login')
    print ('2) Create Account')
    print ('3) Exit')
    title_selection = input()

    if (title_selection == '2'):
        createAccount()







title()





