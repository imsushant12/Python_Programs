# USING BACKTRACKING
# Time Complexity: O(n * n!)

"""
def print_permutations(input_string, output_string):
    # base case
    if len(input_string) == 0:
        print(output_string)
       
        return

    # getting the current character fixed and calling the function recursively on both the halves of the string:
    for i in range(len(input_string)):
        current_character = input_string[i]
        current_string = input_string[0:i] + input_string[i+1:]
        print_permutations(current_string, output_string+current_character)
"""


def generatePermutations(s, index, answer):
    # handling the base case
    if index >= len(s):
        if len(s) > 0:
            print(s)
            answer.append(s.copy())
        return

    for i in range(index, len(s)):
        # swapping the current character.
        s[index], s[i] = s[i], s[index]

        # recursively solving rest
        generatePermutations(s, index+1, answer)

        # backtracking
        s[index], s[i] = s[i], s[index]


if __name__ == "__main__":
    input_string = "abc"
    output_string = ""
    # print_permutations(input_string, output_string)

    answer = []
    index = 0
    generatePermutations(list(input_string), index, answer)
    print(answer)
