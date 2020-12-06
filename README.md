# The-One-Python
https://github.com/jalowe13/The-One-Python/
Command Line Based Text Adventure Game
Created In Python off of a concept made in 2010, ported into Python instead of Batch Script
Implementations will include a town area, dungeon, and basic combat system, as well as randomly generated encounters
Jacob Lowe

[Project Notice]  [This is not a completed Version of the Game]
The following program only has the following parts implemented for the ECE 2524 Project to correctly show the UNIX System Administration work involved, such as file management
--------------------
Features Implemented
--------------------
- File Creation, Updating, and Reference
- Main Town
- Heal at Town
- Save at Town
- Basic Combat
- Equip in Combat

-------------------
Instructions (Saving Files and Loading Files)
-------------------
Included in the The-One-Python folder is all of the data needed to execute the game
- Launch The_One_Python.py with any python executer
- At the title screen you'll be able to make a save file with create account by pressing 2, after that when you start the program again you can load those values by pressing 1
- After this point you can create your own username and password required for gaining information about the file later
- Once the save file is created then it will be made in the directory with the game in a text file with all information about the player
- If you enter 5 you can go into basic combat in the cave
- If you enter 9 you will write all the current data about your current session of your game to your save file
- If you enter 10 your health will be restored after paying a fine declared in your character file


-------------------
Cave Mechanics (Using Python Classes and Reading Data of Files in Directories to Make Enemy Encounters)
-------------------
Cave encounters also use the same method of loading data values from files about Enemies or Weapons in order to use them in this combat section
- If you enter 1 you can attack the randomly selected enemy from the enemies directory with your currently equipped weapon
- If you enter 2 you can select a weapon in the weapons directory to skew your attack numbers against an enemy to help with combat
- If you enter 3 you run away if you have more health than your currently faced enemy

After your combat you will either perish or you'll be able to decent deeper into the cave by selecting 1, or go back to the town so you can heal or save with 2

---
Note
---
There are also test accounts that you can test login with with the provided information

username=Hokie
password=gotech

username=Newbie
password=throw

---
Hope you enjoy my game mechanics!
---

