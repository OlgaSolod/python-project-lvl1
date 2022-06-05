from random import randint
from brain_game.logic import greeting
from brain_game.logic import ask_question
from brain_game.logic import get_answer
from brain_game.logic import check_answer
from brain_game.logic import check_right_answers


def play_prime():
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    counter = 0
    while i < 3:
        number = randint(1, 100)
        result = check_number(number)
        ask_question(number)
        answer = get_answer()
        if check_answer(answer, result, name):
            counter += 1
            check_right_answers(counter, name)
        else:
            return
        i += 1


def check_number(number):
    i = 2
    positive_answer = "yes"
    negative_answer = "no"
    while i < number:
        if number % i != 0:
            i += 1
            continue
        else:
            return negative_answer
    return positive_answer
