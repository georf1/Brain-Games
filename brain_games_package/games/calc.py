from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def generate_round():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    operator = choice(['-', '+', '*'])

    expression = f"{first_num} {operator} {second_num}"

    if operator == '-':
        right_answer = first_num - second_num
    elif operator == '+':
        right_answer = first_num + second_num
    else:
        right_answer = first_num * second_num

    return expression, str(right_answer)
