"""
Класс Player
"""

from classes.card import Card

QUANTITY_CARD = 1  # по умолчанию карточек 1

# типы игроков
types_of_players = {0: 'Компьютер', 1: 'Человек'}


class Player:
    def __init(self, number=1, who=0):
        self.number = number
        self.is_playing = True
        self.who = who
        # присваиваем имя игрока
        name_player = input(f'Введите имя нового игрока (по умолчанию Неизвестный # {number}) :')
        self.name = (name_player if name_player else 'Неизвестный ' + '#' + str(number))
        # TODO: проверить имя на уникальность
        # заполняем карточку игрока
        self.cards = Card()
    def show_cards(self):
        self.card.show_card()

    def move_on(selfself, barrel):
        print('Делаю ход')

class Human(Player):
    def __init__(selfself, number=1):
        super().__init__(number, 1)


    def move_on(self, barrel):
        if self.is_playing:
            print(f'\nХод: {self.name} (Человек')
            self.card.show_card()
            answer('Зачеркнуть цифру? (y/ n').lower()
            # исключим ошибку: русская 'н' на той же клавише, что и английская 'y'
            if (answer == 'y') or (answer == 'н'):
                if barrel in self.card.field:
                    print(f'Есть номер {barrel}!\n')
                    self.cards.close_box(self.cards.field.index(barrel))
                    return 0 if self.cards.is_empty() else 1     # 0 -продолжить игру, 1-карточка заполнена
                else:
                    print(f'Ошибка: зачеркнутой цифры у Вас нет! ')
                    self.is_playing = False
                    return -2 # ошибка: нет зачеркнутой цифры
            else:
                if barrel in self.cards.field:
                    print(f'Ошибка: пропущена цифра! ')
                    self.is_playing = False
                    return -3    # Ошибка: пропущена цифра
                else:
                    print('Мимо!\n')
        else:
            print(f'{self.name} выбыл из игры')
        return 0    # продолжаем играть



class Computer(Player):

    def __init__(self, number=1):
            super().__init__(number, 0)

    def move_on(self, barrel):
            print(f'\nХод: {self.name} ({types_of_players[self.who]}) ')
            self.cards.show_card()
            if barrel in self.cards.field:
                print(f'Есть номер {barrel}!\n')
                self.cards.close_box(self.cards.field.index(barrel))
            else:
                print('Мимо!\n')
            return 0 if self.cards.is_empty() else 1    # 0-продолжить игру, 1- карточка заполнена



