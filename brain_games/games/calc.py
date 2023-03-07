from random import randint, choice
from operator import add, mul, sub

DESCRIPTION = 'What is the result of the expression?'


def make_question_and_correct_answer():
    min_number = 1
    max_number = 12
    operand_1 = randint(min_number, max_number)
    operand_2 = randint(min_number, max_number)
    operation, operator = choice([
        (add, '+'),
        (mul, '*'),
        (sub, '-'),
    ])
    correct_answer = str(operation(operand_1, operand_2))
    question = f"{operand_1} {operator} {operand_2}"
    return question, correct_answer
