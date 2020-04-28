import random


# user has to input numbers, count total when user type -1


def main():
    total = 0

    num = int(input('Type a number: '))
    while num != -1:
        num = int(input('Type a number: '))
        total = total + num

    print('total is ' + str(total))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
