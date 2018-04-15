import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizards(Creature):
    # def __init__(self, name, level):
    #     self.name = name
    #     self.level = level

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print('The wizard rolled {}...'.format(my_roll))
        print('The {} rolled {}...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard triumphs over the {}!'.format(creature.name))
            return True
        else:
            print('The wizard was DEFEATED by the {}!'.format(creature.name))
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = VALUE IF TRUE if SOME TEST else VALUE IF FALSE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier
