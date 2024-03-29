from random import randint, choice
from view import Display
from model import Squad, Soldier_pmc, Soldier_scav, Raid
from controller_scripts import savegame, loadgame
from controller_raid import Controller_Raid


class Controller:
    def __init__(self, view, model):
        # LOOPS
        self.GAME = True
        self.MAINMENU = True
        self.CREDITS = False
        self.CREATESQUAD = False
        self.SHELTER = False
        self.SAVE = False
        self.LOAD = False
        # VIEW / MODEL
        self.squad = model
        self.view = view
        self.view.game_name = 'Tarkov Squad'
        self.view.squad = self.squad
        self.controller_raid = Controller_Raid(view=self.view, squad=self.squad)

    # CREDITS
    def credits(self):
        title = 'Credits'
        text = ('В мрачном Таркове ЧВК BEAR и USEC разгорячены войной, а Дикие поджидают вас на каждом углу. Вы - '
                'часть отряда выживших, борющихся за ресурсы и территории. Погрузитесь в стратегические миссии, '
                'собирайте припасы и остерегайтесь коварных противников. В этом опасном мире вы - единственные герои '
                'своей истории. Удачи в выживании!')
        self.view.display_text_page(title, text)
        self.CREDITS = False
        self.MAINMENU = True

    # ГЛАВНОЕ МЕНЮ
    def main_menu(self):
        menu_dict = {'title': 'Главное меню',
                     'items': {'1': 'Новая игра', '2': 'Продолжить', '3': 'Об игре', '0': 'Сохранить и выйти'}}
        choice = self.view.display_main_menu_page(menu_dict)
        if choice == '1':
            self.MAINMENU = False
            self.CREATESQUAD = True
        elif choice == '2':
            self.MAINMENU = False
            self.LOAD = True
        elif choice == '3':
            self.MAINMENU = False
            self.CREDITS = True
        elif choice == '0':
            self.MAINMENU = False
            self.SAVE = True
            self.GAME = False

    # НОВАЯ ИГРА
    def new_game(self):
        question_list = ['Название отряда:', 'Имя командира:']
        answer_list = self.view.display_questionnaire_page(title='Новая игра', questions_list=question_list)
        answer_list = ['BEAR', 'Timur Kussainov']
        self.squad.title = answer_list[0]
        self.squad.members.append(Soldier_pmc(name=answer_list[1], is_commander=True,
                                              w_type_list=['Пистолет-пулемет', 'Автомат'], w_min_cond=90))
        self.squad.members.append(Soldier_pmc())
        self.squad.members.append(Soldier_pmc())
        text = (f"Приветствую, командир {self.squad.members[0].name.upper()}! Ты вновь вступаешь в бой в мире Таркова. "
                f"Твой отряд {self.squad.title.upper()} - твоя последняя надежда на выживание в этом безжалостном "
                f"городе. Собери своих соратников, готовься к опасностям и действуй с умом. Судьба Таркова и твоя "
                f"собственная судьба теперь в твоих руках. Удачи, командир!")
        self.view.display_text_page(self.squad.title, text)
        self.CREATESQUAD = False
        self.SHELTER = True


    # УБЕЖИЩЕ
    def shelter(self):
        self.view.display_shelter_page()
        menu_dict = {'title': 'Приказы:', 'items': {'1': 'Команда', '2': 'Убежище', '3': 'Барахолка', '0': 'Выйти'}}
        choice = self.view.display_menu_block(menu_dict, True)

        # ПРОВЕРКА ИМЕНИ
        if choice.isalpha():
            for i, member in enumerate(self.squad.members, start=0):
                if choice.lower() in member.name.lower():
                    index = i
                    self.view.display_soldier_page(self.squad.members[index])
                    menu_dict = {'title': 'Приказы:', 'items': {'1': 'Поднять уровень', '2': 'Уволить', '0': 'Выйти'}}
                    self.view.display_menu_block(menu_dict=menu_dict, is_title=False)
        # ПРОВЕРКА РЕЙДА
        if choice.isalpha() and choice.lower() in ['raid', 'рейд']:
            self.controller_raid.start_raid()

        # КОМАНДА
        elif choice == '1':
            self.view.display_shelter_page()
            menu_dict = {'title': 'Команда:',
                         'items': {'1': 'В рейд', '2': 'В госпиталь', '3': 'Нанять рекрутов', '0': 'Выйти'}}
            choice = self.view.display_menu_block(menu_dict=menu_dict, is_title=True)
            if choice == '1':
                self.controller_raid.start_raid()

        # УБЕЖИЩЕ
        elif choice == '2':
            self.view.display_text_page('Убежище', 'Улучшайте убежище, чтобы получить доступ к бонусам')
        # БАРАХОЛКА
        elif choice == '3':
            self.view.display_text_page('Барахолка',
                                        'Зарабатывайте репутацию в рейдах, чтобы открыть доступ на барахолку')
        # НАЗАД
        elif choice == '0':
            self.SHELTER = False
            self.MAINMENU = True
