from random import randint
from brain_game.logic import check_answer
from brain_game.logic import ask_question
from brain_game.logic import greeting
from brain_game.logic import get_answer
from brain_game.logic import congrats


def play_gcd():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    right_answer_counter = 0
    while i < 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        result = search_divider(number_1, number_2)
        question = f'{number_1} {number_2}'
        ask_question(question)
        answer = get_answer()
        if check_answer(answer, result, name):
            right_answer_counter += 1
        else:
            return
        if right_answer_counter == 3:
            congrats(name)
        i += 1


def search_divider(number_1, number_2):
    max_num = max(number_1, number_2)
    min_num = min(number_1, number_2)
    divider = min_num
    while max_num % min_num != 0:
        divider = max_num % min_num
        max_num = min_num
        min_num = divider
    return divider
