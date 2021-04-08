import random

#Generating a random number using random.randint() function
n = random.randint(0,100)

total_guess = 10
flag = True

print("Guess the number game! Try to guess the number ranging between 1 to 100\n")

for i in range(total_guess):
    a = int(input("Enter a number : "))
    guess_left = (total_guess - 1 - i)
    if (a < n):
        print("Try larger number!")
        print("Number of guesses left = ",guess_left)
    elif (a>n):
        print("Try smaller number!")
        print("Number of guesses left = ",guess_left)
    else:
        flag = False
        break;

if flag == True:
    print("Game over,You lost the game. Correct number was ",n)
elif flag == False:
    print("You have won the game in ", (total_guess - guess_left) ,"attempts")

