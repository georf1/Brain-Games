from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def calculate_expression(first_num: int, second_num: int, operator: str):
    if operator == '-':
        right_answer = first_num - second_num
    elif operator == '+':
        right_answer = first_num + second_num
    else:
        right_answer = first_num * second_num

    return right_answer


def generate_round():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    operator = choice(['-', '+', '*'])

    expression = f"{first_num} {operator} {second_num}"

    right_answer = calculate_expression(first_num, second_num, operator)

    return expression, str(right_answer)
