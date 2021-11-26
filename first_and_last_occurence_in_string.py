def find_occurence(input_string, character):
    firstOccurence = -1
    lastOccurence = -1
    for i in range(len(input_string)):
        if character == input_string[i] and firstOccurence == -1:
            firstOccurence = i
        elif character == input_string[i]:
            lastOccurence = i

    print("First Occurence is at index:", firstOccurence)
    print("Last Occurence is at indec:", lastOccurence)


if __name__ == "__main__":
    input_string = "ababcdtraeaxc"
    character = "a"
    find_occurence(input_string, character)
