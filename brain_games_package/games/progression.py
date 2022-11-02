from random import randint


DESCRIPTION = "What number is missing in the progression?"


def generate_round():
    sequence = ''

    begin = randint(1, 25)
    end = randint(80, 100)
    step = randint(1, 10)

    length = randint(5, 10)
    progression = list(range(begin, end, step))[:length]

    random_index = randint(0, len(progression) - 1)
    right_answer = progression[random_index]

    progression[random_index] = '..'

    for element in progression:
        sequence += str(element) + ' '

    return sequence.strip(), str(right_answer)
