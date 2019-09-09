#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import numpy as np

num_matrix = [itm for itm in range(1, 90)]

#@decor
def cart():
    f_matrix = np.array(random.sample(num_matrix, 9*3)).reshape(3, 9)
    f_matrix = np.array(([sorted(itm) for itm in f_matrix]), int)
    for itm in f_matrix:
        i = 0
        while i < 4:
            box = random.randint(0, 8)
            if itm[box] != 0:
                itm[box] = 0
                i +=1
    return f_matrix

user = cart()
bot = cart()

def num(pix,ans):
    #print(num_matrix)
    num_matrix.remove(pix)
    result_1 = np.where(bot == pix)
    result_2 = np.where(user == pix)
    if result_1:
        bot[result_1] = -1

    if result_2:
        if ans == 'y':
            if pix in user[result_2]:
                user[result_2] = -1
                return True
            else:
                print("Такого числа в вашем билете нет")
                return False
        elif ans == 'n':
            if pix in user[result_2]:
                print('К сожалению число было в карте!')
                return False
            else:
                return True

def decor(render):
    def wrapper(data, name):
        print(f'---------- Карточка {name} -------------')
        render(data,name)
        print('----------------------------------------\n')

    return wrapper
@decor
def render(data, name):
    text = ''
    for i in data:
        for itm in i:
            if itm == 0:
                text = text + '   '
            elif itm == -1:
                text = text + ' — '
            else:
                text = text + '   ' +str(itm)
        text = text + '\n'
    print(text)
    #print(' '.join(res))


while True:
    if user.sum() == -15 or bot.sum() == -15:
        if user.sum() == -15:
            print('Ура! Ты победил!')
            break
        elif bot.sum() == -15:
            print('Ты проиграл!')
            break

    render(bot, 'Bot')
    render(user, 'User')

    pix = random.choice(num_matrix)
    numa = len(num_matrix)
    ans = input(f'Новый бочонок: {pix}!!! (осталось {numa}). Зачеркнуть цифру? (y/n) ')

    if num(pix,ans) is False:
        print('Игра окончена!')
        break




