'''
Problem Statement:
------------------
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
'''


def locate_cards(cards, query):
    position = -1

    if len(cards) == 0:
        return position

    low = 0
    high = len(cards) - 1

    # Binary Search Technique
    while low <= high and high >= low:
        mid = (low + high) // 2

        if cards[mid] == query:
            position = mid
            break

        if cards[mid] <= query:
            high = mid - 1

        else:
            low = mid + 1

    return position


if __name__ == '__main__':
    cards = [13, 12, 11, 7, 4, 3, 1, 0]
    query = 12

    position = locate_cards(cards, query)
    if position != -1:
        print("Card found at position:", position)
    else:
        print("Card not found")
