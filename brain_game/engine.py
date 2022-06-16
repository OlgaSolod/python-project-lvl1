import prompt


COUNT_OF_QUESTIONS = 3


def start(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULES)
    counter = 0
    for _ in range(COUNT_OF_QUESTIONS):
        question, result = game.generate_question_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
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
