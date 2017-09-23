#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import math
import random


class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("The {} does {} damage to {}".format(self.name, self.power, enemy.name))

    def alive(self):
        return self.health > 0

    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))


class Hero(Character):
    def attack(self, enemy):
        power = self.power
        if random.randint(0,100) < 20:
            power = self.power * 2
            print('Critical hit!')
        enemy.health -= power
        print("The {} does {} damage to {}".format(self.name, power, enemy.name))

class Goblin(Character):
    pass

class Zombie(Character):
    pass

class Medic(Character):
    pass
    # if random.randint(0,100) < 20:
    #     health = self.health + 2
    #     print('Medic has recovered 2 health points!')

class Shadow(Character):
    def alive(self, health):
        if random.randint(0,100) < 10:
            health = self.health - 1
        else:
            self.health == 1


class Battlemage(Character):
    def attack(self, enemy):
        power = self.power
        if random.randint(0,100) < 10:
            health = self.health + 20
            power = self.power * 5
            print("Battlemage has gained 20 health points AND 5 times the power!")
        enemy.health -= power
        print("The {} does {} damage to {}".format(self.name, power, enemy.name))

class Nightwitch(Character):
    pass
    #I want to add something but



def main():
    hero = Hero('Hero', 200, 25)
    goblin = Goblin('Goblin', 60, 10)
    zombie = Zombie('Zombie', math.inf, 10)
    medic = Medic('Medic', 100, 10)
    shadow = Shadow('Shadow', 1, 10)
    battlemage = Battlemage('Battlemage', 120, 10)
    nightwitch = Nightwitch('Nightwitch', 40, 20)

    characters = [hero, goblin, zombie, medic, shadow, battlemage, nightwitch]
    while True:
        if not hero.alive():
            break
        else:
        # while goblin.alive() and hero.alive() and zombie.alive() and battlemage.alive() and nightwitch.alive():
            hero.print_status()
            goblin.print_status()
            zombie.print_status()
            medic.print_status()
            shadow.print_status()
            battlemage.print_status()
            nightwitch.print_status()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. fight medic")
            print("3. fight zombie")
            print("4. fight medic")
            print("5. fight shadow")
            print("6. fight battlemage")
            print("7. fight nightwitch")
            print("8. do nothing")
            print("9. flee")
            print("> ", end=' ')
            raw_input = input()

            if raw_input == '1':
                if hero.health > 0:
                    hero.attack(goblin)
            elif raw_input == "2":
                if hero.health > 0:
                    hero.attack(medic)
            elif raw_input == "3":
                if hero.health > 0:
                    hero.attack(zombie)
            elif raw_input == "4":
                if hero.health > 0:
                    hero.attack(medic)
            elif raw_input == "5":
                if hero.health > 0:
                    hero.attack(shadow)
            elif raw_input == "6":
                if hero.health > 0:
                    hero.attack(battlemage)
            elif raw_input == "7":
                if hero.health > 0:
                    hero.attack(nightwitch)
            elif raw_input == "8":
                pass
            elif raw_input == "9":
                print("You're scared huh. I knew it! Goodbye")
            else:
                print("Invalid input {}".format(raw_input))

            if goblin.health <= 0:
                print("The goblin is dead.")
            if goblin.health > 0:
                goblin.attack(hero)
            if hero.health <= 0:
                print("Oh no! You are dead.")
                break

            if zombie.health == math.inf:
                zombie.attack(hero)
            if hero.health <=0:
                print("Oh no! You are dead.")
                break

            if medic.health > 0:
                medic.attack(shadow)
            if medic.health <= 0:
                print("The medic has died.")

            if shadow.health > 0:
                shadow.attack(nightwitch)
            if shadow.health <= 0:
                print("Shadow has died.")

            if battlemage.health > 0:
                battlemage.attack(medic)
            if shadow.health <= 0:
                print("The Battlemage has died")

            if nightwitch.health > 0:
                nightwitch.attack(medic)
            if nightwitch.health <= 0:
                print("The Nightwitch has retreated to her lair")



main()
