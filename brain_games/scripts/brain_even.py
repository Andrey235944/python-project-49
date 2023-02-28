import prompt
import random

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')
print('Answer "yes" if the number is even, otherwise answer "no".')


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
    if a % 2 == 0 and answer == n:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again," + name + '!')
        break
    if a % 2 != 0 and answer != n:
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again," + name + '!')
        break
    if a % 2 == 0 and answer != n:
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
        print("Let's try again," + name + '!')
        break
