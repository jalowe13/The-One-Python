# Basic Combat Methods
import os
import random
import importlib

game = importlib.import_module('The_One_Python')
media = importlib.import_module('basic_media')

def start(player, enemy):
    os.system('cls')
    print("[" + player.getName() + "] [Level " + str(player.getLevel()) + "] [" + str(
        player.getHP()) + "HP]  [" + enemy.getName() + "][Level" + str(enemy.getLevel()) + "] [" + str(
        enemy.getHP()) + "HP]")
    print("[Currently Equipped][" + player.getWeapon() + "] [Base Damage] [" + str(player.getWeaponDmg()) + "]")
    print("")
    print("What would you like to do?")
    print("")
    print("")
    print(" 1)Attack")
    print(" 2)Equip")
    print(" 3)Run")
    combat_selection = input("Selection: ")
    if combat_selection == '1':  # Attack
        won = player_move(player, enemy)
        if won:
            return True
    if combat_selection == '2':  # Equip
        player.equip()
        start(player, enemy)
    if combat_selection == '3':  # Run
        if (player.getHP() > enemy.getHP()):
            print(player.getName() + " runs away from " + enemy.getName())
            os.system("pause")
            game.elv_cave_exit(player)
        else:
            print("The " + enemy.getName() + " strikes fear into your heart. You cannot escape")
            os.system("pause")
            start(player, enemy)
    start(player, enemy)

def player_move(player, enemy):
    os.system("cls")
    damage = player.attack()
    print(player.getName() + " attacked " + enemy.getName())
    media.hitenemy()
    enemy.attacked(damage)
    enemyHP = int(enemy.getHP())
    if enemyHP <= 0:
        gold = enemy.getGold()
        player.addGold(gold)
        return True
    else:
        kill = enemy_move(player, enemy)
        if kill:
            faint(player)
        else:
            return True

    # Enemy attack portion of the cave


def enemy_move(player, enemy):
    os.system("cls")
    damage = enemy.attack()
    print(enemy.getName() + " attacked " + player.getName())
    media.enemyhit()
    player.attacked(damage)
    enemyHP = int(enemy.getHP())
    playerHP = int(player.getHP())
    if playerHP <= 0:
        return True
    if enemyHP <= 0:
        gold = enemy.getGold()
        player.addGold(gold)
        return False
    start(player, enemy)

def faint(player):  # Player fainting under 0 HP
    print(player.getName() + " has faded into existance, only the winds whisper " + player.getName() + "'s name now.")
    print(" ")
    print("[Game Over]")
    media.printimage("death.txt")
    media.exitsound()
    os.system("pause")
    main()
