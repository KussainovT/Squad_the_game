from model import Squad
from random import choice, randint
from view_draw import *


class Display:
    def __init__(self):
        # IMPORTS
        self.draw = Draw()
        self.menu = Menu()
        self.game_name = None
        self.squad = None

        # РЕЙД

    def display_raid_page(self, points_list):

        # ЗАГРУЗКА КАРТЫ
        self.draw.cls()
        self.draw.title(self.squad.raid.location.title)
        self.draw.p_wrapped(self.squad.raid.location.mission.mission_type.upper(), color=yellow)
        self.draw.br()
        self.draw.p_wrapped(self.squad.raid.location.mission.mission_description)
        self.draw.br()
        self.draw.p_wrapped(f"{green}Награда: ${self.squad.raid.location.mission.reward}{reset}")
        self.draw.br()
        self.draw.progress(f'    ПОИСК СЕРВЕРА')
        self.draw.progress(f'    ЗАГРУЗКА ЛУТА', step=randint(5, 10))
        self.draw.progress(f'    ОЖИДАНИЕ ИГРОКОВ', step=randint(5, 10))
        print(' ' * 30, end='\r')
        self.draw.progress(f'    ВЫСАДКА В РЕЙД', step=randint(8, 10))
        input("\n    ")

        # ЭКРАН РЕЙДА
        raid_log = []
        action_list = ['Двигаемся', 'Бежим', 'Рашим', 'Передислоцируемся', 'Выдвигаемся']
        prepare_list = ['Занимаем позицию', 'Осматриваемся', 'Прислушиваемся']
        todo_list = ['Лутаемся', 'Сидим в засаде', 'Чекаем', 'Выполняем задание']
        self.draw.cls()
        self.draw.title(self.squad.raid.location.title)
        self.display_squad_block(self.squad, '    Моя команда:')
        self.draw.br()
        self.draw.line()
        self.draw.br()
        self.draw.p_wrapped(f"{yellow}Ход рейда:{reset}")

        # ХОД РЕЙДА
        for point in points_list:
            if point != points_list[-1]:
                # Идем
                action = f"{choice(action_list)} на точку {point.upper()}"
                self.draw.progress(f"    {action}", step=randint(1, 5))
                raid_log.append(f"    {green}{action} 100%{reset}")
                print(f"    {green}{action} 100%{reset}")
                # Осматриваемся
                action = f"{choice(prepare_list)}"
                self.draw.progress(f"    {action}", step=randint(1, 5))
                raid_log.append(f"    {green}{action} 100%{reset}")
                print(f"    {green}{action} 100%{reset}")
                # Делаем
                action = f"{choice(todo_list)} на точке {point.upper()}"
                self.draw.progress(f"    {action}", step=randint(1, 5))
                raid_log.append(f"    {green}{action} 100%{reset}\n")
                print(f"    {green}{action} 100%{reset}")
                input(' >   ')
            else:
                action = f"{choice(action_list)} к выходу {point.upper()}"
                self.draw.progress(f"    {action}", step=randint(1, 5))
                raid_log.append(f"    {green}{action} 100%{reset}\n")
                print(f"    {green}{action} 100%{reset}")
                input(' >   ')

        input('    РЕЙД ОКОНЧЕН')



    # # РЕЙД
    # def display_raid_page(self):
    #     # ЗАГРУЗКА КАРТЫ
    #     self.draw.cls()
    #     self.draw.title(self.squad.raid.location.title)
    #     self.draw.p_wrapped(self.squad.raid.location.mission.mission_type.upper(), color=yellow)
    #     self.draw.br()
    #     self.draw.p_wrapped(self.squad.raid.location.mission.mission_description)
    #     self.draw.br()
    #     self.draw.p_wrapped(f"Награда: {green}${self.squad.raid.location.mission.reward}{reset}")
    #     self.draw.br()
    #     self.draw.progress(f'    ПОИСК СЕРВЕРА')
    #     self.draw.progress(f'    ЗАГРУЗКА ЛУТА', step=randint(2, 10))
    #     self.draw.progress(f'    ОЖИДАНИЕ ИГРОКОВ', step=randint(2, 10))
    #     print(' ' * 30, end='\r')
    #     self.draw.progress(f'    ВЫСАДКА В РЕЙД', step=randint(8, 10))
    #     input("\n    ")
    #     action_list = ['Двигаемся', 'Бежим', 'Рашим', 'Передислоцируемся', 'Выдвигаемся']
    #     todo_list = ['Лутаемся', 'Осматриваемся', 'Сидим в засаде', 'Чекаем', 'Слушаем']
    #
    #     # ВЫПОЛНЕНИЕ ЗАДАНИЙ
    #     self.draw.cls()
    #     self.draw.title(self.squad.raid.location.title)
    #     self.display_squad_block(self.squad, '    Моя команда:')
    #     self.draw.br()
    #     self.draw.line()
    #     self.draw.br()
    #     self.draw.p_wrapped(f"{yellow}Ход рейда:{reset}")
    #     # Задания
    #     for i in range(randint(2, 4)):
    #         current_point = self.squad.raid.get_location_point()
    #
    #         action = f"{choice(action_list)} на точку {current_point.upper()}"
    #         self.draw.progress( f"    {action}", step=randint(1, 5))
    #         print(f"    {green}{action} 100%{reset}")
    #
    #         action = f"Занимаем позицию"
    #         self.draw.progress(f"    {action}", step=randint(1, 5))
    #         print(f"    {green}{action} 100%{reset}")
    #
    #         action = f"{choice(todo_list)} на точке {current_point.upper()}"
    #         self.draw.progress(f"    {action}", step=randint(1, 5))
    #         print(f"    {green}{action} 100%{reset}")
    #         input('    ')
    #     # Выход
    #     current_exit = self.squad.raid.get_location_exit()
    #     action = f"{choice(action_list)} к выходу {current_exit.upper()}"
    #     self.draw.progress(f"    {action}", step=randint(1, 5))
    #     print(f"    {green}{action} 100%{reset}")
    #     input('    ')


    # СТРАНИЦА СОЛДАТА
    def display_soldier_page(self, soldier):
        self.draw.cls()
        self.draw.title_shelter(self.squad.title, self.squad.money)
        soldier_info = [('Имя: ', soldier.name), ('Уровень: ', soldier.lvl),
                        ('Здоровье: ', f"{soldier.hp}/{soldier.maxhp}"), ]
        self.draw.point_list(soldier_info, '    ДОСЬЕ:', True, ' ', '')
        self.draw.br()
        weapon_info = [
            (f"{soldier.weapon.type} ", soldier.weapon.name),
            ('Состояние: ', f"{soldier.weapon.cond}%"),
            ('Урон: ', f"{soldier.weapon.min_dmg}-{soldier.weapon.max_dmg}"),
            ('Точность: ', f"{soldier.weapon.min_acc}-{soldier.weapon.max_acc}"),
            ('Пробивание: ', f"{soldier.weapon.pen}"),
        ]
        self.draw.point_list(weapon_info, '    ЭКИПИРОВКА:', True, ' ', '')
        self.draw.br()

    # УБЕЖИЩЕ
    def display_shelter_page(self):
        self.draw.cls()
        self.draw.title_shelter(self.squad.title, self.squad.money)
        # ОТРЯД
        list_of_members = []
        for soldier in self.squad.members:
            list_of_members.append((f"[{soldier.lvl}] ", f"{soldier.name.upper()}  ",
                                    f"{green}{soldier.hp}/{soldier.maxhp}{reset}  ",
                                    f"{soldier.weapon.name} {soldier.weapon.cond}%",))
        self.draw.point_list(list_of_members, '    Моя команда:', True, ' ', '')
        self.draw.br()
        self.draw.line()
        self.draw.br()

    # ГЛАВНОЕ МЕНЮ
    def display_main_menu_page(self, menu_dict: dict, is_title: bool = False) -> str:
        self.draw.cls()
        self.draw.title(menu_dict['title'], green)
        self.menu.show_menu(menu_dict, is_title)
        return input("\n#   ")

    # ТЕКСТ
    def display_text_page(self, title: str = 'title', text: str = 'text') -> None:
        self.draw.cls()
        self.draw.title(title, green)
        self.draw.p_wrapped(text)
        input("\n    ")

    # АНКЕТА
    def display_questionnaire_page(self, title: str = 'title', questions_list: list = None) -> list:
        self.draw.cls()
        self.draw.title(title, green)
        answers = []
        for question in questions_list:
            answer = input(f"    {question} ")
            answers.append(answer)
        return answers

    # БЛОК МЕНЮ
    def display_menu_block(self, menu_dict: dict, is_title: bool = False, title_color='') -> str:
        self.menu.show_menu(menu_dict, is_title)
        return input("\n#   ")

    # БЛОК СПИСОК ОТРЯДА
    def display_squad_block(self, squad: Squad, title: str = '', is_title: bool = False) -> None:
        list_of_members = []
        for member in squad.members:
            list_of_members.append((f"[{member.lvl}] ", f"{member.name.upper()}  ",
                                    f"{green}{member.hp}/{member.maxhp}{reset}  ",
                                    f"{member.weapon.name} {member.weapon.cond}%",))
        if is_title:
            self.draw.point_list(list_of_members, title, True, ' ', '')
        else:
            self.draw.point_list(list_of_members, title, False, ' ', '')


class Menu:
    def __init__(self):
        self.name = ''
        self.choice = None

    @staticmethod
    def show_menu(menu_dict: dict = None, is_title: bool = True, title_color='') -> None:
        title = menu_dict['title']
        menu = menu_dict['items']
        if is_title:
            print(f"    {title_color}{title}{reset}")
            # print(' ' * 4 + '-' * len(title))
        for k, v in menu.items():
            print(f"{k} - {v.upper()}")
