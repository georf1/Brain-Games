from brain_games_package.cli import welcome_user
import random


def main():
    name = welcome_user()

    tries = 0
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    while tries < 3:
        num = random.randint(1, 100)

        print(f'Question: {num}')
        answer = input('Your answer: ')

        if (num % 2 == 0 and answer == 'yes') or (num % 2 != 0 and answer == 'no'):
            tries += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{num % 2 == 0 and 'yes' or 'no'}'")
            print(f"Let's try again, {name}")
            break

    if tries == 3:
        print('Congratulations, {name}')


if __name__ == '__main__':
    main()
