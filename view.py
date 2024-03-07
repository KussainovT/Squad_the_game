from view_draw import *


class Display:
    def __init__(self):
        # IMPORTS
        self.draw = Draw()
        self.menu = Menu()
        self.game_name = None
        self.squad = None

    # УБЕЖИЩЕ
    def display_soldier_page(self, soldier):
        self.draw.cls()
        self.draw.title_shelter(self.squad.title, self.squad.money)
        soldier_info = [('Имя: ', soldier.name), ('Уровень: ', soldier.lvl),('Оружие: ', soldier.weapon), ('Здоровье: ', f"{soldier.hp}/{soldier.maxhp}"),]
        self.draw.point_list(soldier_info, '    ДОСЬЕ:', True, ' ', '')
        self.draw.br()

    # УБЕЖИЩЕ
    def display_shelter_page(self):
        self.draw.cls()
        self.draw.title_shelter(self.squad.title, self.squad.money)
        # ОТРЯД
        list_of_members = []
        for soldier in self.squad.members:
            list_of_members.append((f"[{soldier.lvl}] ", f"{soldier.name.upper()}  ", f"{green}{soldier.hp}/{soldier.maxhp}{reset}  ", f"{soldier.weapon.name} {soldier.weapon.cond}%",))
        self.draw.point_list(list_of_members, '    Моя команда:', True, ' ', '')
        self.draw.br()
        self.draw.line()
        self.draw.br()

    # ГЛАВНОЕ МЕНЮ
    def display_main_menu_page(self, menu_dict: dict, is_title:bool = False) -> str:
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
    def display_questionnaire_page(self, title: str = 'title', questions: list = None) -> list:
        self.draw.cls()
        self.draw.title(title, green)
        answers = []
        for question in questions:
            answer = input(f"    {question} ")
            answers.append(answer)
        return answers

    # БЛОК МЕНЮ
    def display_menu(self, menu_dict: dict, is_title: bool = False) -> str:
        self.menu.show_menu(menu_dict, is_title)
        return input("\n#   ")


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

