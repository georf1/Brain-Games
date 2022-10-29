from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(num):
    divider = 2

    while divider * divider <= num and num % divider != 0:
        divider += 1

    if num >= 2 and divider * divider > num:
        return 'yes'
    else:
        return 'no'


def generate_round():
    num = randint(1, 100)
    right_answer = isPrime(num)

    return num, right_answer
