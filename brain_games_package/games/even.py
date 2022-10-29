from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def isEven(num):
    return num % 2 == 0


def generate_round():
    num = randint(1, 100)
    right_answer = isEven(num) and 'yes' or 'no'

    return num, right_answer
