import random


class Wizards:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('The wizard rolled {}...'.format(my_roll))
        print('The {} rolled {}...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard triumphs over the {}!'.format(creature.name))
            return True
        else:
            print('The wizard was DEFEATED by the {}!'.format(creature.name))
            return False


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

