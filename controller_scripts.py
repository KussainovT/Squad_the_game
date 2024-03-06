import pickle


def savegame(controller):
    data = controller
    with open('save_game.pkl', 'wb') as f:
        pickle.dump(data, f)


def loadgame():
    with open('save_game.pkl', 'rb') as f:
        controller = pickle.load(f)
        return controller
