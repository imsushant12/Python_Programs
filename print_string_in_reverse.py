def print_reverse_recursive(input_string, index):
    if index == 0:
        print(input_string[0], end="")
        return
    print(input_string[index], end="")
    print_reverse_recursive(input_string, index - 1)


def print_reverse_iterative(input_string):
    last_index = len(input_string) - 1
    for i in range(last_index, -1, -1):
        print(input_string[i], end="")


if __name__ == "__main__":
    input_string = "abcde"
    starting_index = len(input_string) - 1
    print_reverse_recursive(input_string, starting_index)
    print()
    print_reverse_iterative(input_string)
