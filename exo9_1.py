# Exercice 9_1 :

import random


class Guerrier():
    def __init__(self, name, lvl=1) -> None:
        self.name = name
        self.lvl = lvl

        self.strenght_max = random.randint(12, 18)
        self.agility_max = random.randint(8, 18)
        self.stamina_max = random.randint(12, 18)

        self.strenght = self.strenght_max
        self.agility = self.agility_max
        self.stamina = self.stamina_max

        self.max_hit_points = self.stamina * self.lvl
        self.hit_points = self.max_hit_points


class Healer():
    def __init__(self, name, lvl=1) -> None:
        self.name = name
        self.lvl = lvl

        self.strenght_max = random.randint(10, 18)
        self.agility_max = random.randint(14, 18)
        self.stamina_max = random.randint(10, 18)

        self.strenght = self.strenght_max
        self.agility = self.agility_max
        self.stamina = self.stamina_max

        self.max_hit_points = self.stamina * self.lvl
        self.hit_points = self.max_hit_points

    def cast_buff_agility(self, target):
        target.agility_max += 1 + self.lvl
        print(f"{self.name} lance un buff d'agilité sur {target.name}")


guerrier = Guerrier("John")
healer = Healer("jane")

print(f"{guerrier.name} a {guerrier.agility_max} points d'agilité max")

healer.cast_buff_agility(guerrier)
print(f"{guerrier.name} a {guerrier.agility_max} points d'agilité max")
