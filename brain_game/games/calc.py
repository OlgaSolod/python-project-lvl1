from random import randint


GAME_RULES = 'What is the result of the expression?'


def generate_question_answer():
    operations = ("-", "+", "*")
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    sign_index = randint(0, len(operations) - 1)
    sign = operations[sign_index]
    result = get_result(sign, number_1, number_2)
    question = f'{number_1} {sign} {number_2}'
    return question, result


def get_result(sign, number_1, number_2):
    result = 0
    if sign == "+":
        result = number_1 + number_2
    elif sign == "-":
        result = number_1 - number_2
    elif sign == "*":
        result = number_1 * number_2
    return result
