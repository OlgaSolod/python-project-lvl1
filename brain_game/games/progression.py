from random import randint
from brain_game.logic import ask_question
from brain_game.logic import get_answer
from brain_game.logic import greeting
from brain_game.logic import check_answer
from brain_game.logic import check_right_answers


def play_progression():
    name = greeting()
    print('What number is missing in the progression?')
    i = 0
    counter = 0
    while i < 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 10)
        index = randint(0, 9)
        list = get_progression(number_1, number_2).split()
        result = list[index]
        list[index] = ".."
        question = f'{" ".join(list)}'
        ask_question(question)
        answer = get_answer()
        if check_answer(answer, result, name):
            counter += 1
            check_right_answers(counter, name)
        else:
            return
        i += 1


def get_progression(start_number, difference):
    string = ""
    i = 2
    while i < 12:
        string = f'{string} {str(start_number + (i - 1) * difference)}'
        i += 1
    return string
