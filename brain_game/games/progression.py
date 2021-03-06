from random import randint


GAME_RULES = 'What number is missing in the progression?'


def generate_question_answer():
    number_1 = randint(1, 100)
    number_2 = randint(1, 10)
    index = randint(0, 9)
    progression = get_progression(number_1, number_2)
    result = progression[index]
    progression[index] = '..'
    question = create_question(progression)
    return question, str(result)


def create_question(new_progression):
    string = ''
    for item in new_progression:
        string = string + ' ' + str(item)
    return string.strip()


def get_progression(start_number, difference):
    list = []
    i = 2
    while i < 12:
        new_element = start_number + (i - 1) * difference
        list.append(new_element)
        i += 1
    return list
