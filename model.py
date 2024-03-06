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
        self.hp = round(randint(50, 120)/10)*10
        self.maxhp = self.hp
        self.weapon = choice(weapons)
