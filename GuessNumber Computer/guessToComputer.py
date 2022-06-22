import random

from soupsieve import select

def guess_computer(number):
    first = 1
    last = 10

    selection = ''

    while selection != 'q':
        if first <= last:
            my_guess = random.randint(first, last)
        else:
            my_guess = first
        selection = input(f"Press 1 if the number you've guessed is bigger than {my_guess}\nPress 2 if the number you've guessed is smaller than {my_guess}\nPress 3 if the number you've guessed is equal to {my_guess}\nPress q to quit")
        
        if int(selection) == 1:
            first = my_guess + 1
        elif int(selection) == 2:
            last = my_guess - 1
        elif int(selection) == 3:
            print("Correct Guess!")
            break
        elif selection == 'q':
            break
guess_computer(12)
        