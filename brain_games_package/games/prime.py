from random import randint


description = "Answer 'yes' if the number is prime, otherwise answer 'no'."


def start_round():
    condition = randint(1, 100)

    d = 2
    while d * d <= condition and condition % d != 0:
        d += 1

    right_answer = 'yes' if d * d > condition else 'no'

    return condition, right_answer
