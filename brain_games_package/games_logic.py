from brain_games_package.cli import welcome_user


def start_game(game):
    name = welcome_user()

    tries = 0
    condition, right_answer = game.start_round()
    print(game.DESCRIPTION)

    while tries < 3:
        print(f'Question: {condition}')
        answer = input('Your answer: ')

        if answer == right_answer:
            tries += 1
            print('Correct!')

            condition, right_answer = game.start_round()
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {name}!")
            break

    if tries == 3:
        print(f'Congratulations, {name}!')
