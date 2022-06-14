import prompt


def engine(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULES)
    i = 0
    counter = 0
    while i < 3:
        question, result = game.generate_question_answer()
        print(f'Question: {question}')
        print('Your answer: ', end='')
        answer = prompt.string('')
        if answer == result:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
        i += 1
