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
        self.raid_log = []
        self.encounter_choise = ''

    # РЕЙД
    # ЭКРАН ЗАГРУЗКИ
    def display_raid_load_page(self):
        self.draw.cls()
        self.draw.title(self.squad.raid.location.title)
        self.draw.p_wrapped(self.squad.raid.location.mission.mission_type.upper(), color=yellow)
        self.draw.p_wrapped(self.squad.raid.location.mission.mission_description)
        self.draw.br()
        self.draw.p_wrapped(f"{green}Награда: ${self.squad.raid.location.mission.reward}{reset}")
        self.draw.br()
        self.draw.progress(f'    ПОИСК СЕРВЕРА', step=randint(9, 10))
        self.draw.progress(f'    ЗАГРУЗКА ЛУТА', step=randint(9, 10))
        self.draw.progress(f'    ОЖИДАНИЕ ИГРОКОВ', step=randint(9, 10))
        print(' ' * 30, end='\r')
        self.draw.progress(f'    ВЫСАДКА В РЕЙД', step=randint(9, 10))
        print(f'    ВЫСАДКА В РЕЙД: {green}100%{reset}')
        input(' >  ')

    # ЭКРАН РЕЙДА
    def display_raid_page(self, point: str, action: dict, encounter=False, is_new_raid: bool = False):
        self.draw.cls()
        self.draw.title(f"{self.squad.raid.location.title} | {point}")
        self.display_squad_block(self.squad, '    Моя команда:')
        self.draw.br()
        self.draw.line()
        self.draw.br()
        self.draw.p_wrapped(f"{yellow}Ход рейда:{reset}")
        # Логирование
        if is_new_raid:
            self.raid_log = []
        else:
            for log in self.raid_log:
                print(log)
        # Ход рейда
        if 'движение' in action:
            action_text = f"{choice(list(action['движение']))} на точку {point.upper()}"
        elif 'осмотр' in action:
            action_text = f"{choice(list(action['осмотр']))}"
        elif 'действие' in action:
            action_text = f"{choice(list(action['действие']))} на точке {point.upper()}"
        elif 'выход' in action:
            action_text = f"{choice(list(action['выход']))} к выходу {point.upper()}"
        self.draw.progress(text=f"    {action_text}", step=randint(4, 10))  # Прогресс бар
        print(f"    {action_text} {green}100%{reset}")  # Зеленый 100%
        self.raid_log.append(f"    {action_text} {green}100%{reset}")  # Лог
        # ENCOUNTER
        if encounter:
            if encounter.type == 'scav':
                encounter_text = f"    {red}Обнаружена группа из {len(encounter.enemy_squad.members)} диких{reset}"
                print(encounter_text)
            elif self.squad.raid.encounter.type == 'pmc':
                encounter_text = f"    {red}Обнаружена группа из {len(encounter.enemy_squad.members)} ЧВК{reset}"
                print(encounter_text)
            self.display_squad_block(squad=encounter.enemy_squad, title=f'    {red}Враги:{reset}', is_title=False)
            # ENCOUNTER MENU
            self.draw.br()
            encounter_menu = {'title': 'Действия:', 'items': {'1': 'Напасть', '2': 'Уйти'}, }
            self.encounter_choise = self.display_menu_block(menu_dict=encounter_menu, is_title=False)
            if self.encounter_choise == '1':
                self.raid_log.append(f"{encounter_text} {red}с которыми завязался бой{reset}")  # Лог
            elif self.encounter_choise == '2':
                self.raid_log.append(f"{encounter_text} {red}от которых удалось уйти{reset}")  # Лог
        if 'действие' in action:
            self.draw.br()
            self.raid_log.append('')  # Лог
            input(' >  ')
        if 'выход' in action:
            input('    РЕЙД ОКОНЧЕН')

    # ЭКРАН БОЯ
    def display_battle_page(self, squad1, squad2, battle_log=None):
        self.draw.cls()
        self.draw.title(title=f"БОЙ", color=red)
        self.display_squad_block(squad1, '    Моя команда:')
        self.draw.br()
        self.draw.p_wrapped('ПРОТИВ', red)
        self.draw.br()
        self.display_squad_block(squad2, '    Моя команда:')
        self.draw.br()
        self.draw.line()
        self.draw.br()
        self.draw.p_wrapped(f"{yellow}Ход рейда:{reset}")
        # Лог боя
        if battle_log is not None:
            for log in battle_log:
                damage = ' '.join(str(txt) for txt in log[4])
                string = f"    {log[0]}{log[1].upper()}{reset} атаковал {log[2]}{log[3].upper()}{reset} [{log[0]}{damage}{reset}]"
                print(string)

        input()





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
        self.display_squad_block(squad=self.squad, title='    Моя команда:', is_title=True)
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
            if member.is_commander:
                list_of_members.append((f"[{member.lvl}] ", f"{yellow}★{reset} {member.name.upper()}  ",
                                        f"{green}{member.hp}/{member.maxhp}{reset}  ",
                                        f"{member.weapon.name} {member.weapon.cond}%",))
            else:
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
