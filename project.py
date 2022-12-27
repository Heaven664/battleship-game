import os
import sys
import cowsay
import re
from helper import nums, letters, fleet, bombs, spotted, lives, MAX_LIVES, killed, rules, farewell


def main():
    while True:
        try:
            answer = input(rules).lower()
            if answer == "y":
                break
            if answer == "n":
                clear()
                sys.exit(farewell())
        except EOFError:
            clear()
            sys.exit(farewell())
    while True:
        try:
            # Prints lives
            print_field()
            print_lives()
            if lives == 0:
                lost()
                break
            if killed == len(fleet):
                won()
                break
            cell = input(
                "🐳Canons are ready, Captain. We are waiting for coordinates🐳:  "
            ).upper().strip()
            if not validate_cell(cell):
                continue
            spotted.append(cell)
        except EOFError:
            clear()
            sys.exit(farewell())


def validate_cell(cell):
    """Validates if cell on the map"""
    if cell := re.search(r"^[A-J]{1}(?:[1-9]|10)$", cell, flags=re.IGNORECASE):
        return True
    return False


def print_letters(i):
    """Prints letter for each column"""
    if i == "1":
        print(" ", end=" ")
        for letter in letters:
            print(letter, end=" ")
        print()


def print_number(i):
    """Prints number of the row"""
    i = int(i)
    if i == 10:
        print(nums[i - 1], end="")
    else:
        print(nums[i - 1], end=" ")


def print_field():
    """Prints entire field"""
    kill1 = 0
    live1 = 0
    for i in nums:
        # Prints letters for columns
        print_letters(i)
        # Prints number for the row
        print_number(i)
        # Prints each cell
        kill, live = print_row(i)
        kill1 += kill
        live1 += live
        # Moves cursor to new line
        print()
    print()
    global killed
    killed = kill1
    global lives
    lives = MAX_LIVES - live1


def print_row(i):
    """ "Prints one row of cells"""
    kill1 = 0
    live1 = 0
    for j in letters:
        kill, live = print_cell(j, i)
        kill1 += kill
        live1 += live
    return kill1, live1


def print_cell(letter, number):
    """Prints one cell"""
    kill = 0
    live = 0
    for spot in spotted:
        if spot[0] == letter and spot[1:] == number:
            if spot in fleet:
                print("💥", end="")
                kill += 1
            elif spot in bombs:
                print("💣", end="")
                live += 1
            else:
                print("💦", end="")
            return kill, live
    print("⬜️", end="")
    return kill, live


def print_lives():
    print("Lives: ", end="")
    for _ in range(lives):
        print("💛", end="")
    print()
    print()


def clear():
    return os.system("clear")


def won():
    clear()
    cowsay.tux("Congratulations, you won 🎉🎉🎉")
    print()



def lost():
    clear()
    cowsay.tux("🐳Loser, try again!🐳")
    print()


if __name__ == "__main__":
    main()
