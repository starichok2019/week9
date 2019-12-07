"""
Класс Game
"""

from classes.player  import Computer, Human, types_of_players
from classes.bag import Bag

QUANTITY_PLAYERS = 2   # по умолчанию игроков два

MAX_PLAYERS = 4

# можем перенести в описание класса Player

def choose_who():
    print('\nВыбираем тип нового игрока из ')
    for t in range(0, len(types_of_players)):
        print(f' {types_of_players[]} - {t}')
    try:
        who = int(input(f'Введите тип игрока(по уиолчанию тип {types_of_players[0]}) :'))
        if who > len(types_of_players):
            raise ValueError
    except ValueError:
        who = 0
        print(f'становлен тип по умолчанию {types_of_players[0]}')
    return who


# определяем количество игроков

def get_quantity_players():
    try:
        quantity_players = int(input(f'Введите количество игроков (не более {MAX_PLAYERS}, по умолчанию {QUANTITY_PLAYERS}) :'))
        if (quantity_players < 1) or (quantity_players > MAX_PLAYERS): raise ValueError
    except ValueError:
        quantity_players = QUANTITY_PLAYERS
        print(f'Установлено количество игроков по умолчанию {QUANTITY_PLAYERS}')
    return quantity_players


class Game:

    def __init__(self):
        self.bag = Bag()
        self.is_run = True
        self.players = []
        self.running_players = get_quantity_players()
        self.lap = 1


# набираем игроков
    for i in range(1, self.running_players + 1 ):
# присваиваем тип игрока
        self.players.append(Human(i) if choose_who() else Computer(i))
# TODO: проверка типов


# Вытаскиваем и показываем бочонок
    def show_barrel(self):
        print(f'РАУНД № {self.lap}')
        print('перемешиваем бочонки в мешке')
        self.bag.shake_bag()
        barrel = self.bag.get_barrel()
        print(f'Номер {barrel}  ')
        self.bag.throw_out_barrel(barrel)
        self.is_run = self.bag.is_not_empty()    # последний бочонок, игра закончилась
        print(f'В мешке осталось {self.bag.is.not_empty()} бочонков \n')
        self.lap += 1
        return barrel



