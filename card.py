"""
Класс Card
"""

import random
from bag import QUANTITY_BARRELS

# размеры карточек, заполненность, количество по умолчанию
CARD_WIDTH = 9
CARD_HEIGHT = 3
CARD_FILLED = 5
CARD_BOX = CARD_WIDTH * CARD_HEIGHT
CARD_FILLED_BOX = CARD_FILLED * CARD_HEIGHT
EMPTY_BOX = 0
CHECKED_BOX = -1     # если цифра отрицательная, то число в карточке закрыто


class Card:
    def __init__(self, number=1):
        self.number = number
        self.rest = CARD_FILLED_BOX   # считаем сколько незакрытых карточек
        # заполняем карточку
        self.field = []
        population = list(range(1, QUANTITY_BARRELS +1))   # все бочонки от 1 до максимума
        position = list(range(0, CARD_WIDTH ))             # позиции от 0 до ширины строки карточки
        card_population = random.sample(population, CARD_FILLED * CARD_HEIGHT)
        for i in range(0, CARD_HEIGHT):
            row_population = sorted(card_population[(i * CARD_FILLED):((i + 1) * CARD_FILLED)])
            filled_position = sorted(random.sample(position, CARD_FILLED))
            row = [row_population[filled_position.index(i)] if i in filled_position else EMPTY_BOX for i in range(0, CARD_WIDTH)]
            # заполняем. если пусто то 0
            self.field.extend(row)
    def close_box(self, number):
        self.field[number] = CHECKED_BOX *self.field[number] # делаем число отрицательным, это значит число в карточке закрыто
        self.rest -= 1

    def is_empty(self):
        return self.rest

    def show_card(self):
        """
        Рисуем:
        пусто, если 0
        --, если отрицательное (число на карточке закрыто)
        :return:

        """
        for i in range(0, CARD_HEIGHT):
            print('-' * ((CARD_WIDTH*5)+1) )
            print('', end='|')
            for j in range(i*CARD_WIDTH, (i+1)*CARD_WIDTH):
                if self.field[j] < 0 :
                    box = '--'
                elif self.field[j] > 0:
                    box = str(self.field[j])
                else:
                    box = ' '
                print(box.center(4), end='|')
            print('')
        print('-' * ((CARD_WIDTH * 5) + 1))




