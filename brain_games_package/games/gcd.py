from random import randint
import math


DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    first_num = randint(1, 100)
    second_num = randint(1, 100)

    nums = f'{first_num} {second_num}'
    right_answer = math.gcd(first_num, second_num)

    return nums, str(right_answer)
