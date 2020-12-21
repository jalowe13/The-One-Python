# Basic Combat Methods
import os
from . import basic_media
from .. import title

print("Importing Basic Combat...")


def start(player, enemy):
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
        os.system("cls")
        player_move(player, enemy)
        return True
    if combat_selection == '2':  # Equip
        os.system("cls")
        player.equip()
        start(player, enemy)
    if combat_selection == '3':  # Run
        if player.get_hp() > enemy.get_hp():
            print(player.get_name() + " runs away from " + enemy.get_name())
            os.system("pause")
            title.elv_cave_exit(player)
        else:
            print("The " + enemy.get_name() + " strikes fear into your heart. You cannot escape")
            os.system("pause")
            start(player, enemy)
    else:
        start(player, enemy)


def player_move(player, enemy):
    os.system("cls")
    damage = player.attack()
    print(player.get_name() + " attacked " + enemy.get_name())
    basic_media.hitenemy()
    enemy.attacked(damage)
    enemy_hp = int(enemy.get_hp())
    if enemy_hp <= 0:
        gold = enemy.get_gold()
        player.add_gold(gold)
        return True
    else:
        enemy_move(player, enemy)

    # Enemy attack portion of the cave


def enemy_move(player, enemy):
    os.system("cls")
    damage = enemy.attack()
    print(enemy.get_name() + " attacked " + player.get_name())
    basic_media.enemyhit()
    player.attacked(damage)
    enemy_hp = int(enemy.get_hp())
    player_hp = int(player.get_hp())
    if player_hp <= 0:
        faint(player)
    if enemy_hp <= 0:
        gold = enemy.get_gold()
        player.add_gold(gold)
    else:
        os.system("cls")
        start(player, enemy)


def faint(player):  # Player fainting under 0 HP
    os.system("cls")
    print(player.get_name() + " has faded into existence, only the winds whisper " + player.get_name() + "'s name now.")
    print(player.get_name() + " has lost all of their gold.")
    print(" ")
    player.set_gold(9999)
    player.heal(1)
    player.set_gold(0)
    player.set_cave_level(1)
    title.save_file(player)
    print(" ")
    print("[Game Over]")
    basic_media.printimage("death.txt")
    basic_media.exitsound()
    os.system("pause")
    os.system("cls")
    title.launch()


print("Basic Combat Imported!...")
