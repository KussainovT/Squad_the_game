from controller import *


# INITS
view = Display()
model = Squad()
c = Controller(view, model)

# GAME
while c.GAME:

    # CREDITS
    while c.CREDITS:
        c.credits()

    # ГЛАВНОЕ МЕНЮ
    while c.MAINMENU:
        c.main_menu()

    # ЗАГРУЗИТЬ/СОХРАНИТЬ
    if c.LOAD:
        c = loadgame()
        c.LOAD = False
        c.GAME = True
        c.SHELTER = True
        input(f"{c.squad.commandor}, с возвращением в {c.squad.title}, продолжаем работать!")
    if c.SAVE and c.squad.commandor is not None:
        c.SAVE = False
        c.MAINMENU = True
        savegame(c)
        input(f"Game saved!")

    # НОВАЯ ИГРА
    while c.CREATESQUAD:
        c.new_game()

    # УБЕЖИЩЕ
    while c.SHELTER:
        c.shelter()


