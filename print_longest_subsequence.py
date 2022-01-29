answer_string = ""

def print_longest_subsequence(input_string, output_string):
    # base case
    global answer_string
    if len(input_string) == 0:
        if len(output_string) > len(answer_string):
            answer_string = output_string
            return 
        else:
            return 

    current_character = input_string[0]
    # including current character as we have to make largest subsequence
    print_longest_subsequence(
        input_string[1:], output_string + current_character)


if __name__ == "__main__":
    input_string = "abc"
    output_string = ""
    print_longest_subsequence(input_string, output_string)
    print(answer_string)
