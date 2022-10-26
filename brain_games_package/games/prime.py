from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_round():
    condition = randint(1, 100)

    divider = 2
    while divider * divider <= condition and condition % divider != 0:
        divider += 1

    right_answer = 'yes' if divider * divider > condition else 'no'

    return condition, right_answer
