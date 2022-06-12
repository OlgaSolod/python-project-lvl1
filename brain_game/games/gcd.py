from random import randint


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    result = search_divider(number_1, number_2)
    question = f'{number_1} {number_2}'
    return question, result


def search_divider(number_1, number_2):
    max_num = max(number_1, number_2)
    min_num = min(number_1, number_2)
    divider = min_num
    while max_num % min_num != 0:
        divider = max_num % min_num
        max_num = min_num
        min_num = divider
    return divider
