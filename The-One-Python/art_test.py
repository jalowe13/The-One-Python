import os
import winsound
#236 66 Max
# 118 for ascii art width
# 55 height max?


def colorText(text):

    return text

#Example printing out an ASCII file
file = open("art/" + "title_valley.txt", 'r')  # Opening the file in a different directory
os.system("color")
ascii = "".join(file.readlines())
#print(colorText(ascii))

freq = 100
dur = 50
  
# loop iterates 5 times i.e, 5 beeps will be produced. 
for i in range(0, 5):     
    winsound.Beep(freq, dur)     
    freq+= 100
    dur+= 1

os.system("pause")