'''
2- Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
Тот, кто берет последнюю конфету - проиграл.
Предусмотрите последний ход, ибо там конфет остается меньше.
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''

from random import randint
from time import sleep


def players_choice(actual_candies, max_candies):
    try:
        value = int(input(f'{actual_candies} candies left\nEnter how much values you want to take (in range from 1 to {max_candies}):\n'))
        if value > 0 and value <= max_candies:
            return value
        else:
            print('Value is out of range')
            return players_choice(actual_candies, max_candies)
    except ValueError:
        print('This is not a number')
        return players_choice(actual_candies, max_candies)


def total_candies():
    try:
        value = int(input(f'Enter amount of candies in the game:\n'))
        return value
    except ValueError:
        print('This is not a number')
        return total_candies()


def max_for_step():
    try:
        value = int(input(f'Enter amount of candies you can take for a step:\n'))
        return value
    except ValueError:
        print('This is not a number')
        return max_for_step()


def user_game_logic(candies_amount, limit, user_id):
    if candies_amount < limit:
        candies_amount = 0
        return candies_amount
    player_taken = players_choice(candies_amount, limit)
    candies_amount -= player_taken
    return candies_amount


def bot_game_logic(candies_amount, limit):
    if candies_amount < limit:
        candies_amount = 0
        return candies_amount
    candies_amount -= randint(1, limit)
    return candies_amount


def start_game():
    candies_amount = total_candies()
    limit = max_for_step()
    bot = input('Want to play with bot? (yes/no)\n').lower()
    print('******** THE GAME HAS BEGUN ********')
    user = 1
    step = 1
    if 'y' not in bot:
        while candies_amount > 0:
            print(f'*** ROUND NUMBER {step} ***')
            if user == 1:
                print(f'First player\'s turn')
                candies_amount = user_game_logic(candies_amount, limit, user)
                user = 2
                continue
            if user == 2:
                print(f'Second player\'s turn')
                candies_amount = user_game_logic(candies_amount, limit, user)
                user = 1
                step += 1
    else:
        while candies_amount > 0:
            print(f'*** ROUND NUMBER {step} ***')
            if user == 1:
                print(f'First player\'s turn')
                candies_amount = user_game_logic(candies_amount, limit, user)
                user = 2
                continue
            if user == 2:
                print(f'Bot\'s turn')
                a = candies_amount
                candies_amount = bot_game_logic(candies_amount, limit)
                print(f'Bot has taken {a - candies_amount} candies')
                user = 1
                sleep(1)
                step += 1
        if user == 2:
            user = 'bot'
    print(f'******** Player {user} WINS ********')


start_game()
