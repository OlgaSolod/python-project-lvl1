import prompt


def greeting():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


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
        print(f"{answer} is wrong answer ;(. "
              f"Correct answer was '{actual_result}'.")
        print(f"Let's try again, {username}!")
        return False


def congrats(name):
    print(f'Congratulations, {name}!')
