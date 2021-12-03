# Time Complexity: O(n!)

def print_permutations(input_string, output_string):
    # base case
    if len(input_string) == 0:
        print(output_string)
        return

    # getting the current charcter finxed and calling the function recursively on both the halves of the string:
    for i in range(len(input_string)):
        current_character = input_string[i]
        current_string = input_string[0:i] + input_string[i+1:]
        print_permutations(current_string, output_string+current_character)

if __name__ == "__main__":
    input_string = "abc"
    output_string = ""
    print_permutations(input_string, output_string)
