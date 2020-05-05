"""
File: nondecreasing.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():

    i = 0
    print('Enter a sequence of non-decreasing numbers.')

    first = float(input('Enter num: '))
    i += 1
    second = float(input('Enter num: '))
    i += 1

    while second >= first:
        first = second
        second = float(input('Enter num: '))
        i += 1

    print('Thanks for playing!')
    print('Sequence length: ' + str(i - 1))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
