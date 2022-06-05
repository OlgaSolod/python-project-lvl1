from random import randint
from brain_game.logic import check_answer
from brain_game.logic import ask_question
from brain_game.logic import greeting
from brain_game.logic import get_answer
from brain_game.logic import check_right_answers


def play_gcd():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    counter = 0
    while i < 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        result = search_divider(number_1, number_2)
        question = f'{number_1} {number_2}'
        ask_question(question)
        answer = get_answer()
        if check_answer(answer, result, name):
            counter += 1
            check_right_answers(counter, name)
        else:
            return
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
