from random import randint
from brain_game.logic import greeting
from brain_game.logic import ask_question
from brain_game.logic import get_answer
from brain_game.logic import check_answer
from brain_game.logic import check_right_answers


def game_check_even_start():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    counter = 0
    while i < 3:
        number = randint(1, 100)
        result = is_number_even(number)
        ask_question(number)
        answer = get_answer()
        if check_answer(answer, result, name):
            counter += 1
            check_right_answers(counter, name)
        else:
            return
        i += 1


def is_number_even(number):
    even = 'yes'
    not_even = 'no'
    return even if number % 2 == 0 else not_even
