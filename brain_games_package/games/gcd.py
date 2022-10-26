from random import randint
import math


description = "Find the greatest common divisor of given numbers."


def start_round():
    first_num = randint(1, 100)
    second_num = randint(1, 100)

    condition = f'{first_num} {second_num}'
    right_answer = math.gcd(first_num, second_num)

    return condition, str(right_answer)
