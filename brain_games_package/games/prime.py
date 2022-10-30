from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divider = 2

    while divider * divider <= num and num % divider != 0:
        divider += 1

    if num >= 2 and divider * divider > num:
        return True
    else:
        return False


def generate_round():
    num = randint(1, 100)
    right_answer = 'yes' if is_prime(num) else 'no'

    return num, right_answer
