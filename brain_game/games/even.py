from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    number = randint(1, 100)
    result = is_number_even(number)
    question = f'{number}'
    return question, result


def is_number_even(number):
    even = 'yes'
    not_even = 'no'
    return even if number % 2 == 0 else not_even
