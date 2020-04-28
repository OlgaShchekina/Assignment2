"""
File: moon_weight.py
--------------------
Add your comments here.
"""

"""
This program calculates a user's weight on the moon, given their weight on earth.
The user enters a weight on earth. Program will print the corresponding weight on the moon,
which is 16.5% of the weight on earth.
"""


def main():
    user = input('Enter a weight on earth: ')
    user_weight = float(user)
    print('Equivalent weight on moon: ' + str(user_weight * 16.5 / 100))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
