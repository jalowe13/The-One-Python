import os
# import winsound

print("Importing Basic Media...")
# 236 66 Max
# 118 for ascii art width
# 55 height max?


def colorText(text):
    os.system("color")
    return text


def printimage(image_name):
    # Example printing out an ASCII file
    file = open("game/art/" + image_name, 'r')  # Opening the file in a different directory
    ascii = "".join(file.readlines())
    print(colorText(ascii))


# def playsound():
#     freq = 100
#     dur = 50
#     for i in range(0, 5):
#         winsound.Beep(freq, dur)
#         freq += 100
#         dur += 1


# def exitsound():
#     freq = 600
#     dur = 50
#     for i in range(0, 5):
#         winsound.Beep(freq, dur)
#         freq = freq - 100
#         dur += 1


# def savesound():
#     freq = 1500
#     dur = 50
#     for i in range(0, 2):
#         winsound.Beep(freq, dur)
#         dur += 1


# def hitenemy():
#     freq = 200
#     dur = 100
#     for i in range(0, 2):
#         winsound.Beep(freq, dur)


# def enemyhit():
#     freq = 100
#     dur = 100
#     for i in range(0, 2):
#         winsound.Beep(freq, dur)


# playsound()

print("Basic Media Imported!")
