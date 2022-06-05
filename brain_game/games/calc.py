from random import randint
from brain_game.logic import check_answer
from brain_game.logic import ask_question
from brain_game.logic import greeting
from brain_game.logic import get_answer
from brain_game.logic import check_right_answers


def play_calc():
    name = greeting()
    print("What is the result of the expression?")
    i = 0
    operations = ("-", "+", "*")
    counter = 0
    while i < 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        sign_index = randint(0, len(operations) - 1)
        result = get_result(operations[sign_index], number_1, number_2)
        question = f'{number_1} {operations[sign_index]} {number_2}'
        ask_question(question)
        answer = get_answer()
        if check_answer(answer, result, name):
            counter += 1
            check_right_answers(counter, name)
        else:
            return
        i += 1


def get_result(sign, number_1, number_2):
    result = 0
    if sign == "+":
        result = number_1 + number_2
    elif sign == "-":
        result = number_1 - number_2
    elif sign == "*":
        result = number_1 * number_2
    return result
