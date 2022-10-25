from random import randint


description = "Answer 'yes' if the number is even, otherwise answer 'no'."


def start_round():
    condition = randint(1, 100)
    right_answer = condition % 2 == 0 and 'yes' or 'no'

    return condition, right_answer
