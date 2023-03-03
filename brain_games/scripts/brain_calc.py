#!/usr/bin/env python3

from brain_games import cli
import random
import prompt

name = cli.welcome_user()

print('What is the result of the expression?')


def main():
    c = 1
    i = 1
    while i <= 4:
        i += i
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        x = random.randint(1, 3)
        if x == 1:
            y = a + b
            str_1 = f'{a} + {b}'
        if x == 2:
            y = a - b
            str_1 = f'{a} - {b}'
        if x == 3:
            y = a * b
            str_1 = f'{a} * {b}'
        print(f"Question: {str_1}")
        answer = prompt.integer('Your answer: ')

        if answer != y:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{y}'.")
            print("Let's try again," + name + '!')
            break

        if answer == y:
            print('Correct!')
            c += 1
            if c == 4:
                print('Congratulations,' + name + '!')


if __name__ == "__main__":
    main()
