import random
# r>s , s>p and p>r

def is_Win(player , computer):
    # Winning possibilities : r>s , s>p and p>r
    if ((player == 'r' and computer == 's') \
        or (player == 's' and computer == 'p') \
        or (player == 'p' and computer == 'r')):
        return True

if __name__=="__main__":
    player = input("What's your choice? Rock --> (r) / Paper --> (p) / Scissor --> (s) : ").lower()
    computer = random.choice(['r' , 'p' , 's'])

    if ((player == computer) or (is_Win(player , computer))):
        print(f"You have won! Computer has also chosen : {computer}.")

    else:
        print(f"You have lost the game! as computer has chosen : {computer}.")