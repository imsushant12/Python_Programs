import random

def hangman():
    # select a random word from the list of words.
    word_list = ["india" , "python" , "programming" , "coding" , "hangman"]
    word = random.choice(word_list)
    turns = 10
    # initially guess made is none
    guess_made = ''

    while (len(word) > 0):
        main_word = ""

        for letter in word:
            if letter in guess_made:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        if main_word == word:
            print(main_word)
            print("\nYou Won!!! and saved a man!")
            break

        print("Guess the word : " , main_word)
        guess = input()

        if guess.isalpha():
            guess_made = guess_made + guess

        else:
            guess = input("Enter a valid character : ")

        if guess not in word:
            turns -= 1

            if turns == 9:
                print("\n9 attempts left!!!")
                print("-------------------")

            if turns == 8:
                print("\n8 attempts left!!!")
                print("-------------------")
                print("         O         ")

            if turns == 7:
                print("\n7 attempts left!!!")
                print("-------------------")
                print("         O         ")
                print("         |         ")

            if turns == 6:
                print("\n6 attempts left!!!")
                print("-------------------")
                print("         O         ")
                print("         |         ")
                print("        /          ")

            if turns == 5:
                print("\n5 attempts left!!!")
                print("-------------------")
                print("         O         ")
                print("         |         ")
                print("        / \        ")

            if turns == 4:
                print("\n4 attempts left!!!")
                print("-------------------")
                print("        \O         ")
                print("         |         ")
                print("        / \        ")

            if turns == 3:
                print("\n3 attempts left!!!")
                print("-------------------")
                print("        \O/        ")
                print("         |         ")
                print("        / \        ")

            if turns == 2:
                print("\n2 attempts left!!!")
                print("-------------------")
                print("        \O/  |     ")
                print("         |         ")
                print("        / \        ")

            if turns == 1:
                print("\nOnly one attempt is left!!!")
                print("-------------------")
                print("        \O/__|     ")
                print("         |         ")
                print("        / \        ")

            if turns == 0:
                print("\nYou Lost the game!!!")
                print("-------------------")
                print("        _o_|       ")
                print("        /|\        ")
                print("        / \        ")
                break

if __name__=="__main__":
    print("Welcome tho th HangMan Game !!! ")
    print("\nYou will get 10 attempts to guess the word correctly!")
    hangman()