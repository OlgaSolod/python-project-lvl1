from random import randint
import prompt


def game_check_even_start():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    counter = 0
    while i < 3:
        number = randint(1, 100)
        check_even = is_number_even(number)
        print(f'Question: {number}')
        answer = prompt.string('')
        if answer == check_even:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{check_even}'.")
            print(f"Let's try again, {username}!")
            return
        i += 1
    if counter == 3:
        print(f'Congratulations, {username}!')


def is_number_even(number):
    even = 'yes'
    not_even = 'no'
    return even if number % 2 == 0 else not_even
