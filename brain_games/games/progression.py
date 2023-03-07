from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def make_question_and_correct_answer():
    first_number = randint(1, 20)
    step = randint(1, 20)
    progression = [first_number, ]
    for i in range(9):
        next_number = first_number + step
        progression.append(next_number)
        first_number = next_number
    random_index = randint(0, len(progression) - 1)
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
