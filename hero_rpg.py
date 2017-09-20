#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        return self.health > 0

    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))


class Hero(Character):
    pass
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    # def print_status(self):
    #     print("You have {} health and {} power.".format(self.health, self.power))

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("You do {} damage to the goblin.".format(self.power))
    #
    # def alive(self):
    #     return self.health > 0

class Goblin(Character):
    pass
    # def __init__(self, health, power):
    #     self.health = health
    #     self.power = power

    # def print_status(self):
    #     print("The goblin has {} health and {} power.".format(self.health, self.power))

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("The goblin does {} damage to you.".format(self.power))
    #
    # def alive(self):
    #     return self.health > 0


def main():
    hero = Hero('Hero', 10, 5)
    goblin = Goblin('Goblin', 6, 2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == '1':                        #Hero attacks goblin
            if hero.health > 0:
                hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
        else:
            print("Invalid input {}".format(raw_input))
        if goblin.health <= 0:
            print("The goblin is dead.")

        if goblin.health > 0:                       #Goblin attacks hero
            goblin.attack(hero)
        if hero.health <= 0:
                print("You are dead.")

main()
