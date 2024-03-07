from random import randint, choice
from model_data import *


class Squad:
    def __init__(self):
        self.title = None
        self.commandor = None
        self.money = 1000
        self.members = [Soldier(), Soldier(), Soldier()]
        self.stash = ['Самогон', 'Присадка', 'Видеокарта']


class Soldier:
    def __init__(self):
        self.name = choice(names) + ' ' + choice(surnames)
        self.lvl = randint(1, 2)
        self.hp = round(randint(50, 120) / 10) * 10
        self.maxhp = self.hp
        self.weapon = Weapon()


class Weapon:
    def __init__(self, w_type=None, w_tier=None, w_min_cond=None, w_name=None, w_list=weapons):
        # ТИП pistol, shotgun, assault, sniper
        if w_type is None:
            rand = randint(1, 100)
            print(rand)
            w_type = (
                'Пистолет' if rand < 53 else 'Дробовик' if rand < 83 else 'Пистолет-пулемет' if rand < 93 else 'Автомат' if rand < 98 else 'Снайперская винтовка')
        # ТИР 1, 2, 3
        if w_tier is None:
            rand = randint(1, 1000)
            w_tier = (1 if rand < 700 else 2 if rand < 900 else 3)

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


# while True:
#     weapon = Weapon(w_type='Автомат', w_tier=randint(2, 3), w_min_cond=90)
#
#     print(f"{'Имя:'} - {weapon.name}")
#     print(f"{'Тип:'} - {weapon.type}")
#     print(f"{'Тир:'} - {weapon.tier}")
#     print(f"{'Состояние:'} - {weapon.cond}%")
#     print(f"{'Урон:'} - {weapon.min_dmg}-{weapon.max_dmg}")
#     print(f"{'Точность:'} - {weapon.min_acc}-{weapon.max_acc}%")
#     print(f"{'Пробивание:'} - {weapon.pen}")
#     print(f"{'Авторежим:'} - {weapon.is_auto}")
#
#     input()
#     weapon.cond -= 10
#
#     print(f"{'Имя:'} - {weapon.name}")
#     print(f"{'Тип:'} - {weapon.type}")
#     print(f"{'Тир:'} - {weapon.tier}")
#     print(f"{'Состояние:'} - {weapon.cond}%")
#     print(f"{'Урон:'} - {weapon.min_dmg}-{weapon.max_dmg}")
#     print(f"{'Точность:'} - {weapon.min_acc}-{weapon.max_acc}%")
#     print(f"{'Пробивание:'} - {weapon.pen}")
#     print(f"{'Авторежим:'} - {weapon.is_auto}")
#
#     input()
