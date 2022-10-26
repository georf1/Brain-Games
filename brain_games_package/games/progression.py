from random import randint


DESCRIPTION = "What number is missing in the progression?"


def start_round():
    condition = ''

    length = randint(5, 10)
    lst = list(range(randint(1, 25), randint(80, 100), randint(1, 10)))[:length]

    random_index = randint(0, len(lst) - 1)
    right_answer = lst[random_index]

    lst.pop(random_index)
    lst.insert(random_index, '..')

    for el in lst:
        condition += str(el) + ' '

    return condition.strip(), str(right_answer)
