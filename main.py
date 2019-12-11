
"""
ЛОТО
"""


from game import Game, QUANTITY_PLAYERS, MAX_PLAYERS



RULE_FILE = 'rule.txt'


# определяем количество игроков
def get_quantity_players():
    try:
        quantity_players = int(
            input(f'Введите количество игроков (не более {MAX_PLAYERS}, по умолчанию  {QUANTITY_PLAYERS}) :'))
        if (quantity_players < 1) or (quantity_players > MAX_PLAYERS): raise ValueError
    except ValueError:
        quantity_players = QUANTITY_PLAYERS
        print(f'Установлено количество игроков по умолчанию {QUANTITY_PLAYERS}')
    return quantity_players


if __name__ == '__main__':

    print('********************* ЛОТО ********************')
    print('Рассказываем правила ...')
    with open(RULE_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
    input('\n Для продолжения нажмите <ENTER>')
    loto = Game(get_quantity_players())
    print('\nПоехали!\n')
    while loto.is_running:
        # вытаскиваем очередной бочонок
        barrel = loto.pull_out_barrel()
        # что у игроков ?
        for player in loto.players:
            result = player.move_on(barrel)  # 0- продолжаем
            if result == 1:
                print('\nПобеда !!! Карточка заполнена. Игра закончена')
                loto.is_running = False
                break
            elif result < 0:
                print(f'Игрок {player.name} выбыл из игры')
                loto.running_players -= 1
                if loto.running_players == 0:  # остались ли игроки?
                    result = -100  # никого не осталось
                    loto.is_running = False
                    break
    winner = (player.name if result != -100 else 'не определён')
    print(f'\nПобедитель {winner}  ({loto.lap - 1} раунд)')
