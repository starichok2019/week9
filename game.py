
"""
Класс Game
"""

from player import Computer, Human, types_of_players


QUANTITY_PLAYERS = 2  # по умолчанию игроков два
MAX_PLAYERS = 4


# может перенести в описание класса Player?
def choose_who():
    print('\nВыбираем тип нового игрока из ')
    for t in range(0, len(types_of_players)):
        print(f' {types_of_players[t]} - {t} ')
    try:
        who = int(input(f'Введите тип игрока (по умолчанию тип {types_of_players[0]}) :'))
        if who > len(types_of_players): raise ValueError
    except ValueError:
        who = 0
        print(f'Установлен тип по умолчанию {types_of_players[0]}')
    return who


class Game:

    def __init__(self, running_players=QUANTITY_PLAYERS):
        self.bag = Bag()
        self.is_running = True
        self.players = []
        self.running_players = running_players
        self.lap = 1

        # набираем игроков
        for i in range(1, self.running_players + 1):
            # присваиваем тип игрока
            self.players.append(Human(i) if choose_who() else Computer(i))
            # TODO: проверка типов

    # Вытаскиваем и показываем бочонок
    def pull_out_barrel(self):
        print(f'РАУНД № {self.lap}')
        print('Кручу-верчу запутать хочу ...')
        self.bag.shake_bag()
        barrel = self.bag.get_barrel()
        print(f'Номер {barrel} !!!')
        self.bag.throw_out_barrel(barrel)
        self.is_running = self.bag.is_not_empty()  # последний бочонок, игра закончилась
        print(f'В мешке осталось {self.bag.is_not_empty} бочонков \n')
        self.lap += 1
        return  barrel