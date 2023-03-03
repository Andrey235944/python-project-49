#!/usr/bin/env python3

from brain_games import cli
import random
import prompt

name = cli.welcome_user()

print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    i = 1
    b = 1
    y = 'yes'
    n = 'no'
    while i <= 4:
        a = random.randint(1, 200)
        print('Question: ' + str(a))
        answer = prompt.string('Your answer: ')
        i += i
        if a % 2 == 0 and answer == y or a % 2 != 0 and answer == n:
            print('Correct!')
            b += 1
            if b == 4:
                print('Congratulations,' + name + '!')
        if a % 2 == 0 and answer != y:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{y}'.")
            print("Let's try again," + name + '!')
            break
        if a % 2 != 0 and answer != n:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{n}'.")
            print("Let's try again," + name + '!')
            break


if __name__ == "__main__":
    main()
