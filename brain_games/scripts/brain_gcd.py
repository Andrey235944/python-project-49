#!/usr/bin/env python3

from brain_games import cli
import random
import prompt
import math

name = cli.welcome_user()

print('Find the greatest common divisor of given numbers.')


def main():
    c = 1
    i = 1
    while i <= 4:
        i += i
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        y = math.gcd(a, b)
        str_1 = f'{a}  {b}'
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
