import prompt


def greeting():
    print("Welcome to the Brain Games!")
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def play_game(game):
    name = greeting()
    print(game.GAME_RULES)
    round(game, name)


def round(game, name):
    i = 0
    counter = 0
    while i < 3:
        question, result = game.generate_question_answer()
        print(result)
        ask_question(question)
        answer = get_answer()
        if check_answer(answer, result, name):
            counter += 1
            check_right_answers(counter, name)
        else:
            return
        i += 1


def check_right_answers(counter, name):
    if counter == 3:
        congrats(name)


def ask_question(question):
    print(f'Question: {question}')


def get_answer():
    print('Your answer: ', end='')
    user_answer = prompt.string('')
    return user_answer


def check_answer(answer, actual_result, username):
    if answer == str(actual_result):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{actual_result}'.")
        print(f"Let's try again, {username}!")
        return False


def congrats(name):
    print(f'Congratulations, {name}!')
