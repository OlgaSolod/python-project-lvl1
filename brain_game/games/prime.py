from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    number = randint(1, 100)
    question = number
    if is_prime(number):
        result = "yes"
    else:
        result = "no"
    return str(question), result


def is_prime(number):
    if number == 0 or number == 1:
        return False
    i = 2
    while i < number:
        if number % i != 0:
            i += 1
        else:
            return False
    return True
