from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    number = randint(1, 100)
    if is_even(number):
        result = "yes"
    else:
        result = "no"

    question = f'{number}'
    return str(question), str(result)


def is_even(number):
    return True if number % 2 == 0 else False
