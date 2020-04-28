import random
# user has to guess a number between 1 and 99
num = random.randint(1, 99)


def main():
    print('I am thinking of a number between 0 and 99...')
    guess = int(input('Enter a guess: '))
    while guess != num:
        if guess < num:
            print('Your guess is too low')
        else:
            print('Your guess is too high')

        print('')
        guess = int(input('Enter a guess: '))
    print('Congrats!')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
