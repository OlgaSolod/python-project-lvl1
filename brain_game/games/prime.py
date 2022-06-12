from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    number = randint(1, 100)
    question = f'{number}'
    result = check_data(number)
    return question, result


def check_data(number):
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
