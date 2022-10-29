from brain_games_package.cli import welcome_user


def start_game(game):
    name = welcome_user()

    successful_tries = 0
    print(game.DESCRIPTION)

    while successful_tries < 3:
        question, right_answer = game.generate_round()

        print(f'Question: {question}')
        answer = input('Your answer: ')

        if answer == right_answer:
            successful_tries += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {name}!")
            break

    if successful_tries == 3:
        print(f'Congratulations, {name}!')
