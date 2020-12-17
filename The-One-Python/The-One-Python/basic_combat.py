# Basic Combat Methods
import os
import importlib

game = importlib.import_module('The_One_Python')
media = importlib.import_module('basic_media')


def start(player, enemy):
    os.system('cls')
    print("[" + player.get_name() + "] [Level " + str(player.get_level()) + "] [" + str(
        player.get_hp()) + "HP]  [" + enemy.get_name() + "][Level" + str(enemy.get_level()) + "] [" + str(
        enemy.get_hp()) + "HP]")
    print("[Currently Equipped][" + player.get_weapon() + "] [Base Damage] [" + str(player.get_weapon_dmg()) + "]")
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
        if player.get_hp() > enemy.get_hp():
            print(player.get_name() + " runs away from " + enemy.get_name())
            os.system("pause")
            game.elv_cave_exit(player)
        else:
            print("The " + enemy.get_name() + " strikes fear into your heart. You cannot escape")
            os.system("pause")
            start(player, enemy)
    start(player, enemy)


def player_move(player, enemy):
    os.system("cls")
    damage = player.attack()
    print(player.get_name() + " attacked " + enemy.get_name())
    media.hitenemy()
    enemy.attacked(damage)
    enemy_hp = int(enemy.get_hp())
    if enemy_hp <= 0:
        gold = enemy.get_gold()
        player.add_gold(gold)
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
    print(enemy.get_name() + " attacked " + player.get_name())
    media.enemyhit()
    player.attacked(damage)
    enemy_hp = int(enemy.get_hp())
    player_hp = int(player.get_hp())
    if player_hp <= 0:
        return True
    if enemy_hp <= 0:
        gold = enemy.get_gold()
        player.add_gold(gold)
        return False
    start(player, enemy)


def faint(player):  # Player fainting under 0 HP
    print(player.get_name() + " has faded into existence, only the winds whisper " + player.get_name() + "'s name now.")
    print(player.get_name() + " has lost all of their gold.")
    print(" ")
    player.set_gold(9999)
    player.heal(1)
    player.set_gold(0)
    game.save_file(player)
    print(" ")
    print("[Game Over]")
    media.printimage("death.txt")
    media.exitsound()
    os.system("pause")
    os.system("cls")
    game.main()
