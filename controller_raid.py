from random import randint, choice
from model import Squad, Soldier_pmc, Soldier_scav
from view import Display

red = '\033[31m'
green = '\033[32m'
reset = '\033[0m'


class Controller_Raid:
    def __init__(self, view: Display, squad: Squad, ):
        self.squad = squad
        self.view = view

    def start_raid(self):
        # ВЫБОР ЛОКАЦИИ
        locations_menu = {'title': 'Локация:',
                          'items': {'1': 'Завод', '2': 'Таможня', '3': 'Эпицентр', '4': 'Лес', '5': 'Развязка',
                                    '6': 'Резерв', '7': 'Улицы Таркова', '8': 'Маяк', '9': 'Берег',
                                    '10': 'Лаборатория'}}
        self.view.display_shelter_page()
        menu_choice = self.view.display_menu_block(menu_dict=locations_menu, is_title=True)
        self.squad.new_raid(location=locations_menu['items'][menu_choice])
        # ЗАГРУЗКА КАРТЫ
        self.view.display_raid_load_page()
        # ТОЧКИ ИНТЕРЕСА
        points_list = self.squad.raid.location.get_points_list()
        points_number = self.squad.raid.location.points_number
        actions_list = [
            {'движение': ['Двигаемся', 'Бежим', 'Рашим', 'Передислоцируемся', 'Выдвигаемся', 'Продвигаемся',
                          'Пробиваемся']},
            {'осмотр': ['Занимаем позицию', 'Осматриваемся', 'Прислушиваемся', 'Изучаем обстановку', 'Наблюдаем',
                        'Рассматриваем', 'Отслеживаем', 'Собираем информацию', 'Проверяем окрестности',
                        'Тщательно исследуем', 'Анализируем уровень опасности', 'Проводим разведку',
                        'Рассматриваем внимательно', 'Разбираемся с ситуацией', 'Исследуем окружающее', 'Следим',
                        'Подробно изучаем', 'Оцениваем ситуацию']},
            {'действие': ['Лутаемся', 'Сидим в засаде', 'Чекаем', 'Выполняем задание', 'Исследуем локацию',
                          'Осуществляем контроль', 'Собираем данные', 'Патрулируем']}, ]
        is_new_raid_flag = True
        for i in range(points_number):
            for action in actions_list:
                self.squad.raid.get_encounter()
                self.view.display_raid_page(point=points_list[i], action=action, encounter=self.squad.raid.encounter,
                                            is_new_raid=is_new_raid_flag)
                if self.view.encounter_choise == '1':
                    self.start_battle()
                    self.view.encounter_choise = ''

                is_new_raid_flag = False
        # ВЫХОД
        actions_list = [{'выход': ['Двигаемся', 'Бежим', 'Рашим', 'Передислоцируемся', 'Выдвигаемся', 'Продвигаемся',
                                   'Пробиваемся']}, ]
        exits_list = self.squad.raid.location.get_exits_list()
        self.squad.raid.get_encounter()
        self.view.display_raid_page(point=exits_list[0], action=actions_list[0], encounter=self.squad.raid.encounter,
                                    is_new_raid=is_new_raid_flag)

    def start_battle(self):
        squad1 = self.squad
        squad2 = self.squad.raid.encounter.enemy_squad
        self.view.display_battle_page(squad1, squad2)

        # Обновляем списки выживших
        squad1_alive_members = []
        squad2_alive_members = []
        battle_log = []
        for member in squad1.members:
            if member.hp > 0:
                squad1_alive_members.append(member)
        for member in squad2.members:
            if member.hp > 0:
                squad2_alive_members.append(member)

        battle = True
        while battle:
            battle_log = []
            # Атакуем врагов
            if squad1_alive_members and squad2_alive_members:
                for member in squad1_alive_members:
                    # Выбираем врага
                    enemy_index = randint(0, len(squad2_alive_members) - 1) if len(squad2_alive_members) > 1 else 0
                    # Атакуем и получаем лог урона (список)
                    damage_list = member.attack(squad2_alive_members[enemy_index])
                    # Формируем лог
                    attack_log = [green, member.name, red, squad2_alive_members[enemy_index].name, damage_list]
                    battle_log.append(attack_log)
                    # Отрисовывем
                    self.view.display_battle_page(squad1, squad2, battle_log)
                    # Удаляем если убили
                    if squad2_alive_members[enemy_index].hp <= 0:
                        squad2_alive_members.pop(enemy_index)
                    if not squad2_alive_members:
                        input(f"    {green}ПОБЕДА!{reset}")
                        battle = False
                        break

            # Враги атакуют
            if squad1_alive_members and squad2_alive_members:
                for member in squad2_alive_members:
                    # Выбираем врага
                    enemy_index = randint(0, len(squad1_alive_members) - 1) if len(squad1_alive_members) > 1 else 0
                    # Атакуем и получаем лог урона (список)
                    damage_list = member.attack(squad1_alive_members[enemy_index])
                    # Формируем лог
                    attack_log = [red, member.name, green, squad1_alive_members[enemy_index].name, damage_list]
                    battle_log.append(attack_log)
                    # Отрисовывем
                    self.view.display_battle_page(squad1, squad2, battle_log)
                    # Удаляем если убили
                    if squad1_alive_members[enemy_index].hp <= 0:
                        squad1_alive_members.pop(enemy_index)
                    if not squad1_alive_members:
                        input(f"    {red}ПОРАЖЕНИЕ!{reset}")
                        battle = False
                        break

        for member in self.squad.members:
            member.hp = member.maxhp
