"""
File: khansole_academy.py
-------------------------
Program should be able to generate simple addition problems that
involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be
asked for an answer to each problem. Your program should determine if the answer was
correct or not, and give the user an appropriate message to let them know. Your program
should keep giving the user problems until the user has gotten 3 problems correct in a row.
"""

import random


def main():
    i = 0  # declare the counter

    while i < 3:  # while the counter value is less than 3, perform the actions
        num1 = random.randint(10, 99)  # declare random numbers between 10 and 99
        num2 = random.randint(10, 99)
        total = num1 + num2  # count the total ot two numbers

        question = (input('What is ' + str(num1) + ' + ' + str(num2) + '?'))  # asking questions
        answer = int(input('Your answer: '))  # user should type his answer

        # if the user's answer is not correct, he sees a warning and the correct answer
        # if the answer is correct, sees a message that counts its correct questions
        # if he answers 3 questions in a row, then he will win.

        if answer != total:
            i = 0
            print('Incorrect. The expected answer is ' + str(total))
        else:
            i = i + 1
            print("Correct! You've gotten " + str(i) + " correct in a row.")

    print('Congratulations! You mastered addition.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
