from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_round():
    condition = randint(1, 100)

    divider = 2
    while divider * divider <= condition and condition % divider != 0:
        divider += 1

    if condition >= 2 and divider * divider > condition:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return condition, right_answer
