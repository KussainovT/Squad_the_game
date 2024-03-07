from random import randint
w_type = 'sniper'

while True:
    rand = randint(1, 1000)
    w_type = ('pistol' if rand < 600 else 'shotgun' if rand < 900 else 'pp' if rand < 930 else 'assaut' if rand < 980 else 'sniper')
    print(w_type)
