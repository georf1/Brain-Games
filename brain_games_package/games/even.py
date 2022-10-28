from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def isEven(num):
    return num % 2 == 0


def start_round():
    condition = randint(1, 100)
    right_answer = isEven(condition) and 'yes' or 'no'

    return condition, right_answer
