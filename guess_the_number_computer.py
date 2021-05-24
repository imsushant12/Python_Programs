# computer will guess the number we have chosen randomly:
import random

def guess_the_number(maximum):
    count = 0
    low = 1
    high = maximum
    result = ''

    while (result != 'c'):
        # random number generation.
        guess = random.randint(low, high)
        result = input(f"Is the {guess}, correct: (C) / Too Low: (L) / Too High: (H) ?? : ").lower()

        if (result == 'l'):
            low = guess + 1
            count += 1

        elif (result == 'h'):
            high = guess - 1
            count += 1

    print(f"Computer guessed has guessed your number : {guess}, in {count} number of attempts!")

maximum = int(input("Enter maximum range of number : "))
guess_the_number(maximum)

