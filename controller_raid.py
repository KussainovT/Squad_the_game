from random import randint, choice
from model import Squad, Soldier_pmc, Soldier_scav
from view import Display


class Controller_Raid:
    def __init__(self, view: Display, squad: Squad, ):
        self.squad = squad
        self.view = view

    def start_raid(self):
        # ВЫБОР ЛОКАЦИИ
        locations_menu = {'title': 'Локация:', 'items': {'1': 'Завод', '2': 'Таможня', '3': 'Эпицентр', '4': 'Лес', '5': 'Развязка', '6': 'Резерв', '7': 'Улицы Таркова', '8': 'Маяк', '9': 'Берег', '10': 'Лаборатория'}}
        self.view.display_shelter_page()
        menu_choice = self.view.display_menu_block(menu_dict=locations_menu, is_title=True)
        self.squad.new_raid(location=locations_menu['items'][menu_choice])
        # ЗАГРУЗКА КАРТЫ
        self.view.display_raid_load_page()
        # ТОЧКИ ИНТЕРЕСА
        points_list = self.squad.raid.location.get_points_list()
        points_number = self.squad.raid.location.points_number
        actions_list = [
            {'движение': ['Двигаемся', 'Бежим', 'Рашим', 'Передислоцируемся', 'Выдвигаемся', 'Продвигаемся', 'Пробиваемся']},
            {'осмотр': ['Занимаем позицию', 'Осматриваемся', 'Прислушиваемся', 'Изучаем обстановку', 'Наблюдаем', 'Рассматриваем', 'Отслеживаем', 'Собираем информацию', 'Проверяем окрестности', 'Тщательно исследуем', 'Анализируем уровень опасности', 'Проводим разведку', 'Рассматриваем внимательно', 'Разбираемся с ситуацией', 'Исследуем окружающее', 'Следим', 'Подробно изучаем', 'Оцениваем ситуацию']},
            {'действие': ['Лутаемся', 'Сидим в засаде', 'Чекаем', 'Выполняем задание', 'Исследуем локацию', 'Осуществляем контроль', 'Собираем данные', 'Патрулируем']},]
        is_new_raid_flag = True
        for i in range(points_number):
            for action in actions_list:
                self.squad.raid.get_encounter()
                self.view.display_raid_page(point=points_list[i], action=action, encounter=self.squad.raid.encounter, is_new_raid=is_new_raid_flag)
                is_new_raid_flag = False
        # ВЫХОД
        actions_list = [{'выход': ['Двигаемся', 'Бежим', 'Рашим', 'Передислоцируемся', 'Выдвигаемся', 'Продвигаемся', 'Пробиваемся']},]
        exits_list = self.squad.raid.location.get_exits_list()
        self.squad.raid.get_encounter()
        self.view.display_raid_page(point=exits_list[0], action=actions_list[0], encounter=self.squad.raid.encounter, is_new_raid=is_new_raid_flag)