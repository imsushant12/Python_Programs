def helper(s, letters, index, output, answer):
    # handling the base case.
    if index >= len(s):
        answer.append("".join(output))
        return

    # getting the first pressed number
    number = int(s[index])

    # extracting the string present on the current number
    numberValue = letters[number]

    for i in range(len(numberValue)):
        # adding the current character
        output.append(numberValue[i])

        # recursively calling the helper function
        helper(s, letters, index+1, output, answer)

        # backtracking
        output.pop()



def printCombinations(s):
    answer = []
    letters = ["", "", "abc", "def", "ghi",
               "jkl", "mno", "pqrs", "tuv", "wxyz"]

    if len(s) == 0:
        return answer

    output = []
    index = 0

    helper(s, letters, index, output, answer)
    print(answer)


s = "26"
printCombinations(s)
