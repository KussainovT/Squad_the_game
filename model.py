from random import randint, choice
from model_data import *


class Squad:
    def __init__(self):
        self.title = None
        self.money = 10
        self.members = []
        self.stash = []
        self.raid = None


class Soldier:
    def __init__(self):
        self.lvl = 1
        self.hp = 100
        self.maxhp = self.hp


class Soldier_pmc(Soldier):
    def __init__(self, name=None, is_commander=False, max_lvl=1,
                 w_type_list: list = ['Пистолет', 'Дробовик', 'Пистолет-пулемет', 'Автомат', 'Снайперская винтовка'],
                 max_w_tier=3, w_min_cond=80):
        super().__init__()
        self.name = (choice(names) + ' ' + choice(surnames) if name is None else name)
        self.is_commander = is_commander
        self.weapon = Weapon(w_type_list=w_type_list, w_tier=max_w_tier, w_min_cond=w_min_cond)
        self.lvl = randint(1, max_lvl)


class Weapon:
    def __init__(self, w_type_list: list = None, w_tier=None, w_min_cond=None):

        # ТИП pistol, shotgun, assault, sniper
        if w_type_list is None:
            rand = randint(1, 100)
            w_type = (
                'Пистолет' if rand < 53 else 'Дробовик' if rand < 83 else 'Пистолет-пулемет' if rand < 93 else 'Автомат' if rand < 98 else 'Снайперская винтовка')
        else:
            while True:
                rand = randint(1, 100)
                w_type = (
                    'Пистолет' if rand < 53 else 'Дробовик' if rand < 83 else 'Пистолет-пулемет' if rand < 93 else 'Автомат' if rand < 98 else 'Снайперская винтовка')
                if w_type in w_type_list:
                    break

        # ТИР 1, 2, 3
        if w_tier is None:
            rand = randint(1, 1000)
            w_tier = (1 if rand < 700 else 2 if rand < 900 else 3)
        else:
            w_tier = randint(1, w_tier)

        # СОСТОЯНИЕ
        if w_min_cond is None:
            self._cond = randint(30, 90)
        else:
            self._cond = randint(w_min_cond, 99)

        self.type = w_type
        self.tier = w_tier
        self.name = choice(list(weapons[self.type][self.tier]))
        self.acc = weapons[w_type][w_tier][self.name]['acc']
        self.pen = weapons[w_type][w_tier][self.name]['pen']
        self.is_auto = weapons[w_type][w_tier][self.name]['is_auto']
        self.max_dmg = weapons[w_type][w_tier][self.name]['dmg']
        self.min_dmg = round(self.max_dmg / 100 * self.cond)
        self.max_acc = weapons[w_type][w_tier][self.name]['acc']
        self.min_acc = round(self.max_acc / 100 * self.cond)

    @property
    def cond(self):
        return self._cond

    @cond.setter
    def cond(self, value):
        self._cond = value
        self.min_dmg = round(self.max_dmg / 100 * self._cond)
        self.min_acc = round(self.max_acc / 100 * self._cond)


class Raid:
    def __init__(self, location=None):
        self.location = Location(location)

    def get_location_point(self):
        return choice(list(self.location.points.values()))

    def get_location_exit(self):
        return choice(list(self.location.exits.values()))


class Location:
    def __init__(self, location=None, locations_dict=locations):
        if location in list(locations_dict.keys()):
            self.title = location
        else:
            self.title = choice(list(locations_dict.keys()))
        self.points = locations_dict[self.title]['points']
        self.exits = locations_dict[self.title]['exits']
        self.mission = Mission()


class Mission:
    def __init__(self, missions_dict=missions):
        self.mission_type = choice(list(missions_dict.keys()))
        self.mission_description = missions_dict[self.mission_type][randint(1, len(missions_dict[self.mission_type]))]
        self.reward = round(randint(100, 500), -2)
