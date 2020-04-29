"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    i = 0  # declare the player counter
    stones = 20  # the number of stones at the beginning of the game
    print('There are 20 stones left')

    while stones != 0:  # the game continues as long as there are stones in a pile
        for i in range(1, 3):  # i = 1 - player 1, i = 2 - player 2
            player_input = int(input('Player ' + str(i) + ' would you like to remove 1 or 2 stones? '))
            while player_input != 1 and player_input != 2:  # if player input is not 1 or 2, he will se the warning
                player_input = int(input('Please enter 1 or 2: '))

            # count the number of stones by subtracting the number of stones that the player entered
            # from their previous number

            stones = stones - player_input
            if stones > 0:  # here I delete the last line 'There are 0 stones left'
                print('\nThere are ' + str(stones) + ' stones left')
            else:
                break

    if i == 1:  # since the player who has no stones left wins, I change the player number
        i = 2
    else:
        i = 1
    print('\nPlayer ' + str(i) + ' wins!')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
