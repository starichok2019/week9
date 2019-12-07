"""
Игра ЛОТО
"""

from classes.game import Game

RULE_FILE = 'rule.txt'

if __name__ == '__main__':
    print('******************** ЛОТО ********************')
    print('приводим правила ...')
    with open(RULE_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
    input('\n Для продолжения нажмите ENTER')
    loto = Game()
    print('\n Начали!\n')
    while loto.is_run:
        # вынимаем очередной бочонок
        barrel = loto.show_barrel()
        # что у игроков ?
        for player in loto.players:
            result = player.move_on(barrel)  # 0 - продолжаем
            if result == 1:
                print('\Победа! Карточка заполнена. Игра закончина')
                loto.is_run = False
                break
            elif result < 0:
                print(f'Игрок {player.name} выбыл из игры')
                loto.running_players -= 1
                if loto.running_players == 0: # остались ли игроки для игры?
                    result = -100 # никого не осталось
                    loto.is_run = False
                    break
    winner = (player.name if result != -100 else 'не определен')
    print(f'\nПобедитель {winner} ({loto.lap - 1} раунд')