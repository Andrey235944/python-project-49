from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question_and_correct_answer():
    min_number = 1
    max_number = 99
    operator_1 = randint(min_number, max_number)
    operator_2 = randint(min_number, max_number)
    correct_answer = str(gcd(operator_1, operator_2))
    question = f"{operator_1} {operator_2}"
    return question, correct_answer
